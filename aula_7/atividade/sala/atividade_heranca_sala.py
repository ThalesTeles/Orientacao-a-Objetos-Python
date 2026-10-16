"""
==============================================================================
AULA 7 - ATIVIDADE DE SALA - HERANÇA, SOBRESCRITA E AGREGAÇÃO
==============================================================================

Nesta atividade você vai montar a venda de ingressos de um show. Existem
tipos diferentes de ingresso (inteira, meia e VIP), e cada um calcula o
preço de um jeito.

Complete os trechos marcados com # TODO e execute o arquivo depois de
cada parte para ver se está funcionando.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - A CLASSE BASE INGRESSO
# ==============================================================================
"""
Crie a classe "Ingresso" com:
  - um construtor que recebe "setor" (ex: "Pista", "Arquibancada") e
    "preco_base"
  - um método "preco_final(self)" que devolve o preco_base
  - um método "descrever(self)" que imprime:

      "Ingresso Pista - R$ 120.00"

    Para mostrar o preço, use self.preco_final(), e não self.preco_base.
    Isso vai fazer diferença nas próximas partes.

Crie um ingresso e chame descrever().
"""

# TODO: crie a classe Ingresso e teste aqui


# ==============================================================================
# PARTE 2 - MEIA-ENTRADA: SOBRESCREVENDO UM MÉTODO
# ==============================================================================
"""
Crie a classe "MeiaEntrada", que herda de Ingresso. Ela só precisa
sobrescrever um método: preco_final(), que agora devolve metade do
preco_base.

Não escreva __init__ nem descrever() em MeiaEntrada.

Crie uma meia-entrada para a Pista com preço base 120 e chame
descrever(). Deve aparecer R$ 60.00.

Responda em um comentário: o método descrever() não foi reescrito em
MeiaEntrada. Como ele sabe que precisa mostrar o preço pela metade?
"""

# TODO: crie a classe MeiaEntrada e teste aqui


# TODO: escreva sua resposta aqui


# ==============================================================================
# PARTE 3 - VIP: USANDO super()
# ==============================================================================
"""
Crie a classe "IngressoVIP", que herda de Ingresso e tem um atributo a
mais: "brinde" (ex: "camiseta do show").

  1. No __init__, receba setor, preco_base e brinde. Use
     super().__init__(setor, preco_base) para guardar os dois primeiros
     e depois guarde o brinde com self.brinde.
  2. Sobrescreva preco_final(): o VIP custa o preço normal mais R$ 80.
     Use super().preco_final() + 80 em vez de repetir a conta.
  3. Sobrescreva descrever(): chame super().descrever() e depois imprima
     uma linha a mais com o brinde.

Crie um ingresso VIP e chame descrever().
"""

# TODO: crie a classe IngressoVIP e teste aqui


# ==============================================================================
# PARTE 4 - MESMA CHAMADA, PREÇOS DIFERENTES
# ==============================================================================
"""
Crie uma lista com pelo menos 5 ingressos misturados (inteira, meia e
VIP). Use um for para:
  - chamar descrever() de cada um
  - somar o preco_final() de todos

No final, imprima o total. O for não deve ter nenhum if para descobrir
o tipo do ingresso.
"""

# TODO: crie a lista, percorra com o for e imprima o total


# ==============================================================================
# PARTE 5 - AGREGAÇÃO: O SHOW TEM INGRESSOS
# ==============================================================================
"""
Um show não é um ingresso. Ele tem vários ingressos vendidos. Por isso,
a classe "Show" não herda de Ingresso.

Crie a classe "Show" com:
  - um construtor que recebe "artista" e "capacidade" (quantas pessoas
    cabem) e cria a lista vazia "ingressos_vendidos"
  - um método "vender(self, ingresso)":
      se ainda couber gente, adiciona o ingresso na lista e imprime
      "Ingresso vendido para o show de [artista]"
      se já estiver lotado, imprime "Show esgotado"
  - um método "faturamento(self)" que devolve a soma do preco_final()
    de todos os ingressos vendidos

Crie um show com capacidade 4, tente vender os 5 ingressos da Parte 4
e imprima o faturamento.
"""

# TODO: crie a classe Show e teste aqui


# ==============================================================================
# PARTE 6 - É UM OU TEM UM?
# ==============================================================================
"""
Para cada par abaixo, responda em um comentário se a relação é de
herança (é um) ou de agregação (tem um). Se não for nenhuma das duas,
escreva "nenhuma".

  a) IngressoVIP e Ingresso
  b) Show e Palco
  c) Moto e Veiculo
  d) Playlist e Musica
  e) Professor e Pessoa
  f) Celular e Bateria
  g) Turma e Aluno
  h) Cachorro e Gato
"""

# TODO: escreva suas respostas aqui


# ==============================================================================
# DESAFIO EXTRA
# ==============================================================================
"""
Crie a classe "Cortesia", que herda de Ingresso e tem preço final zero.
Venda uma cortesia em um show novo junto com outros ingressos e
confira se o faturamento continua certo, sem mudar nada na classe Show.
"""

# TODO (desafio extra): crie a classe Cortesia e teste aqui


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
