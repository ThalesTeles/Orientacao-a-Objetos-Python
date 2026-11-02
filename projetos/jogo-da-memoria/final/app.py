"""Controller: as rotas do Flask ligam os cliques da página às partidas."""

from flask import Flask, render_template, request, redirect, url_for, abort

from imagens import salvar_imagem
from modelos import (db, criar_tabelas, Tema, Figura, Partida, Carta,
                     PASTA_IMAGENS, TAMANHO_IMAGEM, PARES_POSSIVEIS)
from modos import MODOS

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 30 * 1024 * 1024  # 30 MB por envio
criar_tabelas()


@app.before_request
def conectar():
    db.connect(reuse_if_open=True)


@app.teardown_request
def desconectar(erro):
    if not db.is_closed():
        db.close()


def buscar_ou_404(modelo, id):
    objeto = modelo.get_or_none(modelo.id == id)
    if objeto is None:
        abort(404)
    return objeto


# ---------------------------------------------------------------- partidas
@app.route("/")
def index():
    temas = [tema for tema in Tema.select().order_by(Tema.nome) if tema.pares_possiveis()]
    em_andamento = Partida.select().where(~Partida.terminada).order_by(
        Partida.criada_em.desc())
    return render_template("index.html", temas=temas, em_andamento=em_andamento,
                           ranking=Partida.ranking(), duplas=Partida.ultimas_duplas(),
                           modos=MODOS,
                           pares_possiveis=PARES_POSSIVEIS, erro=request.args.get("erro"))


@app.route("/nova", methods=["POST"])
def nova():
    tema = buscar_ou_404(Tema, int(request.form["tema"]))
    modo = request.form.get("modo", "solo")
    if modo not in MODOS:
        modo = "solo"
    jogador1 = request.form["jogador1"].strip() or "Jogador 1"
    jogador2 = request.form.get("jogador2", "").strip() or None
    if modo == "dupla" and not jogador2:
        return redirect(url_for("index", erro="Dois jogadores: preencha o nome do jogador 2."))
    if modo == "solo":
        jogador2 = None
    pares = int(request.form["pares"])
    if pares not in tema.pares_possiveis():
        pares = max(tema.pares_possiveis())
    partida = Partida.nova(tema, pares, modo, jogador1, jogador2)
    return redirect(url_for("partida", id=partida.id))


@app.route("/partida/<int:id>")
def partida(id):
    partida = buscar_ou_404(Partida, id)
    total = partida.pares() * 2
    colunas = 4 if total <= 16 else total // 4
    return render_template("partida.html", partida=partida, colunas=colunas)


@app.route("/partida/<int:id>/virar/<int:carta_id>", methods=["POST"])
def virar(id, carta_id):
    partida = buscar_ou_404(Partida, id)
    carta = Carta.get_or_none(Carta.id == carta_id, Carta.partida == partida)
    if carta:
        partida.virar(carta)
    return redirect(url_for("partida", id=id))


@app.route("/partida/<int:id>/remover", methods=["POST"])
def remover_partida(id):
    buscar_ou_404(Partida, id).delete_instance(recursive=True)
    return redirect(url_for("index"))


# ---------------------------------------------------------------- temas
@app.route("/temas")
def temas():
    return render_template("temas.html", temas=Tema.select().order_by(Tema.nome),
                           erro=request.args.get("erro"))


@app.route("/temas", methods=["POST"])
def criar_tema():
    nome = request.form["nome"].strip()
    tipo = "texto" if request.form.get("tipo") == "texto" else "imagem"
    if not nome:
        return redirect(url_for("temas", erro="Dê um nome ao tema."))
    if Tema.select().where(Tema.nome == nome).exists():
        return redirect(url_for("temas", erro=f"Já existe um tema chamado {nome}."))
    tema = Tema.create(nome=nome, tipo=tipo)
    return redirect(url_for("tema", id=tema.id))


@app.route("/temas/<int:id>")
def tema(id):
    return render_template("tema.html", tema=buscar_ou_404(Tema, id),
                           tamanho=TAMANHO_IMAGEM, minimo=PARES_POSSIVEIS[0],
                           erro=request.args.get("erro"))


@app.route("/temas/<int:id>/renomear", methods=["POST"])
def renomear_tema(id):
    tema = buscar_ou_404(Tema, id)
    nome = request.form["nome"].strip()
    if not nome:
        return redirect(url_for("tema", id=id, erro="O nome não pode ficar vazio."))
    if Tema.select().where(Tema.nome == nome, Tema.id != id).exists():
        return redirect(url_for("tema", id=id, erro=f"Já existe um tema chamado {nome}."))
    tema.nome = nome
    tema.save()  # UPDATE só na linha do tema: figuras e partidas continuam ligadas pelo id
    return redirect(url_for("tema", id=id))


@app.route("/temas/<int:id>/imagens", methods=["POST"])
def enviar_imagens(id):
    tema = buscar_ou_404(Tema, id)
    recusadas = []
    for arquivo in request.files.getlist("imagens"):
        if not arquivo.filename:
            continue
        nome = salvar_imagem(arquivo, PASTA_IMAGENS, TAMANHO_IMAGEM)
        if nome:
            Figura.create(tema=tema, valor=nome)
        else:
            recusadas.append(arquivo.filename)
    if recusadas:
        return redirect(url_for("tema", id=id, erro="Não são imagens: " + ", ".join(recusadas)))
    return redirect(url_for("tema", id=id))


@app.route("/temas/<int:id>/textos", methods=["POST"])
def adicionar_textos(id):
    tema = buscar_ou_404(Tema, id)
    existentes = {figura.valor for figura in tema.figuras}
    for texto in dict.fromkeys(request.form["textos"].split()):  # sem repetidos
        if texto not in existentes:
            Figura.create(tema=tema, valor=texto)
    return redirect(url_for("tema", id=id))


@app.route("/figuras/<int:id>/remover", methods=["POST"])
def remover_figura(id):
    figura = buscar_ou_404(Figura, id)
    tema_id = figura.tema_id
    figura.remover()
    return redirect(url_for("tema", id=tema_id))


@app.route("/temas/<int:id>/remover", methods=["POST"])
def remover_tema(id):
    buscar_ou_404(Tema, id).remover()
    return redirect(url_for("temas"))


@app.errorhandler(413)
def arquivo_grande(erro):
    return redirect(url_for("temas", erro="Envio grande demais: mande no máximo 30 MB por vez."))


if __name__ == "__main__":
    app.run(debug=True)
