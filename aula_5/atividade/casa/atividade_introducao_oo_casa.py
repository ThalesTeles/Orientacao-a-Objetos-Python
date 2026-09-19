"""
==============================================================================
AULA 5 - ATIVIDADE DE CASA - USANDO CLASSES PARA RESOLVER UM PROBLEMA PRÁTICO
==============================================================================

Na aula, criamos classes e objetos apenas para representar e exibir
informações. Agora vamos usar classes e objetos para RESOLVER UM PROBLEMA
de verdade: organizar o estoque de uma loja.

Complete os espaços marcados com "___" e com o comentário # TODO.
Ao final, execute o arquivo e confira se as respostas fazem sentido.

Guarde este arquivo! Na Aula 6 vamos reaproveitar a classe "Produto" para
transformar essas funções soltas em MÉTODOS dentro da própria classe.
==============================================================================
"""

# ==============================================================================
# CONTEXTO DO PROBLEMA
# ==============================================================================
"""
Você foi contratado(a) para organizar o sistema de estoque de uma loja de
eletrônicos. Cada produto do estoque tem:
  - nome
  - preco (por unidade)
  - quantidade (quantas unidades existem no estoque)

Sua tarefa é usar CLASSES para representar cada produto e, depois, escrever
FUNÇÕES (fora da classe) que analisem a lista de produtos e respondam a
perguntas do dono da loja.

Lembre-se: ainda não vimos "métodos" dentro de classes, então as funções
que vamos usar aqui recebem os objetos como parâmetro, do mesmo jeito que
fizemos com a função "atacar_estruturado" na aula.
"""

# ==============================================================================
# PARTE 1 - CRIANDO A CLASSE
# ==============================================================================
"""
Crie uma classe chamada "Produto", vazia (com pass).
"""

# TODO: crie a classe Produto aqui


# ==============================================================================
# PARTE 2 - CADASTRANDO O ESTOQUE
# ==============================================================================
"""
Crie 5 objetos da classe Produto, representando produtos de uma loja de
eletrônicos (ex: "Fone de Ouvido", "Mouse", "Teclado", "Carregador",
"Caixa de Som"). Para cada um, defina os atributos:
  - nome
  - preco       (número, ex: 49.90)
  - quantidade  (número inteiro, ex: 12)

Depois, coloque todos os 5 objetos dentro de uma lista chamada "estoque".
"""

# TODO: crie os 5 objetos Produto aqui


# TODO: crie a lista "estoque" com os 5 produtos
estoque = []  # substitua pela lista com os seus produtos


# ==============================================================================
# PARTE 3 - RESOLVENDO PROBLEMAS COM O ESTOQUE
# ==============================================================================
"""
Agora, complete as funções abaixo. Cada uma recebe a lista "estoque"
(uma lista de objetos Produto) e deve devolver uma resposta para um
problema real da loja.
"""

# ------------------------------------------------------------------
# Problema 1: Qual é o valor total (em R$) parado no estoque?
# ------------------------------------------------------------------
def calcular_valor_total_estoque(lista_produtos):
    total = 0
    # TODO

    return total


# ------------------------------------------------------------------
# Problema 2: Quais produtos estão com estoque baixo (quantidade < 5)?
# A loja quer saber quais produtos precisam ser repostos.
# ------------------------------------------------------------------
def produtos_para_repor(lista_produtos):
    produtos_baixos = []
    # TODO
    return produtos_baixos


# ------------------------------------------------------------------
# Problema 3: Qual é o produto mais caro do estoque?
# A função deve devolver o OBJETO do produto mais caro (não só o nome).
# ------------------------------------------------------------------
def produto_mais_caro(lista_produtos):
    # TODO
    pass


# ------------------------------------------------------------------
# Problema 4: Dado um nome de produto digitado pelo cliente, qual é o
# preço dele? Se o produto não existir no estoque, devolva None.
# ------------------------------------------------------------------
def buscar_preco_por_nome(lista_produtos, nome_buscado):
    # TODO
    pass


# ==============================================================================
# PARTE 4 - TESTANDO SUAS FUNÇÕES
# ==============================================================================
"""
Descomente e complete os prints abaixo para testar as funções que você
escreveu na Parte 3.
"""

# print(f"Valor total do estoque: R$ {calcular_valor_total_estoque(estoque):.2f}")

# print(f"Produtos para repor: {produtos_para_repor(estoque)}")

# produto_caro = produto_mais_caro(estoque)
# print(f"Produto mais caro: {produto_caro.nome} - R$ {produto_caro.preco:.2f}")

# TODO: escolha o nome de um produto do seu estoque e teste a busca:
# preco_encontrado = buscar_preco_por_nome(estoque, "___")
# print(f"Preço encontrado: {preco_encontrado}")


# ==============================================================================
# DESAFIO EXTRA
# ==============================================================================
"""
A loja quer fazer uma promoção: todos os produtos com quantidade maior
que 10 devem ter o preço reduzido em 10%.

Escreva uma função "aplicar_promocao(lista_produtos)" que percorre o
estoque e, para os produtos com quantidade > 10, ATUALIZA o atributo
"preco" do objeto (multiplicando por 0.9).

Depois, chame a função e imprima novamente os preços de todos os
produtos para confirmar que a promoção foi aplicada corretamente.

Lembrete: como os objetos são um tipo de referência, se você alterar o atributo
de um objeto dentro da função, essa alteração permanece mesmo depois
que a função terminar.
"""

# TODO (desafio extra): crie a função aplicar_promocao aqui


# TODO (desafio extra): chame a função e imprima os preços atualizados


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Se cada produto fosse representado por 3 variáveis soltas (nome1, preco1,
quantidade1, nome2, preco2, quantidade2...) em vez de objetos dentro de
uma lista, essas funções seriam mais fáceis ou mais difíceis de escrever?
Por quê?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DA ATIVIDADE DE CASA
# ==============================================================================
