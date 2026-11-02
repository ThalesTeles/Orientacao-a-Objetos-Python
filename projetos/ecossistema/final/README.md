# Simulador de Ecossistema (versão final)

Projeto final de Orientação a Objetos com Python: plantas, coelhos e raposas numa grade. A cada ciclo, todos os seres agem. O estado fica salvo num banco SQLite (Peewee), e a página é servida pelo Flask.

## Como rodar

```bash
cd cursos/orientacao-a-objetos-python/projetos/ecossistema/final
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abra **http://127.0.0.1:5000** no navegador. Para parar o servidor: `Ctrl+C` no terminal.

- O banco `ecossistema.db` é criado na primeira execução, nesta pasta.
- Fechar o navegador ou parar o servidor **não** apaga o ecossistema: rode de novo e ele continua do mesmo ciclo.
- Para recomeçar do zero: botão **Reiniciar** (ou apague o `ecossistema.db`).

## Estrutura (MVC)

| Arquivo | Papel |
|---|---|
| `modelos.py` | **Model**: `BaseModel`, `Estado` (ciclo) e os seres `Ser` → `Planta`, `Animal` → `Coelho`, `Raposa` |
| `ecossistema.py` | Classe `Ecossistema`: a lista de seres (agregação), a grade e o ciclo |
| `app.py` | **Controller**: rotas do Flask (`/`, `/avancar`, `/adicionar`, `/remover`, `/reiniciar`) |
| `templates/index.html` | **View**: a grade, os contadores e os botões |
| `static/estilo.css` | Visual da página |

## Conceitos usados

- **Herança de models**: `Ser` declara `energia`, `idade`, `x`, `y`; cada espécie tem a sua tabela com essas colunas.
- **Sobrescrita e polimorfismo**: `Planta.agir()` cresce e se espalha; `Animal.agir()` come, anda e se reproduz. O ciclo só faz `ser.agir(self)` para cada ser.
- **Sobrescrita com `super()`**: `Coelho.casas_para_andar()` filtra as casas de `Animal` e foge das raposas.
- **Agregação**: o `Ecossistema` guarda os seres, mas eles existem no banco por conta própria.
- **`random`**: ordem dos seres em cada ciclo, presa escolhida, chance de a caça dar certo, casa do filhote e brotos novos.
- **Formulários POST + `redirect`**: cada botão é um `<form method="post">`; a rota altera o banco e redireciona para `/` (Post/Redirect/Get), sem JavaScript.
- **CRUD**: criar (Adicionar), ler (grade e contadores), atualizar (Avançar ciclo), remover (clicar num ser).

## Regras

| Ser | A cada ciclo |
|---|---|
| 🌱 Planta | +1 de energia; com energia ≥ 4, solta um broto numa casa vizinha livre |
| 🐰 Coelho | −1 de energia; come uma planta vizinha (+3) ou anda (fugindo das raposas); filhote com energia ≥ 7 |
| 🦊 Raposa | −1 de energia; tenta comer um coelho vizinho (50% de chance, +5) ou anda; filhote com energia ≥ 12 |

- Energia 0 ou idade acima do limite da espécie: o ser morre.
- O filhote leva metade da energia do pai.
- Todo ciclo brotam 8 plantas em casas livres (sementes trazidas pelo vento), para as plantas nunca acabarem.
- Os números ficam nas constantes de cada classe (`modelos.py`) e no topo de `ecossistema.py`.

## Equilíbrio

Predador e presa numa grade pequena oscilam: os coelhos se multiplicam, as raposas crescem atrás deles, os coelhos caem e as raposas passam fome. Numa simulação de 8 rodadas de 200 ciclos, as três espécies sobreviveram até o fim em metade delas; nas outras, uma espécie sumiu entre os ciclos 50 e 140. Para a demonstração, basta usar os botões **Adicionar** e reintroduzir a espécie.
