"""
==============================================================================
HERANÇA E OUTRAS RELAÇÕES ENTRE OBJETOS
==============================================================================

Este arquivo é um material de apoio. Você pode executá-lo no Python para
ver os exemplos funcionando na prática.

Pré-requisitos (vistos na aula passada): classes, objetos, atributos,
métodos, o parâmetro self e o construtor __init__.
==============================================================================
"""

# ==============================================================================
# 1. RELEMBRANDO A AULA PASSADA
# ==============================================================================
"""
Na aula anterior vimos que uma classe pode ter MÉTODOS (ações) além de
atributos, e que o construtor __init__ garante que todo objeto já nasça
com os atributos definidos.

Exemplo de revisão:
"""

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, alvo):
        alvo.vida -= self.forca
        print(f"{self.nome} ataca {alvo.nome} causando {self.forca} de dano!")

    def esta_vivo(self):
        return self.vida > 0


heroi = Personagem("Aldric", 100, 20)
vilao = Personagem("Malvor", 80, 15)

heroi.atacar(vilao)
print(f"Vida restante de {vilao.nome}: {vilao.vida}")

"""
Reparem que o método "atacar" recebeu OUTRO objeto (alvo) como parâmetro
e mexeu diretamente nos atributos dele. Isso é a base do próximo assunto:
como os objetos se comunicam entre si.
"""

# ==============================================================================
# 2. COMUNICAÇÃO ENTRE OBJETOS
# ==============================================================================
"""
Objetos raramente vivem sozinhos. Na maioria dos programas, um objeto
precisa "conversar" com outro: chamar seus métodos, ler ou alterar seus
atributos.

No exemplo acima, "heroi.atacar(vilao)" é justamente isso: o objeto
"heroi" chama seu próprio método "atacar", passando o objeto "vilao"
como argumento, e dentro do método mexemos em "alvo.vida" (ou seja,
na vida do OUTRO objeto).

Outro exemplo: um objeto "Mochila" que guarda objetos "Item".
"""

class Item:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso


class MochilaComunicativa:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.itens = []

    def adicionar_item(self, item):
        peso_atual = sum(i.peso for i in self.itens)
        if peso_atual + item.peso <= self.capacidade_maxima:
            self.itens.append(item)
            print(f"{item.nome} adicionado à mochila!")
        else:
            print(f"Não foi possível adicionar {item.nome}: mochila cheia!")


espada = Item("Espada", 5)
pocao = Item("Poção de vida", 1)

mochila = MochilaComunicativa(capacidade_maxima=6)
mochila.adicionar_item(espada)
mochila.adicionar_item(pocao)

"""
Aqui, o método "adicionar_item" da classe MochilaComunicativa recebe um
objeto Item e lê o atributo "peso" dele para decidir o que fazer.
Dois objetos de classes DIFERENTES estão se comunicando.
"""

# ==============================================================================
# 3. REAPROVEITAMENTO DE CÓDIGO: O PROBLEMA
# ==============================================================================
"""
Imagine que, no nosso jogo, existem dois tipos de personagem: Guerreiro
e Mago. Os dois têm nome, vida e podem se apresentar - mas cada um também
tem uma habilidade própria (o guerreiro dá um golpe forte, o mago
conjura uma magia).

Sem saber de nenhuma técnica nova, faríamos isso criando DUAS classes
parecidas:
"""

class Guerreiro:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def se_apresentar(self):
        print(f"Eu sou {self.nome}, um guerreiro com {self.vida} de vida!")

    def golpe_forte(self):
        print(f"{self.nome} desfere um golpe forte com a espada!")


class Mago:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def se_apresentar(self):
        print(f"Eu sou {self.nome}, um mago com {self.vida} de vida!")

    def conjurar_magia(self):
        print(f"{self.nome} conjura uma bola de fogo!")


guerreiro1 = Guerreiro("Thorin", 120)
mago1 = Mago("Elandra", 90)

