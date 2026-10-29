"""Comprobación de datos para documentación y cierre de evidencia."""
from django.core.management.base import BaseCommand, CommandError
from ordenes.models import Cliente, Vehiculo, Mecanico, OrdenServicio

class Command(BaseCommand):
    help = 'Comprueba los conteos y los registros del módulo TallerExpress.'

    def handle(self, *args, **options):
        counts = {
            'cliente': Cliente.objects.count(),
            'vehiculo': Vehiculo.objects.count(),
            'mecanico': Mecanico.objects.count(),
            'orden_servicio': OrdenServicio.objects.count(),
        }
        for table, count in counts.items():
            self.stdout.write(f'{table}: {count}')
        self.stdout.write(f'Última orden: {OrdenServicio.objects.order_by("-id").values_list("numero_orden", flat=True).first() or "(ninguna)"}')
        if counts['orden_servicio'] < 100:
            raise CommandError('No están cargadas las 100 órdenes de demostración.')
        self.stdout.write(self.style.SUCCESS('Verificación finalizada.'))
