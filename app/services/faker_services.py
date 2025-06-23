from faker import Faker
import random

fake = Faker()

def faker_service(cantidad=1000, x1=0, x2=0):
    resultados = []
    for _ in range(cantidad):
        monto = fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=500, max_value=1000)
        fecha = fake.date_between(start_date='-5m', end_date='today')
        detalle = fake.sentence(nb_words=6)
        categoria_id = random.randint(x1, x2)
        resultados.append({
            'monto': monto,
            'fecha': fecha,
            'detalle': detalle,
            'categoria_id': categoria_id
        })
        
    return resultados

