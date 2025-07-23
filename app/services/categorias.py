from app.models import Categorias
from app.repositories import CategoriasRepositorio

class CategoriaServicios:

    repository = CategoriasRepositorio()

    def agregar_categoria(self, attr: dict) -> Categorias:
        categoria = Categorias()
        for key, value in attr.items():
            setattr(categoria, key, value) if hasattr (categoria, key) else print("Atributo desconocido")
        return self.repository.agregar_categoria(categoria)
    
    def buscar_por_id(self, id_cat: int) -> Categorias:
        return self.repository.buscar_por_id(id_cat)

    def eliminar_categoria(self, id_cat: int) -> None:
        categoria = self.buscar_por_id(id_cat)
        return self.repository.eliminar_categoria(categoria)

    def modificar_categoria(self, attr: dict, id_cat: int) -> Categorias:
        cat = self.repository.buscar_por_id(id_cat)

        if isinstance(cat, Categorias):
            for key, value in attr.items():
                setattr(cat, key, value) if hasattr (cat, key) else print("Atributo desconocido")
            return self.repository.modificar_categoria(cat)
        else:
            raise KeyError

    def listar_categorias(self) -> list[Categorias]:
        return self.repository.listar_categorias()