from flask import Blueprint, request, jsonify
from app.models import Vehiculo
from app import db

vehiculos_blueprint = Blueprint('vehiculos', __name__)

@vehiculos_blueprint.route('/vehiculos', methods=['GET'])
def listar_vehiculos():
    vehiculos = Vehiculo.query.all()
    return jsonify([vehiculo.to_dict() for vehiculo in vehiculos])

@vehiculos_blueprint.route('/vehiculos', methods=['POST'])
def crear_vehiculo():
    data = request.get_json()
    nuevo_vehiculo = Vehiculo(
        propietario_nombre=data['propietario_nombre'],
        propietario_direccion=data['propietario_direccion'],
        propietario_correo=data['propietario_correo'],
        placa=data['placa'],
        chasis=data['chasis'],
        motor=data['motor'],
        marca=data['marca'],
        modelo=data['modelo'],
        clase_vehiculo=data['clase_vehiculo'],
        tipo_vehiculo=data['tipo_vehiculo'],
        color=data['color'],
        anio=data['anio'],
        fecha_matricula=data['fecha_matricula'],
        fecha_ultima_revision=data.get('fecha_ultima_revision')
    )
    db.session.add(nuevo_vehiculo)
    db.session.commit()
    return jsonify(nuevo_vehiculo.to_dict()), 201

@vehiculos_blueprint.route('/vehiculos/<int:id>', methods=['GET'])
def obtener_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    return jsonify(vehiculo.to_dict())

# ... (puedes agregar más rutas aquí para actualizar o eliminar vehículos)
