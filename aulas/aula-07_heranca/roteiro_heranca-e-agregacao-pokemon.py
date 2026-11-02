"""
==============================================================================
AULA 7 - HERANÇA E AGREGAÇÃO EM PYTHON - EDIÇÃO POKÉMON
==============================================================================

Neste roteiro vamos construir um sistema de batalha Pokémon no terminal
aplicando:

  - HERANÇA   (relação "é um")   para especializar tipos de Pokémon;
  - AGREGAÇÃO (relação "tem um") para gerenciar a equipe de um Treinador.

Pré-requisitos: classes, objetos, método construtor (__init__), atributos e
métodos em Python.

Este arquivo roda do começo ao fim: ao executá-lo, a batalha do final começa
no terminal. Na prática da aula, o código abaixo é dividido em três arquivos
dentro de uma pasta "pokemon_tc63oo":

  pokemon.py    -> classes dos Pokémons (superclasse e subclasses)
  treinador.py  -> classe do Treinador (agregação: equipe e mochila)
  jogo.py       -> loop interativo da batalha no terminal
==============================================================================
"""

# ==============================================================================
# 1. HERANÇA x AGREGAÇÃO
# ==============================================================================
"""
Quando o projeto cresce e passa a ter várias classes, elas precisam se
relacionar sem que a gente copie e cole o mesmo código em vários lugares.
Na Orientação a Objetos, usamos duas ferramentas principais para isso:

  HERANÇA   -> pergunta-chave: "É UM?"
      Uma classe filha (subclasse) herda atributos e métodos de uma classe
      mãe (superclasse) e pode alterar ou acrescentar comportamentos.
      Exemplo: um PokemonFogo É UM PokemonBase.

  AGREGAÇÃO -> pergunta-chave: "TEM UM?"
      Um objeto guarda, dentro de um atributo, a referência (ou uma lista)
      de outros objetos independentes.
      Exemplo: um Treinador TEM UMA equipe de objetos PokemonBase.

Dica de ouro:
  - Se a frase "A é um tipo de B" fizer sentido, use HERANÇA: class A(B):
  - Se a frase "A possui um ou mais objetos B" fizer sentido, use
    AGREGAÇÃO: self.lista_b = []
"""


# ==============================================================================
# 2. A SUPERCLASSE PokemonBase  (arquivo pokemon.py)
# ==============================================================================
"""
Todo Pokémon, independentemente do elemento, tem nome, pontos de vida,
ataque e defesa, além de sofrer dano e atacar. Vamos concentrar essa lógica
em uma única classe base.

O dano real, descontando a defesa, segue a fórmula:

    dano_real = max(1, dano_bruto - defesa)

E a vida nunca fica negativa:

    vida = max(0, vida - dano_real)

Também guardamos vida_maxima para saber o limite ao curar o Pokémon.
"""

class PokemonBase:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano_bruto):
        dano_real = max(1, dano_bruto - self.defesa)
        self.vida = max(0, self.vida - dano_real)
        print(f"{self.nome} sofreu {dano_real} de dano! (HP: {self.vida}/{self.vida_maxima})")

    def atacar(self, alvo):
        print(f"⚔️ {self.nome} usou Investida em {alvo.nome}!")
        alvo.receber_dano(self.ataque)


# ==============================================================================
# 3. SUBCLASSES E super()  (arquivo pokemon.py)
# ==============================================================================
"""
Agora criamos três subclasses que herdam de PokemonBase. Cada tipo elemental
já nasce com atributos balanceados e SOBRESCREVE o método atacar(alvo):

  Subclasse      Vida  Ataque  Defesa  Efeito especial no atacar(alvo)
  PokemonAgua     60     12      8     Jato d'Água: causa self.ataque de dano.
  PokemonFogo     45     18      4     Lança-Chamas: causa ataque + 3 de dano.
  PokemonPlanta   50     14      6     Folha Navalha: causa self.ataque e
                                       recupera até 3 de HP.

Como funciona o super()?
Dentro do __init__ da subclasse, chamamos
super().__init__(nome, vida=..., ataque=..., defesa=...) para acionar o
construtor da classe mãe (PokemonBase), sem repetir self.nome = nome,
self.vida = vida etc.
"""

class PokemonAgua(PokemonBase):
    def __init__(self, nome):
        super().__init__(nome, vida=60, ataque=12, defesa=8)

    def atacar(self, alvo):
        print(f"{self.nome} usou Jato d'Água em {alvo.nome}!")
        alvo.receber_dano(self.ataque)


class PokemonFogo(PokemonBase):
    def __init__(self, nome):
        super().__init__(nome, vida=45, ataque=18, defesa=4)

    def atacar(self, alvo):
        print(f"{self.nome} usou Lança-Chamas em {alvo.nome}!")
        alvo.receber_dano(self.ataque + 3)


