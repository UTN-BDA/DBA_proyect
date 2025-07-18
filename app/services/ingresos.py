from app.models import Ingresos
from app.repositories import IngresosRepositorios

class IngresosServicios:
     repo= IngresosRepositorios()
     def agregar_saldo(self, monto, fecha, detalle, categoria_id):
        nuevo_ingreso = Ingresos(monto=monto, fecha=fecha, detalle=detalle, categoria_id=categoria_id)
        return self.repo.agregar_saldo(nuevo_ingreso) 

     def eliminar_ingresos(self, ingreso_id: int):
         ingreso = self.repo.consultar_ingresos(ingreso_id)
         if ingreso:
            self.repo.eliminar_ingresos(ingreso)
         else:
            raise KeyError("Ingreso no encontrado")
        
     def consultar_ingresos(self, ingreso_id: int) -> Ingresos:
         return self.repo.consultar_ingresos(ingreso_id)
     
     def total_ingresos(self):
        total = self.repo.total_ingresos()
        return total if total else 0
     
     def listar_ingresos(self) -> list[Ingresos]:
         return self.repo.listar_ingresos()