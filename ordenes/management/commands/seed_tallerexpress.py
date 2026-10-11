"""Carga el SQL oficial del Anexo A sobre una base recién migrada y vacía."""
from pathlib import Path
import sqlparse
from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from ordenes.models import Cliente, Vehiculo, Mecanico, OrdenServicio

class Command(BaseCommand):
    help = 'Carga 8 mecánicos, 20 clientes, 30 vehículos y 100 órdenes del Anexo A.'

    def handle(self, *args, **options):
        if any(model.objects.exists() for model in (Cliente, Vehiculo, Mecanico, OrdenServicio)):
            raise CommandError('La base ya tiene datos: para prevenir duplicados se cancela la semilla.')
        source = Path(__file__).resolve().parents[3] / 'sql' / 'seed_tallerexpress.sql'
        if not source.is_file():
            raise CommandError(f'SQL no encontrado: {source}')
        statements = sqlparse.split(source.read_text(encoding='utf-8'))
        with transaction.atomic():
            with connection.cursor() as cursor:
                for stmt in statements:
                    clean = sqlparse.format(stmt, strip_comments=True).strip()
                    if not clean or clean.upper().startswith(('START TRANSACTION', 'COMMIT')):
                        continue
                    cursor.execute(clean)
        totals = (Mecanico.objects.count(), Cliente.objects.count(), Vehiculo.objects.count(), OrdenServicio.objects.count())
        if totals != (8, 20, 30, 100):
            raise CommandError(f'Conteo de registros diferente al esperado: {totals}')
        self.stdout.write(self.style.SUCCESS('Datos cargados: 8 mecánicos, 20 clientes, 30 vehículos, 100 órdenes.'))
