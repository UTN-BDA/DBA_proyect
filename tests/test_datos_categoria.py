import unittest
from app.services.categorias import CategoriaServicios
from app.services.faker_datos_categorias import generar_categorias_realistas
from app import create_app, db

class CategoriaTestCase(unittest.TestCase):
    service = CategoriaServicios()

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        self.app_context.pop()

    # Agrega categorías del tipo "Egreso"
    def test_agregar_varias_categorias_egreso(self):
        # Se le tiene que pasar el tipo si es de ingreso o egreso y la cantidad de 
        # de categorias.
        categorias_data = generar_categorias_realistas(tipo='egreso', cantidad=6)
        
        for categoria_data in categorias_data:
            categoria = self.service.agregar_categoria(categoria_data)
            # Verifica atributos del objeto
            for key in categoria_data:
                self.assertEqual(categoria_data[key], getattr(categoria, key))

    # Agrega categorías del tipo "Ingreso"
    def test_agregar_varias_categorias_ingreso(self):
        # Se le tiene que pasar el tipo si es de ingreso o egreso y la cantidad de 
        # de categorias.
        categorias_data = generar_categorias_realistas(tipo='ingreso', cantidad=4)
        
        for categoria_data in categorias_data:
            categoria = self.service.agregar_categoria(categoria_data)
            # Verifica atributos del objeto
            for key in categoria_data:
                self.assertEqual(categoria_data[key], getattr(categoria, key))
