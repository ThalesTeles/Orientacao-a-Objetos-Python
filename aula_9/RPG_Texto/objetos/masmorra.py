"""
masmorra.py

Masmorra: agrega o Personagem e a lista de Salas; controla a partida inteira.

# PROBLEMA
Alguém precisa percorrer as salas em ordem, tocar cada evento e decidir
quando o jogo acaba (o personagem morreu ou venceu todas as salas).

# PERGUNTA
Onde fica a "regra de fim de jogo", dentro de Sala ou dentro de Masmorra?
Por que faz mais sentido aqui?

# DICA
- __init__: crie a lista self.salas como [Sala(i) for i in range(1, numero_salas+1)].
- jogar(): percorra self.salas; para cada uma, chame sala.executar(personagem)
  e depois personagem.atualizar_buffs(); se o personagem morrer
  (not personagem.esta_vivo()), pare o loop e avise a derrota; se sobreviver
  a todas, avise a vitória.
"""
from sala import Sala


class Masmorra:
    def __init__(self, personagem, numero_salas=5):
        # TODO: guarde self.personagem e crie self.salas (ver DICA).
        pass

    def jogar(self):
        # TODO: percorra as salas chamando sala.executar(...) e
        # personagem.atualizar_buffs(); trate derrota e vitória.
        pass
