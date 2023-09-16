from flask import Blueprint, request, jsonify
from app.models import Comprador
from app import db

compradores_blueprint = Blueprint('compradores', __name__)

@compradores_blueprint.route('/compradores', methods=['GET'])
def listar_compradores():
    compradores = Comprador.query.all()
    return jsonify([comprador.to_dict() for comprador in compradores])

@compradores_blueprint.route('/compradores', methods=['POST'])
def crear_comprador():
    data = request.get_json()
    nuevo_comprador = Comprador(
        nombre=data['nombre'],
        contacto=data['contacto']
    )
    db.session.add(nuevo_comprador)
    db.session.commit()
    return jsonify(nuevo_comprador.to_dict()), 201

@compradores_blueprint.route('/compradores/<int:id>', methods=['GET'])
def obtener_comprador(id):
    comprador = Comprador.query.get_or_404(id)
    return jsonify(comprador.to_dict())

# ... (puedes agregar más rutas aquí para actualizar o eliminar compradores)
