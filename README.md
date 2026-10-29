# TallerExpress - GA7-220501096-AA2-EV02

Aplicación web desarrollada en Django para gestionar órdenes de servicio de un taller mecánico. Permite registrar, consultar, editar y eliminar órdenes, relacionando clientes, vehículos y mecánicos.

Repositorio: <https://github.com/JuanDiaz-xy/TallerExpress>

## Funcionalidades

- Registro y consulta de órdenes de servicio.
- Edición del problema, mecánico asignado y estado de la orden.
- Eliminación mediante `POST`, protección CSRF y confirmación previa.
- Validación de la relación entre cliente y vehículo.
- Estados controlados para el seguimiento de cada orden.
- Listado paginado con 10 registros por página.
- Interfaz web responsiva basada en Bootstrap y color rojo.
- Carga opcional de 8 mecánicos, 20 clientes, 30 vehículos y 100 órdenes de ejemplo.
- Nueve pruebas automatizadas.

## Requisitos

- Python 3.10 o posterior.
- Conexión a Internet durante la instalación de dependencias.
- SQLite, incluido con Python, para la ejecución predeterminada.
- MySQL/Laragon únicamente si se desea utilizar ese motor de base de datos.

## Instalación

Clona el repositorio y entra en su carpeta:

```text
git clone https://github.com/JuanDiaz-xy/TallerExpress.git
cd TallerExpress
```

### PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_tallerexpress
python manage.py runserver
```

### Símbolo del sistema (CMD)

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_tallerexpress
python manage.py runserver
```

Abre <http://127.0.0.1:8000/ordenes/>.

`seed_tallerexpress` carga los datos de demostración y solo debe ejecutarse sobre una base vacía. Para trabajar sin datos iniciales, omite ese comando.

## Configuración de la base de datos

SQLite es la configuración predeterminada y no requiere un archivo `.env`.

Para utilizar MySQL:

1. Copia `.env.example` con el nombre `.env`.
2. Cambia `DB_ENGINE=sqlite` por `DB_ENGINE=mysql`.
3. Completa los datos de conexión en `.env`.
4. Inicia MySQL.
5. Ejecuta `python manage.py migrate`.
6. Ejecuta `python manage.py seed_tallerexpress` si necesitas los datos de ejemplo.

El archivo `.env` contiene información local y está excluido del repositorio.

## Pruebas y verificación

Con el entorno virtual activo:

```text
python manage.py check
python manage.py test ordenes
```

Resultado esperado:

```text
Ran 9 tests
OK
```

Para comprobar los conteos después de cargar la semilla:

```text
python manage.py verificar_tallerexpress
```

## Estructura

```text
TallerExpress/
|-- manage.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
|-- README.md
|-- tallerexpress/           Configuración del proyecto Django
|-- ordenes/                 Aplicación, modelos, vistas, plantillas y pruebas
|-- sql/                     Datos SQL de referencia
`-- documentacion/
    |-- Informe_Evidencia_GA7-220501096-AA2-EV02.pdf
    `-- capturas/            Evidencias visuales CP-01 a CP-06
```

## Documentación

El informe final se encuentra en:

```text
documentacion/Informe_Evidencia_GA7-220501096-AA2-EV02.pdf
```

Las capturas de las pruebas manuales están en `documentacion/capturas/`.

## Archivos excluidos de la entrega

El repositorio y el ZIP final no incluyen:

- `.venv/`
- `.env`
- `db.sqlite3`
- `__pycache__/`
- archivos `.pyc`
- registros y archivos temporales

Estos elementos se generan localmente y no son necesarios para instalar el proyecto en otro equipo.

## Alcance

El proyecto corresponde al módulo académico de órdenes de servicio. No incluye facturación, cotizaciones comerciales ni notificaciones automáticas al cliente.
