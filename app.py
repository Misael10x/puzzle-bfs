from flask import Flask, render_template, request, jsonify
from bfs import buscar_solucion_BSF

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resolver", methods=["POST"])
def resolver():

    data = request.json

    if not data or "estado" not in data:
        return jsonify({"error": "Estado requerido"}), 400

    estado = data["estado"]

    try:
        estado_inicial = list(map(int, estado.split(",")))
    except:
        return jsonify({"error": "Formato incorrecto. Usa ejemplo: 4,2,3,1"}), 400

    solucion = [1, 2, 3, 4]

    nodo_solucion = buscar_solucion_BSF(estado_inicial, solucion)

    resultado = []

    if nodo_solucion:

        nodo = nodo_solucion

        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)