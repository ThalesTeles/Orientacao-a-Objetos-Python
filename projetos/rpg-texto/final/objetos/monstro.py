"""
monstro.py

Monstro: herda de PersonagemBase (reaproveita atacar, receber_dano, esta_vivo).

# PROBLEMA
O monstro precisa se comportar como um personagem no combate (atacar, tomar
dano, morrer) mas também precisa de dados próprios: dificuldade e o que ele
"dropa" ao ser derrotado.

# PERGUNTA
Por que Monstro deve herdar de PersonagemBase em vez de ter sua própria
implementação de atacar() do zero?

# DICA
- No __init__, chame super().__init__(nome, vida, ataque, defesa, chance_critico)
  e depois adicione os atributos extras (dificuldade, pontos_atributo_drop,
  chance_drop_item).
- gerar_monstro(dificuldade) é uma função solta (fora da classe) que cria e
  devolve um Monstro com atributos que crescem com a dificuldade.
"""
from personagem import PersonagemBase


class Monstro(PersonagemBase):
    def __init__(self, nome, vida, ataque, defesa, chance_critico, dificuldade):
        # TODO: super().__init__(...) e depois guarde dificuldade,
        # pontos_atributo_drop e chance_drop_item (proporcionais à dificuldade).
        pass


def gerar_monstro(dificuldade):
    """TODO: crie e retorne um Monstro com vida/ataque/defesa que crescem
    conforme o parâmetro dificuldade (1 a 5)."""
    pass
