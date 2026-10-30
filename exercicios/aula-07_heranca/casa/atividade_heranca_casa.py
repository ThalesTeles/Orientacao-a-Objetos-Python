"""
==============================================================================
EXERCÍCIO PARA CASA - EVOLUINDO O SISTEMA DE ESTOQUE COM HERANÇA
==============================================================================

Na aula 5, criamos uma classe "Produto" para representar o estoque de uma
loja de eletrônicos. Hoje, vamos EVOLUIR esse sistema aplicando herança e
agregação, para que ele fique mais próximo da realidade: uma loja não
vende só eletrônicos, ela também pode vender produtos alimentícios, por
exemplo, e cada tipo de produto tem particularidades diferentes.

Complete os espaços marcados com "___" e com o comentário # TODO.
Ao final, execute o arquivo e confira se as respostas fazem sentido.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - CLASSE BASE "PRODUTO"
# ==============================================================================
"""
Crie uma classe "Produto" com:
  - um construtor __init__ que recebe e guarda: nome, preco, quantidade
  - um método "calcular_valor_total(self)" que devolve preco * quantidade
  - um método "exibir_informacoes(self)" que imprime algo como:
      "Fone de Ouvido - R$ 49.90 (12 unidades)"
"""

# TODO: crie a classe Produto aqui


# ==============================================================================
# PARTE 2 - SUBCLASSE "PRODUTOELETRONICO"
# ==============================================================================
"""
Crie a classe "ProdutoEletronico", que HERDA de Produto e adiciona:
  - um atributo extra "garantia_meses" (defina no __init__ desta classe,
    chamando o __init__ da classe mãe com super() para nome/preco/quantidade)
  - SOBRESCREVA exibir_informacoes(self) para incluir a garantia, algo como:
      "Fone de Ouvido - R$ 49.90 (12 unidades) - Garantia: 12 meses"

Dica de __init__ com super():

    class ProdutoEletronico(Produto):
        def __init__(self, nome, preco, quantidade, garantia_meses):
            super().__init__(nome, preco, quantidade)
            self.garantia_meses = garantia_meses
"""

# TODO: crie a classe ProdutoEletronico aqui


# ==============================================================================
# PARTE 3 - SUBCLASSE "PRODUTOALIMENTICIO"
# ==============================================================================
"""
Crie a classe "ProdutoAlimenticio", que também HERDA de Produto e
adiciona:
  - um atributo extra "validade" (uma string com a data, ex: "12/2026")

SOBRESCREVA exibir_informacoes(self) para incluir a validade, algo como:
    "Chocolate - R$ 8.50 (30 unidades) - Validade: 12/2026"
"""

# TODO: crie a classe ProdutoAlimenticio aqui


# ==============================================================================
# PARTE 4 - CADASTRANDO O ESTOQUE
# ==============================================================================
"""
Crie:
  - 2 objetos ProdutoEletronico (ex: "Fone de Ouvido", "Carregador")
  - 2 objetos ProdutoAlimenticio (ex: "Chocolate", "Refrigerante")
  - 1 objeto Produto "comum" (algo que não se encaixa nas categorias
    acima, ex: "Caneca")

Coloque todos os 5 objetos dentro de uma lista chamada "estoque".
"""

# TODO: crie os 5 objetos aqui


# TODO: crie a lista "estoque" com os 5 produtos
estoque = []  # substitua pela lista com os seus produtos


# ==============================================================================
# PARTE 5 - TESTANDO O POLIMORFISMO
# ==============================================================================
"""
Percorra a lista "estoque" com um for e chame exibir_informacoes() para
cada produto - SEM verificar de qual classe cada objeto é. Repare que
cada tipo de produto exibe suas informações de um jeito diferente,
mesmo recebendo a MESMA chamada de método.
"""

# TODO: percorra "estoque" e chame exibir_informacoes() para cada produto


# ==============================================================================
# PARTE 6 - REAPROVEITANDO O MÉTODO HERDADO
# ==============================================================================
"""
Escreva uma função "calcular_valor_total_estoque(lista_produtos)" que
percorre a lista e SOMA o resultado de calcular_valor_total() de cada
produto (esse método já foi herdado por todas as subclasses - não é
preciso reescrevê-lo em nenhuma delas!).

Chame a função e imprima o valor total do estoque.
"""

# TODO: crie a função calcular_valor_total_estoque aqui


# TODO: chame a função e imprima o resultado


# ==============================================================================
# PARTE 7 - AGREGAÇÃO: A CLASSE "LOJA"
# ==============================================================================
"""
Crie uma classe "Loja" que representa a loja em si. Ela deve:
  - ter um construtor __init__ que recebe "nome" (nome da loja) e cria
    uma lista vazia chamada "estoque"
  - ter um método "adicionar_produto(self, produto)" que adiciona um
    produto à lista "estoque" e imprime uma mensagem de confirmação
  - ter um método "valor_total(self)" que devolve a soma de
    calcular_valor_total() de todos os produtos da loja

IMPORTANTE: a classe Loja NÃO deve herdar de Produto! Uma loja não É UM
produto, ela TEM VÁRIOS produtos - isso é agregação, não herança.

Crie um objeto Loja, adicione os 5 produtos que você já criou usando
adicionar_produto(), e imprima o valor_total() da loja.
"""

# TODO: crie a classe Loja aqui


# TODO: crie um objeto Loja com o nome que você quiser


# TODO: adicione os 5 produtos à loja usando adicionar_produto()


# TODO: imprima o valor_total() da loja


# ==============================================================================
# DESAFIO EXTRA (opcional)
# ==============================================================================
"""
Crie mais uma subclasse de Produto chamada "ProdutoEmPromocao", que
recebe os mesmos dados de Produto mais um "desconto_percentual"
(ex: 10 para 10% de desconto).

Sobrescreva o método calcular_valor_total(self) para que ele devolva o
valor total JÁ COM O DESCONTO aplicado (dica: multiplique o resultado
do método da classe mãe por (1 - desconto_percentual / 100); você pode
usar super().calcular_valor_total() dentro do método sobrescrito).

Crie um objeto ProdutoEmPromocao, adicione-o à sua loja e confira se o
valor_total() da loja mudou corretamente.
"""

# TODO (desafio extra): crie a classe ProdutoEmPromocao aqui


# TODO (desafio extra): crie o objeto, adicione à loja e confira o valor_total()


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Se cada tipo de produto fosse uma classe totalmente separada (sem
herdar de Produto), quais partes do código você teria que duplicar?
E por que a classe Loja usa agregação em vez de herança?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DO EXERCÍCIO
# ==============================================================================
