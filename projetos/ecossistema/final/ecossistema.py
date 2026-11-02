"""O Ecossistema: guarda a lista de seres (agregação) e roda os ciclos."""

import random

from modelos import db, Estado, Planta, Coelho, Raposa, ESPECIES

LARGURA = 16
ALTURA = 10
POPULACAO_INICIAL = {Planta: 40, Coelho: 12, Raposa: 3}
BROTOS_POR_CICLO = 8  # sementes trazidas pelo vento: as plantas nunca acabam


class Ecossistema:
    def __init__(self):
        self.estado, _ = Estado.get_or_create(id=1)
        self.seres = []
        for especie in ESPECIES:
            self.seres.extend(especie.select())
        # posição (x, y) -> ser, para achar vizinhos sem percorrer a lista
        self.grade = {(ser.x, ser.y): ser for ser in self.seres}

    @property
    def ciclo(self):
        return self.estado.ciclo

    # ------------------------------------------------------------ vizinhança
    def vizinhas(self, x, y):
        """As até 8 casas em volta de (x, y), dentro da grade."""
        casas = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if (dx, dy) != (0, 0) and 0 <= nx < LARGURA and 0 <= ny < ALTURA:
                    casas.append((nx, ny))
        return casas

    def vizinhas_livres(self, x, y):
        return [casa for casa in self.vizinhas(x, y) if casa not in self.grade]

    def vizinhos_do_tipo(self, x, y, especie):
        return [self.grade[casa] for casa in self.vizinhas(x, y)
                if isinstance(self.grade.get(casa), especie)]

    def casas_livres(self):
        return [(x, y) for y in range(ALTURA) for x in range(LARGURA)
                if (x, y) not in self.grade]

    # ------------------------------------------------------------ alterações
    def adicionar(self, especie, x, y, energia=None):
        if energia is None:
            energia = especie.ENERGIA_INICIAL
        ser = especie.create(x=x, y=y, energia=energia)
        self.seres.append(ser)
        self.grade[(x, y)] = ser
        return ser

    def adicionar_aleatorio(self, especie):
        livres = self.casas_livres()
        if not livres:
            return None
        x, y = random.choice(livres)
        return self.adicionar(especie, x, y)

    def mover(self, ser, x, y):
        del self.grade[(ser.x, ser.y)]
        ser.x, ser.y = x, y
        self.grade[(x, y)] = ser

    def remover(self, ser):
        del self.grade[(ser.x, ser.y)]
        self.seres.remove(ser)
        ser.delete_instance()

    def esta_na_grade(self, ser):
        return self.grade.get((ser.x, ser.y)) is ser

    # ------------------------------------------------------------ simulação
    def avancar(self):
        """Um ciclo: cada ser age uma vez, em ordem sorteada."""
        with db.atomic():
            self.estado.ciclo += 1
            self.estado.save()
            # cópia embaralhada: quem nasce neste ciclo só age no próximo
            for ser in random.sample(self.seres, len(self.seres)):
                if not self.esta_na_grade(ser):  # foi comido antes da sua vez
                    continue
                ser.agir(self)  # polimorfismo: cada espécie age do seu jeito
                if ser.esta_vivo():
                    ser.save()
                else:
                    self.remover(ser)
            for _ in range(BROTOS_POR_CICLO):
                self.adicionar_aleatorio(Planta)

    def reiniciar(self):
        with db.atomic():
            for especie in ESPECIES:
                especie.delete().execute()
            self.seres.clear()
            self.grade.clear()
            self.estado.ciclo = 0
            self.estado.save()
            for especie, quantidade in POPULACAO_INICIAL.items():
                for _ in range(quantidade):
                    self.adicionar_aleatorio(especie)

    # ------------------------------------------------------------ para a página
    def contagem(self):
        return {especie: sum(isinstance(ser, especie) for ser in self.seres)
                for especie in ESPECIES}

    def linhas(self):
        """A grade como lista de linhas; casa vazia = None."""
        return [[self.grade.get((x, y)) for x in range(LARGURA)]
                for y in range(ALTURA)]