class PokemonPlanta(PokemonBase):
    def __init__(self, nome):
        super().__init__(nome, vida=50, ataque=14, defesa=6)

    def atacar(self, alvo):
        print(f"{self.nome} usou Folha Navalha em {alvo.nome}!")
        alvo.receber_dano(self.ataque)
        cura = min(3, self.vida_maxima - self.vida)
        self.vida += cura
        if cura > 0:
            print(f"{self.nome} absorveu energia e recuperou {cura} de HP!")


# ==============================================================================
# 4. AGREGAÇÃO: A CLASSE Treinador  (arquivo treinador.py)
# ==============================================================================
"""
Um treinador NÃO É um Pokémon; ele TEM uma equipe de Pokémons e TEM uma
mochila de itens. Por isso usamos AGREGAÇÃO.

  - __init__ recebe apenas o nome e inicializa self.equipe = [] (guarda
    objetos PokemonBase) e self.mochila = ["Poção", "Poção"].
  - capturar(pokemon) adiciona o Pokémon à equipe (máximo de 6).
  - pokemon_ativo() devolve o primeiro Pokémon vivo, ou None se todos
    estiverem derrotados.
  - usar_pocao() remove uma "Poção" da mochila e recupera até 20 de vida do
    Pokémon ativo, sem ultrapassar vida_maxima.
"""

class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.equipe = []
        self.mochila = ["Poção", "Poção"]

    def capturar(self, pokemon):
        if len(self.equipe) < 6:
            self.equipe.append(pokemon)
            print(f"{self.nome} adicionou {pokemon.nome} à equipe!")
        else:
            print("Equipe cheia! (Máximo de 6 Pokémons)")

    def pokemon_ativo(self):
        for pokemon in self.equipe:
            if pokemon.esta_vivo():
                return pokemon
        return None

    def usar_pocao(self):
        ativo = self.pokemon_ativo()
        if "Poção" in self.mochila and ativo is not None:
            self.mochila.remove("Poção")
            ativo.vida = min(ativo.vida_maxima, ativo.vida + 20)
            print(f"{self.nome} usou Poção em {ativo.nome}! (HP: {ativo.vida}/{ativo.vida_maxima})")
        else:
            print("Você não tem mais Poções na mochila!")


# ==============================================================================
# 5. O JOGO INTERATIVO NO TERMINAL  (arquivo jogo.py)
# ==============================================================================
"""
Por fim, integramos as classes e rodamos a primeira batalha no terminal.
Em jogo.py, no começo do arquivo, ficariam os imports:

    from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
    from treinador import Treinador
"""

def jogar():
    print("=== BEM-VINDO(A) AO MUNDO POKÉMON (TC63OO) ===")
    nome_treinador = input("Digite seu nome de Treinador(a): ")
    jogador = Treinador(nome_treinador)

    print("\nEscolha seu Pokémon inicial:")
    print("1 - Squirtle   (Água: alta vida e defesa)")
    print("2 - Charmander (Fogo: alto ataque e queimadura)")
    print("3 - Bulbasaur  (Planta: equilibrado e regenera vida)")

    opcao = input("Opção (1/2/3): ")
    apelido = input("Dê um apelido ao seu Pokémon: ")

    if opcao == "1":
        inicial = PokemonAgua(apelido)
    elif opcao == "2":
        inicial = PokemonFogo(apelido)
    else:
        inicial = PokemonPlanta(apelido)

    jogador.capturar(inicial)

    # Oponente de teste em sala
    rival = PokemonFogo("Charmeleon Selvagem")
    print(f"\nUm {rival.nome} (HP: {rival.vida}) apareceu no caminho!")

    while jogador.pokemon_ativo() is not None and rival.esta_vivo():
        meu_poke = jogador.pokemon_ativo()
        print(f"\n--- Turno de {jogador.nome} ---")
        print(f"Seu Pokémon: {meu_poke.nome} (HP: {meu_poke.vida}/{meu_poke.vida_maxima})")
        print(f"Oponente:    {rival.nome} (HP: {rival.vida}/{rival.vida_maxima})")
        print(f"Poções na mochila: {jogador.mochila.count('Poção')}")

        acao = input("Escolha: (1) Atacar | (2) Usar Poção > ")
        if acao == "2":
            jogador.usar_pocao()
        else:
            meu_poke.atacar(rival)

        if rival.esta_vivo():
            print(f"\n--- Turno de {rival.nome} ---")
            rival.atacar(meu_poke)

    if jogador.pokemon_ativo() is not None:
        print(f"\nVitória! {jogador.nome} e {inicial.nome} venceram a batalha!")
    else:
        print(f"\nTodos os Pokémons de {jogador.nome} foram derrotados...")


if __name__ == "__main__":
    jogar()
