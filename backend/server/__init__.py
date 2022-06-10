from distutils.log import error
from flask import (
    Flask,
    jsonify,
    abort,
    request
)
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from models import setup_db, Usuario, Auto, Estacionamiento, Reserva

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, max_age=10)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/usuario', methods=['POST'])
    def create_usuario():
        data = request.get_json()
        if not data:
            abort(404)
        dni = data.get('DNI')
        celular = data.get('celular')
        print(data)
        usuario = data.get('nombres')
        correo = data.get('email')
        contrasena = data.get('contrasena')
        
        nuevo_usuario = Usuario(dni, celular, usuario, correo, generate_password_hash(contrasena), 'REG')
        nuevo_usuario.insert()
        return jsonify({
            'success': True,
            'usuario': nuevo_usuario.format()
            }
        )

    return app