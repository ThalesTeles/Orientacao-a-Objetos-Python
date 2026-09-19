"""
==============================================================================
EXERCÍCIO DE SALA - HERANÇA, SOBRESCRITA E AGREGAÇÃO
==============================================================================

Nesta atividade vamos RECONSTRUIR as classes de Animal que criamos na
aula 5, agora aplicando os conceitos de herança que acabamos de ver.

Complete os espaços marcados com o comentário # TODO.
Depois de completar cada parte, execute o arquivo para conferir se os
prints aparecem corretamente.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - CLASSE BASE COM CONSTRUTOR E MÉTODOS
# ==============================================================================
"""
Crie uma classe "Animal" com um construtor __init__ que recebe e guarda:
  - nome
  - especie
  - idade

Adicione também dois métodos:
  - apresentar(self): imprime algo como
      "Rex é um(a) cachorro de 3 anos."
  - fazer_som(self): imprime
      "Este animal faz um som genérico."
    (esse método vai ser SOBRESCRITO pelas subclasses depois)
"""

# TODO: crie a classe Animal aqui, com __init__, apresentar() e fazer_som()


# ==============================================================================
# PARTE 2 - SUBCLASSES COM HERANÇA
# ==============================================================================
"""
Crie duas subclasses de Animal: "Cachorro" e "Gato".

Cada uma deve SOBRESCREVER o método fazer_som():
  - Cachorro.fazer_som() deve imprimir algo como "Rex faz: Au au!"
  - Gato.fazer_som() deve imprimir algo como "Mimi faz: Miau!"

Dica: as subclasses NÃO precisam reescrever o __init__ nem o
apresentar() - eles já vêm herdados da classe Animal!
"""

# TODO: crie a classe Cachorro(Animal) aqui, sobrescrevendo fazer_som()


# TODO: crie a classe Gato(Animal) aqui, sobrescrevendo fazer_som()


# ==============================================================================
# PARTE 3 - CRIANDO OS OBJETOS
# ==============================================================================
"""
Crie um objeto Cachorro e um objeto Gato, com valores de nome, especie
e idade à sua escolha. Em seguida, para cada um deles, chame:
  - apresentar()
  - fazer_som()
"""

# TODO: crie o objeto cachorro aqui e chame apresentar() e fazer_som()


# TODO: crie o objeto gato aqui e chame apresentar() e fazer_som()


# ==============================================================================
# PARTE 4 - MAIS UM TIPO DE ANIMAL
# ==============================================================================
"""
Crie uma TERCEIRA subclasse de Animal, com o animal que você quiser
(pode ser um bicho de estimação real, um animal exótico, ou até um
animal fictício/lendário). Sobrescreva o método fazer_som() com um som
apropriado para esse animal.

Crie um objeto dessa nova classe e chame apresentar() e fazer_som().
"""

# TODO: crie a subclasse do seu animal aqui


# TODO: crie o objeto e chame apresentar() e fazer_som() aqui


# ==============================================================================
# PARTE 5 - MESMA CHAMADA, SONS DIFERENTES
# ==============================================================================
"""
Coloque os três objetos de animais que você criou (cachorro, gato e o
terceiro animal) dentro de uma lista chamada "bichario".

Depois, percorra a lista com um "for" chamando fazer_som() para cada
animal - sem se preocupar em saber qual é a classe exata de cada um.
"""

# TODO: crie a lista "bichario" com os três animais


# TODO: percorra "bichario" com um for e chame fazer_som() para cada um


# ==============================================================================
# PARTE 6 - AGREGAÇÃO: O ZOOLÓGICO "TEM" ANIMAIS
# ==============================================================================
"""
Agora vamos praticar AGREGAÇÃO (a relação "tem um/tem vários").

Crie uma classe "Zoologico" com:
  - um construtor __init__ que recebe "nome" (nome do zoológico) e cria
    uma lista vazia chamada "animais"
  - um método "receber_animal(self, animal)" que adiciona um animal à
    lista "animais" e imprime algo como
      "Rex foi recebido no Zoológico Savana Feliz!"
  - um método "fazer_todos_os_sons(self)" que percorre a lista de
    animais e chama fazer_som() de cada um

IMPORTANTE: a classe Zoologico NÃO deve herdar de Animal! Um zoológico
não É UM animal, ele TEM VÁRIOS animais - isso é agregação, não herança.
"""

# TODO: crie a classe Zoologico aqui


# TODO: crie um objeto Zoologico com o nome que você quiser


# TODO: use receber_animal() para adicionar o cachorro, o gato e o
# terceiro animal ao zoológico


# TODO: chame fazer_todos_os_sons() no objeto Zoologico


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Qual foi a vantagem de usar herança em vez de escrever uma classe
Cachorro e uma classe Gato totalmente separadas (do jeito que faríamos
sem herança)? E por que o Zoologico usa agregação em vez de herança?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DO EXERCÍCIO
# ==============================================================================
