"""
==============================================================================
RPG DE TEXTO - CLASSES (GABARITO / REFERÊNCIA DO PROFESSOR)
==============================================================================

Implementação de referência das classes descritas na especificação.
Útil para:
  - Testar se o jogo (rpg_jogo.py) funciona de ponta a ponta.
  - Conferir as soluções dos alunos.

Para rodar o jogo completo com este gabarito, troque temporariamente o
nome deste arquivo para "classes_rpg.py" (fazendo backup do arquivo dos
alunos antes) - rpg_jogo.py importa sempre de "classes_rpg".
==============================================================================
"""

import random


# ==============================================================================
# PERSONAGEM BASE
# ==============================================================================
class PersonagemBase:
    def __init__(self, nome, vida, ataque, defesa, chance_critico):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa
        self.chance_critico = chance_critico
        self.mochila = []
        self.buffs = []

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} sofreu {dano} de dano! (vida: {self.vida}/{self.vida_maxima})")

    def atacar(self, alvo):
        dado = random.randint(1, 20)
        total = dado + self.ataque
        print(f"{self.nome} ataca {alvo.nome}! (d20={dado} + {self.ataque} = {total} vs defesa {alvo.defesa})")

        if total >= alvo.defesa:
            dano = self.ataque + random.randint(1, 6)
            critico = random.random() < self.chance_critico
            if critico:
                dano *= 2
                print("CRÍTICO!")
            print(f"Acertou! {dano} de dano.")
            alvo.receber_dano(dano)
        else:
            print("O ataque errou!")

    def usar_item(self, item):
        item.aplicar_efeito(self)
        self.mochila.remove(item)

    def atualizar_buffs(self):
        buffs_restantes = []
        for buff in self.buffs:
            buff["turnos_restantes"] -= 1
            if buff["turnos_restantes"] <= 0:
                atributo_atual = getattr(self, buff["atributo"])
                setattr(self, buff["atributo"], atributo_atual - buff["valor"])
                print(f"O efeito de {buff['atributo']} de {self.nome} acabou.")
            else:
                buffs_restantes.append(buff)
        self.buffs = buffs_restantes

    def status(self):
        print(f"{self.nome}: {self.vida}/{self.vida_maxima} vida | ataque {self.ataque} | defesa {self.defesa}")


# ==============================================================================
# SUBCLASSES DE PERSONAGEM (HERANÇA)
# ==============================================================================
class Guerreiro(PersonagemBase):
    def golpe_forte(self, alvo):
        dado = random.randint(1, 20)
        total = dado + self.ataque
        print(f"{self.nome} desfere um GOLPE FORTE em {alvo.nome}! (d20={dado} + {self.ataque} = {total} vs defesa {alvo.defesa})")
        if total >= alvo.defesa:
            dano = self.ataque + random.randint(1, 6) + 5
            if random.random() < self.chance_critico:
                dano *= 2
                print("CRÍTICO!")
            print(f"Acertou! {dano} de dano.")
            alvo.receber_dano(dano)
        else:
            print("O golpe errou!")


class Mago(PersonagemBase):
    def bola_de_fogo(self, alvo):
        dado = random.randint(1, 20)
        defesa_reduzida = alvo.defesa // 2
        total = dado + self.ataque
        print(f"{self.nome} conjura uma BOLA DE FOGO em {alvo.nome}! (d20={dado} + {self.ataque} = {total} vs defesa reduzida {defesa_reduzida})")
        if total >= defesa_reduzida:
            dano = self.ataque + random.randint(1, 6)
            if random.random() < self.chance_critico:
                dano *= 2
                print("CRÍTICO!")
            print(f"Acertou! {dano} de dano.")
            alvo.receber_dano(dano)
        else:
            print("A bola de fogo errou!")


