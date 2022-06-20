from distutils.log import error
import json
from functools import wraps
from flask import (
    Flask,
    current_app,
    jsonify,
    abort,
    request
)
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from models import setup_db, Usuario, Auto, Estacionamiento, Reserva

import jwt
import datetime
from server.funciones import *

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            abort(401, invalid_msg)

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = Usuario.query.filter_by(email=data['correo']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            abort(401, expired_msg) # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            abort(401, invalid_msg)

    return _verify


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    setup_db(app)
    CORS(app, max_age=10)

    crear_persona()
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
            
        user = Usuario.authenticate(**datos)
        if not user:
            abort(401, 'Usuario o contraseña incorrectos')
        
        token = jwt.encode({
            'id': user.idUsuario,
            'correo': user.correo,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'])
        
        return jsonify({
            'success': True,
            'user': user.format(),
            'token': token
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

    @app.route("/estacionamiento", methods=['GET'])
    def get_estacionamientos():
        lugaresEstacionamiento=[estacionamiento.format() for estacionamiento in Estacionamiento.query.order_by('idEstacionamiento').all()]

        if len(lugaresEstacionamiento) == 0:
                abort(404,'No hay estacionamientos')
        return jsonify({
                'success':True,
                'estacionamientos':lugaresEstacionamiento,
                'total_estacionamientos':len(lugaresEstacionamiento)
        })

    @app.route("/auto/<usuario>", methods=['GET'])
    def get_autos(usuario):
        usuario = Usuario.query.filter_by(correo=usuario).first()
        if not usuario or usuario is None:
            abort(403,'Requiere cuenta para acceder a contenido')
        idUsuario = usuario.idUsuario
        autos = [auto.format() for auto in Auto.query.filter_by(idUsuario=idUsuario).order_by("idAuto").all()]
        return jsonify({
            'success':True,
            'autos':autos,
            'total_autos':len(autos)
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
            'aunthenticated': False,
            'message': 'Unauthorized' if not error.description else error.description
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Forbidden' if not error.description else error.description
        }), 403
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not found' if not error.description else error.description
        }), 404
    
    return app