from flask import Blueprint, request, jsonify
from app.models import Venta
from app import db

ventas_blueprint = Blueprint('ventas', __name__)

@ventas_blueprint.route('/ventas', methods=['GET'])
def listar_ventas():
    ventas = Venta.query.all()
    return jsonify([venta.to_dict() for venta in ventas])

@ventas_blueprint.route('/ventas', methods=['POST'])
def crear_venta():
    data = request.get_json()
    nueva_venta = Venta(
        vendedor_id=data['vendedor_id'],
        comprador_id=data['comprador_id'],
        vehiculo_id=data['vehiculo_id'],
        precio_venta=data['precio_venta']
    )
    db.session.add(nueva_venta)
    db.session.commit()
    return jsonify(nueva_venta.to_dict()), 201

@ventas_blueprint.route('/ventas/<int:id>', methods=['GET'])
def obtener_venta(id):
    venta = Venta.query.get_or_404(id)
    return jsonify(venta.to_dict())

# ... (puedes agregar más rutas aquí para actualizar o eliminar ventas)
