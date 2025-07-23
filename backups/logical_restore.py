import os
import sys
from get_db_credentials import get_db_credentrials

if __name__ == '__main__':
    db_credentials = get_db_credentrials()
    host, port, db_name = db_credentials['host'], db_credentials['port'], db_credentials['db_name']
    user = db_credentials['user']
    # Obtenemos todos los nombres de archivos de backup y nos quedamos con el mas reciente
    file_names = os.listdir('./backups')
    file_dump_names = list(filter(lambda name: name[:5] == 'dump_' and name[-4:] == '.sql', file_names))
    if len(file_dump_names) == 0:
        print('WARNING: No existen dumps lógicos para restablecer la base de datos.')
        sys.exit()
    last_file_dump = max(file_dump_names)

    # Ejecutar comando para restablecer base de datos
    comando = f"psql -h {host} -p {port} -U {user} -d {db_name} < ./backups/{last_file_dump}"
    status_code = os.system(comando)