from app import db
from app.models import Categorias
from sqlalchemy.exc import IntegrityError, NoResultFound

class CategoriasRepositorio:
    def agregar_categoria(self, categoria: c) -> Categorias:
        try:
            db.session.add(categoria) 
            db.session.commit()
            return categoria
        except IntegrityError as e:
            db.session.rollback()
            raise e

    def eliminar_categoria(self, categoria: Categorias) -> None:
        try:
            db.session.delete(categoria)
            db.session.commit()
        except NoResultFound as e:
            db.session.rollback()
            raise e

    def modificar_categoria(self, categoria: Categorias) -> Categorias:
        try:
            db.session.add(categoria) 
            db.session.commit()
            return categoria
        except IntegrityError as e:
            db.session.rollback()
            raise e

    def listar_categorias(self) -> list[Categorias]:
        return db.session.query(Categorias).all()
    
    def buscar_por_id(self, id: int) -> Categorias:
        try:
            return db.session.query(Categorias).filter_by(id_categoria = id).one()
        except NoResultFound as e:
            raise e
