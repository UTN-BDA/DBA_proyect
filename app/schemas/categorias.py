from app import ma

class CategoriasSchema:
    class Meta:
        fields = ('id_categoria', 'nombre', 'descripcion')

categoria_schema = CategoriasSchema()
categorias_schema = CategoriasSchema(many=True)