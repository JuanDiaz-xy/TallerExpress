# TallerExpress

Sistema web para gestionar órdenes de servicio de un taller mecánico.

Desarrollado con Python, Django y MySQL.

## Funcionalidades

- Consultar órdenes de servicio.
- Crear nuevas órdenes.
- Editar órdenes existentes.
- Eliminar órdenes con confirmación.
- Validar formularios y relaciones cliente-vehículo.
- Consultar registros con paginación.

## Requisitos

- Windows
- Python 3.10 o superior
- Git Bash
- Laragon con MySQL 8
- Conexión a Internet para instalar dependencias

## Instalación en otro computador

1. Descargar o clonar el repositorio.
2. Abrir Git Bash en la carpeta del proyecto.
3. Crear y activar el entorno virtual:

    python -m venv .venv
    source .venv/Scripts/activate

4. Instalar dependencias:

    python -m pip install -r requirements.txt

5. Crear el archivo de configuración:

    cp .env.example .env

6. Iniciar MySQL desde Laragon (Start All).

7. Configurar .env según la instalación local:

    DB_NAME=tallerexpress
    DB_USER=root
    DB_PASSWORD=
    DB_HOST=127.0.0.1
    DB_PORT=3306

8. Crear la base de datos:

    python scripts/crear_base_mysql.py

9. Aplicar migraciones:

    python manage.py migrate

10. Cargar datos iniciales (solo en una base vacía):

    python manage.py seed_tallerexpress

11. Iniciar el servidor:

    python manage.py runserver

## Acceso

http://127.0.0.1:8000/ordenes/

## Ejecutar pruebas

    python manage.py check

    TALLEREXPRESS_TEST_SQLITE=1 python manage.py test ordenes

## Consideraciones

- La base de datos MySQL debe estar iniciada.
- No ejecutar nuevamente la carga inicial si existen registros.
- El archivo .env contiene configuración local y no debe publicarse.
- El entorno virtual .venv no se incluye en Git.
- La aplicación está preparada para uso académico local, no para producción.
