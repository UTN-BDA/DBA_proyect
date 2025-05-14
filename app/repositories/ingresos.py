from app import db
from app.models import Ingresos
from sqlalchemy.exc import IntegrityError, NoResultFound

class IngresosRepositorios:
    def agregar_saldo(self, ingreso: Ingresos) ->Ingresos:
        try:
            db.session.add(ingreso)
            db.session.commit()
            return ingreso
        except IntegrityError as e:
            db.session.rollback()
            raise e
        
""" #acá va delete
    def eliminar_ingresos(self,...): #investigar 
        pass

    def consultar_ingresos(self,..):
        pass

    def modificar_ingresos(self, ...):
        pass

 """