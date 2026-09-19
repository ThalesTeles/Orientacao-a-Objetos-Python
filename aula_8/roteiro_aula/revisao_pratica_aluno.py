"""
==============================================================================
AULA 8 - REVISÃO E PRÁTICA DE POO + MÓDULO random
==============================================================================

Este arquivo é um material de apoio. Você pode executá-lo no Python para
ver os exemplos funcionando na prática.

Aviso importante: Não temos conteúdo teórico novo de POO. O objetivo
da aula é PRATICAR tudo que vimos até aqui (classes, objetos, atributos,
métodos, self, construtores, herança, agregação), porque a maior parte
do tempo de hoje vai ser mão na massa na atividade de sala.

A única novidade de hoje é uma ferramenta nova: o módulo "random", que
vamos precisar na próxima aula para construir um RPG de texto.
==============================================================================
"""

# ==============================================================================
# 1. REVISÃO RÁPIDA: O QUE JÁ SABEMOS
# ==============================================================================
"""
Antes de praticar, um resumo do que vimos nas Aulas 5, 6 e 7:

  CLASSE      -> o molde. Define atributos (no __init__) e comportamentos
                 (métodos).
  OBJETO      -> uma instância da classe, com valores próprios.
  self        -> dentro de um método, representa o PRÓPRIO objeto.
  __init__    -> construtor: roda automaticamente ao criar um objeto,
                 garantindo que ele já nasça com os atributos certos.
  ESTADO      -> os valores dos atributos de um objeto em um momento -
                 muda através dos métodos.
  HERANÇA     -> relação "É UM". Uma subclasse reaproveita atributos e
                 métodos de uma superclasse (e pode sobrescrevê-los).
  AGREGAÇÃO   -> relação "TEM UM". Um objeto guarda outro objeto (ou uma
                 lista deles) como atributo.

Vamos ver tudo isso junto em um único exemplo de revisão:
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Eu sou {self.nome}, tenho {self.idade} anos.")


class Jogador(Pessoa):  # HERANÇA: Jogador É UMA Pessoa
    def __init__(self, nome, idade, time):
        super().__init__(nome, idade)
        self.time = time

    def apresentar(self):  # SOBRESCRITA do método da superclasse
        super().apresentar()
        print(f"Jogo pelo time {self.time}.")


class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []  # AGREGAÇÃO: Time TEM VÁRIOS Jogadores

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.jogadores:
            jogador.apresentar()


time_a = Time("Estrelas FC")
time_a.adicionar_jogador(Jogador("Bia", 17, "Estrelas FC"))
time_a.adicionar_jogador(Jogador("Caio", 18, "Estrelas FC"))
time_a.listar_jogadores()

"""
Se cada peça desse exemplo (classe, objeto, self, __init__, herança,
agregação) fez sentido para você, ótimo, é exatamente isso que vamos
treinar hoje em situações novas.
"""

# ==============================================================================
# 2. O MÓDULO "random"
# ==============================================================================
"""
Até agora, nossos programas sempre faziam a MESMA coisa toda vez que
rodavam. Mas jogos (como o RPG que vamos construir na próxima aula)
precisam de ACASO: uma chance de encontrar um monstro, uma chance de
conseguir fugir, um dano que varia um pouco a cada ataque (acerto crítico)...

Para isso, o Python tem o módulo "random". Para usá-lo, importamos no
topo do arquivo:

    import random

As funções mais úteis para o nosso caso:
"""

import random

# random.random() -> devolve um número decimal aleatório entre 0 e 1.
# Serve para simular PROBABILIDADES (ex: 30% de chance = valor < 0.3)
numero = random.random()
print(f"Número aleatório entre 0 e 1: {numero}")

# random.randint(a, b) -> devolve um número inteiro aleatório entre
# a e b, incluindo os dois extremos. Ótimo para dados, dano variável, etc.
dado = random.randint(1, 6)
print(f"Resultado do dado (1 a 6): {dado}")

# random.choice(lista) -> escolhe um elemento aleatório de uma lista.
opcoes = ["pedra", "papel", "tesoura"]
escolha = random.choice(opcoes)
print(f"Escolha aleatória: {escolha}")

"""
Como simular uma PROBABILIDADE com random.random():

  Se eu quero que algo tenha 25% de chance de acontecer, eu comparo:

      if random.random() < 0.25:
          print("Aconteceu!")
      else:
          print("Não aconteceu.")

