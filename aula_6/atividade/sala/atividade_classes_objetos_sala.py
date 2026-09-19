"""
==============================================================================
AULA 6 - ATIVIDADE DE SALA - RECONSTRUINDO AS CLASSES COM MÉTODOS
==============================================================================

Na Aula 5 criamos uma classe "Animal" bem simples, com "pass", e
definimos os atributos manualmente em cada objeto. Hoje vamos
RECONSTRUIR essa mesma classe usando __init__ e métodos.

Complete os espaços marcados com o comentário # TODO.
Depois de completar cada parte, execute o arquivo para conferir se os
prints aparecem corretamente.
==============================================================================
"""

# ==============================================================================
# PARTE 1 - CONSTRUTOR DA CLASSE ANIMAL
# ==============================================================================
"""
Crie a classe "Animal" com um construtor __init__ que recebe e guarda:
  - nome
  - especie
  - idade
  - som   (o som que o animal faz, ex: "Au au", "Miau")
"""

# TODO: crie a classe Animal aqui, com o __init__


# ==============================================================================
# PARTE 2 - MÉTODO "apresentar"
# ==============================================================================
"""
Adicione à classe Animal um método "apresentar(self)" que imprime algo
como:

  "Rex é um(a) cachorro de 3 anos e faz Au au"

Dica: volte na classe que você criou na Parte 1 e adicione o método
dentro dela (lembre-se da indentação!).
"""

# TODO: adicione o método apresentar() na classe Animal


# ==============================================================================
# PARTE 3 - CRIANDO OS OBJETOS COM O CONSTRUTOR
# ==============================================================================
"""
Agora crie DOIS objetos da classe Animal, "cachorro" e "gato", passando
os valores diretamente no construtor (nada de atribuir atributo por
atributo como na Aula 5!). Em seguida, chame apresentar() para cada um.
"""

# TODO: crie o objeto "cachorro" usando Animal(...)


# TODO: crie o objeto "gato" usando Animal(...)


# TODO: chame cachorro.apresentar() e gato.apresentar()


# ==============================================================================
# PARTE 4 - MÉTODO QUE MUDA O ESTADO: "fazer_aniversario"
# ==============================================================================
"""
Adicione à classe Animal um método "fazer_aniversario(self)" que:
  - soma 1 ao atributo "idade" do animal
  - imprime algo como "Rex agora tem 4 anos!"

Depois, chame esse método no objeto "cachorro" e imprima a idade dele
ANTES e DEPOIS de chamar o método, para confirmar que o ESTADO do
objeto mudou.
"""

# TODO: adicione o método fazer_aniversario() na classe Animal


# TODO: imprima a idade do cachorro antes, chame fazer_aniversario(),
# e imprima a idade depois


# ==============================================================================
# PARTE 5 - OBJETOS x VARIÁVEIS (CUIDADO COM A PEGADINHA!)
# ==============================================================================
"""
Faça o seguinte teste:

  gato_apelido = gato       # NÃO cria um novo objeto!
  gato_apelido.nome = "Bichano"
  print(gato.nome)

Rode e observe o resultado. Depois, como comentário, explique com suas
palavras por que "gato.nome" mudou mesmo você tendo alterado só
"gato_apelido.nome".
"""

# TODO: faça o teste acima e imprima o resultado


# TODO: escreva sua explicação aqui como comentário


"""
Agora faça o oposto: crie um objeto REALMENTE novo e independente,
chamado "gato2", usando o construtor Animal(...) de novo (não copiando
a variável "gato"). Altere o nome de "gato2" e confirme que "gato.nome"
NÃO muda dessa vez.
"""

# TODO: crie o objeto "gato2" com o construtor, altere o nome dele e
# confirme que "gato" não foi afetado


# ==============================================================================
# PARTE 6 - MAIS UM ANIMAL E SUA PRÓPRIA CLASSE
# ==============================================================================
"""
Crie um terceiro objeto Animal, com o animal que você quiser, e chame
apresentar() e fazer_aniversario() nele.

Depois, pegue a classe que você criou sozinho(a) na atividade de sala
da Aula 5 (Carro, Jogador, Celular ou Personagem de RPG) e:
  1. Adicione um __init__ com os mesmos atributos de antes.
  2. Adicione PELO MENOS UM método que faça sentido para essa classe
     (ex: Carro.acelerar(), Jogador.marcar_gol(),
     Celular.instalar_app(), Personagem.atacar()...).
  3. Crie dois objetos dessa classe usando o construtor e chame o novo
     método em cada um.
"""

# TODO: crie o terceiro objeto Animal e chame apresentar() e fazer_aniversario()


# TODO: reconstrua sua própria classe da Aula 5 aqui, com __init__ e
# pelo menos um método


# TODO: crie dois objetos dessa classe e chame o novo método neles


# ==============================================================================
# REFLEXÃO FINAL (responda em uma frase, como comentário abaixo)
# ==============================================================================
"""
Comparando com a forma como criamos objetos na Aula 5 (sem __init__,
atribuindo atributo por atributo): o que ficou melhor ou mais seguro
hoje, usando construtor e métodos?
"""

# TODO: escreva sua resposta aqui como comentário


# ==============================================================================
# FIM DA ATIVIDADE DE SALA
# ==============================================================================
