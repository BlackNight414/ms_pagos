from app import db
from app.models import Pago


class PagosRepository:
    
    def add(self, pago: Pago):
        db.session.add(pago)
        db.session.commit()
        return pago