"""
==============================================================================
ROTEIRO DE AULA - HERANÇA E OUTRAS RELAÇÕES ENTRE OBJETOS
Público-alvo: alunos de 15 a 19 anos
Duração sugerida: 1h30 a 2h
==============================================================================

Pré-requisitos (aula anterior - Classes x Objetos): métodos, o parâmetro
self, estado do objeto, diferença entre classe e objeto, construtores
(__init__).

Este arquivo é um roteiro comentado. Ele pode ser executado no Python para
que os alunos vejam os exemplos rodando ao vivo, enquanto o professor segue
a explicação nos comentários.

Sugestão de dinâmica: projete este arquivo e vá executando trecho por trecho
(ou copie os blocos para o terminal/REPL) conforme avança na explicação.
==============================================================================
"""

# ==============================================================================
# 1. RELEMBRANDO A AULA PASSADA (10 min)
# ==============================================================================
"""
Comece com uma revisão rápida e participativa, perguntando à turma:
  - "O que é o self?"
  - "Para que serve o __init__?"
  - "Qual a diferença entre classe e objeto?"

Depois, rode o exemplo de revisão abaixo ao vivo.
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
Chame atenção para o fato de que "atacar" recebeu OUTRO objeto (alvo)
como parâmetro. Use isso como gancho para o próximo tópico: como os
objetos se comunicam entre si.
"""

# ==============================================================================
# 2. COMUNICAÇÃO ENTRE OBJETOS (10 min)
# ==============================================================================
"""
Explique: objetos raramente vivem sozinhos. Um objeto costuma chamar
métodos de outro objeto ou ler/alterar seus atributos.

Rode o exemplo da mochila que guarda objetos Item, mostrando que dois
objetos de classes DIFERENTES conseguem "conversar".
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
Pergunta para a turma: "Onde mais no nosso dia a dia vemos objetos que
precisam de outros objetos para funcionar?" (ex: um carro precisa de
rodas, um computador precisa de um teclado...)
"""

# ==============================================================================
# 3. REAPROVEITAMENTO DE CÓDIGO: O PROBLEMA (15 min)
# ==============================================================================
"""
Apresente o cenário: dois tipos de personagem, Guerreiro e Mago, que
compartilham nome, vida e a forma de se apresentar, mas têm uma
habilidade própria cada um.

Rode o código abaixo e DEIXE EVIDENTE, ao vivo, que __init__ e
se_apresentar() estão duplicados entre as duas classes.
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
Provoque a turma:
  "O que vocês acham desse código? Tem algo se repetindo?"
  "Se eu quisesse mudar a frase de se_apresentar() para incluir o
   nível do personagem, quantos lugares eu precisaria alterar?"

Deixe a turma especular sobre como evitar essa duplicação antes de
revelar a solução. Anote as ideias no quadro (normalmente alguém chega
perto da ideia de "classe base" ou "classe genérica").
"""

# ==============================================================================
# 4. O QUE É HERANÇA? (15 min)
# ==============================================================================
"""
Apresente a definição:

HERANÇA é um mecanismo que permite que uma SUBCLASSE (classe filha)
reaproveite atributos e métodos de uma SUPERCLASSE (classe mãe/pai).

A relação central é o teste do "É UM":
  - Um Guerreiro É UM Personagem.
  - Um Mago É UM Personagem.

Em Python: class Filha(Mae): ...

Reescreva o exemplo anterior ao vivo, criando PersonagemBase e fazendo
GuerreiroHeranca e MagoHeranca herdarem dela.
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
guerreiro2.golpe_forte()

mago2.se_apresentar()       # herdado de PersonagemBase!
mago2.conjurar_magia()

"""
Destaque bem: GuerreiroHeranca e MagoHeranca NÃO escreveram __init__ nem
se_apresentar(), mas mesmo assim funcionam - porque herdaram tudo isso
de PersonagemBase. Peça para a turma comparar com a versão duplicada
de antes e perceber a economia de código.
"""

# ==============================================================================
# 5. SOBRESCREVENDO MÉTODOS HERDADOS (OVERRIDE) (15 min)
# ==============================================================================
"""
Explique que às vezes a classe filha quer mudar o comportamento de um
método herdado - isso se chama SOBRESCRITA (override): basta criar, na
classe filha, um método com o MESMO nome.
"""

class Arqueiro(PersonagemBase):
    def se_apresentar(self):
        print(f"Eu sou {self.nome}, um arqueiro furtivo com {self.vida} de vida!")

    def atirar_flecha(self):
        print(f"{self.nome} atira uma flecha certeira!")


arqueiro1 = Arqueiro("Kaelan", 85)
arqueiro1.se_apresentar()  # usa a versão sobrescrita

"""
Em seguida, apresente "super()" como forma de reaproveitar parte do
comportamento da classe mãe dentro do método sobrescrito.
"""

class Paladino(PersonagemBase):
    def se_apresentar(self):
        super().se_apresentar()
        print("...e também sou abençoado pela luz sagrada!")


paladino1 = Paladino("Serana", 130)
paladino1.se_apresentar()

"""
Dica de condução: pergunte "o que vocês acham que vai acontecer" ANTES
de rodar cada bloco, para estimular previsão/raciocínio.
"""

# ==============================================================================
# 6. AGREGAÇÃO: A RELAÇÃO "TEM UM" (15 min)
# ==============================================================================
"""
Apresente a segunda relação importante entre classes: AGREGAÇÃO,
representando "TEM UM" (não "é um").

