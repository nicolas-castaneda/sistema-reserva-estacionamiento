from distutils.log import error
import json
from functools import wraps
from flask import (
    Flask,
    current_app,
    jsonify,
    abort,
    render_template,
    request
)
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from models import setup_db, Usuario, Auto, Estacionamiento, Reserva

import jwt
import threading
from datetime import datetime, timedelta
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
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = Usuario.query.filter_by(correo=data['correo']).first()
            if not user:
                abort(401, 'User not found')
            return f(user)
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
    #CORS(app, max_age=10)
    CORS(app)
    crear_persona()
    crear_estacionamientos()

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS,UPDATE')
        return response
    
    
    @app.route('/usuario', methods=['GET'])
    def get_usuarios():
        users = Usuario.query.all()
        return jsonify({'success': True,
                        'users':[user.format() for user in users],
                        'count': len(users)
                        })
    
    @app.route('/session', methods=['POST'])
    def login():
        datos = request.get_json()
        correo = datos.get('correo', None)
        if msg:= v_correo(correo, True):
            abort(400, msg)
        contrasena = datos.get('contrasena', None)
        if msg:= v_contrasena(contrasena, True):
            abort(400, msg)
            
        informacion = v_login(correo, contrasena)
        if not informacion['success']:
            abort(401, informacion['message'])
        user = informacion['user']
        token = jwt.encode({
            'id': user.idUsuario,
            'correo': user.correo,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, current_app.config['SECRET_KEY'],
        algorithm='HS256')
        
        return jsonify({
            'success': True,
            'user': user.format(),
            'token': token
        })
    
    @app.route('/session', methods=['PATCH'])
    @token_required
    def session_update(user):
        return jsonify({
            'success': True,
            'time': datetime.utcnow(),
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

    @app.route("/autos/<usuario>", methods=['POST'])
    def create_auto(usuario):
        data = request.get_json()
        usuario = Usuario.query.filter_by(correo=usuario).first()
        idUsuario = usuario.idUsuario
        if not idUsuario:
            abort(400, 'No se recibio un usuario')
        if not data:
            abort(400, 'No se recibieron datos')
        placa = data.get('placa',None)
        if msg:= v_placa(placa):
            abort(400, msg)
        marca = data.get('marca',None)
        if msg:= v_marca(marca):
            abort(400, msg)
        modelo = data.get('modelo',None)
        if msg:= v_modelo(modelo):
            abort(400, msg)
        color = data.get('color',None)
        if msg:= v_color(color):
            abort(400, msg)
        try:
            auto = Auto(idUsuario=idUsuario,placa=placa, marca=marca, modelo=modelo, color=color, estado='DIS')
            newAutoId = auto.insert()
            return jsonify({
                'success':True,
                'created':newAutoId,
            })
        except Exception as e:
            print(e)
            abort(500)
        
    @app.route("/reserva", methods=['POST'])
    def create_reserva():
        data = request.get_json()
        if not data:
            abort(400, 'No se recibieron datos')

        usuario = Usuario.query.filter_by(correo=data.get('usuario',None)).first()
        idUsuario = usuario.idUsuario
        if not idUsuario:
            abort(400, 'No se recibio un usuario')
        

        lugar=data.get('lugar', None)
        if msg:= v_lugar(lugar):
                abort(400, msg)

        inicioReserva=data.get('inicioReserva',None)
        finReserva=data.get('finReserva',None)

        datetimeInicioReserva=datetime.strptime(inicioReserva, "%Y-%m-%dT%H:%M")
        datetimeFinReserva=datetime.strptime(finReserva, "%Y-%m-%dT%H:%M")

        inicioReserva=str(datetimeInicioReserva)
        finReserva=str(datetimeFinReserva)

        if msg:= v_fecha(datetimeInicioReserva,datetimeFinReserva):
            abort(400,msg)

        costoReserva=data.get('costoReserva',None)
        costoTotal=data.get('costoTotal',None)
    
        placa = data.get('placa',None)

        opcion = data.get('opcion', None)
        if opcion:
            if msg:= v_placa(placa):
                abort(400, msg)
            marca = data.get('marca',None)
            if msg:= v_marca(marca):
                abort(400, msg)
            modelo = data.get('modelo',None)
            if msg:= v_modelo(modelo):
                abort(400, msg)
            color = data.get('color',None)
            if msg:= v_color(color):
                abort(400, msg)

            auto=Auto(idUsuario, placa, marca, modelo, color, estado='NOD')
            auto.insert()
        else:
            auto=Auto.query.filter_by(idUsuario=idUsuario, placa=placa).first()
            auto.estado = 'NOD'
            auto.update()

        now = datetime.now()

        delayInicio = (datetimeInicioReserva - now).total_seconds()
        delayFin = (datetimeFinReserva - now).total_seconds()

        auto = Auto.query.filter_by(placa=placa).first()
        idAuto = auto.idAuto

        estacionamiento=Estacionamiento.query.filter_by(lugar=lugar).first()
        idEstacionamiento=estacionamiento.idEstacionamiento
        estacionamiento.estadoRegistro='RES'
        estacionamiento.update()

        reserva=Reserva(idUsuario, idEstacionamiento, idAuto, datetimeInicioReserva, datetimeFinReserva, costoReserva, costoTotal, estadoRegistro='PEN')
        idReserva = reserva.insert()

        threading.Timer(delayFin, actualizarEstadoAuto, args=[placa, idReserva]).start()

        threading.Timer(delayInicio, actualizarEstadoEstacionamiento, args=[lugar, idReserva]).start()
        threading.Timer(delayFin, actualizarEstadoEstacionamiento, args=[lugar, idReserva]).start()

        threading.Timer(delayInicio, actualizarEstadoReserva, args=[idReserva]).start()
        threading.Timer(delayFin, actualizarEstadoReserva, args=[idReserva]).start()

        return jsonify({
            'success':True,
            'created':idReserva,
        })

    # @app.route("/autos/<usuario>", methods=['POST'])
    # def create_auto(usuario):
    #     data = request.get_json()
    #     usuario = Usuario.query.filter_by(correo=usuario).first()
    #     idUsuario = usuario.idUsuario
    #     if not idUsuario:
    #         abort(400, 'No se recibio un usuario')
    #     if not data:
    #         abort(400, 'No se recibieron datos')
    #     placa = data.get('placa',None)
    #     if msg:= v_placa(placa):
    #         abort(400, msg)
    #     marca = data.get('marca',None)
    #     if msg:= v_marca(marca):
    #         abort(400, msg)
    #     modelo = data.get('modelo',None)
    #     if msg:= v_modelo(modelo):
    #         abort(400, msg)
    #     color = data.get('color',None)
    #     if msg:= v_color(color):
    #         abort(400, msg)
    #     try:
    #         auto = Auto(idUsuario=idUsuario,placa=placa, marca=marca, modelo=modelo, color=color, estado='DIS')
    #         newAutoId = auto.insert()
    #         return jsonify({
    #             'success':True,
    #             'created':newAutoId,
    #         })
    #     except Exception as e:
    #         print(e)
    #         abort(500)

    @app.route("/autos/<idAuto>", methods=['DELETE'])
    def delete_auto():
        data = request.get_json()
        if not data:
            abort(400, 'No se recibieron datos')
        idAuto = data.get('idAuto',None)
        if not idAuto:
            abort(400, 'No se recibio un idAuto')
        auto = Auto.query.filter_by(idAuto=idAuto).first()
        if not auto:
            abort(400, 'No se encontro el auto')
        auto.delete()
        return jsonify({
            'success':True,
            'deleted':idAuto,
        })
    
    @app.route("/autos/<idAuto>", methods=['PATCH'])
    def update_auto():
        data = request.get_json()
        if not data:
            abort(400, 'No se recibieron datos')
        idAuto = data.get('idAuto',None)
        if not idAuto:
            abort(400, 'No se recibio un idAuto')
        marca = data.get('marca',None)
        if msg:= v_marca(marca):
            abort(400, msg)
        modelo = data.get('modelo',None)
        if msg:= v_modelo(modelo):
            abort(400, msg)
        color = data.get('color',None)
        if msg:= v_color(color):
            abort(400, msg)

        auto = Auto.query.filter_by(idAuto=idAuto).first()
        if not auto:
            abort(400, 'No se encontro el auto')
        auto.marca = marca
        auto.modelo = modelo
        auto.color = color
        auto.update()
        return jsonify({
            'success':True,
            'updated':idAuto,
        })

    @app.route("/reservas/<idReserva>", methods=['DELETE'])
    def delete_reserva():
        data = request.get_json()
        if not data:
            abort(400, 'No se recibieron datos')
        idReserva = data.get('idReserva',None)
        if not idReserva:
            abort(400, 'No se recibio un idReserva')
        reserva = Reserva.query.filter_by(idReserva=idReserva).first()
        if not reserva:
            abort(400, 'No se encontro la reserva')
        reserva.delete()
        return jsonify({
            'success':True,
            'deleted':idReserva,
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

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
                'success': False,
                'error': 422,
                'message': 'Unprocessable' if not error.description else error.description
            }), 422

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Server error' if not error.description else error.description
        }), 500
    
    return app