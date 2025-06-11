from app.models import Egresos
from app.repositories import EgresosRepositorio
from datetime import date

class EgresosServicio:

    def __init__(self):
        self.egreso_repositorio = EgresosRepositorio()

    def retirar_saldo(self, egreso: Egresos) -> Egresos:
        return self.egreso_repositorio.agregar_egreso(egreso)
    
    def buscar_por_id(self, id: int) -> Egresos:
        return self.egreso_repositorio.buscar_por_id(id)
    
    def filtrar_por_fecha(self, fecha: date):
        return self.egreso_repositorio.filtrar_por_fecha(fecha)