"""
==============================================================================
AULA 6 - ATIVIDADE DE SALA - MÉTODOS, SELF E ESTADO
==============================================================================

Nesta atividade você vai criar uma conta bancária simples, com depósito,
saque e Pix.

Complete os trechos marcados com # TODO e execute o arquivo depois de
cada parte para ver se está funcionando.

Todos os métodos ficam dentro da classe Conta. Quando a parte pedir um
método novo, volte na classe e adicione lá.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - A CLASSE CONTA
# ==============================================================================
"""
Crie a classe "Conta" com um construtor que recebe:
  - titular
  - saldo, com valor padrão 0

Assim, quem abre uma conta sem dinheiro pode escrever só Conta("Ana"),
e quem já começa com dinheiro escreve Conta("Bruno", 200).

Adicione também o método "mostrar_saldo(self)", que imprime:

  "Saldo de Ana: R$ 0.00"

Crie duas contas, uma de cada jeito, e chame mostrar_saldo() nas duas.
"""

# TODO: crie a classe Conta com __init__ e mostrar_saldo()


# TODO: crie as duas contas e mostre o saldo de cada uma


# ==============================================================================
# PARTE 2 - DEPOSITAR: UM MÉTODO QUE MUDA O ESTADO
# ==============================================================================
"""
Adicione o método "depositar(self, valor)", que soma o valor ao saldo
da conta e imprime:

  "Depósito de R$ 50.00 na conta de Ana"

Faça dois depósitos na conta da Ana e mostre o saldo no final.
"""

# TODO: adicione depositar() na classe e teste aqui


# ==============================================================================
# PARTE 3 - SACAR: UM MÉTODO QUE DEVOLVE UMA RESPOSTA
# ==============================================================================
"""
Adicione o método "sacar(self, valor)":
  - se o saldo for suficiente, desconta o valor, imprime uma mensagem de
    saque e devolve True
  - se não for, imprime "Saldo insuficiente" e devolve False

O return permite que o código de fora saiba se deu certo. Teste assim:

  if conta_ana.sacar(30):
      print("Pode entregar o lanche")
  else:
      print("Compra cancelada")

Teste uma vez com um valor que a conta tem e outra com um valor maior
que o saldo.
"""

# TODO: adicione sacar() na classe e faça os dois testes aqui


# ==============================================================================
# PARTE 4 - PIX: UM OBJETO MEXENDO EM OUTRO
# ==============================================================================
"""
Adicione o método "pix(self, destino, valor)". O parâmetro "destino" é
outra Conta.

Dentro do método, não repita a lógica do saque. Use o que você já fez:
  1. chame self.sacar(valor)
  2. se o saque deu certo, chame destino.depositar(valor)

Faça um Pix do Bruno para a Ana e mostre o saldo das duas contas. Depois
tente um Pix maior do que o saldo do Bruno e confira que nenhum dos dois
saldos mudou.
"""

# TODO: adicione pix() na classe e teste aqui


# ==============================================================================
# PARTE 5 - DUAS VARIÁVEIS, UMA CONTA SÓ
# ==============================================================================
"""
A mãe da Ana também tem acesso à conta dela pelo aplicativo. Rode:

  conta_no_app_da_mae = conta_ana
  conta_no_app_da_mae.depositar(100)
  conta_ana.mostrar_saldo()

Responda em um comentário: por que o saldo da Ana aumentou, se o
depósito foi feito por conta_no_app_da_mae?

Agora crie uma conta nova com Conta("Ana") e faça um depósito nela.
Mostre o saldo das duas contas da Ana. Por que dessa vez elas não estão
ligadas?
"""

# TODO: faça o teste e escreva suas respostas aqui


# ==============================================================================
# PARTE 6 - EXTRATO
# ==============================================================================
"""
Todo banco guarda as movimentações da conta. Faça assim:

  1. No __init__, crie o atributo "historico" como uma lista vazia.
     Ele não vem por parâmetro, toda conta começa com o histórico vazio.
  2. Em depositar() e em sacar() (quando o saque der certo), adicione
     um texto na lista, como "Depósito: +50.00" ou "Saque: -30.00".
  3. Crie o método "extrato(self)", que imprime o nome do titular, cada
     item do histórico e o saldo final.

Chame extrato() na conta da Ana e na do Bruno. O Pix da Parte 4
aparece no extrato, mesmo você não tendo mexido no método pix()?
Por quê?
"""

# TODO: faça as mudanças na classe e chame extrato() aqui


# ==============================================================================
# PARA PENSAR (responda como comentário)
# ==============================================================================
"""
Nada impede alguém de escrever direto:

  conta_ana.saldo = conta_ana.saldo - 1000

O que dá errado se o programa fizer isso em vez de chamar sacar()?
Pense no saldo e no histórico.
"""

# TODO: escreva sua resposta aqui


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
