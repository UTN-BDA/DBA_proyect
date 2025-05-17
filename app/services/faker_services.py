from faker import Faker
import random

fake = Faker()

def faker_service(cantidad, x1, x2):
    resultados = []
    for _ in range(cantidad):
        monto = fake.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=1000, max_value=10000)
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

