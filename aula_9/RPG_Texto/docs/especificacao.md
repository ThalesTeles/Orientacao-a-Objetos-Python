# Projeto Final — RPG de Texto em POO

## 1. O que você vai construir

Um RPG de texto jogado no terminal: você escolhe uma classe de personagem,
entra em uma masmorra com 5 salas e enfrenta monstros, armadilhas e itens até
vencer todas as salas (vitória) ou morrer (derrota).

Você **não** precisa escrever o menu, o loop do jogo nem o combate por
turnos, isso já vem pronto nos arquivos `jogo.py`, `combate.py` e
`dados.py`. Sua tarefa é implementar as **classes** que esses arquivos usam.

## 2. Diagrama de classes

```
PersonagemBase
 ├── Guerreiro
 ├── Mago
 ├── Arqueiro
 └── Monstro

Item            (a mochila de PersonagemBase guarda Itens)
Sala            (pode conter um Monstro e/ou um Item)
Masmorra        (contém um Personagem e uma lista de Salas)
```

- `Guerreiro`, `Mago`, `Arqueiro` e `Monstro` **são um** `PersonagemBase`
  (herança), todos reaproveitam `atacar()`, `receber_dano()` e
  `esta_vivo()` sem reescrever nada disso.
- `PersonagemBase` **tem uma** mochila de `Item`.
- `Sala` **tem** (opcionalmente) um `Monstro` ou um `Item`.
- `Masmorra` **tem** um personagem e uma lista de `Sala`.

## 3. Classes que você vai implementar

### 3.1 `PersonagemBase` (arquivo `personagem.py`)

| Atributo | Tipo | Descrição |
|---|---|---|
| `nome` | str | Nome do personagem |
| `vida` | int | Vida atual |
| `vida_maxima` | int | Teto de cura |
| `ataque` | int | Bônus somado ao d20 para acertar e usado no cálculo de dano |
| `defesa` | int | Valor que o `d20 + ataque` do oponente precisa superar |
| `chance_critico` | float | Probabilidade (0 a 1) de dano crítico |
| `mochila` | list[Item] | Itens carregados |
| `buffs` | list[dict] | Efeitos temporários ativos |

| Método | Descrição |
|---|---|
| `__init__(nome, vida, ataque, defesa, chance_critico)` | Construtor |
| `atacar(alvo)` | Rola `d20 + self.ataque` contra `alvo.defesa`; se acertar, calcula dano (com chance de crítico) e chama `alvo.receber_dano()` |
| `receber_dano(dano)` | Subtrai `dano` de `vida`, sem deixar negativo |
| `usar_item(item)` | Chama `item.aplicar_efeito(self)` e remove o item da mochila |
| `esta_vivo()` | Retorna `vida > 0` |
| `atualizar_buffs()` | Reduz `turnos_restantes` de cada buff; remove os que zeraram e desfaz o bônus |
| `status()` | Imprime nome, vida e vida_maxima (já implementado como exemplo) |

### 3.2 `Guerreiro(PersonagemBase)`
Vida alta, defesa alta, ataque médio. Método extra `golpe_forte(alvo)`: ataque
com bônus de dano fixo (ex: +5), reaproveitando `atacar()`.

### 3.3 `Mago(PersonagemBase)`
Vida baixa, ataque alto, crítico alto. Método extra `bola_de_fogo(alvo)`:
ataque que ignora parte da defesa do alvo (`alvo.defesa // 2`).

### 3.4 `Arqueiro(PersonagemBase)`
Equilibrado entre Guerreiro e Mago. Método extra `tiro_certeiro(alvo)`:
ataque com `chance_critico` dobrada só naquele golpe.

### 3.5 `Monstro(PersonagemBase)` (arquivo `monstro.py`)

Atributos extras: `dificuldade` (1 a 5), `pontos_atributo_drop` (ganho do
jogador ao vencer) e `chance_drop_item` (chance de deixar item ao morrer),
ambos proporcionais à dificuldade.

Função auxiliar (fora da classe): `gerar_monstro(dificuldade)` — cria e
retorna um `Monstro` com vida, ataque e defesa que crescem com a
dificuldade.

### 3.6 `Item` (arquivo `item.py`)

