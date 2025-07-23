import os
import sys
from pathlib import Path
from dotenv import load_dotenv

basedir = os.path.abspath(Path(__file__).parents[1])
load_dotenv(os.path.join(basedir, '.env'))

def get_db_credentrials():
    url_db = os.environ.get('DEV_DATABASE_URI')
    if url_db is None:
        print('ERROR: Se requiere variable de entorno DEV_DATABASE_URI')
        sys.exit()
    
    # parsear la url para obtener: host, port, user, password, y db_name
    conection_info = url_db.split('/')[2].split('@')
    user, password = conection_info[0].split(':')
    host, port = conection_info[1].split(':')
    db_name = url_db.split('/')[3]
    return {
        'user': user,
        'host': host,
        'port': port,
        'db_name': db_name
    }
