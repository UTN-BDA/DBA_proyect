from app.models import Egresos
from app.repositories import EgresosRepositorio
from app.services.ingresos import IngresosServicios
# from app.services.balance import Balance
from datetime import date

class EgresosServicio:

    def __init__(self):
        self.__egreso_repositorio = EgresosRepositorio()
        self.__ingreso_service = IngresosServicios()

    def retirar_saldo(self, egreso: Egresos) -> Egresos:
        # Si se tiene saldo suficiente.
        saldo = self.__ingreso_service.total_ingresos() - self.total_gastos()
        if saldo >= egreso.monto:
            return self.__egreso_repositorio.agregar_egreso(egreso)
        else:
            raise ValueError 
    
    def buscar_por_id(self, id: int) -> Egresos:
        return self.__egreso_repositorio.buscar_por_id(id)
    
    def filtrar_por_fecha(self, fecha: date):
        return self.__egreso_repositorio.filtrar_por_fecha(fecha)
    
    def total_gastos(self):
        total = self.__egreso_repositorio.total_gastos()
        return total if total else 0