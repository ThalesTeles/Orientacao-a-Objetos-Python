"""
==============================================================================
ROTEIRO DE AULA 6 - CLASSES X OBJETOS: MÉTODOS, SELF E CONSTRUTORES
Público-alvo: alunos de 15 a 19 anos
Duração sugerida: 1h30 a 2h
Módulo: POO (aula 6 de 8 do módulo) | Aula anterior: "Introdução à POO"
Próxima aula: "Herança e outras relações" (agregação, override, super())
==============================================================================

Este arquivo é um roteiro comentado. Ele pode ser executado no Python para
que os alunos vejam os exemplos rodando ao vivo, enquanto o professor segue
a explicação nos comentários.

Versão temática: os exemplos principais usam Pokémon (nome, hp, ataque),
pensados para engajar a turma - especialmente quem curte Pokémon TCG.

Sugestão de dinâmica: projete este arquivo e vá executando trecho por trecho
(ou copie os blocos para o terminal/REPL) conforme avança na explicação.
==============================================================================
"""

# ==============================================================================
# 1. RETOMANDO O PROBLEMA DA AULA PASSADA (10 min)
# ==============================================================================
"""
Comece relembrando o "gancho" que ficou da Aula 5: perguntar à turma se
alguém lembra do problema do AttributeError (esquecer de definir um
atributo) e da pergunta em aberto sobre "onde moram as ações do Pokémon".

Rode o exemplo abaixo para reativar a memória da turma.
"""

class PokemonAntigo:
    pass


pikachu_antigo = PokemonAntigo()
pikachu_antigo.nome = "Pikachu"
pikachu_antigo.hp = 60
pikachu_antigo.ataque = 10

"""
Reforce: hoje vamos resolver os dois problemas de uma vez - o construtor
garante os atributos, e os métodos vão hospedar as ações (os "ataques").
"""

# ==============================================================================
# 2. O CONSTRUTOR: O MÉTODO __init__ (15 min)
# ==============================================================================
"""
Apresente a definição:

CONSTRUTOR é um método especial executado AUTOMATICAMENTE pelo Python
toda vez que um objeto é criado. Em Python, se chama "__init__".
"""

class Pokemon:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque


pikachu = Pokemon("Pikachu", 60, 10)
charizard = Pokemon("Charizard", 120, 30)

print(f"{pikachu.nome} tem {pikachu.hp} de HP e {pikachu.ataque} de ataque.")
print(f"{charizard.nome} tem {charizard.hp} de HP e {charizard.ataque} de ataque.")

"""
Demonstração AO VIVO (importante): tente rodar

  Pokemon("Squirtle", 70)

e mostre o TypeError na tela (falta o argumento "ataque"). Compare com o
AttributeError "silencioso" da aula passada - agora o erro aparece
IMEDIATAMENTE, no momento da criação, e não escondido lá na frente do
código. Essa comparação costuma ser o "momento aha" da aula.

Dica: se a turma manjar de Pokémon TCG, vale comentar que toda carta
sempre TEM nome, HP e um ataque com dano - o construtor está só
garantindo em código o que já é natural para quem joga o card game.
"""

# ==============================================================================
# 3. O PARÂMETRO "self" (15 min)
# ==============================================================================
"""
Este é tipicamente o ponto mais confuso da aula - vá com calma.

Explique: "self" representa o PRÓPRIO OBJETO. O Python passa esse valor
sozinho; nunca escrevemos "self" ao CHAMAR o método, só ao DEFINI-LO.

Analogia sugerida: uma carta de Pokémon em branco (a classe) que várias
cartas específicas preenchem (os objetos). Quando o molde da carta diz
"nome:", "HP:", "ataque:", ele não sabe de antemão qual Pokémon vai
preencher aqueles espaços - "self" é essa carta genérica, "esta aqui
que estou preenchendo agora".

Prove que self é mesmo o objeto mostrando os endereços de memória:
"""

print(pikachu)
print(charizard)

"""
Pergunta para a turma: "Por que esses dois prints mostram endereços
diferentes, mesmo vindo da mesma classe Pokemon?"
(Resposta esperada: são objetos DIFERENTES, cada um sua própria carta
preenchida - self, dentro do método, aponta para a carta correspondente
a quem chamou o método.)
"""

# ==============================================================================
# 4. MÉTODOS: OS COMPORTAMENTOS DO OBJETO (15 min)
# ==============================================================================
"""
Agora finalmente respondemos à pergunta que ficou em aberto na aula
passada: "onde moram as ações do Pokémon?" - dentro de MÉTODOS, funções
definidas dentro da classe que sempre recebem "self" primeiro.
"""

