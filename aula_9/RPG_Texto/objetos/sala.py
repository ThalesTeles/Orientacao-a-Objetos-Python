"""
sala.py
Sala: sorteia e executa um evento (monstro, item, armadilha ou vazia).

# PROBLEMA
Cada sala da masmorra precisa "sortear" o que vai acontecer nela e depois
saber executar esse evento, sem repetir if/else espalhados pelo resto do
código.

# PERGUNTA
Por que usar random.choices() com weights em vez de random.choice() simples?
(pense: como dar prioridade a monstros sem eliminar item/armadilha)

# DICA
- sortear_evento(): random.choices(["monstro", "item", "armadilha"],
  weights=[50, 30, 20], k=1)[0], guarde o resultado em self.tipo_evento e
  já crie o monstro (gerar_monstro) ou o item (gerar_item_aleatorio)
  correspondente.
- executar(personagem): um if/elif para cada tipo_evento. Para "monstro",
  chame iniciar_combate(personagem, self.monstro), essa função já está
  pronta em combate.py, você só precisa importá-la e chamá-la.
"""
import random
from monstro import gerar_monstro
from item import gerar_item_aleatorio


class Sala:
    def __init__(self, numero):
        # TODO: guarde numero, defina dificuldade = numero, tipo_evento = None,
        # monstro = None, item = None, e chame self.sortear_evento().
        pass

    def sortear_evento(self):
        # TODO: sorteie o tipo_evento com pesos (ver DICA acima) e, se for
        # "monstro" ou "item", já crie o objeto correspondente.
        pass

    def executar(self, personagem):
        print(f"\n=== Sala {self.numero} (dificuldade {self.dificuldade}) ===")
        # TODO: trate cada tipo_evento:
        #   "vazia"     -> só avisa que a sala está vazia
        #   "armadilha" -> calcula um dano e chama personagem.receber_dano()
        #   "item"      -> adiciona self.item na mochila do personagem
        #   "monstro"   -> from combate import iniciar_combate; chame a função
        pass