guerreiro1.se_apresentar()
mago1.se_apresentar()

"""
Percebam o problema: o construtor __init__ e o método se_apresentar()
são EXATAMENTE IGUAIS nas duas classes! Só copiamos e colamos o código.

Se um dia quisermos mudar a forma como um personagem se apresenta
(por exemplo, adicionar o nível dele na frase), teríamos que lembrar de
alterar em TODAS as classes parecidas. Isso é um convite a bugs e
retrabalho.

Pense e discuta com um colega:
  - Existe algum jeito de escrever o código de "nome", "vida" e
    "se_apresentar" em um ÚNICO lugar e reaproveitar em várias classes,
    sem copiar e colar?

Guarde essa ideia - é exatamente esse problema que a HERANÇA resolve!
"""

# ==============================================================================
# 4. O QUE É HERANÇA?
# ==============================================================================
"""
HERANÇA é um mecanismo que permite que uma classe (chamada de SUBCLASSE
ou classe filha) reaproveite atributos e métodos de outra classe
(chamada de SUPERCLASSE ou classe mãe/pai).

A ideia central é a relação "É UM":
  - Um Guerreiro É UM Personagem.
  - Um Mago É UM Personagem.
  - Um Cachorro É UM Animal.

Quando existe essa relação "é um" entre dois conceitos, geralmente faz
sentido usar herança.

Em Python, indicamos herança colocando a superclasse entre parênteses
no momento de criar a classe filha:

    class Filha(Mae):
        ...

Vamos reescrever o exemplo do Guerreiro e do Mago usando herança:
"""

class PersonagemBase:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def se_apresentar(self):
        print(f"Eu sou {self.nome}, com {self.vida} de vida!")


class GuerreiroHeranca(PersonagemBase):
    def golpe_forte(self):
        print(f"{self.nome} desfere um golpe forte com a espada!")


class MagoHeranca(PersonagemBase):
    def conjurar_magia(self):
        print(f"{self.nome} conjura uma bola de fogo!")


guerreiro2 = GuerreiroHeranca("Bram", 110)
mago2 = MagoHeranca("Sylra", 95)

guerreiro2.se_apresentar()  # herdado de PersonagemBase!
guerreiro2.golpe_forte()    # exclusivo de GuerreiroHeranca

mago2.se_apresentar()       # herdado de PersonagemBase!
mago2.conjurar_magia()      # exclusivo de MagoHeranca

"""
Observem:
  - GuerreiroHeranca e MagoHeranca NÃO têm __init__ próprio, mas mesmo
    assim conseguem receber "nome" e "vida" - eles HERDARAM o construtor
    de PersonagemBase.
  - O método se_apresentar() também foi herdado - não precisamos
    reescrevê-lo em nenhuma das duas classes filhas.
  - Cada classe filha ainda pode ter métodos EXCLUSIVOS dela
    (golpe_forte e conjurar_magia).

Isso resolve o problema de duplicação de código que vimos antes!
"""

# ==============================================================================
# 5. SOBRESCREVENDO MÉTODOS HERDADOS (OVERRIDE)
# ==============================================================================
"""
Às vezes, a classe filha quer reaproveitar QUASE tudo da classe mãe, mas
mudar o comportamento de um método específico. Isso se chama
SOBRESCRITA (ou "override") de método.

Basta criar, na classe filha, um método com o MESMO NOME do método da
classe mãe. O Python vai usar a versão da classe filha.
"""

class Arqueiro(PersonagemBase):
    def se_apresentar(self):
        # Sobrescrevendo o método da superclasse
        print(f"Eu sou {self.nome}, um arqueiro furtivo com {self.vida} de vida!")

    def atirar_flecha(self):
        print(f"{self.nome} atira uma flecha certeira!")


arqueiro1 = Arqueiro("Kaelan", 85)
arqueiro1.se_apresentar()  # usa a versão sobrescrita, não a da classe mãe!

"""
Também é possível reaproveitar parte do comportamento da classe mãe
dentro do método sobrescrito, usando a função "super()":
"""

