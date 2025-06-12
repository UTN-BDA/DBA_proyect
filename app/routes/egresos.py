from flask import Blueprint, request, jsonify
from app.services import EgresosServicio
from app.schemas import egreso_schema, egresos_schema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from datetime import date

egresos = Blueprint('egresos', __name__, url_prefix='/api/egresos')
egresos_servicio = EgresosServicio()

@egresos.route('/retirar_saldo', methods=['POST'])
def retirar_saldo():
    try:
        egreso = egreso_schema.load(request.get_json())
        resp = egreso_schema.dump(egresos_servicio.retirar_saldo(egreso)), 201
    except Exception as excepcion:
        if isinstance(excepcion, ValidationError):
            resp = jsonify(excepcion.messages), 422
        elif isinstance(excepcion, IntegrityError):
            resp = jsonify('No existe categoria ingresada'), 422
        elif isinstance(excepcion, ValueError):
            resp = jsonify('Saldo insuficiente'), 422
        else:
            resp = jsonify('Error inesperado'), 500
    
    return resp

@egresos.route('/obtener/<id>', methods=['GET'])
def obtener(id):
    return egreso_schema.dump(egresos_servicio.buscar_por_id(id))

@egresos.route('/gastos-por-fecha/<fecha>', methods=['GET'])
def gastos_por_fecha(fecha):
    try:
        fecha_filtro = date.fromisoformat(fecha)
        gastos = egresos_servicio.filtrar_por_fecha(fecha_filtro)
        return egresos_schema.dump(gastos)
    except ValueError:
        return jsonify('Formato de fecha incorrecto. Debe ser AAAA-MM-DD')