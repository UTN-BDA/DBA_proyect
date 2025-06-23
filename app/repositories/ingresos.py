from app import db
from app.models import Ingresos
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy import func

class IngresosRepositorios:
    def agregar_saldo(self, ingreso: Ingresos) ->Ingresos:
        try:
            db.session.add(ingreso)
            db.session.commit()
            return ingreso
        except IntegrityError as e:
            db.session.rollback()
            raise e
             
    def consultar_ingresos(self, ingreso_id: int) -> Ingresos:
         try:
             return db.session.query(Ingresos).filter_by(id = ingreso_id).one()
         except NoResultFound as e:
             raise e
        
        
    def eliminar_ingresos(self, ingreso: Ingresos):
        try:
            db.session.delete(ingreso)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            raise e
    
    def total_ingresos(self):
        return db.session.query(func.sum(Ingresos.monto)).scalar()
    
    def listar_ingresos(self) -> list[Ingresos]:
        return db.session.query(Ingresos).all()
    
   