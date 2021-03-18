from django.contrib import admin
from .models import MeioEnvio, Tipo, Tecnologia

# Register your models here.
admin.site.register(MeioEnvio)
admin.site.register(Tecnologia)
admin.site.register(Tipo)