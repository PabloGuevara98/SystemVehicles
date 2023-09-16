from flask import Blueprint, request, jsonify
from app.models import Vendedor
from app import db

vendedores_blueprint = Blueprint('vendedores', __name__)

@vendedores_blueprint.route('/vendedores', methods=['GET'])
def listar_vendedores():
    vendedores = Vendedor.query.all()
    return jsonify([vendedor.to_dict() for vendedor in vendedores])

@vendedores_blueprint.route('/vendedores', methods=['POST'])
def crear_vendedor():
    data = request.get_json()
    nuevo_vendedor = Vendedor(
        nombre=data['nombre'],
        correo_electronico=data['correo_electronico'],
        contraseña_hash=data['contrasena_hash']
    )
    db.session.add(nuevo_vendedor)
    db.session.commit()
    return jsonify(nuevo_vendedor.to_dict()), 201

@vendedores_blueprint.route('/vendedores/<int:id>', methods=['GET'])
def obtener_vendedor(id):
    vendedor = Vendedor.query.get_or_404(id)
    return jsonify(vendedor.to_dict())

# ... (puedes agregar más rutas aquí para actualizar o eliminar vendedores)

