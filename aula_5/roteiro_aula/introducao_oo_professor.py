"""
==============================================================================
ROTEIRO DE AULA 5 - INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
Público-alvo: alunos de 15 a 19 anos
Duração sugerida: 1h30 a 2h
Módulo: POO (aula 5 de 8 do módulo) | Próxima aula: "Classes x Objetos" (métodos, self, construtores)
==============================================================================
"""

# ==============================================================================
# 1. CONTEXTUALIZAÇÃO HISTÓRICA (10 min)
# ==============================================================================
"""
Falar com os alunos, sem código ainda - pode ser um bate-papo introdutório:

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

Pergunta para engajar a turma:
  "Vocês já tentaram organizar um quarto bagunçado sem caixas ou gavetas?
   É basicamente assim que era programar antes da POO."
"""

# ==============================================================================
# 2. O QUE É POO? (10 min)
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

Dica para o professor: grife/destaque bem a divisão "TEM x FAZ" no quadro.
Hoje só trabalhamos o "TEM" (atributos); o "FAZ" (métodos) é o gancho para
a Aula 6 - vale reforçar isso desde já.
"""

# ==============================================================================
# 3. POR QUE USAR POO AO INVÉS DE PROGRAMAÇÃO ESTRUTURADA? (10 min)
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
# 4. DEFINIÇÃO DE OBJETOS (10 min)
# ==============================================================================
"""
OBJETO é qualquer "coisa" concreta que pode ser descrita por:
  - características (o que ela TEM)
  - comportamentos (o que ela FAZ)

Peça exemplos para a turma! Ex: um celular, um cachorro, uma mochila,
uma sala de aula, um jogador de futebol...

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
# 5. ATRIBUTOS (10 min)
# ==============================================================================
"""
ATRIBUTOS são as características/variáveis que pertencem a um objeto.
Eles guardam o ESTADO do objeto (os dados dele).

Exemplo - Objeto "Personagem de RPG":
  Atributos: nome, vida, nível, força, inventário...

Exemplo - Objeto "Aluno":
  Atributos: nome, idade, série, notas...

Pergunte à turma: "Quais atributos vocês dariam para um objeto 'celular'?"
(Ex: marca, modelo, cor, capacidade de armazenamento, bateria...)

No próximo tópico vamos ver como agrupar atributos dentro de uma CLASSE.
"""

# ==============================================================================
# 6. O QUE SÃO CLASSES? (10 min)
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
# 7. PRIMEIRA CLASSE EM PYTHON (SEM MÉTODOS) (15 min)
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
Observação importante para os alunos:
  - "heroi" e "vilao" são dois objetos DIFERENTES, criados a partir da
    MESMA classe "Personagem".
  - Cada um guarda seus próprios valores de nome, vida e força.
  - Isso já mostra a vantagem da POO: não precisamos de variáveis soltas
    tipo nome1, vida1, nome2, vida2... cada objeto organiza seus
    próprios dados.

PROBLEMA para provocar a turma (fazer ao vivo, no quadro ou no interpretador):

  novo_personagem = Personagem()
  novo_personagem.nome = "Thalia"
  novo_personagem.vida = 90
  # "esquecer" de definir novo_personagem.forca

  print(novo_personagem.forca)  # -> AttributeError!

  Mostrar esse erro rodando ao vivo. Deixar a turma perceber que o Python
  deixou criar o objeto "Thalia" sem forca alguma, e o erro só aparece
  quando alguém tenta USAR esse atributo - às vezes bem longe de onde o
  objeto foi criado, o que dificulta encontrar o problema.

  Perguntar para a turma:
    "Nada aqui obriga que todo Personagem tenha nome, vida e força.
     Hoje isso depende só da nossa memória e disciplina como
     programadores. Como vocês resolveriam esse problema? Existe algum
     jeito de garantir que TODO objeto criado a partir da classe
     Personagem já nasça com esses atributos definidos?"

  Deixar a turma especular livremente (ex: "fazer uma função que cria o
  personagem e já define tudo", "colocar valores padrão na classe"...).
  Não entregar a resposta - anotar as ideias no quadro e comentar que
  esse problema tem uma solução elegante em Python, que será o assunto
  da PRÓXIMA AULA: o método especial __init__.

  Pergunta extra de fechamento (gancho para métodos):
    "E se eu quisesse que 'heroi' pudesse atacar sozinho, tipo
     heroi.atacar()? Onde esse comportamento moraria?"
  Também não entregar a resposta - só plantar a dúvida.

(Na próxima aula: método __init__ para criar esses atributos de forma
automática e obrigatória, além dos MÉTODOS, que são as ações/comportamentos
dos objetos.)
"""

# ==============================================================================
# 8. EXEMPLOS DE CLASSES: PERSONAGEM, MOCHILA, SALAS... (20 min)
# ==============================================================================
"""
Vamos exercitar a IDENTIFICAÇÃO de atributos em diferentes contextos,
sempre no formato: "O que esse objeto TEM?"
Ideal fazer isso de forma participativa, no quadro, com a turma sugerindo.
"""

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
Discussão com a turma:
  - Percebam que TODOS esses exemplos seguem o mesmo padrão:
    1. Criamos a classe (o molde).
    2. Criamos o objeto (instância) a partir da classe.
    3. Damos valores aos atributos daquele objeto específico.

  - Proponha aos alunos criarem, em duplas, uma classe própria
    (ex: Carro, Time de futebol, Pet, Celular...) e listarem pelo menos
    4 atributos para ela, sem se preocupar ainda com métodos.
"""

# ==============================================================================
# 9. FECHAMENTO E PRÉVIA DA AULA 6 (5 min)
# ==============================================================================
"""
Recapitule rapidamente com a turma:
  - Objeto = "coisa" com características (atributos).
  - Classe = molde que define quais atributos um objeto terá.
  - Hoje criamos atributos "na mão", um a um, fora da classe - e isso é
    frágil (ninguém é obrigado a preencher tudo).

Avise que a Aula 6 ("Classes x Objetos") vai:
  - Resolver o problema do AttributeError com o construtor (__init__).
  - Explicar o misterioso parâmetro "self".
  - Introduzir MÉTODOS, para os objetos finalmente "fazerem" coisas.
  - Reforçar a diferença entre Classe e Objeto, e entre Objeto e Variável.

Passe a atividade de casa (arquivo separado) para os alunos praticarem
antes da próxima aula.
"""

# ==============================================================================
# FIM DO ROTEIRO
# ==============================================================================
