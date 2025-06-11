from app import ma
from app.models import Egresos
from marshmallow import fields, Schema, post_load, validate
from datetime import datetime

class EgresosSchema(Schema):
    id: int = fields.Integer()
    monto: float = fields.Float(required=True, validate=validate.Range(min=0, min_inclusive=False, error='Monto inválido'))
    fecha: datetime = fields.DateTime(load_default=datetime.today())
    detalle: str = fields.String()
    categoria_id: int = fields.Integer(required=True)

    @post_load
    def deserializar_egreso(self, data, **kwargs):
        return Egresos(**data)

egreso_schema = EgresosSchema()
egresos_schema = EgresosSchema(many=True)