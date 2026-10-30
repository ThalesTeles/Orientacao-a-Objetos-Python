"""
==============================================================================
AULA 8 - ATIVIDADE DE CASA - SIMULADOR DE DUELO
==============================================================================

Hoje vamos construir um pequeno "simulador de duelo" entre dois
lutadores. Ele NÃO é o RPG da Aula 9 (o RPG vai ter salas, monstros,
itens e muito mais) - mas o loop de batalha por turnos que você vai
programar aqui é MUITO parecido com o que o RPG vai precisar. Pense
nisso como um "ensaio" para o projeto.

Complete os espaços marcados com "___" e com o comentário # TODO.
Ao final, execute o arquivo e confira se as respostas fazem sentido.
==============================================================================
"""

import random

# ==============================================================================
# PARTE 1 - A CLASSE "Lutador"
# ==============================================================================
"""
Crie uma classe "Lutador" com:
  - um __init__ que recebe nome, vida e ataque
  - um método "esta_vivo(self)" que devolve True se vida > 0
  - um método "atacar(self, alvo)" que:
      1. calcula um dano com uma pequena variação aleatória:
         dano = self.ataque + random.randint(-3, 3)
         (dica: garanta que o dano nunca fique negativo - se o cálculo
         der um valor menor que 1, use 1 no lugar)
      2. subtrai esse dano da vida do "alvo" (nunca deixe a vida ficar
         negativa - se passar de 0 para baixo, ajuste para 0)
      3. imprime algo como "Rex ataca Thor causando 13 de dano!"
"""

# TODO: crie a classe Lutador aqui, com __init__, esta_vivo() e atacar()


# ==============================================================================
# PARTE 2 - CRIANDO OS DOIS LUTADORES
# ==============================================================================
"""
Crie dois objetos Lutador com nome, vida e ataque à sua escolha (pode
usar nomes de personagens que você goste).
"""

# TODO: crie "lutador1" e "lutador2" aqui


# ==============================================================================
# PARTE 3 - O LOOP DE BATALHA POR TURNOS
# ==============================================================================
"""
Escreva uma função "duelo(lutador1, lutador2)" que:
  1. Enquanto os DOIS lutadores estiverem vivos (esta_vivo()):
       - lutador1 ataca lutador2
       - se lutador2 ainda estiver vivo, lutador2 ataca lutador1
  2. Ao final do loop, descubra quem venceu (quem ainda está vivo) e
     imprima algo como "Rex venceu o duelo!"

Dica: use um "while lutador1.esta_vivo() and lutador2.esta_vivo():" e,
dentro dele, lembre de checar se o alvo continua vivo ANTES de ele
revidar (senão um lutador "morto" ainda consegue atacar de volta!).
"""

# TODO: crie a função duelo(lutador1, lutador2) aqui


# TODO: chame a função duelo() passando os dois lutadores que você criou


# ==============================================================================
# PARTE 4 - REPETINDO O DUELO VÁRIAS VEZES
# ==============================================================================
"""
Como o dano tem uma variação aleatória, o resultado do duelo pode mudar
a cada execução! Para conferir isso, crie DOIS lutadores NOVOS (com os
mesmos atributos de antes) e rode a função duelo() de novo.

Rode o arquivo inteiro umas 3 vezes seguidas (Ctrl+F5 ou o botão de
executar) e veja se o vencedor muda entre as execuções.
"""

# TODO: crie dois lutadores novos com os mesmos atributos de antes


# TODO: chame duelo() de novo com esses lutadores novos


# ==============================================================================
# DESAFIO EXTRA (opcional)
# ==============================================================================
"""
Adicione ao Lutador um método "curar(self, quantidade)" que soma vida
(sem passar de um limite - adicione também um atributo "vida_maxima" no
__init__). Modifique o loop de duelo() para que, com 20% de chance a
cada turno, o lutador que está atacando se cure em vez de atacar
(sorteie com random.random() < 0.2 no início do turno de cada lutador).
"""

# TODO (desafio extra): adicione vida_maxima e o método curar() ao Lutador


# TODO (desafio extra): ajuste a função duelo() para incluir a chance de cura


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Que partes desse duelo você imagina que vão aparecer de novo no RPG da
próxima aula (loop de turnos, dano variável, checar quem está vivo...)?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DA ATIVIDADE DE CASA
# ==============================================================================
