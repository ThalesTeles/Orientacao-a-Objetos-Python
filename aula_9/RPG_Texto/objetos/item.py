"""
item.py

Item: poções e equipamentos que o personagem pode carregar e usar.

# PROBLEMA
O jogo precisa de itens que curem vida ou dêem bônus temporários (buff) de
ataque, defesa ou crítico durante alguns turnos de combate.

# PERGUNTA
Como o mesmo método aplicar_efeito() pode ter dois comportamentos bem
diferentes (curar OU dar um buff) dependendo só do valor de self.tipo?

# DICA
- Se self.tipo == "cura": soma self.valor à vida do personagem, sem passar
  de personagem.vida_maxima.
- Senão: crie um dicionário de buff, ex:
  {"atributo": "ataque", "valor": self.valor, "turnos_restantes": self.duracao_turnos}
  adicione em personagem.buffs e já aplique o bônus, usando if/elif para
  saber qual atributo somar (ex: personagem.ataque += self.valor).
"""


class Item:
    def __init__(self, nome, tipo, valor, duracao_turnos=0):
        # TODO: guarde nome, tipo ("cura", "ataque", "defesa" ou "critico"),
        # valor e duracao_turnos como atributos do objeto.
        pass

    def aplicar_efeito(self, personagem):
        # TODO: implemente a lógica descrita no bloco PROBLEMA/DICA acima.
        pass

    def __repr__(self):
        return f"Item({self.nome})"


def gerar_item_aleatorio():
    """Sorteia um Item entre algumas opções fixas."""
    import random
    opcoes = [
        Item("Poção de Cura", "cura", 15, 0),
        Item("Elixir de Ataque", "ataque", 3, 3),
        Item("Escudo de Ferro", "defesa", 3, 3),
        Item("Poeira Crítica", "critico", 0.15, 3),
    ]
    return random.choice(opcoes)
