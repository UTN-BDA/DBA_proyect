from app import db
from datetime import datetime

class Egresos(db.Model):
    __tablename__ = 'egresos'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column('monto', db.Float, nullable=False)
    fecha = db.Column('fecha', db.DateTime, nullable=False, default=datetime.today())
    detalle = db.Column('detalle', db.String(255))

    categoria_id = db.Column('categoria_id', db.Integer, db.ForeignKey('categorias.id_categoria'), nullable=False)
    categs = db.relationship('Categorias', back_populates='egresos_cat')