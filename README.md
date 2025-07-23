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
- Postgres (contenedor o preferentemente en local)
- Configurar archivo .env con las credenciales para la conexión con la base de datos EN EL DIRECTORIO RAIZ. A modo de ejemplo, debería verse asi:\
  `DEV_DATABASE_URI='postgresql+psycopg2://postgres:contrasena_postgres@localhost:5432/nombre_db'`\
  `PROD_DATABASE_URI='postgresql+psycopg2://postgres:contrasena_postgres@localhost:5432/nombre_db'`\
  `TEST_DATABASE_URI='postgresql+psycopg2://postgres:contrasena_postgres@localhost:5432/nombre_db'`\
- Recomendado:\
  Instalar entorno virtual\
  Activar entorno virtual

### Primera ejecución

En la carpeta raíz, ejecutar el script `sh ./initial_script.sh`
Para visualizar los resultados, abra el link proporcionado por la consola en su navegador (Ejemplo: Running on http://127.0.0.1:5000)

### Para ejecuciones posteriores

En la carpeta raíz, ejecutar `python app.py` y luego abra el link proporcionado por la consola

### Backup y Restore Lógicos

Previamente, se requiere 
- Tener instalado postgres localmente (no necesariamente la BD también deba estarlo). 
- En el caso de Windows, agregar al PATH la ruta donde se encuentran los comandos de postgres, típicamente en C:\Program Files\PostgreSQL\version\bin
- Tener variable de entorno: `DEV_DATABSE_URI`, con el formato descripto anteriormente.

#### Backup

Desde la ruta raíz del proyecto, ejecutar el comando:
`python .\backups\logical_backup.py`. Pedirá ingresar password del usuario que se use para la conexión.

#### Restore

La restauración se hace para una base de datos que esté recientemente creada, la cual no deba contener ninguna tabla

Desde la ruta raíz del proyecto, ejecutar el comando:
`python .\backups\logical_restore.py`. Pedirá ingresar password del usuario que se use para la conexión.


### Integrantes

- DONOZO, Cristian
- GELDES, Matias
- GUEVARA, Pamela
- TABOADA, Lautaro
