import unittest
from app.services.ingresos import IngresosServicios
from app.services.faker_services import faker_service
from app import create_app, db
from app.models import Ingresos

class CategoriaTestCase(unittest.TestCase):
    service = IngresosServicios()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        
    def test_agregar_varios_ingresos(self):
        # En el faker services, ( recibe como argumento la catidad de ingresos, el id de categoria que serian para
        # ingresos en este caso yo considere del 1 al 5, pero es en el orden que primeo inice el test para categoria)
        ingresos_data = faker_service(cantidad = 1000, x1 = 1, x2 = 5)

        for data in ingresos_data:
            ingreso = self.service.agregar_saldo(**data)
            self.assertEqual(ingreso.monto, data['monto'])
            self.assertEqual(ingreso.detalle, data['detalle'])
            self.assertEqual(ingreso.categoria_id, data['categoria_id'])
            self.assertIsNotNone(ingreso.fecha)

        total_ingresos = db.session.query(Ingresos).count()
        # verfica la cantidad en la base de datos, tiene que ser acorde al numero de
        # ingresos que genere 
        self.assertEqual(total_ingresos, 1000)