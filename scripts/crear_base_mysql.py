"""Crea la BD en MySQL de Laragon usando los datos de .env; no necesita CLI mysql."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import pymysql

load_dotenv(Path(__file__).resolve().parents[1] / '.env')
database = os.getenv('DB_NAME', 'tallerexpress')
if not database.replace('_', '').isalnum():
    sys.exit('DB_NAME solo admite letras, números y guion bajo.')
try:
    connection = pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        port=int(os.getenv('DB_PORT', '3306')),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        charset='utf8mb4', autocommit=True,
        connect_timeout=5,
    )
    with connection.cursor() as cursor:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS `{database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
    connection.close()
    print(f'BD `{database}` disponible en MySQL.')
except pymysql.MySQLError as exc:
    sys.exit('No se pudo conectar a MySQL. Inicia Laragon (Start All) y revisa DB_USER, DB_PASSWORD y DB_PORT en .env.\n' + str(exc))
