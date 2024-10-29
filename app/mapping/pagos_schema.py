from marshmallow import Schema, fields, post_load
from app.models import Pago
from datetime import datetime

class PagoSchema(Schema):
    id: int = fields.Integer()
    producto_id: int = fields.Integer(required=True)
    precio: float = fields.Float(required=True)
    medio_pago: str = fields.String(required=True)
    fecha_eliminacion: datetime = fields.DateTime(dump_only=True) 
    observaciones: str = fields.String()

    @post_load
    def deserealizar_pago(self, data, **kwargs):
        return Pago(**data)