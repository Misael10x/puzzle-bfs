from flask import Flask, render_template, request, jsonify
from bfs import buscar_solucion_BSF

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resolver", methods=["POST"])
def resolver():

    estado = request.json["estado"]

    estado_inicial = list(map(int, estado.split(",")))
    solucion = [1,2,3,4]

    nodo_solucion = buscar_solucion_BSF(estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)