from app import db
from sqlalchemy.sql import func

class Ingresos(db.Model):
    __tablename__ = 'Ingresos'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column('monto', db.Float, nullable=False)
    fecha = db.Column('fecha', db.Datetime(timezone=True), default=func.now(), nullable=False)
    detalle = db.Column('detalle', db.String(255))
    
    # Relación many-to-one: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many
    # muchos ingresos - una categoria
    categoria_id = db.Column('categoria_id', db.ForeignKey('categorias.id_categoria'), nullable=False)
    categs = db.relationship('Categorias', back_populates='ingresos_cat')
   