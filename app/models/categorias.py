from app import db

class Categorias(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column('id_categoria', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(255), nullable=False)
    descripcion = db.Column('descripcion', db.String(255), nullable=False)
    
    # Relación one-to-many: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many
    # Una categoria - muchos ingresos
    ingresos_cat = db.relationship("Ingresos", back_populates="categs", cascade="all, delete-orphan")

    # Relación one-to-many: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-many
    # Una categoria - muchos egresos
    egresos_cat = db.relationship("Egresos", back_populates="categs", cascade="all, delete-orphan")