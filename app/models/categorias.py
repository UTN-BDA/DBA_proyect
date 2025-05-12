from app import db

class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column('id_categoria', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(255), nullable=False)
    descripcion = db.Column('descripcion', db.String(255), nullable=False)