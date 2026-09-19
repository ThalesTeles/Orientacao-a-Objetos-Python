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
atributo) e da pergunta em aberto sobre "onde moram as ações do
personagem".

Rode o exemplo abaixo para reativar a memória da turma.
"""

class PersonagemAntigo:
    pass


heroi_antigo = PersonagemAntigo()
heroi_antigo.nome = "Aldric"
heroi_antigo.vida = 100
heroi_antigo.forca = 20

"""
Reforce: hoje vamos resolver os dois problemas de uma vez - o construtor
garante os atributos, e os métodos vão hospedar as ações.
"""

# ==============================================================================
# 2. O CONSTRUTOR: O MÉTODO __init__ (15 min)
# ==============================================================================
"""
Apresente a definição:

CONSTRUTOR é um método especial executado AUTOMATICAMENTE pelo Python
toda vez que um objeto é criado. Em Python, se chama "__init__".
"""

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca


heroi = Personagem("Aldric", 100, 20)
vilao = Personagem("Malvor", 150, 30)

print(f"{heroi.nome} tem {heroi.vida} de vida e {heroi.forca} de força.")
print(f"{vilao.nome} tem {vilao.vida} de vida e {vilao.forca} de força.")

"""
Demonstração AO VIVO (importante): tente rodar

  Personagem("Thalia", 90)

e mostre o TypeError na tela. Compare com o AttributeError "silencioso"
da aula passada - agora o erro aparece IMEDIATAMENTE, no momento da
criação, e não escondido lá na frente do código. Essa comparação costuma
ser o "momento aha" da aula.
"""

# ==============================================================================
# 3. O PARÂMETRO "self" (15 min)
# ==============================================================================
"""
Este é tipicamente o ponto mais confuso da aula - vá com calma.

Explique: "self" representa o PRÓPRIO OBJETO. O Python passa esse valor
sozinho; nunca escrevemos "self" ao CHAMAR o método, só ao DEFINI-LO.

Analogia sugerida: uma ficha de cadastro em branco (classe) que várias
pessoas preenchem (objetos). Quando a ficha diz "seu nome:", ela não
sabe de antemão quem vai preencher - "self" é esse "seu" genérico.

Prove que self é mesmo o objeto mostrando os endereços de memória:
"""

print(heroi)
print(vilao)

"""
Pergunta para a turma: "Por que esses dois prints mostram endereços
diferentes, mesmo vindo da mesma classe Personagem?"
(Resposta esperada: são objetos DIFERENTES, cada um com sua própria
ficha preenchida - self, dentro do método, aponta para a ficha
correspondente a quem chamou o método.)
"""

# ==============================================================================
# 4. MÉTODOS: OS COMPORTAMENTOS DO OBJETO (15 min)
# ==============================================================================
"""
Agora finalmente respondemos à pergunta que ficou em aberto na aula
passada: "onde moram as ações do personagem?" - dentro de MÉTODOS,
funções definidas dentro da classe que sempre recebem "self" primeiro.
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
Destaque: "guerreiro.atacar(mago)" passa só "mago" como argumento -
"self" (o próprio guerreiro) é passado automaticamente pelo Python.
Peça para a turma identificar, em voz alta, quem é "self" e quem é
"alvo" dentro do método atacar().
"""

# ==============================================================================
# 5. ESTADO DO OBJETO (10 min)
# ==============================================================================
"""
Introduza o termo ESTADO: o conjunto de valores dos atributos de um
objeto EM UM DADO MOMENTO, que muda através dos métodos.
"""

print(f"Estado atual de {mago.nome}: vida = {mago.vida}")

guerreiro.atacar(mago)
print(f"Estado de {mago.nome} depois de outro ataque: vida = {mago.vida}")

"""
Pergunta para reflexão: "O objeto 'mago' continua sendo o mesmo objeto
depois do segundo ataque? O que mudou nele?"
(Resposta esperada: é o MESMO objeto - só o ESTADO [vida] mudou.)
"""

# ==============================================================================
# 6. DIFERENÇA ENTRE CLASSE E OBJETO (REVISÃO) (5 min)
# ==============================================================================
"""
Revisão rápida e falada (sem novo código):
  CLASSE = molde único, define atributos (via __init__) e comportamentos
           (via métodos).
  OBJETO = instância concreta, com valores próprios e estado que muda.

Reforce que os métodos são escritos UMA VEZ na classe, mas cada objeto
os "veste" com seus próprios dados via self.
"""

# ==============================================================================
# 7. OBJETOS x VARIÁVEIS (15 min)
# ==============================================================================
"""
Esta é uma pegadinha clássica e MUITO importante - reserve um tempo bom
para ela.

Pergunte à turma o que ela acha que vai imprimir ANTES de rodar:

  mago2 = mago
  mago2.nome = "Sylra"
  print(mago.nome)
"""

mago2 = mago
mago2.nome = "Sylra"
print(f"mago.nome agora é: {mago.nome}")

"""
A maioria da turma provavelmente vai esperar que "mago.nome" continue
"Elandra" - surpreenda mostrando que ele também virou "Sylra".

Explique com a analogia de ETIQUETAS: "mago" e "mago2" são duas
ETIQUETAS apontando para a MESMA caixa (objeto) na memória. Não existem
duas caixas, só uma - com duas etiquetas coladas nela.

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

mago3 = PersonagemComMetodos("Vesper", 100, 18)
mago3.nome = "Outra Vesper"
print(f"mago.nome continua: {mago.nome}")  # não foi afetado

"""
Dica pedagógica: se sobrar tempo, peça para a turma prever o resultado
de mais um ou dois exemplos de aliasing antes de rodar, para fixar o
conceito - é um erro comum mesmo em alunos mais avançados.
"""

# ==============================================================================
# 8. CONSTRUTORES COM VALORES PADRÃO (10 min)
# ==============================================================================
"""
Mostre que __init__ aceita parâmetros com valor padrão, do mesmo jeito
que funções comuns (assunto que a turma já viu no curso de algoritmos).
"""

class PersonagemNivel1:
    def __init__(self, nome, vida=100, forca=10, nivel=1):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.nivel = nivel

    def apresentar(self):
        print(f"{self.nome} (nível {self.nivel}) - vida: {self.vida}, força: {self.forca}")


novato = PersonagemNivel1("Finn")
novato.apresentar()

veterano = PersonagemNivel1("Draven", vida=200, forca=40, nivel=15)
veterano.apresentar()

# ==============================================================================
# 9. EXEMPLIFICANDO EM DIVERSAS SITUAÇÕES (15 min)
# ==============================================================================
"""
Percorra rapidamente os quatro exemplos abaixo (Animal, Pessoa,
Triângulo, Carro), pedindo para a turma identificar, em cada um:
  - quais são os atributos (definidos no __init__)?
  - quais são os métodos (comportamentos)?
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
    etiqueta para o MESMO objeto.

Avise que a Aula 7 ("Herança e outras relações") vai:
  - Ensinar como reaproveitar atributos e métodos entre classes
    parecidas (herança - relação "é um").
  - Mostrar como sobrescrever métodos herdados (override) e super().
  - Apresentar agregação (relação "tem um"), como um Personagem que
    TEM uma Mochila.

Direcione a turma para a atividade de sala: reconstruir as classes
"Animal" (cachorro, gato) da Aula 5 usando __init__ e métodos.
"""

# ==============================================================================
# FIM DO ROTEIRO
# ==============================================================================
