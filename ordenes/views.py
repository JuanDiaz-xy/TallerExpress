"""Vistas del módulo de órdenes: paginación y CRUD completo."""
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from .forms import OrdenServicioForm
from .models import OrdenServicio, Vehiculo


def lista_ordenes(request):
    qs = OrdenServicio.objects.select_related('cliente', 'vehiculo', 'mecanico').order_by(
        '-fecha_actualizacion', '-pk'
    )
    paginator = Paginator(qs, 10)
    ordenes = paginator.get_page(request.GET.get('page'))
    paginas = paginator.get_elided_page_range(number=ordenes.number, on_each_side=1, on_ends=1)
    return render(request, 'ordenes/lista.html', {
        'ordenes': ordenes,
        'paginas': paginas,
    })


def crear_orden(request):
    if request.method == 'POST':
        form = OrdenServicioForm(request.POST)
        if form.is_valid():
            orden = form.save()
            messages.success(request, f'La orden {orden.numero_orden} se creó correctamente.')
            return redirect('ordenes:lista')
    else:
        form = OrdenServicioForm()
    return render(request, 'ordenes/formulario.html', {
        'form': form,
        'titulo': 'Nueva orden',
        'modo': 'crear',
    })


def editar_orden(request, pk):
    orden = get_object_or_404(OrdenServicio, pk=pk)
    if request.method == 'POST':
        form = OrdenServicioForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save()
            messages.success(request, f'La orden {orden.numero_orden} se actualizó correctamente.')
            return redirect('ordenes:lista')
    else:
        form = OrdenServicioForm(instance=orden)
    return render(request, 'ordenes/formulario.html', {
        'form': form,
        'titulo': f'Editar orden {orden.numero_orden}',
        'modo': 'editar',
    })


def eliminar_orden(request, pk):
    orden = get_object_or_404(OrdenServicio, pk=pk)
    if request.method == 'POST':
        numero = orden.numero_orden
        orden.delete()
        messages.success(request, f'La orden {numero} fue eliminada correctamente.')
        return redirect('ordenes:lista')
    # GET solo presenta confirmación; no elimina información.
    return render(request, 'ordenes/confirmar_eliminacion.html', {'orden': orden})


@require_GET
def vehiculos_cliente(request):
    """Devuelve únicamente vehículos del cliente seleccionado en el formulario."""
    cliente = request.GET.get('cliente', '')
    if not cliente.isdecimal() or int(cliente) <= 0:
        return JsonResponse({'vehiculos': []})
    vehiculos = Vehiculo.objects.filter(cliente_id=int(cliente)).order_by('placa').values(
        'id', 'placa', 'marca', 'modelo'
    )
    return JsonResponse({'vehiculos': list(vehiculos)})
