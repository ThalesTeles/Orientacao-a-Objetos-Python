"""Model: os seres do ecossistema e o estado da simulação, salvos no SQLite."""

import random
from pathlib import Path

from peewee import SqliteDatabase, Model, IntegerField

# o banco fica ao lado deste arquivo, de qualquer pasta que o programa rode
CAMINHO_BANCO = Path(__file__).parent / "ecossistema.db"
db = SqliteDatabase(CAMINHO_BANCO)


class BaseModel(Model):
    class Meta:
        database = db


class Estado(BaseModel):
    """Uma única linha com o número do ciclo atual."""
    ciclo = IntegerField(default=0)


class Ser(BaseModel):
    """Superclasse de todos os seres: os campos viram colunas em cada tabela filha."""
    energia = IntegerField()
    idade = IntegerField(default=0)
    x = IntegerField()
    y = IntegerField()

    # constantes que cada espécie sobrescreve (não são campos do banco)
    NOME = "ser"
    EMOJI = "?"
    ENERGIA_INICIAL = 3
    ENERGIA_REPRODUCAO = 6
    IDADE_MAXIMA = 50

    def esta_vivo(self):
        return self.energia > 0 and self.idade <= self.IDADE_MAXIMA

    def agir(self, ecossistema):
        """Cada espécie sobrescreve este método (polimorfismo)."""
        self.idade += 1

    def reproduzir(self, ecossistema):
        """Com energia suficiente, divide a energia com um filhote numa casa vizinha livre."""
        if self.energia < self.ENERGIA_REPRODUCAO:
            return
        livres = ecossistema.vizinhas_livres(self.x, self.y)
        if not livres:
            return
        x, y = random.choice(livres)
        energia_filhote = self.energia // 2
        self.energia -= energia_filhote
        ecossistema.adicionar(type(self), x, y, energia_filhote)

    def descricao(self):
        return f"{self.NOME} · energia {self.energia} · idade {self.idade}"


class Planta(Ser):
    NOME = "planta"
    EMOJI = "🌱"
    ENERGIA_INICIAL = 2
    ENERGIA_REPRODUCAO = 4
    IDADE_MAXIMA = 40

    def agir(self, ecossistema):
        super().agir(ecossistema)
        self.energia += 1
        self.reproduzir(ecossistema)


class Animal(Ser):
    """Comportamento comum de quem come: Coelho e Raposa só mudam a presa e os números."""
    PRESA = None
    GANHO_AO_COMER = 3
    CHANCE_DE_CACAR = 1.0  # a presa pode escapar

    def agir(self, ecossistema):
        super().agir(ecossistema)
        self.energia -= 1

        presas = ecossistema.vizinhos_do_tipo(self.x, self.y, self.PRESA)
        if presas and random.random() < self.CHANCE_DE_CACAR:
            presa = random.choice(presas)
            x, y = presa.x, presa.y
            ecossistema.remover(presa)
            ecossistema.mover(self, x, y)
            self.energia += self.GANHO_AO_COMER
        else:
            casas = self.casas_para_andar(ecossistema)
            if casas:
                x, y = random.choice(casas)
                ecossistema.mover(self, x, y)

        self.reproduzir(ecossistema)

    def casas_para_andar(self, ecossistema):
        return ecossistema.vizinhas_livres(self.x, self.y)


class Coelho(Animal):
    NOME = "coelho"
    EMOJI = "🐰"
    ENERGIA_INICIAL = 4
    ENERGIA_REPRODUCAO = 7
    IDADE_MAXIMA = 30
    PRESA = Planta
    GANHO_AO_COMER = 3

    def casas_para_andar(self, ecossistema):
        """O coelho foge: prefere casas sem raposa por perto."""
        livres = super().casas_para_andar(ecossistema)
        seguras = [(x, y) for x, y in livres
                   if not ecossistema.vizinhos_do_tipo(x, y, Raposa)]
        return seguras or livres


class Raposa(Animal):
    NOME = "raposa"
    EMOJI = "🦊"
    ENERGIA_INICIAL = 8
    ENERGIA_REPRODUCAO = 12
    IDADE_MAXIMA = 40
    PRESA = Coelho
    GANHO_AO_COMER = 5
    CHANCE_DE_CACAR = 0.5


ESPECIES = [Planta, Coelho, Raposa]


def criar_tabelas():
    with db:
        db.create_tables([Estado, *ESPECIES])
