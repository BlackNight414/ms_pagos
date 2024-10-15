from app.repositories import PagosRepository
from app.models import Pago


class PagosService:

    def __init__(self) -> None:
        self.pagos_respository = PagosRepository()

    def add(self, pago: Pago):
        return self.pagos_respository.add(pago)