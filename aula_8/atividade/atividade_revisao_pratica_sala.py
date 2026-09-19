"""
==============================================================================
AULA 8 - ATIVIDADE DE SALA - DESAFIOS DE REVISÃO
==============================================================================

Esta atividade tem VÁRIOS desafios curtos e independentes (não é um
projeto grande ainda, isso fica para a Aula 9). Cada desafio treina
um conceito separadamente: herança, agregação e random.

Complete os espaços marcados com o comentário # TODO.
Depois de completar cada desafio, execute o arquivo para conferir se os
prints aparecem corretamente. Pode pedir ajuda ao professor a qualquer
momento, hoje o objetivo é praticar, não travar sozinho(a)!
==============================================================================
"""

import random

# ==============================================================================
# DESAFIO 1 - HERANÇA: FUNCIONÁRIOS
# ==============================================================================
"""
Crie uma classe "Funcionario" com um __init__ que recebe nome e salario,
e um método "apresentar(self)" que imprime algo como:
  "Ana ganha R$ 3000.00 por mês."

Depois, crie DUAS subclasses:
  - "Gerente", que HERDA de Funcionario e adiciona um atributo extra
    "equipe_tamanho" (número de pessoas na equipe). SOBRESCREVA
    apresentar() para incluir esse dado.
  - "Estagiario", que HERDA de Funcionario e adiciona um atributo extra
    "faculdade". SOBRESCREVA apresentar() para incluir esse dado.

Crie um objeto de cada classe (Funcionario, Gerente, Estagiario) e
chame apresentar() em cada um.
"""

# TODO: crie a classe Funcionario aqui


# TODO: crie a classe Gerente(Funcionario) aqui


# TODO: crie a classe Estagiario(Funcionario) aqui


# TODO: crie um objeto de cada classe e chame apresentar() neles


# ==============================================================================
# DESAFIO 2 - AGREGAÇÃO: UMA EMPRESA "TEM" FUNCIONÁRIOS
# ==============================================================================
"""
Crie uma classe "Empresa" com:
  - um __init__ que recebe "nome" e cria uma lista vazia "funcionarios"
  - um método "contratar(self, funcionario)" que adiciona o funcionário
    à lista e imprime uma mensagem de confirmação
  - um método "folha_de_pagamento_total(self)" que soma o "salario" de
    TODOS os funcionários da lista (funciona para Funcionario, Gerente
    e Estagiario, já que todos herdam o atributo "salario"!)

Crie um objeto Empresa, contrate os três funcionários do Desafio 1, e
imprima o valor da folha de pagamento total.
"""

# TODO: crie a classe Empresa aqui


# TODO: crie o objeto Empresa e contrate os funcionários do Desafio 1


# TODO: imprima a folha de pagamento total


# ==============================================================================
# DESAFIO 3 - RANDOM: MOEDA E DADO
# ==============================================================================
"""
Crie uma classe "Moeda" com um método "jogar(self)" que devolve "cara"
ou "coroa" aleatoriamente (use random.choice).

Crie uma classe "Dado" com um __init__ que recebe "lados" (valor padrão
6) e um método "rolar(self)" que devolve um número aleatório entre 1 e
"lados" (use random.randint).

Crie um objeto de cada classe e chame os métodos, imprimindo o
resultado.
"""

# TODO: crie a classe Moeda aqui


# TODO: crie a classe Dado aqui


# TODO: crie os objetos e chame jogar() e rolar(), imprimindo os resultados


# ==============================================================================
# DESAFIO 4 - RANDOM + PROBABILIDADE: TESTE DE SORTE
# ==============================================================================
"""
Crie uma classe "TesteDeSorte" com:
  - um __init__ que recebe "chance_de_sucesso" (um número entre 0 e 1,
    ex: 0.3 para 30% de chance)
  - um método "tentar(self)" que:
      1. usa random.random() para decidir se o teste teve sucesso
         (sucesso se o número sorteado for MENOR que chance_de_sucesso)
      2. imprime "Sucesso!" ou "Falhou!" dependendo do resultado
      3. devolve True em caso de sucesso, False em caso de falha

Crie dois objetos TesteDeSorte, um com 80% de chance e outro com 20% de
chance, e chame tentar() em cada um algumas vezes (ex: dentro de um for
que repete 5 vezes) para ver a diferença na prática.
"""

# TODO: crie a classe TesteDeSorte aqui


# TODO: crie os dois objetos (80% e 20% de chance)


# TODO: chame tentar() 5 vezes em cada um, usando um for


# ==============================================================================
# DESAFIO 5 - COMBINANDO TUDO: PERSONAGEM COM ACERTO CRÍTICO
# ==============================================================================
"""
Este último desafio junta herança, self, construtor e random - é o mais
parecido com o que vamos fazer no RPG da próxima aula.

Crie uma classe "Personagem" com:
  - um __init__ que recebe nome, vida e ataque
  - um método "atacar(self)" que:
      1. sorteia se o ataque foi um ACERTO CRÍTICO (25% de chance, use
         random.random())
      2. se foi crítico, o dano causado é o dobro do ataque normal;
         caso contrário, o dano é igual ao ataque normal
      3. imprime algo como "Rex ataca causando 40 de dano (CRÍTICO!)"
         ou "Rex ataca causando 20 de dano."
      4. devolve o valor do dano causado

Crie um objeto Personagem e chame atacar() umas 5 vezes seguidas (com
um for) para ver o crítico acontecer aleatoriamente.
"""

# TODO: crie a classe Personagem aqui


# TODO: crie um objeto Personagem e chame atacar() 5 vezes


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Dos conceitos que você praticou hoje (herança, agregação, random),
qual você sentiu mais confiança e qual ainda quer reforçar antes do
projeto da próxima aula?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
