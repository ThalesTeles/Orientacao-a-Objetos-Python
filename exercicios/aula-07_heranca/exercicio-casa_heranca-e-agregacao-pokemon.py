"""
==============================================================================
AULA 7 - ATIVIDADE DE CASA - A JORNADA NA LIGA POKÉMON
==============================================================================

Para consolidar HERANÇA e AGREGAÇÃO EM VÁRIOS NÍVEIS, expanda o projeto da
aula criando três novas classes. Você vai usar as classes PokemonBase,
PokemonAgua, PokemonFogo, PokemonPlanta e Treinador que já construiu.

Complete os trechos marcados com # TODO. No final, rode o teste da PARTE 4
para conferir se todas as classes funcionam juntas.
==============================================================================
"""

# TODO: traga aqui (ou importe) as classes PokemonBase, PokemonAgua,
# PokemonFogo, PokemonPlanta e Treinador da aula


# ==============================================================================
# PARTE 1 - HERANÇA: A CLASSE PokemonSelvagem  (no arquivo pokemon.py)
# ==============================================================================
"""
Crie a classe "PokemonSelvagem", que herda de PokemonBase.

  - __init__(self, nome, vida, ataque, defesa, raridade) deve chamar
    super().__init__(nome, vida, ataque, defesa) e guardar o atributo extra
    self.raridade (ex.: "Comum", "Raro", "Lendário").
"""

# TODO: crie a classe PokemonSelvagem aqui


# ==============================================================================
# PARTE 2 - AGREGAÇÃO SIMPLES: A CLASSE Ginasio  (no arquivo liga.py)
# ==============================================================================
"""
Um Ginásio TEM uma lista de oponentes.

Crie a classe "Ginasio" com:
  1. __init__(self, nome_ginasio, lider, insignia): guarde os três valores e
     inicialize self.oponentes = [];
  2. adicionar_oponente(self, pokemon): adiciona um PokemonBase (ou
     subclasse) à lista self.oponentes;
  3. desafiar(self, treinador):
       - mostre uma mensagem anunciando o desafio ao ginásio do líder;
       - faça o treinador enfrentar, em sequência, cada oponente enquanto o
         treinador tiver pokemon_ativo() e o oponente estiver vivo;
       - se o treinador derrotar todos os oponentes, mostre que ele
         conquistou a insígnia e devolva True;
       - se ele ficar sem Pokémons vivos antes do fim, devolva False.
"""

# TODO: crie a classe Ginasio aqui


# ==============================================================================
# PARTE 3 - AGREGAÇÃO DE AGREGAÇÕES: A CLASSE LigaPokemon  (no arquivo liga.py)
# ==============================================================================
"""
A Liga Pokémon TEM vários Ginásios.

Crie a classe "LigaPokemon" com:
  1. __init__(self, nome_regiao): guarde o nome e inicialize
     self.ginasios = [];
  2. adicionar_ginasio(self, ginasio): adiciona um Ginasio à lista;
  3. iniciar_jornada(self, treinador):
       - percorra cada ginásio e chame venceu = ginasio.desafiar(treinador);
       - se o treinador perder em algum ginásio (not venceu), interrompa a
         jornada e avise em qual ginásio ele caiu;
       - se vencer todos, mostre a mensagem de Campeão da Liga!
"""

# TODO: crie a classe LigaPokemon aqui


# ==============================================================================
# PARTE 4 - TESTE DA TAREFA DE CASA  (arquivo teste_liga.py)
# ==============================================================================
"""
Quando terminar, descomente o código abaixo e execute-o. Ele monta tudo e
inicia a jornada.
"""

# heroi = Treinador("Red")
# heroi.capturar(PokemonAgua("Blastoise"))
# heroi.capturar(PokemonPlanta("Venusaur"))
#
# ginasio_pedra = Ginasio("Ginásio de Pewter", lider="Brock", insignia="Insígnia da Rocha")
# ginasio_pedra.adicionar_oponente(PokemonSelvagem("Geodude", vida=35, ataque=10, defesa=6, raridade="Comum"))
# ginasio_pedra.adicionar_oponente(PokemonSelvagem("Onix", vida=50, ataque=13, defesa=9, raridade="Raro"))
#
# ginasio_fogo = Ginasio("Ginásio de Cinnabar", lider="Blaine", insignia="Insígnia do Vulcão")
# ginasio_fogo.adicionar_oponente(PokemonSelvagem("Magmar", vida=55, ataque=16, defesa=5, raridade="Raro"))
#
# liga_kanto = LigaPokemon("Kanto")
# liga_kanto.adicionar_ginasio(ginasio_pedra)
# liga_kanto.adicionar_ginasio(ginasio_fogo)
#
# liga_kanto.iniciar_jornada(heroi)


# ==============================================================================
# DESAFIOS EXTRAS (opcional - para ir além!)
# ==============================================================================
"""
1. Vantagem elemental com isinstance(): no método atacar(self, alvo) das
   subclasses, use isinstance(alvo, PokemonFogo) (por exemplo, dentro de
   PokemonAgua) para causar o DOBRO de dano e mostrar "É super efetivo!"
   quando houver vantagem de tipo (Água > Fogo > Planta > Água).

2. Centro Pokémon entre ginásios: crie o método curar_equipe(self) na classe
   Treinador, que restaura o HP de todos os Pokémons de self.equipe para
   vida_maxima depois de vencer cada ginásio.
"""
