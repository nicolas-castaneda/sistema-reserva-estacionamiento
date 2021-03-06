
import re
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario, Auto, Estacionamiento, Reserva, db

def isemail(email):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email)
def v_celular(celular):
    if not celular:
        return "Envie un numero de celular"
    if not celular.isdigit():
        return "El numero de celular debe ser numerico"
    if len(celular) != 9:
        return "El numero de celular debe tener 9 digitos"
    if Usuario.query.filter_by(celular=celular).first() is not None:
        return "El numero de celular ya existe"
    return None

def v_dni(dni):
    if not dni:
        return "Envie un DNI"
    if not dni.isdigit():
        return "El DNI debe ser numerico"
    if len(dni) != 8:
        return "El DNI debe tener 8 digitos"
    if Usuario.query.filter_by(dni=dni).first() is not None:
        return "El DNI ya existe"
    return None

def v_nombre(nombre):
    if not nombre:
        return "Envie un nombre"
    if not nombre.isalpha():
        return "El nombre debe ser solo letras"
    if len(nombre) < 3 or len(nombre) > 50:
        return "El nombre debe tener entre 3 y 50 caracteres"
    return None

def v_correo(correo, get_user=False):
    if not correo:
        return "Envie un correo"
    if not isemail(correo):
        return "El correo debe ser valido"
    if len(correo) < 5 or len(correo) > 50:
        return "El correo debe tener entre 5 y 50 caracteres"
    if not get_user and Usuario.query.filter_by(correo=correo).first() is not None:
        return "El correo ya existe"
    
    return None

def v_login(correo, contrasena):
    user = Usuario.query.filter_by(correo=correo).one_or_none()
    if user is None:
        return {'success': False, 'message': "El correo no existe"}
    if not check_password_hash(user.contrasena, contrasena):
        return {'success': False, 'message': "Contrase??a incorrecta"}
    return {'success': True, 'user': user}

def v_contrasena(contrasena, get_user=False):
    if not contrasena:
        return "Envie una contrase??a"
    if get_user:
        return None
    if not re.search("[a-z]", contrasena):
        return "No hay minusculas en tu contrase??a."
    if not re.search("[A-Z]", contrasena):
        return "No hay mayusculas en tu contrase??a."
    if not re.search("[0-9]", contrasena):
        return "No hay numeros en tu contrase??a."
    if not re.search("[?=.*[@#$%^&-+=()_]", contrasena):
        return "No hay caracteres especiales en tu contrase??a."
    if re.search("\\s", contrasena):
        return "No se permiten espacios en la contrase??a."
    if len(contrasena) < 5 or len(contrasena) > 20:
        return "La contrase??a debe tener entre 5 y 20 caracteres."
    return None

def v_placa(placa):
    if not placa:
        return "Envie una placa"
    if len(placa) > 6:
        return "La placa no debe exceder los 6 digitos"
    if Auto.query.filter_by(placa=placa).first() is not None:
        return "El vehiculo ya existe"
    return None

def v_marca(marca):
    if not marca:
        return "Envie una marca"
    return None

def v_modelo(modelo):
    if not modelo:
        return "Envie un modelo"
    return None

def v_color(color):
    if not color:
        return "Envie un color"
    return None

def v_lugar(lugar):
    estacionamiento=Estacionamiento.query.filter_by(lugar=lugar).first()
    if estacionamiento.estadoRegistro=='DIS':
        return None
    return "Lugar no disponible"

def v_fecha(inicio,fin):
    if datetime.now()>inicio:
        return "Fecha ingresada no valida"
    if datetime.now()>fin:
        return "Fecha ingresada no valida"
    if fin<inicio:
        return "Fecha ingresada no valida"
    return None

def actualizarEstadoAuto(placa, idReserva):
    auto=Auto.query.filter_by(placa=placa).first()
    reserva=Reserva.query.filter_by(idReserva=idReserva).first()
    if auto.estado != 'DIS' and reserva:
        auto.estado='DIS'
    auto.update()
    
def actualizarEstadoEstacionamiento(lugar, idReserva):
    estacionamiento=Estacionamiento.query.filter_by(lugar=lugar).first()
    reserva=Reserva.query.filter_by(idReserva=idReserva).first()
    if estacionamiento.estadoRegistro != 'DIS' and reserva:
        if (estacionamiento.estadoRegistro == 'RES'):
            estacionamiento.estadoRegistro  = 'OCU'
        elif(estacionamiento.estadoRegistro == 'OCU'):
            estacionamiento.estadoRegistro = 'DIS'
    reserva.update()    

def actualizarEstadoReserva(idReserva):
    reserva=Reserva.query.filter_by(idReserva=idReserva).first()
    if reserva:
        if reserva.estadoRegistro != 'CER':
            if (reserva.estadoRegistro == 'PEN'):
                reserva.estadoRegistro  = 'OCU'
            elif(reserva.estadoRegistro == 'OCU'):
                reserva.estadoRegistro = 'CER'
        reserva.update()

def crear_estacionamientos():
    for i in range(5):
        for j in range(ord('A'),ord('F')):
            lugar = chr(j)+str(i+1) 
            testEstacionamiento=Estacionamiento(lugar=lugar, estadoRegistro='DIS')
            db.session.add(testEstacionamiento)
            db.session.commit()

def crear_persona():
    testPersona=Usuario("75330321", "985013664", "Marco Antonio", "a@a.com", generate_password_hash("1234"), "REG")
    db.session.add(testPersona)
    db.session.commit()

def crear_auto():
    testAuto=Auto(1,'A8','Toyota','Corolla','rojo', 'DIS')
    db.session.add(testAuto)
    db.session.commit()

def crear_reserva():
    testReserva=Reserva(1, 1, 1, '2023-05-16T20:57', '2023-05-17T23:57', 4.05, 81, 'DIS')
    db.session.add(testReserva)
    db.session.commit()