class PokemonComMetodos:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

    def atacar(self, alvo):
        alvo.hp -= self.ataque
        print(f"{self.nome} usa um ataque em {alvo.nome} causando {self.ataque} de dano!")

    def curar(self, quantidade):
        self.hp += quantidade
        print(f"{self.nome} recupera {quantidade} pontos de HP!")

    def apresentar(self):
        print(f"Eu sou {self.nome}, tenho {self.hp} de HP e {self.ataque} de ataque.")


charizard = PokemonComMetodos("Charizard", 120, 25)
blastoise = PokemonComMetodos("Blastoise", 80, 15)

charizard.apresentar()
blastoise.apresentar()

charizard.atacar(blastoise)
print(f"HP de {blastoise.nome} após o ataque: {blastoise.hp}")

blastoise.curar(10)
print(f"HP de {blastoise.nome} após se curar: {blastoise.hp}")

"""
Destaque: "charizard.atacar(blastoise)" passa só "blastoise" como
argumento - "self" (o próprio charizard) é passado automaticamente pelo
Python. Peça para a turma identificar, em voz alta, quem é "self" e
quem é "alvo" dentro do método atacar().

Se sobrar gancho, comente que isso é bem parecido com o card game: uma
carta "usa" um ataque contra a carta ativa do adversário - o "self" é
sempre quem está atacando.
"""

# ==============================================================================
# 5. ESTADO DO OBJETO (10 min)
# ==============================================================================
"""
Introduza o termo ESTADO: o conjunto de valores dos atributos de um
objeto EM UM DADO MOMENTO, que muda através dos métodos - no card game,
seria como as fichas/contadores de dano em cima de uma carta na mesa.
"""

print(f"Estado atual de {blastoise.nome}: HP = {blastoise.hp}")

charizard.atacar(blastoise)
print(f"Estado de {blastoise.nome} depois de outro ataque: HP = {blastoise.hp}")

"""
Pergunta para reflexão: "O objeto 'blastoise' continua sendo o mesmo
objeto depois do segundo ataque? O que mudou nele?"
(Resposta esperada: é o MESMO objeto - só o ESTADO [HP] mudou. É a
mesma carta em jogo, só que com mais dano marcado nela.)
"""

# ==============================================================================
# 6. DIFERENÇA ENTRE CLASSE E OBJETO (REVISÃO) (5 min)
# ==============================================================================
"""
Revisão rápida e falada (sem novo código):
  CLASSE = molde único, define atributos (via __init__) e comportamentos
           (via métodos). É como a "regra geral" de como qualquer
           Pokémon funciona no nosso programa.
  OBJETO = instância concreta, com valores próprios e estado que muda.
           É cada carta específica (Charizard, Blastoise...) que existe
           de verdade na "mesa" (na memória).

Reforce que os métodos são escritos UMA VEZ na classe, mas cada objeto
os "veste" com seus próprios dados via self - assim como a regra de
"como um ataque funciona" é a mesma para todas as cartas, mas o dano
causado depende dos atributos daquela carta específica.
"""

# ==============================================================================
# 7. OBJETOS x VARIÁVEIS (15 min)
# ==============================================================================
"""
Esta é uma pegadinha clássica e MUITO importante - reserve um tempo bom
para ela.

Pergunte à turma o que ela acha que vai imprimir ANTES de rodar:

  blastoise2 = blastoise
  blastoise2.nome = "Blastoise de Ouro"
  print(blastoise.nome)
"""

blastoise2 = blastoise
blastoise2.nome = "Blastoise de Ouro"
print(f"blastoise.nome agora é: {blastoise.nome}")

"""
A maioria da turma provavelmente vai esperar que "blastoise.nome"
continue "Blastoise" - surpreenda mostrando que ele também virou
"Blastoise de Ouro".

Explique com a analogia de ETIQUETAS: "blastoise" e "blastoise2" são
duas ETIQUETAS apontando para a MESMA carta (objeto) na memória. Não
existem duas cartas, só uma - com duas etiquetas coladas nela. Não é
como ter duas cópias da carta no baralho!

Compare com números, que NÃO se comportam assim:

  a = 5
  b = a
  b = 10
  print(a)  # continua 5!
"""

a = 5
b = a
b = 10
print(f"a continua sendo: {a}")

"""
Mostre a forma correta de ter um objeto de verdade independente: criar
um objeto NOVO com o construtor, não copiar a variável.
"""

venusaur = PokemonComMetodos("Venusaur", 100, 18)
venusaur.nome = "Venusaur Sombrio"
print(f"blastoise.nome continua: {blastoise.nome}")  # não foi afetado

"""
Dica pedagógica: se sobrar tempo, peça para a turma prever o resultado
de mais um ou dois exemplos de aliasing antes de rodar, para fixar o
conceito - é um erro comum mesmo em alunos mais avançados. Pode
aproveitar o gancho: "Charizard, Blastoise e Venusaur" são os três
iniciais clássicos - boa deixa para comentar rapidamente.
"""

