from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nomeCliente', 'CPNJ', 'cidade', 'estado', 'pais', 'nomeContato', 'telefoneContato', 'observacao')

# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
