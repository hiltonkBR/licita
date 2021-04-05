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
        fields = ('id', 'clienteGerenciadorID', 'clienteBeneficiadoID', 'modalidadeLicitacao', 'tipoPregao', 'numLicitacao', 'registroPreco', 'objeto', 'valorEstimado', 'tecnologiaId', 'dataCriacao', 'observacoes', 'statusLicitacao', 'statusInterjato')

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

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields =('id', 'nome', 'funcao', 'telefone', 'email', 'licitacaoId')

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'tipoLink', 'link', 'licitacaoId')