# ==============================================================================
# 8. CONSTRUTORES COM VALORES PADRÃO (10 min)
# ==============================================================================
"""
Mostre que __init__ aceita parâmetros com valor padrão, do mesmo jeito
que funções comuns (assunto que a turma já viu no curso de algoritmos).

Aproveite para trazer um conceito real do TCG: o ESTÁGIO da carta
(Básico, Estágio 1, Estágio 2), que também pode ter um valor padrão.
"""

class PokemonCarta:
    def __init__(self, nome, hp=100, dano=10, estagio="Básico"):
        self.nome = nome
        self.hp = hp
        self.dano = dano
        self.estagio = estagio

    def apresentar(self):
        print(f"{self.nome} ({self.estagio}) - HP: {self.hp}, dano: {self.dano}")


novato = PokemonCarta("Caterpie")
novato.apresentar()

evoluido = PokemonCarta("Charizard", hp=180, dano=120, estagio="Estágio 2")
evoluido.apresentar()

"""
Dica para o professor: se a turma manjar de TCG, comente que isso
reflete a regra real do jogo - Caterpie é uma carta Básica simples, já
Charizard é Estágio 2 (evolui de Charmander -> Charmeleon -> Charizard),
por isso tem HP e dano bem mais altos. Bom gancho para reforçar que
"valor padrão" não é regra fixa - é só o que a maioria dos casos usa.
"""

# ==============================================================================
# 9. EXEMPLIFICANDO EM DIVERSAS SITUAÇÕES (15 min)
# ==============================================================================
"""
Percorra rapidamente os quatro exemplos abaixo (Animal, Pessoa,
Triângulo, Carro), pedindo para a turma identificar, em cada um:
  - quais são os atributos (definidos no __init__)?
  - quais são os métodos (comportamentos)?

Dica para o professor: vale comentar explicitamente com a turma por que
esses exemplos NÃO são sobre Pokémon - a ideia é mostrar que POO serve
para modelar QUALQUER coisa (pessoas, formas geométricas, veículos...),
não só jogos e personagens.
"""

class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} completou {self.idade} anos!")


rex = Animal("Rex", "cachorro", 3)
rex.fazer_aniversario()


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def eh_maior_de_idade(self):
        return self.idade >= 18


aluno1 = Pessoa("Marina", 17)
print(f"{aluno1.nome} é maior de idade? {aluno1.eh_maior_de_idade()}")


class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


triangulo1 = Triangulo(base=10, altura=4)
print(f"Área do triângulo: {triangulo1.calcular_area()}")


class Carro:
    def __init__(self, modelo, velocidade_max):
        self.modelo = modelo
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self, quantidade):
        nova_velocidade = self.velocidade_atual + quantidade
        self.velocidade_atual = min(nova_velocidade, self.velocidade_max)
        print(f"{self.modelo} agora está a {self.velocidade_atual} km/h")


carro1 = Carro("Fusca", velocidade_max=120)
carro1.acelerar(50)
carro1.acelerar(100)

"""
Destaque o caso do Carro: "velocidade_atual" começa em 0 dentro do
próprio __init__, SEM precisar ser passado como argumento - ótimo
exemplo de estado inicial controlado pela classe, e de um método
(acelerar) que respeita uma regra de negócio (não passar do limite).
"""

# ==============================================================================
# 10. FECHAMENTO E PRÉVIA DA AULA 7 (5 min)
# ==============================================================================
"""
Recapitule com a turma:
  - __init__ garante que todo objeto nasça com os atributos certos.
  - self representa o próprio objeto dentro dos métodos.
  - Métodos são o "FAZ" da classe; atributos são o "TEM".
  - Estado é o valor dos atributos em um dado momento - muda através
    dos métodos.
  - Atenção ao aliasing: "obj2 = obj1" não copia, cria uma segunda
    etiqueta para o MESMO objeto - não é como ter duas cópias da
    mesma carta.

Avise que a Aula 7 ("Herança e outras relações") vai:
  - Ensinar como reaproveitar atributos e métodos entre classes
    parecidas (herança - relação "é um"), ex: Charizard e Blastoise
    herdando de uma classe Pokemon comum.
  - Mostrar como sobrescrever métodos herdados (override) e super().
  - Apresentar agregação (relação "tem um"), como um Treinador que TEM
    um ou mais Pokémon.

Direcione a turma para a atividade de sala: a classe "Animal" (cachorro,
gato) que a turma já construiu na Aula 5 já usa __init__ - hoje o
trabalho é ADICIONAR MÉTODOS a ela (ex: fazer_aniversario, emitir_som),
sem precisar refazer os atributos do zero.
"""

# ==============================================================================
# FIM DO ROTEIRO
# ==============================================================================
