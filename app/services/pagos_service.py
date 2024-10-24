from app.repositories import PagosRepository
from app.models import Pago


class PagosService:

    def __init__(self) -> None:
        self.pagos_respository = PagosRepository()

    def registrar_pago(self, pago: Pago):
        return self.pagos_respository.add(pago)
    
    def eliminar_pago(self, pago_id: int):
        self.pagos_respository.delete(pago_id)