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

from server.funciones import *

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, max_age=10)

    crear_estacionamientos()

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response
    
    
    @app.route('/usuario', methods=['GET'])
    def get_usuarios():
        users = Usuario.query.all()
        return jsonify([user.format() for user in users])
    
    @app.route('/session', methods=['POST'])
    def login():
        datos = request.get_json()
        correo = datos.get('correo', None)
        if msg:= v_correo(correo, True):
            abort(400, msg)
        contrasena = datos.get('contrasena', None)
        if msg:= v_contrasena(contrasena, True):
            abort(400, msg)
            
        user = Usuario.query.filter_by(correo=correo).one_or_none()
        if not user:
            abort(404, 'Usuario no encontrado')
        if not check_password_hash(user.contrasena, contrasena):
            abort(401, 'Contraseña incorrecta')
        
        return jsonify({
            'success': True,
            'user': user.format()
        })
    
    @app.route('/usuario', methods=['POST'])
    def create_usuario():
        data = request.get_json()
        if not data:
            abort(400, 'No se recibieron datos')
        dni = data.get('DNI', None)
        if msg:= v_dni(dni):
            abort(400, msg)
        celular = data.get('celular', None)
        if msg:= v_celular(celular):
            abort(400, msg)
        nombres = data.get('nombres', None)
        if msg:= v_nombre(nombres):
            abort(400, msg)
        correo = data.get('correo', None)
        if msg:= v_correo(correo):
            abort(400, msg)
        contrasena = data.get('contrasena', None)
        if msg:= v_contrasena(contrasena):
            abort(400, msg)
        nuevo_usuario = Usuario(dni, celular, nombres, correo, generate_password_hash(contrasena), 'REG')
        nuevo_usuario.insert()
        return jsonify({
            'success': True,
            'user': nuevo_usuario.format()
            }
        )

    @app.route("/estacionamientos", methods=['GET'])
    def get_estacionamientos():
        lugaresEstacionamiento=[estacionamiento.format() for estacionamiento in Estacionamiento.query.order_by('idEstacionamiento').all()]

        if len(lugaresEstacionamiento) == 0:
                abort(404,'No hay estacionamientos')
        return jsonify({
                'success':True,
                'estacionamientos':lugaresEstacionamiento,
                'total_estacionamientos':len(lugaresEstacionamiento)
        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request' if not error.description else error.description
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized' if not error.description else error.description
        }), 401
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not found' if not error.description else error.description
        }), 404
    
    return app