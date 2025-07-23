from app.services import CategoriaServicios
from app.schemas import categoria_schema, categorias_schema
from flask import Blueprint, request, jsonify

categorias = Blueprint('categorias',__name__,url_prefix='/api/categorias')
servicios = CategoriaServicios()

@categorias.route('/agregar', methods=['POST'])
def agregar_categoria():
    cat = categoria_schema.load(request.json)
    return categoria_schema.dump(servicios.agregar_categoria(cat))
    

@categorias.route('/modificar/<int:id>', methods=['PUT'])
def modificar_categoria(id:int):
    cat = categoria_schema.load(request.json)
    return categoria_schema.dump(servicios.modificar_categoria(cat,id)) 
    

@categorias.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_categoria(id: int):
    servicios.eliminar_categoria(id)
    return jsonify(f'Categoria {id} eliminada')


@categorias.route('/listar_categorias', methods = ['GET'])
def listar_categorias():
    return categorias_schema.dump(servicios.listar_categorias())