Exemplos para engajar a turma:
  - Um Personagem TEM UMA Mochila.
  - Um Carro TEM UM Motor.
  - Uma Sala de aula TEM VÁRIOS Alunos.
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
Destaque a sintaxe "viajante.mochila.itens" - o aluno precisa entender
que está "atravessando" dois objetos (Personagem -> Mochila -> itens).
"""

# ==============================================================================
# 7. HERANÇA x AGREGAÇÃO: QUANDO USAR CADA UMA? (10 min)
# ==============================================================================
"""
Ensine o "teste da frase" no quadro:
  "___ é um ___"   -> se fizer sentido, é HERANÇA
  "___ tem um ___" -> se fizer sentido, é AGREGAÇÃO

Peça para a turma classificar, em duplas, os pares abaixo (pode escrever
no quadro e ir coletando respostas):
  - Cachorro / Animal          -> herança ("Cachorro é um Animal")
  - Carro / Motor              -> agregação ("Carro tem um Motor")
  - Aluno / Pessoa             -> herança
  - Time de futebol / Jogador  -> agregação (um time TEM vários jogadores)
  - Retângulo / Forma Geométrica -> herança

Reforce: usar a relação errada (por ex. Carro herdar de Motor) deixa o
código difícil de entender, mesmo que "funcione" tecnicamente.
"""

# ==============================================================================
# 8. UMA MESMA CHAMADA, COMPORTAMENTOS DIFERENTES (10 min)
# ==============================================================================
"""
Feche o conteúdo mostrando o efeito prático da sobrescrita: podemos
chamar o MESMO método em objetos de classes diferentes e cada um
responde do seu próprio jeito (introdução leve ao conceito de
polimorfismo, sem precisar nomear o termo formalmente ainda).
"""

grupo = [guerreiro2, mago2, arqueiro1, paladino1]

for personagem in grupo:
    personagem.se_apresentar()

"""
Pergunta final para reflexão em grupo:
  "O código do 'for' chama 'personagem.se_apresentar()' da mesma forma
   para todo mundo. Ele precisa saber, antes de rodar, se está lidando
   com um Guerreiro, um Mago ou um Paladino?"

Espera-se que a turma perceba que NÃO - cada objeto "sabe" como se
comportar. Essa ideia será aprofundada em aulas futuras (polimorfismo).
"""

# ==============================================================================
# 9. EXERCÍCIO PRÁTICO (15-20 min)
# ==============================================================================
"""
Direcione a turma para o arquivo "atividade_heranca_sala.py": reconstruir
as classes Animal (Cachorro, Gato) da aula 5, agora aplicando herança,
sobrescrita de métodos e uma relação de agregação (um Zoológico que TEM
vários Animais).

Circule pela sala tirando dúvidas. Se sobrar tempo, peça para alguns
alunos apresentarem sua solução para a turma.
"""

# ==============================================================================
# FIM DO ROTEIRO
# ==============================================================================
