from flask import Flask, render_template, request, jsonify
from bfs import buscar_solucion_BSF

app = Flask(__name__)

# Ruta principal (Frontend)
@app.route("/")
def index():
    return render_template("index.html")


# API que resuelve el puzzle
@app.route("/resolver", methods=["POST"])
def resolver():

    estado = request.json["estado"]

    estado_inicial = list(map(int, estado.split(",")))
    solucion = [1,2,3,4]

    nodo_solucion = buscar_solucion_BSF(estado_inicial, solucion)

    resultado = []

    if nodo_solucion is not None:
        nodo = nodo_solucion

        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()

    return jsonify(resultado)


# Ejecutar local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)