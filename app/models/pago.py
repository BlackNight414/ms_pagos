from app import db
from datetime import datetime

class Pago(db.Model):
    
    __tablename__ = 'pagos'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column('producto_id', db.Integer, nullable=False)
    precio: float = db.Column('precio', db.Float, nullable=False)
    medio_pago: str = db.Column('medio_pago', db.String(120), nullable=False)
    fecha_eliminacion: datetime = db.Column('fecha_eliminacion', db.DateTime)
    observaciones: str = db.Column('observaciones', db.Text)