from django.contrib import admin

# Register your models here.
from apps.vianda.models import Vianda, Tipo_plato

admin.site.register(Tipo_plato)
admin.site.register(Vianda)