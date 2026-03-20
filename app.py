from flask import Flask, render_template, request, jsonify
from collections import deque

app = Flask(__name__)

# Grafo de vuelos
vuelos = {
    "JiloYork": ["CDMX", "Hidalgo"],
    "Hidalgo": ["SLP", "JiloYork", "Monterrey"],
    "Monterrey": ["CDMX", "Hidalgo"],
    "QRO": ["SLP"],
    "SLP": ["Zacatecas", "QRO", "Hidalgo", "CDMX", "Tamaulipas"],
    "Zacatecas": ["GDL", "SLP"],
    "Morelos": ["CDMX", "Tamaulipas"],
    "CDMX":["Monterrey", "Tamaulipas", "Morelos", "JiloYork", "SLP"],
    "Tamaulipas":["CDMX", "Morelos", "SLP"],
    "GDL":["Zacatecas"]
}

# BFS para encontrar ruta
def bfs_vuelos(inicio, destino):

    cola = deque()
    cola.append((inicio, [inicio]))

    visitados = set()

    while cola:

        ciudad, ruta = cola.popleft()

        if ciudad == destino:
            return ruta

        visitados.add(ciudad)

        for vecino in vuelos.get(ciudad, []):
            if vecino not in visitados:
                cola.append((vecino, ruta + [vecino]))

    return None


# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")


# API de búsqueda
@app.route("/buscar", methods=["POST"])
def buscar():

    data = request.json

    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    inicio = data.get("inicio")
    destino = data.get("destino")

    if not inicio or not destino:
        return jsonify({"error": "Completa origen y destino"}), 400

    ruta = bfs_vuelos(inicio, destino)

    if not ruta:
        return jsonify({"error": "No hay ruta disponible"}), 400

    return jsonify({
        "inicio": inicio,
        "destino": destino,
        "ruta": ruta
    })


# Ejecutar
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)