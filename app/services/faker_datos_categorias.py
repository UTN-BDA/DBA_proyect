from faker import Faker
import random

fake = Faker()

categorias_ingresos = ['Salario', 'Bonus', 'Inversión', 'Ingreso Extra']
categorias_egresos = ['Alimentación', 'Transporte', 'Entretenimiento', 'Educación', 'Salud', 'Vestimenta', 'Otros']

def generar_categorias_realistas(tipo, cantidad=5):
    categorias = []
    if tipo == 'ingreso':
        lista = categorias_ingresos
    else:
        lista = categorias_egresos
    
    # Verificar que la cantidad no exceda la cantidad de elementos en la lista
    cantidad = min(cantidad, len(lista))
    seleccionadas = random.sample(lista, cantidad)
    for nombre in seleccionadas:
        descripcion = fake.sentence(nb_words=8)
        categorias.append({
            'nombre': nombre,
            'descripcion': descripcion
        })
    return categorias