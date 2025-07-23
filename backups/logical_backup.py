import os
from datetime import datetime
from get_db_credentials import get_db_credentrials

if __name__ == '__main__':
    db_credentials = get_db_credentrials()
    host, port, db_name = db_credentials['host'], db_credentials['port'], db_credentials['db_name']
    user = db_credentials['user']

    # pg_dump -h host -p port -U user -d db_name -f archivo_timestamp.sql -v 
    fecha = datetime.today().strftime('%d%m%Y%H%M%S')
    comando = f"pg_dump -h {host} -p {port} -U {user} -d {db_name} > ./backups/dump_{fecha}.sql"
    os.system(comando)

