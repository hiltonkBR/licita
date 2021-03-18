from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Alerta)
admin.site.register(Comentario)
admin.site.register(Licitacao)
admin.site.register(Documento)
admin.site.register(Recolhimento)
admin.site.register(Publicacao)