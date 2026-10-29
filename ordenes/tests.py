from django.test import TestCase
from django.urls import reverse
from ordenes.forms import OrdenServicioForm
from ordenes.models import Cliente, Vehiculo, Mecanico, OrdenServicio

class DatosDePrueba(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cliente = Cliente.objects.create(cedula='1234567890', nombre='Laura Pruebas', telefono='3101234567')
        cls.otro_cliente = Cliente.objects.create(cedula='9876543210', nombre='Ana Ejemplo', telefono='3107654321')
        cls.vehiculo = Vehiculo.objects.create(placa='ABC123', marca='Toyota', modelo='Corolla', kilometraje=23000, cliente=cls.cliente)
        cls.otro_vehiculo = Vehiculo.objects.create(placa='DEF456', marca='Mazda', modelo='3', kilometraje=12000, cliente=cls.otro_cliente)
        cls.mecanico = Mecanico.objects.create(nombre='Pedro Mecanico', especialidad='Motor')

    def datos_formulario(self):
        return {
            'cliente': str(self.cliente.pk), 'vehiculo': str(self.vehiculo.pk),
            'mecanico': str(self.mecanico.pk), 'descripcion_problema': 'Problema de frenos',
            'estado': OrdenServicio.Estado.RECIBIDA,
        }

    def test_cp01_crear_orden_valida(self):
        response = self.client.post(reverse('ordenes:crear'), self.datos_formulario())
        self.assertRedirects(response, reverse('ordenes:lista'))
        self.assertEqual(OrdenServicio.objects.count(), 1)
        self.assertEqual(OrdenServicio.objects.first().numero_orden, 'OS-001')

    def test_cp02_crear_sin_cliente(self):
        data = self.datos_formulario()
        data.pop('cliente')
        response = self.client.post(reverse('ordenes:crear'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'obligatorio')
        self.assertEqual(OrdenServicio.objects.count(), 0)

    def test_cp03_rechaza_vehiculo_ajeno(self):
        data = self.datos_formulario()
        data['vehiculo'] = str(self.otro_vehiculo.pk)
        response = self.client.post(reverse('ordenes:crear'), data)
        self.assertContains(response, 'no pertenece al cliente seleccionado')
        self.assertEqual(OrdenServicio.objects.count(), 0)

    def test_cp04_listado_paginado_diez(self):
        for i in range(12):
            OrdenServicio.objects.create(cliente=self.cliente, vehiculo=self.vehiculo,
                descripcion_problema=f'Falla {i}')
        response = self.client.get(reverse('ordenes:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['ordenes']), 10)
        self.assertEqual(response.context['ordenes'].paginator.num_pages, 2)

    def test_cp05_editar_orden(self):
        orden = OrdenServicio.objects.create(cliente=self.cliente, vehiculo=self.vehiculo, descripcion_problema='Falla inicial')
        data = self.datos_formulario()
        data['estado'] = OrdenServicio.Estado.EN_EJECUCION
        response = self.client.post(reverse('ordenes:editar', args=[orden.pk]), data)
        self.assertRedirects(response, reverse('ordenes:lista'))
        orden.refresh_from_db()
        self.assertEqual(orden.estado, OrdenServicio.Estado.EN_EJECUCION)
        self.assertEqual(orden.numero_orden, 'OS-001')

    def test_cp06_eliminar_solo_post(self):
        orden = OrdenServicio.objects.create(cliente=self.cliente, vehiculo=self.vehiculo, descripcion_problema='Para eliminar')
        url = reverse('ordenes:eliminar', args=[orden.pk])
        self.client.get(url)
        self.assertTrue(OrdenServicio.objects.filter(pk=orden.pk).exists())
        self.client.post(url)
        self.assertFalse(OrdenServicio.objects.filter(pk=orden.pk).exists())

    def test_formulario_rechaza_estado_fuera_de_catalogo(self):
        data = self.datos_formulario()
        data['estado'] = 'INVALIDO'
        form = OrdenServicioForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('estado', form.errors)

    def test_vistas_get_y_not_found(self):
        self.assertEqual(self.client.get(reverse('ordenes:crear')).status_code, 200)
        self.assertEqual(self.client.get(reverse('ordenes:editar', args=[9999])).status_code, 404)

    def test_el_formulario_tiene_csrf(self):
        response = self.client.get(reverse('ordenes:crear'))
        self.assertContains(response, 'csrfmiddlewaretoken')
