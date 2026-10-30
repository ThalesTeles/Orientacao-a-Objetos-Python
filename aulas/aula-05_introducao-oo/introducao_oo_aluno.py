"""
==============================================================================
AULA 5 - INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
==============================================================================

Este arquivo é um material de apoio. Você pode executá-lo no Python para
ver os exemplos funcionando na prática.
==============================================================================
"""

# ==============================================================================
# 1. CONTEXTUALIZAÇÃO HISTÓRICA
# ==============================================================================
"""
- Nas décadas de 1950-60, os primeiros programas eram simples e lineares:
  uma lista de instruções que a máquina executava de cima para baixo.

- Com o crescimento dos softwares (anos 60-70), os programas ficaram enormes
  e viraram um emaranhado difícil de entender e manter: o chamado
  "código espaguete".

- Isso gerou a "crise do software": projetos atrasados, caros e cheios de
  bugs porque ninguém mais entendia o próprio código.

- Em 1967, a linguagem Simula 67 (Ole-Johan Dahl e Kristen Nygaard, Noruega)
  introduziu os conceitos de classes e objetos pela primeira vez.

- Nos anos 1970-80, Alan Kay criou a linguagem Smalltalk, que popularizou
  o termo "Programação Orientada a Objetos" e boa parte das ideias que
  usamos até hoje.

- Depois vieram C++ (anos 80), Java (anos 90), Python, C#, etc, todas
  incorporando POO como um dos principais paradigmas de programação.
"""

# ==============================================================================
# 2. O QUE É POO?
# ==============================================================================
"""
POO = Programação Orientada a Objetos.

É um PARADIGMA de programação (uma forma de pensar e organizar o código)
onde modelamos o programa como um conjunto de "objetos" que interagem
entre si, assim como no mundo real.

Em vez de pensar em "uma sequência de comandos", pensamos em:
  - "Quais COISAS existem no meu problema?" (objetos)
  - "O que essas coisas TÊM?" (atributos / características)
  - "O que essas coisas FAZEM?" (métodos / comportamentos)

Exemplo do mundo real: um carro.
  - O que ele TEM: cor, modelo, velocidade atual, quantidade de combustível.
  - O que ele FAZ: acelerar, frear, buzinar, ligar o motor.

A POO tenta aproximar o código da forma como enxergamos o mundo real.
Guarde essa divisão "TEM x FAZ" — ela vai reaparecer na Aula 6, quando
formos representar o "FAZ" dentro do código.
"""

# ==============================================================================
# 3. POR QUE USAR POO AO INVÉS DE PROGRAMAÇÃO ESTRUTURADA?
# ==============================================================================
"""
Na Programação Estruturada, dados e funções ficam separados.
Exemplo: para representar um personagem de jogo, faríamos assim:
"""

nome_personagem = "Guerreiro"
vida_personagem = 100
ataque_personagem = 15

def atacar_estruturado(nome, vida, ataque):
    print(f"{nome} ataca causando {ataque} de dano!")

atacar_estruturado(nome_personagem, vida_personagem, ataque_personagem)

"""
Problemas dessa abordagem quando o projeto cresce:
  1. Se eu tiver 10 personagens, preciso de 30 variáveis soltas (nome1,
     vida1, ataque1, nome2, vida2, ataque2...) -> vira uma bagunça.
  2. Fica fácil "esquecer" de passar algum dado errado para a função.
  3. Não existe uma ligação clara entre os dados (nome, vida, ataque) e
     o comportamento (atacar) — tudo fica solto.
  4. Reaproveitar e organizar o código fica cada vez mais difícil.

Com POO, agrupamos dados (atributos) e comportamentos (métodos) dentro
de uma mesma "caixa": o objeto. Isso traz vantagens como:
  - Organização: cada objeto cuida dos seus próprios dados.
  - Reutilização: uma classe pode gerar vários objetos parecidos.
  - Manutenção mais fácil: mudanças ficam isoladas dentro da classe.
  - Modelagem mais próxima da realidade (mais intuitivo).

Vamos ver como isso fica na prática mais à frente!
"""

# ==============================================================================
# 4. DEFINIÇÃO DE OBJETOS
# ==============================================================================
"""
OBJETO é qualquer "coisa" concreta que pode ser descrita por:
  - características (o que ela TEM)
  - comportamentos (o que ela FAZ)

Exemplo - Objeto "cachorro":
  Características: nome, raça, idade, cor do pelo.
  Comportamentos: latir, correr, comer, abanar o rabo.

Em programação, um objeto é uma "instância" de uma classe — ou seja,
um exemplar real e específico criado a partir de um "molde".

Analogia da FORMA DE BOLO:
  - A FORMA é a classe (o molde, o modelo).
  - Cada BOLO assado nessa forma é um objeto (uma instância).
  - Cada bolo pode ter recheio, cobertura e tamanho diferentes,
    mas todos seguem o mesmo formato básico.
"""

# ==============================================================================
# 5. ATRIBUTOS
# ==============================================================================
"""
ATRIBUTOS são as características/variáveis que pertencem a um objeto.
Eles guardam o ESTADO do objeto (os dados dele).

Exemplo - Objeto "Personagem de RPG":
  Atributos: nome, vida, nível, força, inventário...

Exemplo - Objeto "Aluno":
  Atributos: nome, idade, série, notas...

No próximo tópico vamos ver como agrupar atributos dentro de uma CLASSE.
"""

