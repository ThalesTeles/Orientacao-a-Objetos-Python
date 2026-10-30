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

class PersonagemAntigo:
    pass


heroi_antigo = PersonagemAntigo()
heroi_antigo.nome = "Aldric"
heroi_antigo.vida = 100
heroi_antigo.forca = 20

"""
E vimos um problema: nada impedia a gente de criar um personagem
esquecendo de definir um atributo:

  novo_personagem = PersonagemAntigo()
  novo_personagem.nome = "Thalia"
  print(novo_personagem.forca)  # AttributeError!

Também ficou uma pergunta em aberto: onde morariam as AÇÕES do
personagem, tipo "atacar" ou "se curar"? Hoje vamos resolver os dois
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

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca


# Agora, para criar um objeto, PRECISAMOS passar nome, vida e forca:
heroi = Personagem("Aldric", 100, 20)
vilao = Personagem("Malvor", 150, 30)

print(f"{heroi.nome} tem {heroi.vida} de vida e {heroi.forca} de força.")
print(f"{vilao.nome} tem {vilao.vida} de vida e {vilao.forca} de força.")

"""
Se tentarmos criar um Personagem sem passar todos os argumentos, o
Python já nos avisa NA HORA, com um erro claro:

  Personagem("Thalia", 90)
  # TypeError: __init__() missing 1 required positional argument: 'forca'

Isso é bem melhor do que descobrir um AttributeError escondido lá na
frente do código, como acontecia na Aula 5!
"""

# ==============================================================================
# 3. O PARÂMETRO "self"
# ==============================================================================
"""
Reparem que o __init__ tem um primeiro parâmetro chamado "self", mas
quando chamamos Personagem("Aldric", 100, 20) só passamos 3 valores,
não 4. Por quê?

"self" representa o PRÓPRIO OBJETO que está sendo criado/usado. O
Python passa esse valor automaticamente - nós nunca escrevemos "self"
na hora de CHAMAR o método, só na hora de DEFINIR o método dentro da
classe.

Pense em "self" como "eu mesmo": dentro da classe, "self.nome" quer
dizer "o nome DESTE objeto especificamente".

Analogia: imagine uma ficha de cadastro em branco (a classe) e cada
pessoa que a preenche (o objeto). Quando a ficha diz "seu nome:", ela
não sabe de antemão quem vai preencher - "self" é como esse "seu", que
se refere a quem estiver preenchendo a ficha naquele momento.

Vamos provar que "self" é mesmo o objeto, comparando os endereços de
memória:
"""

print(heroi)
print(vilao)

"""
Cada objeto tem um endereço diferente (algo como
<__main__.Personagem object at 0x...>) - são "fichas" preenchidas de
forma independente, mesmo vindo do mesmo molde (classe).
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

class PersonagemComMetodos:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        alvo.vida -= self.forca
        print(f"{self.nome} ataca {alvo.nome} causando {self.forca} de dano!")

    def curar(self, quantidade):
        self.vida += quantidade
        print(f"{self.nome} se cura em {quantidade} pontos de vida!")

    def apresentar(self):
        print(f"Eu sou {self.nome}, tenho {self.vida} de vida e {self.forca} de força.")


guerreiro = PersonagemComMetodos("Bram", 120, 25)
mago = PersonagemComMetodos("Elandra", 80, 15)

guerreiro.apresentar()
mago.apresentar()

guerreiro.atacar(mago)
print(f"Vida de {mago.nome} após o ataque: {mago.vida}")

mago.curar(10)
print(f"Vida de {mago.nome} após se curar: {mago.vida}")

"""
Reparem que chamamos "guerreiro.atacar(mago)" passando só "mago" - o
"self" (que é o próprio "guerreiro") o Python já passa sozinho. Dentro
do método, "self" é quem ataca e "alvo" é quem recebe o ataque.
"""

