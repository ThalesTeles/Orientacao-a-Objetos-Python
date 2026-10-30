# jogo.py

from objetos.personagem import Guerreiro, Mago, Arqueiro
from objetos.masmorra import Masmorra


def escolher_classe():
    print("=== RPG de Texto — Escolha sua Classe ===")
    print("1 - Guerreiro (mais vida e defesa)")
    print("2 - Mago (ataque alto, vida baixa, crítico alto)")
    print("3 - Arqueiro (equilibrado)")
    escolha = input("> ").strip()
    nome = input("Nome do personagem: ").strip() or "Herói"

    if escolha == "1":
        return Guerreiro(nome)
    elif escolha == "2":
        return Mago(nome)
    elif escolha == "3":
        return Arqueiro(nome)
    else:
        print("Opção inválida, escolhendo Guerreiro por padrão.")
        return Guerreiro(nome)


def main():
    print("Bem-vindo(a) à Masmorra!\n")
    personagem = escolher_classe()
    masmorra = Masmorra(personagem, numero_salas=5)
    masmorra.jogar()


if __name__ == "__main__":
    main()