| Atributo | Tipo | Descrição |
|---|---|---|
| `nome` | str | Ex: "Poção de Cura" |
| `tipo` | str | `"cura"`, `"ataque"`, `"defesa"` ou `"critico"` |
| `valor` | int/float | Quanto cura ou quanto bônus dá |
| `duracao_turnos` | int | Turnos de combate que o efeito dura (0 para cura) |

Método: `aplicar_efeito(personagem)` — se `tipo == "cura"`, soma `valor` à
vida (limitado a `vida_maxima`); senão, adiciona um buff em
`personagem.buffs` por `duracao_turnos` turnos.

### 3.7 `Sala` (arquivo `sala.py`)

| Atributo | Tipo | Descrição |
|---|---|---|
| `numero` | int | Posição na masmorra |
| `dificuldade` | int | Igual ao número da sala |
| `tipo_evento` | str | `"monstro"`, `"item"`, `"armadilha"` ou `"vazia"` |
| `monstro` | Monstro ou None | Preenchido se `tipo_evento == "monstro"` |
| `item` | Item ou None | Preenchido se `tipo_evento == "item"` |

| Método | Descrição |
|---|---|
| `__init__(numero)` | Define dificuldade e chama `sortear_evento()` |
| `sortear_evento()` | Usa `random.choices` com pesos (50% monstro, 30% item, 20% armadilha) |
| `executar(personagem)` | Aplica o evento: inicia combate, entrega item, ou causa dano de armadilha |

### 3.8 `Masmorra` (arquivo `masmorra.py`)

| Atributo | Tipo | Descrição |
|---|---|---|
| `personagem` | PersonagemBase | O jogador |
| `salas` | list[Sala] | Sequência de salas (5 por padrão) |

| Método | Descrição |
|---|---|
| `__init__(personagem, numero_salas)` | Gera a lista de `Sala` |
| `jogar()` | Percorre as salas em ordem até o personagem morrer ou terminar a masmorra |

## 4. Regras do jogo (para entender o que você está implementando)

- No início, o jogador escolhe a classe (Guerreiro, Mago ou Arqueiro).
- Em cada sala:
  - **Vazia** → segue para a próxima.
  - **Armadilha** → dano automático, sem escolha.
  - **Item** → adicionado automaticamente à mochila.
  - **Monstro** → combate por turnos; a cada turno o jogador escolhe entre
    ataque normal, habilidade especial, usar item ou tentar fugir (a chance
    de fuga já está pronta em `dados.py`, na função `chance_fuga`).
- Ao vencer um monstro: o jogador ganha `pontos_atributo_drop` (aplicado
  automaticamente no `ataque`) e, por sorteio, pode ganhar um item extra.
- Se o jogador fugir com sucesso, a sala termina sem prêmio.
- Se a vida chegar a 0, é derrota. Se sobreviver às 5 salas, é vitória.

## 5. O que já está pronto (não mexer)

- `jogo.py` — boas-vindas, escolha de classe, loop principal.
- `combate.py` — menu de combate por turnos (ataque / habilidade / item / fugir).
- `dados.py` — rolagem de d20 e cálculo da chance de fuga.

## 6. Como testar

1. Implemente os arquivos na ordem: `item.py` → `personagem.py` →
   `monstro.py` → `sala.py` → `masmorra.py`.
2. Rode `python jogo.py` no terminal a cada arquivo terminado para ver o
   jogo ganhando vida aos poucos.
3. Jogue até a masmorra terminar (vitória ou derrota) para confirmar que
   todas as classes estão se comunicando corretamente.

## 7. Critérios de entrega

- [ ] Todas as classes implementadas sem usar `pass`/`TODO` restantes.
- [ ] `Guerreiro`, `Mago` e `Arqueiro` usam `super().__init__()` corretamente.
- [ ] `Monstro` herda de `PersonagemBase` e reaproveita `atacar()`,
      `receber_dano()` e `esta_vivo()` sem reescrevê-los.
- [ ] O jogo roda do início ao fim (`python jogo.py`) sem erros.
- [ ] Cada classe especial (`golpe_forte`, `bola_de_fogo`, `tiro_certeiro`)
      funciona como descrito.
