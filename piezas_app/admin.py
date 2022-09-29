from django.contrib import admin
from .models import Moneda, Modelo, Marca, TipoPieza, Estado, Pieza, Location, Taller, Inventario
# Register your models here.

admin.site.register(Moneda)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(TipoPieza)
admin.site.register(Estado)
admin.site.register(Pieza)
admin.site.register(Location)
admin.site.register(Taller)
admin.site.register(Inventario)