"""
personagem.py
PersonagemBase (classe mãe) e as subclasses Guerreiro, Mago e Arqueiro.

# PROBLEMA
Guerreiro, Mago, Arqueiro e (mais tarde) Monstro compartilham os mesmos
atributos e ações básicas (atacar, receber dano, usar item...). Copiar esse
código em cada classe seria repetição, é exatamente o problema que herança
resolve.

# PERGUNTA
O que cada subclasse tem de DIFERENTE da PersonagemBase? (dica: só os valores
iniciais de __init__ e um método extra de habilidade especial)

# DICA
- Em atacar(): role um d20 (random.randint(1, 20)), some com self.ataque
  (+ bonus_ataque) e compare com alvo.defesa (- ignora_defesa). Se acertar,
  calcule o dano, veja se é crítico (random.random() < chance) e chame
  alvo.receber_dano(dano).
- Nas subclasses, use super().__init__(...) para não repetir o __init__ da
  PersonagemBase.
- golpe_forte/bola_de_fogo/tiro_certeiro podem simplesmente chamar
  self.atacar(alvo, bonus_ataque=...) ou self.atacar(alvo, ignora_defesa=...)
  reaproveitando o método atacar() em vez de duplicar a rolagem de dados.
"""
import random


class PersonagemBase:
    def __init__(self, nome, vida, ataque, defesa, chance_critico):
        # TODO: guarde nome, vida, vida_maxima, ataque, defesa, chance_critico.
        # TODO: crie self.mochila = [] e self.buffs = [].
        pass

    def atacar(self, alvo, bonus_ataque=0, ignora_defesa=0, multiplicador_critico=1):
        # TODO: role o d20, calcule ataque_total e defesa_alvo, decida se
        # acerta, calcule o dano (considerando crítico) e chame
        # alvo.receber_dano(dano). Print o resultado para o jogador ver.
        pass

    def receber_dano(self, dano):
        # TODO: subtraia dano de self.vida, sem deixar vida negativa.
        pass

    def usar_item(self, item):
        # TODO: chame item.aplicar_efeito(self) e remova o item da mochila.
        pass

    def esta_vivo(self):
        # TODO: retorne True se vida > 0.
        pass

    def atualizar_buffs(self):
        # TODO: para cada buff em self.buffs, diminua turnos_restantes.
        # Quando chegar a 0, desfaça o bônus (if/elif pelo
        # buff["atributo"], ex: self.ataque -= buff["valor"]) e remova o buff da lista.
        pass

    def status(self):
        print(f"{self.nome}: {self.vida}/{self.vida_maxima} HP")


class Guerreiro(PersonagemBase):
    def __init__(self, nome):
        # TODO: chame super().__init__ com vida alta, defesa alta, ataque médio.
        pass

    def golpe_forte(self, alvo):
        # TODO: ataque com bonus_ataque fixo (ex: +5), reaproveitando self.atacar().
        pass


class Mago(PersonagemBase):
    def __init__(self, nome):
        # TODO: chame super().__init__ com vida baixa, ataque alto, crítico alto.
        pass

    def bola_de_fogo(self, alvo):
        # TODO: ataque que ignora parte da defesa do alvo (alvo.defesa // 2).
        pass


class Arqueiro(PersonagemBase):
    def __init__(self, nome):
        # TODO: chame super().__init__ com atributos equilibrados.
        pass

    def tiro_certeiro(self, alvo):
        # TODO: ataque com multiplicador_critico=2.
        pass