# ==============================================================================
# 5. ESTADO DO OBJETO
# ==============================================================================
"""
ESTADO de um objeto é o conjunto de valores que seus atributos têm EM
UM DETERMINADO MOMENTO. O estado pode MUDAR ao longo do tempo, através
dos métodos.

No exemplo acima, a vida de "mago" mudou de 80 para 65 (depois do
ataque) e depois para 75 (depois de se curar) - o OBJETO continua
sendo o mesmo "mago", mas seu ESTADO foi mudando.
"""

print(f"Estado atual de {mago.nome}: vida = {mago.vida}")

guerreiro.atacar(mago)
print(f"Estado de {mago.nome} depois de outro ataque: vida = {mago.vida}")

"""
Isso é diferente de uma variável comum, tipo "x = 5". Um objeto carrega
VÁRIOS valores relacionados ao mesmo tempo (nome, vida, força...) e
métodos que sabem como alterar esses valores de forma consistente.
"""

# ==============================================================================
# 6. DIFERENÇA ENTRE CLASSE E OBJETO (REVISÃO)
# ==============================================================================
"""
Agora que já vimos construtores e métodos, vale reforçar a diferença:

  CLASSE  -> o molde. Define QUAIS atributos existirão (via __init__)
             e QUAIS comportamentos existirão (via métodos). Só existe
             UMA classe "Personagem" no nosso código.

  OBJETO  -> uma instância concreta da classe, com valores próprios
             para os atributos. Podemos ter VÁRIOS objetos Personagem
             ("guerreiro", "mago"...), cada um com seu próprio estado.

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

  mago2 = mago
  mago2.nome = "Sylra"
  print(mago.nome)
"""

mago2 = mago
mago2.nome = "Sylra"
print(f"mago.nome agora é: {mago.nome}")

"""
Surpresa: o nome de "mago" também mudou para "Sylra"! Isso acontece
porque "mago2 = mago" NÃO cria um novo objeto - ele só cria uma SEGUNDA
ETIQUETA ("mago2") apontando para o MESMO objeto na memória que "mago"
já apontava.

É diferente de variáveis "simples":

  a = 5
  b = a
  b = 10
  print(a)  # continua 5! números não têm esse comportamento.

Mas com objetos, "mago2 = mago" faz "mago" e "mago2" apontarem para a
MESMA "ficha" na memória. Alterar por um nome afeta o outro, porque só
existe UM objeto - só temos duas formas de "chamá-lo".

Se quisermos um objeto REALMENTE independente (uma cópia), precisamos
criar um novo objeto do zero, com o construtor:
"""

mago3 = PersonagemComMetodos("Vesper", 100, 18)  # objeto NOVO e independente
mago3.nome = "Outra Vesper"
print(f"mago.nome continua: {mago.nome}")  # não foi afetado

# ==============================================================================
# 8. CONSTRUTORES COM VALORES PADRÃO (PARÂMETROS OPCIONAIS)
# ==============================================================================
"""
Assim como em funções comuns, o __init__ pode ter parâmetros com valor
padrão (opcionais). Isso é útil quando um atributo costuma começar
sempre com o mesmo valor.
"""

class PersonagemNivel1:
    def __init__(self, nome, vida=100, forca=10, nivel=1):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.nivel = nivel

    def apresentar(self):
        print(f"{self.nome} (nível {self.nivel}) - vida: {self.vida}, força: {self.forca}")


# Posso passar só o nome, e os outros atributos usam o valor padrão:
novato = PersonagemNivel1("Finn")
novato.apresentar()

# Ou posso sobrescrever qualquer valor padrão que eu quiser:
veterano = PersonagemNivel1("Draven", vida=200, forca=40, nivel=15)
veterano.apresentar()

# ==============================================================================
# 9. EXEMPLIFICANDO EM DIVERSAS SITUAÇÕES
# ==============================================================================
"""
A combinação "atributos no __init__ + comportamentos em métodos" serve
para modelar praticamente qualquer coisa. Veja mais alguns exemplos:
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
atributos e métodos de outras classes (ex: Guerreiro e Mago herdando de
Personagem), além de AGREGAÇÃO (quando um objeto "tem" outro objeto,
como um Personagem que tem uma Mochila).
"""

# ==============================================================================
# FIM
# ==============================================================================
