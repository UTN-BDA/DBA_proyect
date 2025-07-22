import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(Path(__file__).parents[1])
load_dotenv(os.path.join(basedir, '.env'))

if __name__ == '__main__':
    # Leer variables de entorno
    url_db = os.environ.get('DEV_DATABASE_URI')
    if url_db is None:
        print('ERROR: Se requiere variable de entorno DEV_DATABASE_URI')
        sys.exit()
    
    # parsear la url para obtener: host, port, user, password, y db_name
    conection_info = url_db.split('/')[2].split('@')
    user, password = conection_info[0].split(':')
    host, port = conection_info[1].split(':')
    db_name = url_db.split('/')[3]

    # pg_dump -h host -p port -U user -d db_name -f archivo_timestamp.sql -v 
    fecha = datetime.today().strftime('%d%m%Y%H%M%S')
    comando = f"pg_dump -h {host} -p {port} -U {user} -d {db_name} > ./backups/dump_{fecha}.sql"
    os.system(comando)

