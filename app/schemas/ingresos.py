from app import ma

class IngresosSchema(ma.Schema):
    class Meta:
        fields=('id','monto','fecha','detalle','categoria_id')

ingreso_schema = IngresosSchema()
ingresos_schema = IngresosSchema(many=True)