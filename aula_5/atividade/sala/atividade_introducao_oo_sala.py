"""
==============================================================================
AULA 5 - ATIVIDADE DE SALA - CLASSES, OBJETOS, ATRIBUTOS E CONSTRUTORES
==============================================================================

Complete os espaços marcados com o comentário # TODO.
Depois de completar cada parte, execute o arquivo para conferir se os
prints aparecem corretamente.

Regra do dia: toda classe que você criar deve ter um construtor
(__init__) que recebe os atributos como parâmetros e os atribui com
"self.atributo = valor". Não use mais "class Nome: pass" + atribuição
manual - isso foi só para entendermos o problema que o construtor
resolve. Métodos (comportamentos, além do __init__) ainda são assunto
da Aula 6!
==============================================================================
"""

# ==============================================================================
# PARTE 1 - CRIANDO UMA CLASSE COM CONSTRUTOR
# ==============================================================================
"""
Crie uma classe chamada "Animal" com um construtor (__init__) que recebe
e define os seguintes atributos:
  - nome
  - especie
  - idade
  - som   (o som que o animal faz, ex: "Au au", "Miau")
"""

# TODO: crie a classe Animal aqui, com __init__(self, nome, especie, idade, som)


# ==============================================================================
# PARTE 2 - CRIANDO OBJETOS COM O CONSTRUTOR
# ==============================================================================
"""
Agora crie DOIS objetos (instâncias) da classe Animal: "cachorro" e "gato",
passando os valores direto no construtor (sem atribuir os atributos "na
mão" depois).

Use valores diferentes para cada animal.
"""

# TODO: crie o objeto "cachorro" chamando o construtor, ex:
# cachorro = Animal(___, ___, ___, ___)


# TODO: crie o objeto "gato" chamando o construtor da mesma forma


# ==============================================================================
# PARTE 3 - EXIBINDO AS INFORMAÇÕES
# ==============================================================================
"""
Complete os prints abaixo para mostrar as informações de cada animal,
no seguinte formato (você pode se inspirar neste modelo):

  "Rex é um(a) cachorro de 3 anos e faz Au au"
"""

# TODO: complete o print do cachorro
# print(f"...")

# TODO: complete o print do gato
# print(f"...")


# ==============================================================================
# PARTE 4 - MAIS UM OBJETO
# ==============================================================================
"""
Crie um terceiro objeto da classe Animal, com o animal que você quiser
(pode ser um bicho de estimação real, um animal exótico, ou até um
animal fictício/lendário). Passe os 4 valores (nome, especie, idade,
som) direto no construtor e faça o print no mesmo formato da Parte 3.
"""

# TODO: crie o terceiro objeto aqui, chamando o construtor


# TODO: print do terceiro objeto aqui


# ==============================================================================
# PARTE 5 - CRIE SUA PRÓPRIA CLASSE (COM CONSTRUTOR)
# ==============================================================================
"""
Escolha um dos temas abaixo (ou sugira outro para o professor):

  a) Carro         -> atributos: marca, modelo, cor, velocidade_max
  b) Jogador       -> atributos: nome, time, posicao, numero_camisa
  c) Celular       -> atributos: marca, modelo, armazenamento, bateria
  d) Personagem de RPG -> atributos: nome, classe, vida, ataque

Faça o seguinte:
  1. Crie a classe escolhida, com um construtor (__init__) que recebe
     os 4 atributos sugeridos (ou outros, se preferir) como parâmetros.
  2. Crie DOIS objetos dessa classe, passando os valores direto no
     construtor, com valores diferentes para cada objeto.
  3. Faça um print para cada objeto, mostrando suas informações de forma
     organizada.
"""

# TODO: crie sua classe aqui, já com __init__


# TODO: crie os dois objetos aqui, chamando o construtor


# TODO: faça os prints de cada objeto aqui


# ==============================================================================
# DESAFIO EXTRA
# ==============================================================================
"""
Crie uma classe "Sala" (com construtor) representando uma sala de uma
casa (ex: cozinha, quarto, sala de estar). O construtor deve receber:
  - nome_comodo
  - metragem (tamanho em m²)
  - itens (uma lista com pelo menos 3 itens que existem nesse cômodo)

Crie pelo menos 2 objetos "Sala" diferentes, passando os valores direto
no construtor, e imprima, para cada um, o nome do cômodo, a metragem e a
lista de itens.
"""

# TODO (desafio extra): crie a classe Sala (com __init__) e os objetos aqui


# ==============================================================================
# PARA PENSAR (sem escrever código - responda como comentário)
# ==============================================================================
"""
Tente, de propósito, criar um objeto da Parte 5 esquecendo de passar UM
dos argumentos na chamada do construtor (ex: Carro("Fiat", "Uno", "branco")
sem a velocidade_max).

O que acontece? Copie a mensagem de erro aqui como comentário e explique,
com suas palavras:
  - Por que esse erro aconteceu?
  - Em que esse erro é DIFERENTE do problema que vimos na aula quando
    ainda não usávamos construtor (aquele AttributeError que só aparecia
    quando a gente tentava USAR o atributo esquecido)?
"""

# TODO: cole aqui o erro que você viu e sua explicação


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
