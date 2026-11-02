"""Model: as tabelas do jogo da memória, escritas como classes do Peewee."""

import random
from datetime import datetime
from pathlib import Path

from peewee import (SqliteDatabase, Model, CharField, IntegerField, BooleanField,
                    DateTimeField, ForeignKeyField)

from imagens import desenhar_formas
from modos import MODOS

PASTA = Path(__file__).parent
CAMINHO_BANCO = PASTA / "memoria.db"
PASTA_IMAGENS = PASTA / "static" / "imagens"
TAMANHO_IMAGEM = 256  # todas as cartas viram 256 x 256 px
PARES_POSSIVEIS = (4, 6, 8, 10, 12)

db = SqliteDatabase(CAMINHO_BANCO, pragmas={"foreign_keys": 1})


class BaseModel(Model):
    class Meta:
        database = db


class Tema(BaseModel):
    nome = CharField(unique=True)
    tipo = CharField(default="imagem")  # "imagem" ou "texto"

    def eh_imagem(self):
        return self.tipo == "imagem"

    def pares_possiveis(self):
        quantidade = self.figuras.count()
        return [p for p in PARES_POSSIVEIS if p <= quantidade]

    def remover(self):
        for figura in self.figuras:
            figura.remover()
        self.delete_instance(recursive=True)


class Figura(BaseModel):
    """A face de um par: cada figura vira duas cartas na mesa."""
    tema = ForeignKeyField(Tema, backref="figuras", on_delete="CASCADE")
    valor = CharField()  # o texto da carta ou o nome do arquivo da imagem

    def eh_imagem(self):
        return self.tema.eh_imagem()

    def remover(self):
        if self.eh_imagem():
            (PASTA_IMAGENS / self.valor).unlink(missing_ok=True)
        self.delete_instance(recursive=True)


class Partida(BaseModel):
    tema = ForeignKeyField(Tema, backref="partidas", on_delete="CASCADE")
    modo = CharField(default="solo")  # chave de MODOS
    jogador1 = CharField()
    jogador2 = CharField(null=True)
    pontos1 = IntegerField(default=0)
    pontos2 = IntegerField(default=0)
    vez = IntegerField(default=1)
    jogadas = IntegerField(default=0)
    terminada = BooleanField(default=False)
    criada_em = DateTimeField(default=datetime.now)

    @property
    def regras(self):
        return MODOS[self.modo](self)  # Solo ou Dupla

    @classmethod
    def nova(cls, tema, pares, modo, jogador1, jogador2=None):
        """Sorteia as figuras, duplica, embaralha e cria as cartas."""
        baralho = random.sample(list(tema.figuras), pares) * 2
        random.shuffle(baralho)
        with db.atomic():
            partida = cls.create(tema=tema, modo=modo, jogador1=jogador1,
                                 jogador2=jogador2)
            for posicao, figura in enumerate(baralho):
                Carta.create(partida=partida, figura=figura, posicao=posicao)
        return partida

    def cartas_em_ordem(self):
        return self.cartas.order_by(Carta.posicao)

    def pares(self):
        return self.cartas.count() // 2

    def encontrados(self):
        return self.cartas.where(Carta.encontrada).count() // 2

    def abertas(self):
        """Cartas viradas que ainda não formaram par."""
        return list(self.cartas.where(Carta.virada, ~Carta.encontrada))

    def virar(self, carta):
        """Uma jogada são duas cartas. O par errado fica aberto até o próximo clique."""
        if self.terminada or carta.encontrada:
            return
        with db.atomic():
            abertas = self.abertas()
            if len(abertas) == 2:  # par errado da jogada anterior: esconde
                for aberta in abertas:
                    aberta.esconder()
                if carta in abertas:
                    return
                abertas = []
            elif carta in abertas:  # clicou de novo na mesma carta
                return

            carta.virada = True
            carta.save()
            if abertas:  # é a segunda carta da jogada
                self.jogadas += 1
                primeira = abertas[0]
                if primeira.forma_par_com(carta):
                    primeira.marcar_encontrada()
                    carta.marcar_encontrada()
                    self.regras.ao_acertar()  # polimorfismo: cada modo pontua do seu jeito
                    self.terminada = self.encontrados() == self.pares()
                else:
                    self.regras.ao_errar()
                self.save()

    @classmethod
    def ranking(cls):
        """Só partidas de um jogador: menos jogadas primeiro."""
        return (cls.select().where(cls.terminada, cls.modo == "solo")
                .order_by(cls.jogadas, cls.criada_em).limit(10))

    @classmethod
    def ultimas_duplas(cls):
        """Partidas de dois jogadores terminadas: as mais recentes primeiro."""
        return (cls.select().where(cls.terminada, cls.modo == "dupla")
                .order_by(cls.criada_em.desc()).limit(10))


class Carta(BaseModel):
    partida = ForeignKeyField(Partida, backref="cartas", on_delete="CASCADE")
    figura = ForeignKeyField(Figura, backref="cartas", on_delete="CASCADE")
    posicao = IntegerField()
    virada = BooleanField(default=False)
    encontrada = BooleanField(default=False)

    @property
    def visivel(self):
        return self.virada or self.encontrada

    def forma_par_com(self, outra):
        return self.figura_id == outra.figura_id

    def esconder(self):
        self.virada = False
        self.save()

    def marcar_encontrada(self):
        self.encontrada = True
        self.save()


TEMAS_DE_TEXTO = {
    "Animais": "🐶 🐱 🐭 🐰 🦊 🐻 🐼 🐨 🐯 🦁 🐸 🐵",
    "Python": "class def self return import for while if None True list dict",
}


def criar_tabelas():
    with db:
        db.create_tables([Tema, Figura, Partida, Carta])
        if Tema.select().exists():
            return
        formas = Tema.create(nome="Formas", tipo="imagem")
        for nome in desenhar_formas(PASTA_IMAGENS, TAMANHO_IMAGEM):
            Figura.create(tema=formas, valor=nome)
        for nome, simbolos in TEMAS_DE_TEXTO.items():
            tema = Tema.create(nome=nome, tipo="texto")
            for simbolo in simbolos.split():
                Figura.create(tema=tema, valor=simbolo)
