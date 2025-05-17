import unittest
from app.services.egresos import EgresosServicio
from app.services.faker_services import faker_service
from app import create_app, db
from app.models import Egresos

class CategoriaTestCase(unittest.TestCase):
    service = EgresosServicio()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        
    def test_agregar_varios_egresos(self):
        #En el faker services, ( recibe como argumento la catidad de egresos, el id de categoria que serian para
        # egresos en este caso yo considere del 6 al 10, pero es en el orden que primeo inicie los test)
        egresos_data = faker_service(cantidad = 1000, x1=6, x2=10)

        for data in egresos_data:
            
            egreso_obj = Egresos(
                monto=data['monto'],
                fecha=data['fecha'],
                detalle=data['detalle'],
                categoria_id=data['categoria_id']
            )
            egreso = self.service.retirar_saldo(egreso_obj)
            self.assertEqual(egreso.monto, data['monto'])
            self.assertEqual(egreso.detalle, data['detalle'])
            self.assertEqual(egreso.categoria_id, data['categoria_id'])
            self.assertIsNotNone(egreso.fecha)

        total_egresos = db.session.query(Egresos).count()
        # verfica la cantidad en la base de datos, tiene que ser acorde al numero de
        # egresos que genere 
        self.assertEqual(total_egresos, 1000)