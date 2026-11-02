# Jogo da Memória (versão final)

Projeto final de Orientação a Objetos com Python. Cada partida, carta e tema é uma linha no banco SQLite (Peewee), e a página é servida pelo Flask. É tudo feito com cliques em formulários, sem JavaScript.

## Como rodar

```bash
cd cursos/orientacao-a-objetos-python/projetos/jogo-da-memoria/final
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abra **http://127.0.0.1:5000**. Para parar: `Ctrl+C`. O banco `memoria.db` é criado na primeira execução, já com três temas (Animais, Frutas, Python).

## Estrutura (MVC)

| Arquivo | Papel |
|---|---|
| `modelos.py` | **Model**: `Tema`, `Figura`, `Partida`, `Carta` e as regras da jogada |
| `modos.py` | `Modo` → `Solo`, `Dupla`: herança e polimorfismo, sem banco |
| `imagens.py` | Ajuste das imagens enviadas (Pillow); funcionalidade extra |
| `app.py` | **Controller**: rotas de partidas e de temas |
| `templates/` | **View**: `base.html` (herança de templates), início, partida, temas, tema |
| `static/` | `estilo.css` e `imagens/` (as figuras enviadas, criada sozinha) |

## Tabelas e relações

```
Tema 1 ── N Figura 1 ── N Carta N ── 1 Partida N ── 1 Tema
```

- **Figura** é a face de um par: cada imagem (ou texto) do tema vira duas cartas na mesa.
- `ForeignKeyField` é a referência de um objeto a outro guardada no banco; `backref` dá a lista do outro lado (`tema.figuras`, `partida.cartas`).
- `on_delete="CASCADE"` + `delete_instance(recursive=True)`: apagar a partida apaga as cartas (composição).

## Herança e polimorfismo: modos de jogo

`Partida.virar()` não sabe se a partida é de um ou de dois jogadores. Depois de cada jogada, ela só chama `self.regras.ao_acertar()` ou `self.regras.ao_errar()`:

| | `Solo` | `Dupla` |
|---|---|---|
| `ao_acertar()` | nada (herdado) | ponto para quem está na vez, que joga de novo |
| `ao_errar()` | nada (herdado) | passa a vez |
| `placar()` | jogadas (herdado) | `super().placar()` + pontos de cada um |
| `resultado()` | "terminou em N jogadas" | vencedor ou empate |

O campo `Partida.modo` guarda a chave (`"solo"`/`"dupla"`) e a propriedade `regras` cria o objeto certo a partir de `MODOS`. Um modo novo (contra o tempo, três jogadores) é só uma subclasse nova em `modos.py`.

## Imagens: como o ajuste funciona

- Tamanho recomendado: **256 × 256 px**, quadrada, PNG com fundo transparente (a página avisa).
- Qualquer outro tamanho é ajustado por `ImageOps.pad` do Pillow: a imagem é ampliada ou reduzida até o lado maior caber em 256 px, mantendo a proporção (sem distorcer), e o espaço que sobra vira transparente. A reamostragem é a LANCZOS, a de melhor qualidade do Pillow.
- `ImageOps.exif_transpose` desvira fotos de celular; tudo é salvo em PNG com nome aleatório (`uuid`), para dois alunos não sobrescreverem `gato.png` um do outro.
- Arquivo que não é imagem é recusado com aviso.

## Regras

- Uma jogada são duas cartas. Par certo: ficam verdes. Par errado: ficam abertas até o próximo clique.
- Um jogador: termina quando acha todos os pares e entra no ranking (menos jogadas primeiro).
- Dois jogadores: quem acerta marca ponto e joga de novo; quem erra passa a vez.

## Temas iniciais

Formas (imagens geradas pelo próprio programa), Animais (emojis) e Python (palavras). Novos temas são de imagens por padrão; também dá para criar de texto ou emoji.
