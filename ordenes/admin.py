from django.contrib import admin
from .models import Cliente, Vehiculo, Mecanico, OrdenServicio

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'telefono')
    search_fields = ('cedula', 'nombre')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cliente')
    search_fields = ('placa',)

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'activo')

@admin.register(OrdenServicio)
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'cliente', 'vehiculo', 'mecanico', 'estado', 'fecha_ingreso')
    search_fields = ('numero_orden', 'vehiculo__placa', 'cliente__nombre')
    list_filter = ('estado',)
    readonly_fields = ('numero_orden', 'fecha_ingreso', 'fecha_actualizacion')
