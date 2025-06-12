from app import db
from app.models import Egresos
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from datetime import date

class EgresosRepositorio:
    
    def agregar_egreso(self, egreso: Egresos) -> Egresos:
        try:
            db.session.add(egreso)
            db.session.commit()
            return egreso
        except IntegrityError as e:
            db.session.rollback()
            raise e
        
    def buscar_por_id(self, id: int) -> Egresos:
        return db.session.query(Egresos).filter_by(id = id).first()
    
    def filtrar_por_fecha(self, fecha: date):
        return db.session.query(Egresos).filter(func.date(Egresos.fecha) == fecha).all()
        # func.date() obtiene solo la parte de la fecha, ignorando la hora
    
    def total_gastos(self):
        return db.session.query(func.sum(Egresos.monto)).scalar()