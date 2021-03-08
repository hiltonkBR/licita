from rest_framework import serializers
from .models import Licitacoes

class licitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacoes
        fields = ('id', 'orgao', 'tecnologia', 'valor')

