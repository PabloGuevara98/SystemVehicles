from app import app, db
from app.models import Vendedor, Comprador, Vehiculo, Venta, Ganancia


if __name__ == "__main__":
    app.run(debug=True)
