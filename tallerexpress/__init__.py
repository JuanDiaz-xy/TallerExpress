"""Se prefiere mysqlclient; se usa PyMySQL cuando no está disponible en Windows."""
try:
    import MySQLdb  # noqa: F401
except ImportError:
    import pymysql
    # El backend MySQL de Django comprueba la versión API de MySQLdb.
    # PyMySQL es compatible, pero informa su versión propia antigua de compatibilidad.
    pymysql.version_info = (2, 2, 1, 'final', 0)
    pymysql.install_as_MySQLdb()
