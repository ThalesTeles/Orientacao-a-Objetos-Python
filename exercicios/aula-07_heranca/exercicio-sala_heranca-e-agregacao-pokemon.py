"""
==============================================================================
AULA 7 - ATIVIDADE DE SALA - HERANÇA E AGREGAÇÃO: BATALHA POKÉMON
==============================================================================

Nesta atividade você vai construir um sistema de batalha Pokémon no terminal.
Use a HERANÇA ("é um") para especializar os tipos de Pokémon e a AGREGAÇÃO
("tem um") para montar a equipe de um Treinador.

Dica: crie uma pasta "pokemon_tc63oo" e três arquivos dentro dela:
pokemon.py, treinador.py e jogo.py. Aqui, para facilitar, as missões estão
todas neste arquivo. Se quiser, pode separá-las depois.

Complete os trechos marcados com # TODO e execute o arquivo depois de cada
missão para ver se está funcionando. Se travar, consulte o roteiro.
==============================================================================
"""

# ==============================================================================
# MISSÃO 1 - A SUPERCLASSE PokemonBase
# ==============================================================================
"""
Todo Pokémon tem nome, vida, ataque e defesa, além de sofrer dano e atacar.

Crie a classe "PokemonBase" com:
  1. o construtor __init__(self, nome, vida, ataque, defesa). Guarde também
     self.vida_maxima = vida (para sabermos o limite ao curar o Pokémon);
  2. o método esta_vivo(self), que devolve True se vida > 0 e False caso
     contrário;
  3. o método receber_dano(self, dano_bruto):
       - dano_real = max(1, dano_bruto - defesa)
       - vida = max(0, vida - dano_real)   (a vida nunca fica negativa)
       - mostre o dano sofrido e a vida atual;
  4. o método atacar(self, alvo), que mostra uma mensagem de ataque básico e
     chama alvo.receber_dano(self.ataque).

Teste: crie dois PokemonBase, faça um atacar o outro e confira a vida.
"""

# TODO: crie a classe PokemonBase e teste aqui


# ==============================================================================
# MISSÃO 2 - SUBCLASSES E super()
# ==============================================================================
"""
Crie três subclasses de PokemonBase. Em cada __init__, receba só o "nome" e
chame super().__init__(nome, vida=..., ataque=..., defesa=...).

  Subclasse      Vida  Ataque  Defesa  Efeito especial em atacar(alvo)
  PokemonAgua     60     12      8     Jato d'Água: causa self.ataque de dano.
  PokemonFogo     45     18      4     Lança-Chamas: causa ataque + 3 de dano.
  PokemonPlanta   50     14      6     Folha Navalha: causa self.ataque e
                                       recupera até 3 de HP (sem passar de
                                       vida_maxima).

Cada subclasse SOBRESCREVE o método atacar(self, alvo).

Responda em um comentário: por que não precisamos reescrever esta_vivo() nem
receber_dano() nas subclasses?
"""

# TODO: crie PokemonAgua, PokemonFogo e PokemonPlanta e teste aqui


# TODO: escreva sua resposta aqui


# ==============================================================================
# MISSÃO 3 - AGREGAÇÃO: A CLASSE Treinador
# ==============================================================================
"""
Um treinador NÃO É um Pokémon; ele TEM uma equipe e TEM uma mochila.

Crie a classe "Treinador" com:
  1. __init__(self, nome): inicialize self.equipe = [] e
     self.mochila = ["Poção", "Poção"];
  2. capturar(self, pokemon): adiciona o Pokémon à equipe (máximo de 6;
     se estiver cheia, avise);
  3. pokemon_ativo(self): devolve o PRIMEIRO Pokémon vivo da equipe, ou None
     se todos estiverem derrotados;
  4. usar_pocao(self): se houver "Poção" na mochila e um Pokémon ativo,
     remova uma "Poção" e recupere até 20 de vida do Pokémon ativo (sem
     ultrapassar vida_maxima). Se não houver, avise.

Responda em um comentário: o que muda entre "PokemonFogo é um PokemonBase" e
"Treinador tem Pokémons"? Qual dos dois usa herança e qual usa agregação?
"""

# TODO: crie a classe Treinador e teste aqui


# TODO: escreva sua resposta aqui


# ==============================================================================
# MISSÃO 4 - O JOGO NO TERMINAL
# ==============================================================================
"""
Integre as classes e rode a primeira batalha:

  1. peça o nome do treinador e crie o Treinador;
  2. mostre o menu: 1 - Squirtle (Água), 2 - Charmander (Fogo),
     3 - Bulbasaur (Planta); peça a opção e um apelido;
  3. crie o Pokémon do tipo escolhido e use capturar();
  4. crie um rival, por exemplo PokemonFogo("Charmeleon Selvagem");
  5. repita enquanto o treinador tiver pokemon_ativo() e o rival estiver vivo:
       - mostre a vida dos dois e quantas poções restam;
       - pergunte: (1) Atacar ou (2) Usar Poção;
       - se o rival ainda estiver vivo, ele ataca de volta;
  6. no final, mostre se o treinador venceu ou se todos os Pokémons caíram.
"""

# TODO: escreva o jogo aqui