# ==============================================================================
# 6. O QUE SÃO CLASSES?
# ==============================================================================
"""
CLASSE é o MOLDE (modelo/planta) que define quais atributos e
comportamentos os objetos criados a partir dela vão ter.

A classe, sozinha, não é "uma coisa real" — ela é a receita.
O OBJETO é o resultado de "seguir essa receita" (isso se chama
INSTANCIAR a classe).

Analogia:
  - Classe = planta baixa de uma casa (o projeto/desenho).
  - Objeto = a casa construída de verdade a partir daquela planta.
  - Posso construir várias casas (objetos) diferentes usando a
    MESMA planta (classe).

Em Python, criamos uma classe usando a palavra-chave "class".
"""

# ==============================================================================
# 7. PRIMEIRA CLASSE EM PYTHON (SEM MÉTODOS)
# ==============================================================================

class Personagem:
    pass  # "pass" significa "essa classe não tem nada dentro por enquanto"


# Agora vamos criar OBJETOS (instâncias) a partir dessa classe:
heroi = Personagem()
vilao = Personagem()

# E atribuir características (atributos) para cada objeto individualmente:
heroi.nome = "Aldric"
heroi.vida = 100
heroi.forca = 20

vilao.nome = "Malvor"
vilao.vida = 150
vilao.forca = 30

print(f"{heroi.nome} tem {heroi.vida} de vida e {heroi.forca} de força.")
print(f"{vilao.nome} tem {vilao.vida} de vida e {vilao.forca} de força.")

"""
- "heroi" e "vilao" são dois objetos DIFERENTES, criados a partir da
  MESMA classe "Personagem".
- Cada um guarda seus próprios valores de nome, vida e força.
- Isso já mostra a vantagem da POO: não precisamos de variáveis soltas
  tipo nome1, vida1, nome2, vida2... cada objeto organiza seus
  próprios dados.

Só que existe um problema nessa forma de criar objetos. Veja o exemplo:

  novo_personagem = Personagem()
  novo_personagem.nome = "Thalia"
  novo_personagem.vida = 90
  # esquecemos de definir novo_personagem.forca

  print(novo_personagem.forca)  # o que você acha que acontece aqui?

Nada na classe "Personagem" obriga que todo objeto criado a partir dela
tenha os atributos nome, vida e forca. Dois objetos da mesma classe podem
acabar com conjuntos de atributos diferentes, dependendo do que o
programador lembrou (ou esqueceu) de definir.

Pense e discuta com um colega:
  - O que você acha que acontece ao tentar rodar "print(novo_personagem.forca)"
    se esse atributo nunca foi definido?
  - Como vocês resolveriam esse problema? Existe algum jeito de garantir
    que TODO objeto criado a partir da classe Personagem já nasça com
    nome, vida e forca definidos, sem depender de lembrarmos disso toda
    vez?
  - E as AÇÕES desse personagem (atacar, se curar...)? Onde elas
    deveriam morar no código?

Guarde suas ideias - vamos usá-las como ponto de partida na próxima aula!
"""

# ==============================================================================
# 8. EXEMPLOS DE CLASSES: PERSONAGEM, MOCHILA, SALAS...
# ==============================================================================

# --- Exemplo 1: Personagem (jogo de RPG) ---
class Personagem2:
    pass

# Atributos possíveis: nome, classe (guerreiro/mago), vida, mana, nível,
# experiência, força, defesa, inventário.


# --- Exemplo 2: Mochila (item de jogo ou de uso real) ---
class Mochila:
    pass

# Atributos possíveis: cor, capacidade máxima, peso atual, lista de itens,
# material, marca.

minha_mochila = Mochila()
minha_mochila.cor = "azul"
minha_mochila.capacidade_maxima = 20  # em kg
minha_mochila.itens = ["caderno", "estojo", "garrafa de água"]

print(f"Mochila {minha_mochila.cor} contém: {minha_mochila.itens}")


# --- Exemplo 3: Sala (de aula ou de um jogo estilo "dungeon") ---
class Sala:
    pass

# Atributos possíveis: nome da sala, descrição, capacidade de pessoas,
# lista de objetos presentes, portas/saídas conectadas.

sala_01 = Sala()
sala_01.nome = "Sala do Tesouro"
sala_01.descricao = "Uma sala escura repleta de moedas de ouro."
sala_01.itens = ["baú", "espada mágica"]

print(f"{sala_01.nome}: {sala_01.descricao}")
print(f"Itens na sala: {sala_01.itens}")

"""
Percebam que todos esses exemplos seguem o mesmo padrão:
  1. Criamos a classe (o molde).
  2. Criamos o objeto (instância) a partir da classe.
  3. Damos valores aos atributos daquele objeto específico.
"""

# ==============================================================================
# 9. PRÉVIA DA PRÓXIMA AULA
# ==============================================================================
"""
Na Aula 6 vamos resolver o problema do tópico 7 e vamos aprender a colocar
COMPORTAMENTOS (o "FAZ") dentro da classe, não só características (o "TEM").
Os assuntos serão:
  - Construtores (o método especial __init__)
  - O parâmetro "self"
  - Métodos
  - Estado de um objeto
  - Diferença entre Classe e Objeto / Objeto x Variável
"""

# ==============================================================================
# FIM
# ==============================================================================
