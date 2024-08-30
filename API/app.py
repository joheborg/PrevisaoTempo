from flask import Flask, render_template, jsonify
from data import Banco
from get_api import Clima

app = Flask(__name__)


@app.route("/")
def hello():
    banco = Banco()
    estados = banco.listar_estados()

    if estados is None:
        estados = []

    return render_template("index.html", estados=estados)


@app.get("/cidades/<estado>")
def buscar_cidades(estado):
    cidades = Clima.buscar_cidades(estado)
    if cidades is None:
        return jsonify({"error": "Não foi possível buscar as cidades"}), 500
    return jsonify(cidades)


@app.get("/weather/<cidade>")
def buscar_clima(cidade):
    clima = Clima.buscar_clima(cidade)
    if clima is None:
        return jsonify({"error": "Não foi possível buscar as cidades"}), 500

    return jsonify(clima)


@app.get("/weather15days/<cidade>")
def buscar_clima_15_dias(cidade):
    clima = Clima.buscar_clima_15_dias(cidade)
    if clima is None:
        return jsonify({"error": "Não foi possível buscar as cidades"}), 500

    return jsonify(clima)


if __name__ == "__main__":
    app.run(debug=True)
