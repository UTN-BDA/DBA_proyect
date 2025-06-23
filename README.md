# DBA_proyect

## Base de datos para control de gastos mensuales.

El proyecto consite en desarrollar una base de datos para gestionar el control de los gastos mensuales, en lo que se incluyen ingresos y egresos mensuales, segmentados en distintos tipos de gastos. Para ello se armará un pequeño backend, para controlar la lógica del proyecto y correcta gestión de los datos. Para la comunicación con la base de datos se utilizará el ORM SQLAlchemy, para la lógica de la aplicación se utilizará Python y para la base de datos se utilizará PostgreSQL.

### Características principales

- Registro de ingresos mensuales (sueldo, ingresos extras).
- Resgistro de gastos (alquiler, impuestos o servicios, supermercado, etc.)
- Etiquetado de gastos (hogar, salud, entretenimiento, etc)

### Pre requisitos

- Python 3.11 o superior
- Docker
- Postgres (contenedor o local)
- Configurar archivo .env con las credenciales para la conexión con la base de datos EN EL DIRECTORIO RAIZ
- Recomendado:\
  Instalar entorno virtual (python -m venv .venv)\
  Activar entorno virtual (cd ./venv/Scripts >> ./activate)

### Primera ejecución

En la carpeta raíz, ejecutar el script `initial_script.sh`
Para visualizar los resultados, abra el link proporcionado por la consola en su navegador (Ejemplo: Running on http://127.0.0.1:5000)

### Para ejecuciones posteriores

En la carpeta raíz, ejecutar `python app.py` y luego abra el link proporcionado por la consola

### Integrantes

- DONOZO, Cristian
- GELDES, Matias
- GUEVARA, Pamela
- TABOADA, Lautaro
