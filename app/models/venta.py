from app import db
from datetime import datetime

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedor.id'), nullable=False)
    comprador_id = db.Column(db.Integer, db.ForeignKey('comprador.id'), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    precio_venta = db.Column(db.Float, nullable=False)

    def __init__(self, vendedor_id, comprador_id, vehiculo_id, precio_venta):
        self.vendedor_id = vendedor_id
        self.comprador_id = comprador_id
        self.vehiculo_id = vehiculo_id
        self.precio_venta = precio_venta

    def to_dict(self):
        return {
            'id': self.id,
            'vendedor_id': self.vendedor_id,
            'comprador_id': self.comprador_id,
            'vehiculo_id': self.vehiculo_id,
            'fecha': self.fecha,
            'precio_venta': self.precio_venta
        }
