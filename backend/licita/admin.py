from django.contrib import admin
from .models import Licitacoes

# Register your models here.

class licitaAdmin(admin.ModelAdmin):
    list_display = ('orgao', 'tecnologia', 'valor')

admin.site.register(Licitacoes, licitaAdmin)
