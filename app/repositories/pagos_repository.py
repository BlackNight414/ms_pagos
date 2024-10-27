from app import db
from app.models import Pago
from datetime import datetime

class PagosRepository:
    
    def add(self, pago: Pago):
        db.session.add(pago)
        db.session.commit()
        return pago
    
    def get_by_id(self, pago_id: int):
        return db.session.query(Pago).filter(Pago.id == pago_id).first()
    
    def delete(self, pago_id: int, observaciones: str = None):
        pago = self.get_by_id(pago_id)
        if pago:
            pago.fecha_eliminacion = datetime.now()
            pago.observaciones = observaciones
            db.session.add(pago)
            db.session.commit()
            return pago