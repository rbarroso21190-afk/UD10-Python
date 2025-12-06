from django.contrib import admin
from .models import Mensaje

# Configuración visual para el panel
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido', 'fecha') # Qué columnas ver
    list_filter = ('fecha',)                         # Filtro lateral por fecha
    search_fields = ('usuario', 'contenido')         # Barra de búsqueda

# Registramos el modelo
admin.site.register(Mensaje, MensajeAdmin)
