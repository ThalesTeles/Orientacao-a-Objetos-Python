# dados.py

import random


def rolar_d20():
    """Rola um d20 (1 a 20)."""
    return random.randint(1, 20)


def chance_fuga(dificuldade):
    """Mesma fórmula da classe Desafio (Aula 8): 0.9 - dificuldade * 0.15."""
    return max(0.0, 0.9 - dificuldade * 0.15)
