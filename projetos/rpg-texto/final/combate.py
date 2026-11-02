# combate.py

import random
from dados import chance_fuga
from objetos.item import gerar_item_aleatorio


def iniciar_combate(personagem, monstro):
    print(f"\nUm {monstro.nome} (dificuldade {monstro.dificuldade}) aparece!")

    while personagem.esta_vivo() and monstro.esta_vivo():
        personagem.status()
        monstro.status()
        print("\nEscolha uma ação:")
        print("1 - Ataque normal")
        print("2 - Habilidade especial")
        print("3 - Usar item")
        print("4 - Tentar fugir")
        escolha = input("> ").strip()

        if escolha == "1":
            personagem.atacar(monstro)
        elif escolha == "2":
            _usar_habilidade_especial(personagem, monstro)
        elif escolha == "3":
            _usar_item_do_menu(personagem)
        elif escolha == "4":
            if random.random() < chance_fuga(monstro.dificuldade):
                print("Você fugiu com sucesso!")
                return
            print("A fuga falhou!")
        else:
            print("Opção inválida.")
            continue

        personagem.atualizar_buffs()

        if not monstro.esta_vivo():
            print(f"\nVocê derrotou {monstro.nome}!")
            personagem.ataque += monstro.pontos_atributo_drop
            print(f"{personagem.nome} ganha +{monstro.pontos_atributo_drop} de ataque!")
            if random.random() < monstro.chance_drop_item:
                item = gerar_item_aleatorio()
                personagem.mochila.append(item)
                print(f"O monstro deixou cair: {item.nome}!")
            return

        if personagem.esta_vivo():
            monstro.atacar(personagem)
            if not personagem.esta_vivo():
                print(f"\n{personagem.nome} foi derrotado...")
                return


def _usar_habilidade_especial(personagem, alvo):
    if hasattr(personagem, "golpe_forte"):
        personagem.golpe_forte(alvo)
    elif hasattr(personagem, "bola_de_fogo"):
        personagem.bola_de_fogo(alvo)
    elif hasattr(personagem, "tiro_certeiro"):
        personagem.tiro_certeiro(alvo)
    else:
        print("Esse personagem não tem habilidade especial.")


def _usar_item_do_menu(personagem):
    if not personagem.mochila:
        print("Sua mochila está vazia!")
        return
    print("Itens na mochila:")
    for i, item in enumerate(personagem.mochila):
        print(f"{i + 1} - {item.nome}")
    escolha = input("Escolha o item (número): ").strip()
    try:
        item = personagem.mochila[int(escolha) - 1]
        personagem.usar_item(item)
    except (ValueError, IndexError):
        print("Escolha inválida.")
