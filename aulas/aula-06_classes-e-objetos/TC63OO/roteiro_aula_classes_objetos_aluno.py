"""
==============================================================================
AULA 6 - CLASSES X OBJETOS: MÉTODOS, SELF E CONSTRUTORES
==============================================================================

Este arquivo é um material de apoio. Você pode executá-lo no Python para
ver os exemplos funcionando na prática.

Pré-requisitos (Aula 5): o que são classes e objetos, atributos, a
diferença entre TEM (atributos) e FAZ (comportamentos).
==============================================================================
"""

# ==============================================================================
# 1. RETOMANDO O PROBLEMA DA AULA PASSADA
# ==============================================================================
"""
Na Aula 5 criamos classes assim:
"""

class PokemonAntigo:
    pass


pikachu_antigo = PokemonAntigo()
pikachu_antigo.nome = "Pikachu"
pikachu_antigo.hp = 60
pikachu_antigo.ataque = 10

"""
E vimos um problema: nada impedia a gente de criar um Pokémon esquecendo
de definir um atributo:

  novo_pokemon = PokemonAntigo()
  novo_pokemon.nome = "Squirtle"
  print(novo_pokemon.ataque)  # AttributeError!

Também ficou uma pergunta em aberto: onde morariam as AÇÕES do Pokémon,
tipo "usar um ataque" ou "se curar"? Hoje vamos resolver os dois
problemas.
"""

# ==============================================================================
# 2. O CONSTRUTOR: O MÉTODO __init__
# ==============================================================================
"""
CONSTRUTOR é um método especial que o Python executa AUTOMATICAMENTE
toda vez que um objeto é criado a partir de uma classe. Em Python, ele
se chama "__init__" (init de "inicializar").

Com o __init__, definimos quais atributos são OBRIGATÓRIOS para criar
um objeto daquela classe - ninguém mais esquece de definir um atributo!
"""

class Pokemon:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque


# Agora, para criar um objeto, PRECISAMOS passar nome, hp e ataque:
pikachu = Pokemon("Pikachu", 60, 10)
charizard = Pokemon("Charizard", 120, 30)

print(f"{pikachu.nome} tem {pikachu.hp} de HP e {pikachu.ataque} de ataque.")
print(f"{charizard.nome} tem {charizard.hp} de HP e {charizard.ataque} de ataque.")

"""
Se tentarmos criar um Pokemon sem passar todos os argumentos, o Python
já nos avisa NA HORA, com um erro claro:

  Pokemon("Squirtle", 70)
  # TypeError: __init__() missing 1 required positional argument: 'ataque'

Isso é bem melhor do que descobrir um AttributeError escondido lá na
frente do código, como acontecia na Aula 5!
"""

# ==============================================================================
# 3. O PARÂMETRO "self"
# ==============================================================================
"""
Reparem que o __init__ tem um primeiro parâmetro chamado "self", mas
quando chamamos Pokemon("Pikachu", 60, 10) só passamos 3 valores, não 4.
Por quê?

"self" representa o PRÓPRIO OBJETO que está sendo criado/usado. O
Python passa esse valor automaticamente - nós nunca escrevemos "self"
na hora de CHAMAR o método, só na hora de DEFINIR o método dentro da
classe.

Pense em "self" como "eu mesmo": dentro da classe, "self.nome" quer
dizer "o nome DESTE objeto especificamente".

Analogia: imagine uma carta de Pokémon em branco (a classe) e cada
carta específica que a preenche (o objeto). Quando o molde diz "nome:",
"HP:", "ataque:", ele não sabe de antemão qual Pokémon vai preencher
aqueles espaços - "self" é como essa carta genérica, "esta aqui que
estou preenchendo agora".

Vamos provar que "self" é mesmo o objeto, comparando os endereços de
memória:
"""

print(pikachu)
print(charizard)

"""
Cada objeto tem um endereço diferente (algo como
<__main__.Pokemon object at 0x...>) - são "cartas" preenchidas de forma
independente, mesmo vindo do mesmo molde (classe).
"""

# ==============================================================================
# 4. MÉTODOS: OS COMPORTAMENTOS DO OBJETO
# ==============================================================================
"""
MÉTODOS são funções definidas DENTRO de uma classe, que representam o
que aquele objeto "FAZ". Assim como o __init__, todo método recebe
"self" como primeiro parâmetro, para poder acessar os atributos daquele
objeto específico.
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
Reparem que chamamos "charizard.atacar(blastoise)" passando só
"blastoise" - o "self" (que é o próprio "charizard") o Python já passa
sozinho. Dentro do método, "self" é quem ataca e "alvo" é quem recebe o
ataque - bem parecido com uma carta "usando" um ataque contra a carta
ativa do adversário no card game.
"""

# ==============================================================================
# 5. ESTADO DO OBJETO
# ==============================================================================
"""
ESTADO de um objeto é o conjunto de valores que seus atributos têm EM
UM DETERMINADO MOMENTO. O estado pode MUDAR ao longo do tempo, através
dos métodos.

No exemplo acima, o HP de "blastoise" mudou de 80 para 65 (depois do
ataque) e depois para 75 (depois de se curar) - o OBJETO continua
sendo o mesmo "blastoise", mas seu ESTADO foi mudando. É como a mesma
carta em jogo acumulando (ou perdendo) marcadores de dano.
"""

print(f"Estado atual de {blastoise.nome}: HP = {blastoise.hp}")

charizard.atacar(blastoise)
print(f"Estado de {blastoise.nome} depois de outro ataque: HP = {blastoise.hp}")

"""
Isso é diferente de uma variável comum, tipo "x = 5". Um objeto carrega
VÁRIOS valores relacionados ao mesmo tempo (nome, HP, ataque...) e
métodos que sabem como alterar esses valores de forma consistente.
"""