class Arqueiro(PersonagemBase):
    def tiro_certeiro(self, alvo):
        dado = random.randint(1, 20)
        total = dado + self.ataque
        print(f"{self.nome} prepara um TIRO CERTEIRO em {alvo.nome}! (d20={dado} + {self.ataque} = {total} vs defesa {alvo.defesa})")
        if total >= alvo.defesa:
            dano = self.ataque + random.randint(1, 6)
            if random.random() < self.chance_critico * 2:
                dano *= 2
                print("CRÍTICO!")
            print(f"Acertou! {dano} de dano.")
            alvo.receber_dano(dano)
        else:
            print("A flecha errou!")


# ==============================================================================
# MONSTRO (também herda de PersonagemBase!)
# ==============================================================================
class Monstro(PersonagemBase):
    def __init__(self, nome, vida, ataque, defesa, dificuldade):
        super().__init__(nome, vida, ataque, defesa, chance_critico=0.1)
        self.dificuldade = dificuldade
        self.pontos_atributo_drop = dificuldade * 2
        self.chance_drop_item = min(dificuldade * 0.1, 1.0)

    def chance_fuga(self):
        chance = 0.9 - (self.dificuldade * 0.15)
        return max(chance, 0.1)


NOMES_MONSTROS = ["Goblin", "Esqueleto", "Lobo Sombrio", "Troll", "Dragão Jovem"]


def gerar_monstro(dificuldade):
    nome = random.choice(NOMES_MONSTROS)
    vida = 20 + dificuldade * 10
    ataque = 2 + dificuldade
    defesa = 8 + dificuldade
    return Monstro(nome, vida, ataque, defesa, dificuldade)


# ==============================================================================
# ITEM
# ==============================================================================
class Item:
    def __init__(self, nome, tipo, valor, duracao_turnos=0):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.duracao_turnos = duracao_turnos

    def aplicar_efeito(self, personagem):
        if self.tipo == "cura":
            vida_antes = personagem.vida
            personagem.vida = min(personagem.vida_maxima, personagem.vida + self.valor)
            recuperado = personagem.vida - vida_antes
            print(f"{personagem.nome} usou {self.nome} e recuperou {recuperado} de vida!")
            return

        nomes_atributos = {"ataque": "ataque", "defesa": "defesa", "critico": "chance_critico"}
        nome_atributo = nomes_atributos[self.tipo]
        valor_atual = getattr(personagem, nome_atributo)
        setattr(personagem, nome_atributo, valor_atual + self.valor)
        personagem.buffs.append({
            "atributo": nome_atributo,
            "valor": self.valor,
            "turnos_restantes": self.duracao_turnos,
        })
        print(f"{personagem.nome} usou {self.nome}! Bônus de {self.tipo} por {self.duracao_turnos} turnos.")


def gerar_item_aleatorio():
    opcoes = [
        Item("Poção de Cura", "cura", 20),
        Item("Poção de Ataque", "ataque", 5, duracao_turnos=3),
        Item("Poção de Defesa", "defesa", 3, duracao_turnos=3),
        Item("Poção de Acerto Crítico", "critico", 0.2, duracao_turnos=3),
    ]
    return random.choice(opcoes)


# ==============================================================================
# SALA
# ==============================================================================
class Sala:
    def __init__(self, numero):
        self.numero = numero
        self.dificuldade = numero
        self.tipo_evento = None
        self.monstro = None
        self.item = None
        self.sortear_evento()

    def sortear_evento(self):
        self.tipo_evento = random.choices(
            ["monstro", "item", "armadilha", "vazia"],
            weights=[50, 25, 15, 10],
        )[0]
        if self.tipo_evento == "monstro":
            self.monstro = gerar_monstro(self.dificuldade)
        elif self.tipo_evento == "item":
            self.item = gerar_item_aleatorio()


# ==============================================================================
# MASMORRA
# ==============================================================================
class Masmorra:
    def __init__(self, personagem, numero_salas=5):
        self.personagem = personagem
        self.salas = self.gerar_salas(numero_salas)

    def gerar_salas(self, numero_salas):
        return [Sala(i) for i in range(1, numero_salas + 1)]
