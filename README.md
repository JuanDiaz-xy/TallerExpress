# TallerExpress — GA7-220501096-AA2-EV02

TallerExpress es una aplicación académica para registrar y consultar órdenes de servicio de un taller. Permite crear, editar, listar y eliminar órdenes, relacionando cada vehículo con su cliente y asignando, cuando corresponde, un mecánico.

## Requisitos

- Python 3.10 o posterior.
- Dependencias instaladas desde `requirements.txt`.
- SQLite funciona como base de datos predeterminada y no requiere instalación adicional.
- MySQL con Laragon es opcional.

## Instalación y ejecución normal

Todos los comandos se ejecutan desde la carpeta raíz del proyecto, donde se encuentra `manage.py`.

### Windows PowerShell

```powershell
py -3 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_tallerexpress
python manage.py runserver
```

### Windows CMD

```bat
py -3 -m venv .venv
.venv\\Scripts\\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_tallerexpress
python manage.py runserver
```

Abre <http://127.0.0.1:8000/ordenes/> en el navegador.

La carga de datos de ejemplo es opcional. Para iniciar una base vacía, omite `python manage.py seed_tallerexpress`.

## Uso opcional de MySQL/Laragon

1. Copia `.env.example` como `.env`.
2. Cambia `DB_ENGINE=sqlite` por `DB_ENGINE=mysql`.
3. Revisa nombre, usuario, contraseña y puerto de MySQL.
4. Inicia MySQL desde Laragon.
5. Ejecuta las migraciones y, si se requieren, la carga de datos de ejemplo.

La configuración se realiza en `.env`; no es necesario modificar `tallerexpress/settings.py`.

## Pruebas

Con el entorno virtual activo:

```text
python manage.py check
python manage.py test ordenes
```

Las pruebas comprueban creación, edición, eliminación, paginación y validación de la relación entre clientes y vehículos.

Para la entrega, registra los resultados y evidencias directamente en el informe PDF solicitado.

## Estructura principal

```text
.
├── manage.py
├── requirements.txt
├── .env.example
├── tallerexpress/       # configuración Django
├── ordenes/             # modelos, vistas, formularios y plantillas
├── documentacion/       # informe PDF de la evidencia
└── sql/                 # datos SQL de referencia
```

## Alcance y limitaciones

- La aplicación gestiona las órdenes y sus relaciones principales.
- La notificación automática al cliente no está implementada; corresponde al caso CP-07 y queda fuera del alcance actual.
- El consecutivo de órdenes está diseñado para el ejercicio académico y no contempla creación simultánea por múltiples usuarios.
- Para producción se debe configurar una clave segura, `DEBUG=0` y un servidor adecuado.

## Entrega

1. Verifica que el informe PDF de `documentacion/` contenga los datos reales y las evidencias solicitadas.
2. Ejecuta las pruebas automatizadas y los casos manuales antes de entregar.
3. Genera el ZIP únicamente cuando la documentación y el código estén verificados.
