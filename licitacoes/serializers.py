from .models import *
from rest_framework import serializers

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = ('id', 'descricao', 'licitacaoId', 'destinatario', 'meioEnvioId', 'dataCriacao')

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'autor', 'comentario', 'criticidade', 'documento', 'licitacaoId', 'dataCriacao')

class LicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacao
        fields = ('id', 'clienteID', 'pregao', 'uasg', 'objeto', 'valorEstimado', 'tecnologiaId', 'dataCriacao', 'observacoes', 'statusLicitacao', 'statusInterjato')

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('id', 'comentario', 'tipoId', 'documento', 'dataPublicacao', 'licitacaoId')

class RecolhimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolhimento
        fields = ('id', 'dataRecolhimento', 'licitacaoId')

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ('id', 'dataPublicacao', 'dataCriacao', 'dataQuestionamento', 'dataImpugnacao','licitacaoId')
