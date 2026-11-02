"""Controller: as rotas do Flask ligam os botões da página ao Ecossistema."""

from flask import Flask, render_template, request, redirect, url_for

from modelos import db, criar_tabelas, ESPECIES
from ecossistema import Ecossistema, LARGURA

app = Flask(__name__)
criar_tabelas()

ESPECIES_POR_NOME = {especie.NOME: especie for especie in ESPECIES}


@app.before_request
def conectar():
    db.connect(reuse_if_open=True)


@app.teardown_request
def desconectar(erro):
    if not db.is_closed():
        db.close()


@app.route("/")
def index():
    ecossistema = Ecossistema()
    if ecossistema.ciclo == 0 and not ecossistema.seres:
        ecossistema.reiniciar()  # primeira vez: povoa a grade
    return render_template("index.html", eco=ecossistema, especies=ESPECIES,
                           largura=LARGURA)


@app.route("/avancar", methods=["POST"])
def avancar():
    ecossistema = Ecossistema()
    ciclos = int(request.form.get("ciclos", 1))
    for _ in range(ciclos):
        ecossistema.avancar()
    return redirect(url_for("index"))


@app.route("/adicionar", methods=["POST"])
def adicionar():
    especie = ESPECIES_POR_NOME.get(request.form["especie"])
    if especie:
        Ecossistema().adicionar_aleatorio(especie)
    return redirect(url_for("index"))


@app.route("/remover", methods=["POST"])
def remover():
    especie = ESPECIES_POR_NOME.get(request.form["especie"])
    if especie:
        ser = especie.get_or_none(especie.id == int(request.form["id"]))
        if ser:
            Ecossistema().remover(ser)
    return redirect(url_for("index"))


@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    Ecossistema().reiniciar()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
