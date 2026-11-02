"""Modos de jogo: herança e polimorfismo, sem banco de dados.

A Partida não sabe se é de um ou de dois jogadores: ela só chama
regras.ao_acertar() e regras.ao_errar(), e cada modo responde do seu jeito.
"""


class Modo:
    NOME = ""

    def __init__(self, partida):
        self.partida = partida

    def ao_acertar(self):
        pass

    def ao_errar(self):
        pass

    def vez_de(self):
        return None

    def placar(self):
        return [f"Jogadas {self.partida.jogadas}"]

    def resultado(self):
        raise NotImplementedError


class Solo(Modo):
    NOME = "Um jogador"

    def resultado(self):
        return f"{self.partida.jogador1} terminou em {self.partida.jogadas} jogadas."


class Dupla(Modo):
    NOME = "Dois jogadores"

    def ao_acertar(self):
        # quem acerta marca ponto e joga de novo
        if self.partida.vez == 1:
            self.partida.pontos1 += 1
        else:
            self.partida.pontos2 += 1

    def ao_errar(self):
        self.partida.vez = 2 if self.partida.vez == 1 else 1

    def vez_de(self):
        p = self.partida
        return p.jogador1 if p.vez == 1 else p.jogador2

    def placar(self):
        p = self.partida
        return super().placar() + [f"{p.jogador1} {p.pontos1}", f"{p.jogador2} {p.pontos2}"]

    def vencedor(self):
        """Nome de quem fez mais pares, ou None no empate."""
        p = self.partida
        if p.pontos1 == p.pontos2:
            return None
        return p.jogador1 if p.pontos1 > p.pontos2 else p.jogador2

    def perdedor(self):
        p = self.partida
        if self.vencedor() is None:
            return None
        return p.jogador2 if self.vencedor() == p.jogador1 else p.jogador1

    def resultado(self):
        p = self.partida
        if p.pontos1 == p.pontos2:
            return f"Empate: {p.pontos1} a {p.pontos2}."
        vencedor = p.jogador1 if p.pontos1 > p.pontos2 else p.jogador2
        return f"{vencedor} venceu por {max(p.pontos1, p.pontos2)} a {min(p.pontos1, p.pontos2)}."


MODOS = {"solo": Solo, "dupla": Dupla}
