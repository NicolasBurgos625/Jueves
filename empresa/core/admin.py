from django.contrib import admin
from .models import Trabajador, Paquete

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'rol')
    search_fields = ('nombre', 'apellido', 'rut')
    list_filter = ('rol',)

admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Paquete)
