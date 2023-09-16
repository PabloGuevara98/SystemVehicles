from flask import Blueprint, request, jsonify
from app.models import Ganancia
from app import db

ganancias_blueprint = Blueprint('ganancias', __name__)

@ganancias_blueprint.route('/ganancias', methods=['GET'])
def listar_ganancias():
    ganancias = Ganancia.query.all()
    return jsonify([ganancia.to_dict() for ganancia in ganancias])

@ganancias_blueprint.route('/ganancias', methods=['POST'])
def crear_ganancia():
    data = request.get_json()
    nueva_ganancia = Ganancia(
        venta_id=data['venta_id'],
        monto=data['monto']
    )
    db.session.add(nueva_ganancia)
    db.session.commit()
    return jsonify(nueva_ganancia.to_dict()), 201

@ganancias_blueprint.route('/ganancias/<int:id>', methods=['GET'])
def obtener_ganancia(id):
    ganancia = Ganancia.query.get_or_404(id)
    return jsonify(ganancia.to_dict())

# ... (puedes agregar más rutas aquí para actualizar o eliminar ganancias)
