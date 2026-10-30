"""
==============================================================================
AULA 5 - ATIVIDADE DE SALA - CLASSES, OBJETOS E CONSTRUTOR
==============================================================================

Nesta atividade você vai montar a base de um aplicativo de músicas.

Complete os trechos marcados com # TODO e execute o arquivo depois de
cada parte para ver se está funcionando.

Toda classe que você criar deve ter um construtor (__init__) que recebe
os atributos como parâmetros. Métodos além do __init__ ficam para a
próxima aula.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - A CLASSE MUSICA
# ==============================================================================
"""
Crie a classe "Musica" com um construtor que recebe e guarda:
  - titulo
  - artista
  - duracao   (em segundos, ex: 215)
"""

# TODO: crie a classe Musica aqui


# ==============================================================================
# PARTE 2 - CRIANDO MÚSICAS
# ==============================================================================
"""
Crie três objetos Musica com músicas que você gosta. Use nomes de
variáveis que façam sentido, como "musica1", "musica2" e "musica3".

Depois, faça um print para cada música mostrando título e artista:

  "Evidências, de Chitãozinho & Xororó"
"""

# TODO: crie os três objetos aqui


# TODO: faça os prints aqui


# ==============================================================================
# PARTE 3 - USANDO OS ATRIBUTOS EM CONTAS
# ==============================================================================
"""
A duração está guardada em segundos, mas aplicativo nenhum mostra
"279 segundos". Para cada música, calcule os minutos e os segundos a
partir do atributo "duracao":

  minutos = musica1.duracao // 60
  segundos = musica1.duracao % 60

E mostre no formato:

  "Evidências, de Chitãozinho & Xororó (4:39)"

Se aparecer algo como "3:5" em vez de "3:05", use {segundos:02d} dentro
da f-string. Isso obriga o número a ter dois dígitos.
"""

# TODO: mostre as três músicas com a duração em minutos e segundos


# ==============================================================================
# PARTE 4 - CADA OBJETO TEM SEUS PRÓPRIOS DADOS
# ==============================================================================
"""
Você percebeu que digitou o nome do artista errado em uma das músicas.
Corrija direto no objeto, sem criar a música de novo:

  musica2.artista = "Nome Certo"

Depois imprima o artista das três músicas. Só uma deve ter mudado.

Responda em um comentário: por que mudar musica2 não afetou musica1 e
musica3, se as três foram criadas pela mesma classe?
"""

# TODO: corrija o artista de uma música e imprima o artista das três


# TODO: escreva sua resposta aqui


# ==============================================================================
# PARTE 5 - QUANDO O CONSTRUTOR RECLAMA (E QUANDO NÃO RECLAMA)
# ==============================================================================
"""
a) Tente criar uma música esquecendo a duração:

     teste = Musica("Bohemian Rhapsody", "Queen")

   Rode, copie a mensagem de erro para um comentário e depois apague ou
   comente essa linha para o resto do arquivo voltar a funcionar.

b) Agora crie uma música trocando a ordem do título e do artista:

     teste = Musica("Queen", "Bohemian Rhapsody", 354)

   Imprima o título e o artista. O Python reclamou dessa vez? O que
   aconteceu com os dados?

c) Para evitar esse tipo de confusão, dá para passar os valores dizendo
   o nome de cada parâmetro. Assim a ordem não importa:

     teste = Musica(artista="Queen", duracao=354, titulo="Bohemian Rhapsody")

   Crie uma quarta música desse jeito e imprima título e artista para
   conferir.
"""

# TODO a): cole o erro aqui como comentário


# TODO b): crie a música com a ordem trocada e imprima


# TODO c): crie a quarta música com os nomes dos parâmetros e imprima


# ==============================================================================
# PARTE 6 - VÁRIOS OBJETOS EM UMA LISTA
# ==============================================================================
"""
Coloque as suas músicas em uma lista chamada "playlist" e use um for
para mostrar todas, no mesmo formato da Parte 3.

Repare que dentro do for você escreve o print uma vez só e ele funciona
para todas as músicas.
"""

# TODO: crie a lista playlist


# TODO: percorra a playlist com um for e mostre cada música


# ==============================================================================
# PARTE 7 - SUA VEZ
# ==============================================================================
"""
Escolha uma coisa do seu dia a dia para virar classe. Pode ser um jogo,
um filme, uma série, um tênis, um prato de comida, o que quiser.

  1. Crie a classe com um construtor de pelo menos 3 atributos.
     Pelo menos um deles deve ser um número.
  2. Crie dois objetos dessa classe.
  3. Faça um print de cada objeto que use o atributo numérico em alguma
     conta (ex: preço com desconto, nota de 0 a 100 virando nota de 0 a 10,
     ano de lançamento virando "lançado há X anos").
"""

# TODO: crie sua classe, os objetos e os prints aqui


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