# ==============================================================================
# 6. DIFERENÇA ENTRE CLASSE E OBJETO (REVISÃO)
# ==============================================================================
"""
Agora que já vimos construtores e métodos, vale reforçar a diferença:

  CLASSE  -> o molde. Define QUAIS atributos existirão (via __init__)
             e QUAIS comportamentos existirão (via métodos). Só existe
             UMA classe "Pokemon" no nosso código - é a "regra geral"
             de como qualquer Pokémon funciona no programa.

  OBJETO  -> uma instância concreta da classe, com valores próprios
             para os atributos. Podemos ter VÁRIOS objetos Pokemon
             ("charizard", "blastoise"...), cada um com seu próprio
             estado - cada um é uma carta específica que existe de
             verdade na "mesa" (na memória).

Os MÉTODOS (o comportamento) são definidos uma única vez na classe, mas
cada objeto os executa "vestindo" seus próprios atributos, graças ao
"self".
"""

# ==============================================================================
# 7. OBJETOS x VARIÁVEIS
# ==============================================================================
"""
Aqui vem uma pegadinha importante. O que você acha que este código
imprime?

  blastoise2 = blastoise
  blastoise2.nome = "Blastoise de Ouro"
  print(blastoise.nome)
"""

blastoise2 = blastoise
blastoise2.nome = "Blastoise de Ouro"
print(f"blastoise.nome agora é: {blastoise.nome}")

"""
Surpresa: o nome de "blastoise" também mudou para "Blastoise de Ouro"!
Isso acontece porque "blastoise2 = blastoise" NÃO cria um novo objeto -
ele só cria uma SEGUNDA ETIQUETA ("blastoise2") apontando para o MESMO
objeto na memória que "blastoise" já apontava.

É diferente de variáveis "simples":

  a = 5
  b = a
  b = 10
  print(a)  # continua 5! números não têm esse comportamento.

Mas com objetos, "blastoise2 = blastoise" faz "blastoise" e "blastoise2"
apontarem para a MESMA "carta" na memória. Alterar por um nome afeta o
outro, porque só existe UM objeto - só temos duas formas de "chamá-lo".
Não é como ter duas cópias da mesma carta no baralho!

Se quisermos um objeto REALMENTE independente (uma cópia), precisamos
criar um novo objeto do zero, com o construtor:
"""

venusaur = PokemonComMetodos("Venusaur", 100, 18)  # objeto NOVO e independente
venusaur.nome = "Venusaur Sombrio"
print(f"blastoise.nome continua: {blastoise.nome}")  # não foi afetado

# ==============================================================================
# 8. CONSTRUTORES COM VALORES PADRÃO (PARÂMETROS OPCIONAIS)
# ==============================================================================
"""
Assim como em funções comuns, o __init__ pode ter parâmetros com valor
padrão (opcionais). Isso é útil quando um atributo costuma começar
sempre com o mesmo valor.

Vamos aproveitar um conceito real do Pokémon TCG: o ESTÁGIO da carta
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


# Posso passar só o nome, e os outros atributos usam o valor padrão:
novato = PokemonCarta("Caterpie")
novato.apresentar()

# Ou posso sobrescrever qualquer valor padrão que eu quiser:
evoluido = PokemonCarta("Charizard", hp=180, dano=120, estagio="Estágio 2")
evoluido.apresentar()

"""
Isso reflete uma regra real do jogo: Caterpie é uma carta Básica simples
(por isso os valores padrão bastam), já Charizard é Estágio 2 - evolui
de Charmander para Charmeleon e depois para Charizard - por isso tem HP
e dano bem mais altos que o padrão.
"""

# ==============================================================================
# 9. EXEMPLIFICANDO EM DIVERSAS SITUAÇÕES
# ==============================================================================
"""
A combinação "atributos no __init__ + comportamentos em métodos" serve
para modelar praticamente qualquer coisa - não só Pokémon! Veja mais
alguns exemplos de domínios bem diferentes:
"""

# --- Exemplo 1: Animal ---
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


# --- Exemplo 2: Pessoa ---
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def eh_maior_de_idade(self):
        return self.idade >= 18


aluno1 = Pessoa("Marina", 17)
print(f"{aluno1.nome} é maior de idade? {aluno1.eh_maior_de_idade()}")


# --- Exemplo 3: Triângulo ---
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


triangulo1 = Triangulo(base=10, altura=4)
print(f"Área do triângulo: {triangulo1.calcular_area()}")


# --- Exemplo 4: Carro ---
class Carro:
    def __init__(self, modelo, velocidade_max):
        self.modelo = modelo
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0  # todo carro começa parado

    def acelerar(self, quantidade):
        nova_velocidade = self.velocidade_atual + quantidade
        self.velocidade_atual = min(nova_velocidade, self.velocidade_max)
        print(f"{self.modelo} agora está a {self.velocidade_atual} km/h")


carro1 = Carro("Fusca", velocidade_max=120)
carro1.acelerar(50)
carro1.acelerar(100)  # não deve passar de 120, mesmo pedindo mais

"""
Reparem no Carro: "velocidade_atual" começa em 0 dentro do próprio
__init__, sem precisar ser passado como argumento - é um exemplo de
ESTADO inicial controlado pela própria classe.
"""

# ==============================================================================
# 10. PRÉVIA DA PRÓXIMA AULA
# ==============================================================================
"""
Na Aula 7 vamos aprender HERANÇA: como criar classes que reaproveitam
atributos e métodos de outras classes (ex: Charizard e Blastoise
herdando de uma classe Pokemon comum), além de AGREGAÇÃO (quando um
objeto "tem" outro objeto, como um Treinador que tem um ou mais
Pokémon).
"""

# ==============================================================================
# FIM
# ==============================================================================
