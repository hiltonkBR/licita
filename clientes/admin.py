from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nomeCliente', 'CPNJ', 'uasg', 'cidade', 'estado', 'pais', 'observacao')

# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
