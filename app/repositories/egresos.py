from app import db
from app.models import Egresos
from sqlalchemy.exc import IntegrityError

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
    