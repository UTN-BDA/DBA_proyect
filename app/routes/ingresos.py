from app.services import IngresosServicios
from app.schemas import ingreso_schema, ingresos_schema
from flask import Blueprint, request

ingresos = Blueprint('ingresos',__name__,url_prefix='/api/ingresos')
servicios = IngresosServicios()

@ingresos.route('/agregar', methods=['POST'])
def agregar_ingreso():
    ingre = ingreso_schema.load(request.json)
    return ingreso_schema.dump(servicios.agregar_saldo(ingre))
    

@ingresos.route('/consultar/<int:id>', methods=['GET'])
def consultar_egreso(id:int):
    return ingreso_schema.dump(servicios.consultar_ingresos(id)) 
    

@ingresos.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_ingreso(id: int):
    return servicios.eliminar_ingresos(id)


@ingresos.route('/listar_ingresos', methods = ['GET'])
def listar_categorias():
    return ingresos_schema.dump(servicios.listar_ingresos())