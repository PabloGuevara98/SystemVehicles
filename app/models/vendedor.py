from app import db

class Vendedor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(200), nullable=False)

    def __init__(self, nombre, correo_electronico, contrasena_hash):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena_hash = contrasena_hash

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo_electronico': self.correo_electronico,
            # No incluyas la contraseña_hash en la respuesta JSON para mantener la seguridad
        }