class Paladino(PersonagemBase):
    def se_apresentar(self):
        super().se_apresentar()  # executa o método original da classe mãe
        print("...e também sou abençoado pela luz sagrada!")


paladino1 = Paladino("Serana", 130)
paladino1.se_apresentar()

"""
"super().se_apresentar()" chama a versão ORIGINAL do método, definida em
PersonagemBase, e depois o método de Paladino ainda acrescenta uma linha
extra. Assim reaproveitamos código em vez de reescrever tudo.
"""

# ==============================================================================
# 6. AGREGAÇÃO: A RELAÇÃO "TEM UM"
# ==============================================================================
"""
Nem toda relação entre classes é do tipo "é um". Existe outra relação
muito comum chamada AGREGAÇÃO, que representa a ideia de "TEM UM".

Exemplos:
  - Um Personagem TEM UMA Mochila.
  - Um Carro TEM UM Motor.
  - Uma Sala de aula TEM VÁRIOS Alunos.

Na agregação, um objeto guarda OUTRO objeto como atributo - mas eles
NÃO têm uma relação de "é um tipo de". Uma Mochila não é um Personagem,
ela só pertence a um.
"""

class MochilaAgregada:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)


class PersonagemComMochila:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.mochila = MochilaAgregada(capacidade_maxima=10)  # TEM UMA mochila


viajante = PersonagemComMochila("Rowan", 100)
viajante.mochila.adicionar_item("Poção de vida")
viajante.mochila.adicionar_item("Corda")

print(f"{viajante.nome} carrega: {viajante.mochila.itens}")

"""
Note que "viajante.mochila" é um objeto DENTRO de outro objeto. Para
acessar os itens, precisamos "atravessar" os dois objetos:
viajante -> mochila -> itens.
"""

# ==============================================================================
# 7. HERANÇA x AGREGAÇÃO: QUANDO USAR CADA UMA?
# ==============================================================================
"""
Pergunta de ouro para decidir: complete a frase "___ é um ___" ou
"___ tem um ___" e veja qual faz mais sentido.

  - "Guerreiro é um Personagem"      -> faz sentido -> HERANÇA
  - "Personagem tem uma Mochila"     -> faz sentido -> AGREGAÇÃO
  - "Mochila é um Personagem"        -> NÃO faz sentido -> não é herança!
  - "Personagem é uma Mochila"       -> NÃO faz sentido -> não é herança!

Resumindo:
  HERANÇA (é um)         -> a classe filha É UM TIPO da classe mãe,
                             e herda diretamente seus atributos/métodos.
  AGREGAÇÃO (tem um)     -> a classe guarda OUTRO objeto como atributo,
                             mas não é um "tipo" dele.

Usar a relação errada deixa o código confuso e difícil de entender!
Por exemplo, seria estranho um Carro "herdar" de Motor, porque um Carro
não é um tipo de Motor - ele apenas TEM UM motor.
"""

# ==============================================================================
# 8. UMA MESMA CHAMADA, COMPORTAMENTOS DIFERENTES
# ==============================================================================
"""
Um efeito interessante da herança com sobrescrita é que podemos chamar
o MESMO método em objetos de classes diferentes, e cada um responde do
seu próprio jeito.
"""

grupo = [guerreiro2, mago2, arqueiro1, paladino1]

for personagem in grupo:
    personagem.se_apresentar()

"""
Reparem: chamamos "personagem.se_apresentar()" da MESMA forma para
todos, mas guerreiro2 e mago2 usam a versão herdada de PersonagemBase,
enquanto arqueiro1 e paladino1 usam suas próprias versões sobrescritas.

O código que faz o "for" nem precisa saber qual é a classe exata de cada
personagem - ele só chama se_apresentar() e cada objeto sabe se
comportar do seu jeito. Isso deixa o código muito mais flexível!
"""

# ==============================================================================
# FIM
# ==============================================================================
