from app import db
from datetime import datetime

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propietario_nombre = db.Column(db.String(100), nullable=False)
    propietario_direccion = db.Column(db.String(200), nullable=False)
    propietario_correo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(20), nullable=False, unique=True)
    chasis = db.Column(db.String(50), nullable=False, unique=True)
    motor = db.Column(db.String(50), nullable=False, unique=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    clase_vehiculo = db.Column(db.String(50), nullable=False)
    tipo_vehiculo = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    fecha_matricula = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_ultima_revision = db.Column(db.DateTime, nullable=True)

    def __init__(self, propietario_nombre, propietario_direccion, propietario_correo, placa, chasis, motor, marca, modelo, clase_vehiculo, tipo_vehiculo, color, anio, fecha_matricula, fecha_ultima_revision=None):
        self.propietario_nombre = propietario_nombre
        self.propietario_direccion = propietario_direccion
        self.propietario_correo = propietario_correo
        self.placa = placa
        self.chasis = chasis
        self.motor = motor
        self.marca = marca
        self.modelo = modelo
        self.clase_vehiculo = clase_vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.color = color
        self.anio = anio
        self.fecha_matricula = fecha_matricula
        self.fecha_ultima_revision = fecha_ultima_revision

    def to_dict(self):
        return {
            'id': self.id,
            'propietario_nombre': self.propietario_nombre,
            'propietario_direccion': self.propietario_direccion,
            'propietario_correo': self.propietario_correo,
            'placa': self.placa,
            'chasis': self.chasis,
            'motor': self.motor,
            'marca': self.marca,
            'modelo': self.modelo,
            'clase_vehiculo': self.clase_vehiculo,
            'tipo_vehiculo': self.tipo_vehiculo,
            'color': self.color,
            'anio': self.anio,
            'fecha_matricula': self.fecha_matricula,
            'fecha_ultima_revision': self.fecha_ultima_revision
        }
