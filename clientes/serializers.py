from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
        class Meta:
                    model = Cliente
                    fields = ('id', 'nomeCliente', 'CPNJ', 'cidade', 'estado', 'pais', 'nomeContato', 'telefoneContato', 'observacao')
