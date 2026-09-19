"""
==============================================================================
AULA 6 - ATIVIDADE DE CASA - TRANSFORMANDO FUNÇÕES EM MÉTODOS
==============================================================================

Na Aula 5 (atividade de casa) você criou uma classe "Produto" vazia e
escreveu FUNÇÕES separadas para analisar o estoque de uma loja. Hoje
vamos reconstruir esse mesmo sistema, mas agora com __init__ e métodos.

Guarde bem este arquivo: na Aula 7 vamos reaproveitar esta MESMA classe
"Produto" para criar subclasses como "ProdutoEletronico" e
"ProdutoAlimenticio" usando herança!

Complete os espaços marcados com "___" e com o comentário # TODO.
Ao final, execute o arquivo e confira se as respostas fazem sentido.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - CONSTRUTOR DA CLASSE PRODUTO
# ==============================================================================
"""
Crie a classe "Produto" com um construtor __init__ que recebe e guarda:
  - nome
  - preco
  - quantidade
"""

# TODO: crie a classe Produto aqui, com o __init__


# ==============================================================================
# PARTE 2 - MÉTODO "calcular_valor_total"
# ==============================================================================
"""
Adicione à classe Produto um método "calcular_valor_total(self)" que
devolve preco * quantidade (na Aula 5 isso era uma função solta que
recebia o produto como parâmetro - agora vira um método!).
"""

# TODO: adicione o método calcular_valor_total() na classe Produto


# ==============================================================================
# PARTE 3 - MÉTODO "exibir_informacoes"
# ==============================================================================
"""
Adicione um método "exibir_informacoes(self)" que imprime algo como:

  "Fone de Ouvido - R$ 49.90 (12 unidades)"
"""

# TODO: adicione o método exibir_informacoes() na classe Produto


# ==============================================================================
# PARTE 4 - CADASTRANDO O ESTOQUE COM O CONSTRUTOR
# ==============================================================================
"""
Crie 5 objetos Produto (pode reaproveitar os mesmos produtos da Aula 5),
agora passando os valores diretamente no construtor. Coloque todos
dentro de uma lista chamada "estoque".
"""

# TODO: crie os 5 objetos Produto aqui, usando Produto(...)


# TODO: crie a lista "estoque" com os 5 produtos
estoque = []  # substitua pela lista com os seus produtos


# ==============================================================================
# PARTE 5 - USANDO OS MÉTODOS
# ==============================================================================
"""
Percorra a lista "estoque" com um for e chame exibir_informacoes() para
cada produto.
"""

# TODO: percorra "estoque" e chame exibir_informacoes() para cada produto


# ==============================================================================
# PARTE 6 - FUNÇÕES QUE USAM OS MÉTODOS
# ==============================================================================
"""
As funções de análise (que trabalham sobre a LISTA inteira de produtos)
continuam sendo funções fora da classe - mas agora, por dentro, elas
usam o método calcular_valor_total() em vez de fazer a conta na mão.

Complete a função abaixo:
"""

def calcular_valor_total_estoque(lista_produtos):
    total = 0
    # TODO: percorra lista_produtos e some produto.calcular_valor_total()
    # de cada produto em "total" (em vez de "produto.preco * produto.quantidade")

    return total


# TODO: chame a função e imprima o valor total do estoque


"""
Agora complete também esta função, que devolve os produtos com estoque
baixo (quantidade < 5). Ela continua funcionando como uma função comum,
só acessando os atributos do objeto (nome, quantidade) normalmente.
"""

def produtos_para_repor(lista_produtos):
    produtos_baixos = []
    # TODO: percorra lista_produtos e adicione o NOME dos produtos com
    # quantidade menor que 5 na lista "produtos_baixos"

    return produtos_baixos


# TODO: chame a função e imprima os produtos para repor


# ==============================================================================
# PARTE 7 - MÉTODO QUE MUDA O ESTADO: "aplicar_desconto"
# ==============================================================================
"""
Adicione à classe Produto um método "aplicar_desconto(self, percentual)"
que reduz o "preco" do produto de acordo com o percentual informado.

Exemplo: se percentual = 10, o preço deve ser multiplicado por 0.9
(preço - 10%).

Depois, escolha um produto do seu estoque, imprima o preço dele ANTES,
chame aplicar_desconto(10) nele, e imprima o preço DEPOIS - para
confirmar que o ESTADO do objeto mudou de verdade.
"""

# TODO: adicione o método aplicar_desconto(self, percentual) na classe Produto


# TODO: teste o método em um produto do seu estoque, mostrando o preço
# antes e depois


# ==============================================================================
# DESAFIO EXTRA (opcional)
# ==============================================================================
"""
Adicione um valor padrão para o parâmetro "quantidade" do __init__ de
Produto (por exemplo, quantidade=0), para representar um produto recém
cadastrado que ainda não chegou ao estoque físico.

Crie um objeto Produto passando só o nome e o preço (sem quantidade) e
confirme, com um print, que a quantidade dele começou em 0.
"""

# TODO (desafio extra): ajuste o __init__ da classe Produto


# TODO (desafio extra): crie o objeto e confirme o valor padrão


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Compare com a Aula 5: o que ficou diferente em ter
"produto.calcular_valor_total()" (um método do objeto) em vez de
"calcular_valor_total_estoque(produto)" (uma função solta)? Alguma
forma parece mais organizada para você? Por quê?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DA ATIVIDADE DE CASA
# ==============================================================================
