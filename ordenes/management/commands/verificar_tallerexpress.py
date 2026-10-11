"""Resume datos de MySQL sin tratar las operaciones legítimas de CRUD como fallos."""
from django.core.management.base import BaseCommand, CommandError
from ordenes.models import Cliente, Vehiculo, Mecanico, OrdenServicio


class Command(BaseCommand):
    help = 'Muestra conteos actuales. --semilla-original verifica exactamente la carga inicial.'

    def add_arguments(self, parser):
        parser.add_argument('--semilla-original', action='store_true',
                            help='Exige los conteos originales antes de crear o eliminar órdenes.')

    def handle(self, *args, **options):
        counts = {
            'cliente': Cliente.objects.count(),
            'vehiculo': Vehiculo.objects.count(),
            'mecanico': Mecanico.objects.count(),
            'orden_servicio': OrdenServicio.objects.count(),
        }
        for tabla, cantidad in counts.items():
            self.stdout.write(f'{tabla}: {cantidad}')
        ultima = OrdenServicio.objects.order_by('-id').values_list('numero_orden', flat=True).first()
        self.stdout.write(f'Última orden por ID: {ultima or "(ninguna)"}')
        if options['semilla_original']:
            esperados = {'cliente': 20, 'vehiculo': 30, 'mecanico': 8, 'orden_servicio': 100}
            if counts != esperados:
                raise CommandError('Conteos diferentes de la semilla inicial. '
                                   'Si ya usaste el CRUD, ejecuta sin --semilla-original.')
            self.stdout.write(self.style.SUCCESS('Semilla inicial verificada.'))
        else:
            if not all(counts[tipo] > 0 for tipo in ('cliente', 'vehiculo', 'mecanico')):
                raise CommandError('Faltan datos maestros de clientes, vehículos o mecánicos.')
            self.stdout.write(self.style.SUCCESS('Consulta completada. '
                'El total de órdenes puede variar después de crear o eliminar registros.'))
