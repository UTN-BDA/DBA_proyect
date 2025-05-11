from app import db

class Ingresos(db.Model):
    __tablename__ = 'Ingresos'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column('monto', db.Float, nullable=False)
    fecha = db.Column('fecha', db.Datetime, nullable=False)
    detalle = db.Column('detalle', db.String)
   # categoria_id = db.Column('categoria_id') #hasta no estar la categoría no se puede entablar la relación
   