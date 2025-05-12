from app.models import Egresos
from app.repositories import EgresosRepositorio

class EgresosServicio:

    def __init__(self):
        self.egreso_repositorio = EgresosRepositorio()

    def retirar_saldo(self, egreso: Egresos) -> Egresos:
        return self.egreso_repositorio.agregar_egreso(egreso)
    
    def buscar_por_id(self, id: int) -> Egresos:
        return self.buscar_por_id(id)