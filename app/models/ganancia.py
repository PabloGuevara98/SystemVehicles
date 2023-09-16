from app import db

class Ganancia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    venta_id = db.Column(db.Integer, db.ForeignKey('venta.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)

    def __init__(self, venta_id, monto):
        self.venta_id = venta_id
        self.monto = monto

    def to_dict(self):
        return {
            'id': self.id,
            'venta_id': self.venta_id,
            'monto': self.monto
        }
