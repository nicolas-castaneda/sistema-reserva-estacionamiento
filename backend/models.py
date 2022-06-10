from flask_sqlalchemy import SQLAlchemy
import os

database_path=f"postgresql://postgres:{os.getenv('POST_PASS')}@localhost:5432/sre"

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Usuario(db.Model):
    __tablename__ = "usuarios"
    idUsuario = db.Column(db.Integer, primary_key = True)
    dni = db.Column(db.String(8), nullable = False)
    celular = db.Column(db.String(9), nullable = False)
    nombres = db.Column(db.String(50), nullable = False)
    correo = db.Column(db.String(50), nullable = False)
    contrasena = db.Column(db.String(256), nullable = False)
    estado = db.Column(db.String(3), nullable = False)
    autos = db.relationship("Adb.uto")
    reservas = db.relationship("Reserva")
    
    def __init__(self, dni, celular, nombres, correo, contrasena, estado):
        self.dni = dni
        self.celular = celular
        self.nombres = nombres
        self.correo = correo
        self.contrasena = contrasena
        self.estado = estado

class Auto(db.Model):
    __tablename__ = "autos"
    idAuto = db.Column(db.Integer, primary_key = True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable = False)
    placa = db.Column(db.String(6), nullable = False)
    marca = db.Column(db.String(50), nullable = False)
    modelo = db.Column(db.String(50), nullable = False)
    color = db.Column(db.String(50), nullable = False)
    estado = db.Column(db.String(3), nullable = False)
    reserva = db.relationship("Reserva")

    def __init__(self, idUsuario,placa, marca, modelo, color, estado):
        self.idUsuario = idUsuario
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estado = estado


class Estacionamiento(db.Model):
    __tablename__ = "estacionamientos"
    idEstacionamiento = db.Column(db.Integer, primary_key = True)
    lugar = db.Column(db.String(10), nullable=False)
    estadoRegistro = db.Column(db.String(3), nullable=False)
    reservas = db.relationship("Reserva")
    def __init__(self,  lugar, estadoRegistro):
        self.lugar = lugar
        self.estadoRegistro = estadoRegistro



class Reserva(db.Model):
    __tablename__ = "reservas"
    idReserva = db.Column(db.Integer, primary_key = True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    idEstacionamiento = db.Column(db.Integer, db.ForeignKey('estacionamientos.idEstacionamiento'), nullable=False)
    idAuto = db.Column(db.Integer, db.ForeignKey('autos.idAuto'), nullable=False)
    inicioReserva = db.Column(db.DateTime, nullable = False)
    finReserva = db.Column(db.DateTime, nullable = False)
    costoReserva = db.Column(db.Float, nullable=False)
    costoTotal = db.Column(db.Float, nullable=False)
    estadoRegistro = db.Column(db.String(3), nullable=False)

    def __init__(self, idUsuario, idEstacionamiento, idAuto, inicioReserva, finReserva, costoReserva, costoTotal, estadoRegistro):
        self.idUsuario = idUsuario
        self.idEstacionamiento = idEstacionamiento
        self.idAuto = idAuto
        self.inicioReserva = inicioReserva
        self.finReserva = finReserva
        self.costoReserva = costoReserva
        self.costoTotal = costoTotal
        self.estadoRegistro = estadoRegistro