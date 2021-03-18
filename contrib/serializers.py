from .models import MeioEnvio, Tecnologia, Tipo
from rest_framework import serializers

class MeioEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeioEnvio
        fields = ['id', 'descricao']

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['id', 'descricao']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'descricao']
