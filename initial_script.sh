#!/bin/bash

# Script de configuración para proyecto Python/Flask
set -e  # Detener ejecución ante cualquier error

echo "1. Instalando dependencias..."
pip install -r requirements.txt

echo "2. Probando conexión a base de datos..."
python -m unittest tests/test_db.py

echo "3. Configurando base de datos..."
flask db init
flask db migrate -m "Primera migración"
flask db upgrade

echo "4. Poblando db con datos de prueba..."
python -m unittest tests/test_datos_categoria.py
python -m unittest tests/test_faker_ingresos.py
python -m unittest tests/test_faker_egresos.py

echo "12. Iniciando aplicación..."
python app.py