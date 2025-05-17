from faker import Faker
import random

fake = Faker()

categorias_ingresos = ['Salario', 'Bonus', 'Inversión', 'Ingreso Ectra']
categorias_egresos = ['Alimentación', 'Transporte', 'Entretenimiento', 'Educación', 'Salud']

def generar_categorias_realistas(tipo='ingreso', cantidad=3):
    categorias = []
    if tipo == 'ingreso':
        lista = categorias_ingresos
    else:
        lista = categorias_egresos
    
    for _ in range(cantidad):
        nombre = random.choice(lista)
        descripcion = fake.sentence(nb_words=8)
        categorias.append({
            'nombre': nombre,
            'descripcion': descripcion
        })
    return categorias

