from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para recibir los datos de las encuestas de KoboToolbox
@app.route('/recibir-datos-kobo', methods=['POST'])
def recibir_datos():
    # Verifica si los datos vienen en formato JSON
    if request.is_json:
        datos_encuesta = request.get_json()  # Se reciben los datos de la encuesta en formato JSON
        print(datos_encuesta)  # Muestra los datos en consola
        return jsonify({"message": "Datos recibidos correctamente"}), 200
    else:
        return jsonify({"error": "Los datos no están en formato JSON"}), 400

# Ruta de prueba para ver que el servidor esté corriendo
@app.route('/')
def index():
    return 'Servidor Flask funcionando correctamente', 200

if __name__ == '__main__':
    # Inicia el servidor Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