Quanto MENOR o número do lado direito (0.25), MENOR a chance de o
"if" ser verdadeiro. Isso vai ser a base da mecânica de fuga do RPG!
"""

chance_de_chover = 0.25
if random.random() < chance_de_chover:
    print("Choveu hoje! (25% de chance)")
else:
    print("Não choveu. (75% de chance)")

# ==============================================================================
# 3. USANDO random DENTRO DE UMA CLASSE
# ==============================================================================
"""
random funciona normalmente dentro de métodos, como qualquer outra
função. Veja dois exemplos combinando random com o que já sabemos de
POO:
"""

class Moeda:
    def jogar(self):
        return random.choice(["cara", "coroa"])


class Dado:
    def __init__(self, lados=6):
        self.lados = lados

    def rolar(self):
        return random.randint(1, self.lados)


moeda1 = Moeda()
print(f"A moeda caiu em: {moeda1.jogar()}")

dado1 = Dado()          # dado comum, de 6 lados (valor padrão)
dado_d20 = Dado(lados=20)  # dado de 20 lados, usando o construtor
print(f"Resultado do dado de {dado1.lados} lados: {dado1.rolar()}")
print(f"Resultado do dado de {dado_d20.lados} lados: {dado_d20.rolar()}")

"""
Reparem: "Dado" usa um parâmetro opcional no __init__ (lados=6), algo
que já vimos na Aula 6 (e no curso de Algoritmos 2 =) ),
random não muda nada da forma como construímos
as classes, só entra como mais uma ferramenta dentro dos métodos.
"""

# ==============================================================================
# 4. PROBABILIDADE QUE DEPENDE DE UMA VARIÁVEL
# ==============================================================================
"""
No RPG da próxima aula, a chance de FUGIR de um monstro vai depender da
DIFICULDADE do monstro: quanto mais difícil, menor a chance de fuga.
Veja um exemplo simplificado dessa ideia:
"""

class Desafio:
    def __init__(self, dificuldade):
        self.dificuldade = dificuldade  # de 1 (fácil) a 5 (muito difícil)

    def chance_de_sucesso(self):
        # quanto maior a dificuldade, menor a chance
        chance = 0.9 - (self.dificuldade * 0.15)
        return max(chance, 0.1)  # nunca deixa a chance ficar abaixo de 10% (caso a dificuldade seja maior do que 5)

    def tentar(self):
        chance = self.chance_de_sucesso()
        print(f"Chance de sucesso: {chance * 100:.0f}%")
        if random.random() < chance:
            print("Sucesso!")
            return True
        else:
            print("Falhou!")
            return False


desafio_facil = Desafio(dificuldade=1)
desafio_dificil = Desafio(dificuldade=5)

desafio_facil.tentar()
desafio_dificil.tentar()

"""
Esse padrão: "quanto maior a dificuldade, menor a chance"; é
exatamente o que vamos usar na Aula 9 para decidir se o personagem
consegue fugir de um monstro ou não.
"""

# ==============================================================================
# 5. PRÉVIA DA PRÓXIMA AULA
# ==============================================================================
"""
Na Aula 9 vamos usar TUDO que praticamos até aqui: classes, objetos,
herança, agregação e agora random; para construir, em uma atividade de
um RPG DE TEXTO completo, com personagem, classes de personagem
(Guerreiro, Mago, Arqueiro), monstros, itens, batalhas por turno e
chance de fuga.

Chegue na próxima aula com esses conceitos bem treinados!
"""

# ==============================================================================
# FIM
# ==============================================================================
