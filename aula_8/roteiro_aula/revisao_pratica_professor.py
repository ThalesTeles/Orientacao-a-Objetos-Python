"""
==============================================================================
ROTEIRO DE AULA 8 - REVISÃO E PRÁTICA DE POO + MÓDULO random
Público-alvo: alunos de 15 a 19 anos
Duração sugerida: 1h30 a 2h
Módulo: POO (aula 8 de 9 do módulo) | Aula anterior: "Herança e outras
relações" | Próxima aula: "Projeto da Unidade - RPG de Texto"
==============================================================================

IMPORTANTE PARA O PROFESSOR: esta aula é DIFERENTE das anteriores. A
turma praticou pouco até agora, então hoje o foco é CONSOLIDAR o que já
foi visto, não ensinar teoria nova. A única novidade é o módulo random,
que é rápida de explicar (15-20 min) porque a turma já domina funções,
parâmetros e retorno.

Reserve a MAIOR PARTE do tempo de aula para a atividade de sala - o
roteiro abaixo é propositalmente curto.

Este arquivo pode ser executado no Python para os alunos verem os
exemplos rodando ao vivo.
==============================================================================
"""

# ==============================================================================
# 1. ABERTURA: POR QUE UMA AULA DE REVISÃO? (5 min)
# ==============================================================================
"""
Explique à turma que hoje não tem assunto novo de POO - o objetivo é
fortalecer o que já foi visto (classes, objetos, self, construtores,
herança, agregação) antes do projeto grande da próxima aula (um RPG de
texto completo).

Seja transparente: "vocês vão passar a maior parte da aula de hoje
programando, com a minha ajuda por perto - é assim que esses conceitos
realmente grudam."
"""

# ==============================================================================
# 2. REVISÃO RÁPIDA COM UM ÚNICO EXEMPLO (15-20 min)
# ==============================================================================
"""
Em vez de reexplicar cada conceito do zero, rode este ÚNICO exemplo que
junta tudo, e vá perguntando à turma "que conceito é esse aqui?" para
cada trecho (self, __init__, herança, override, agregação).
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Eu sou {self.nome}, tenho {self.idade} anos.")


class Jogador(Pessoa):  # pergunte: "isso é herança ou agregação? como sabem?"
    def __init__(self, nome, idade, time):
        super().__init__(nome, idade)
        self.time = time

    def apresentar(self):  # pergunte: "o que esse método está fazendo com o da mãe?"
        super().apresentar()
        print(f"Jogo pelo time {self.time}.")


class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.jogadores = []  # pergunte: "e essa relação aqui, é 'é um' ou 'tem um'?"

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
Se a turma responder bem às perguntas, siga rápido para o módulo
random. Se perceber muita dúvida em algum conceito específico
(geralmente self ou herança/agregação), vale parar 5 minutos extras
nele antes de avançar - é melhor consolidar agora do que sofrer no
projeto da próxima aula.
"""

# ==============================================================================
# 3. NOVIDADE: O MÓDULO "random" (15-20 min)
# ==============================================================================
"""
Apresente o problema: até agora, nossos programas sempre fazem a MESMA
coisa. Jogos precisam de ACASO. Introduza o módulo random com as três
funções que vamos usar:

  random.random()        -> decimal entre 0 e 1 (probabilidades)
  random.randint(a, b)   -> inteiro entre a e b, incluindo os dois
  random.choice(lista)   -> um item aleatório da lista
"""

import random

numero = random.random()
print(f"Número aleatório entre 0 e 1: {numero}")

dado = random.randint(1, 6)
print(f"Resultado do dado (1 a 6): {dado}")

opcoes = ["pedra", "papel", "tesoura"]
escolha = random.choice(opcoes)
print(f"Escolha aleatória: {escolha}")

"""
Destaque bem o padrão de PROBABILIDADE com random.random(), pois é a
base da mecânica de fuga do RPG:

  if random.random() < 0.25:   # 25% de chance
      print("Aconteceu!")

Pergunta para a turma: "se eu quiser 90% de chance, o que eu coloco no
lugar de 0.25? E para 10% de chance?"
"""

chance_de_chover = 0.25
if random.random() < chance_de_chover:
    print("Choveu hoje! (25% de chance)")
else:
    print("Não choveu. (75% de chance)")

# ==============================================================================
# 4. random DENTRO DE CLASSES (10 min)
# ==============================================================================
"""
Mostre que random funciona normalmente dentro de métodos - não muda
nada de como já construímos classes.
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

dado1 = Dado()
dado_d20 = Dado(lados=20)
print(f"Resultado do dado de {dado1.lados} lados: {dado1.rolar()}")
print(f"Resultado do dado de {dado_d20.lados} lados: {dado_d20.rolar()}")

# ==============================================================================
# 5. GANCHO DIRETO PARA O RPG: DIFICULDADE x CHANCE (10 min)
# ==============================================================================
"""
Este exemplo é o mais importante da aula - ele é basicamente a mecânica
de fuga do RPG, só que fora do contexto do jogo. Vale a pena rodar
DEVAGAR e comentar cada linha.
"""

class Desafio:
    def __init__(self, dificuldade):
        self.dificuldade = dificuldade

    def chance_de_sucesso(self):
        chance = 0.9 - (self.dificuldade * 0.15)
        return max(chance, 0.1)

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
Avise explicitamente: "essa fórmula aqui é praticamente igual à que
vocês vão usar no RPG para calcular a chance de fugir de um monstro."
"""

# ==============================================================================
# 6. RESTANTE DA AULA: MÃO NA MASSA (45-55 min)
# ==============================================================================
"""
Direcione a turma para o arquivo da atividade de sala. Ela é composta
por vários desafios CURTOS e INDEPENDENTES (não é um projeto grande
ainda) cobrindo herança, agregação e random separadamente, para
consolidar cada peça antes de juntar tudo no projeto da Aula 9.

Circule bastante entre os alunos. Nesta aula, priorize ficar perto de
quem está com mais dificuldade em vez de acompanhar o ritmo médio da
turma - o objetivo de hoje é nivelar a turma antes do projeto.
"""

# ==============================================================================
# 7. FECHAMENTO E PRÉVIA DA AULA 9 (5 min)
# ==============================================================================
"""
Avise à turma, com empolgação: a Aula 9 vai ser o PROJETO DA UNIDADE -
um RPG de texto completo, feito em 1h30 de aula, reunindo tudo que foi
visto no módulo de POO (classes, objetos, self, construtores, herança,
agregação) mais o random de hoje.

Adiante brevemente a mecânica do jogo (personagem, classes de
personagem, salas, monstros, itens, batalha por turnos com chance de
fuga) para gerar expectativa, sem entrar em detalhes de implementação -
isso será o roteiro da próxima aula.

Se sobrar alguns minutos, deixe a atividade de casa como reforço
opcional para quem quiser chegar ainda mais preparado(a).
"""

# ==============================================================================
# FIM DO ROTEIRO
# ==============================================================================
