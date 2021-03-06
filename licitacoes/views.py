from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *

# Create your views here.
class AlertaViewSet(viewsets.ModelViewSet):
    """
    Alertas: responsável pela emissão de alertas em licitações
    """
    queryset = Alerta.objects.all().order_by('dataCriacao')
    serializer_class = AlertaSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)


class ComentarioViewSet(viewsets.ModelViewSet):
    """
    Comentários: responsável pela realização de comentários em licitações
    """
    queryset = Comentario.objects.all().order_by('id')
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)

class LicitacaoViewSet(viewsets.ModelViewSet):
    """
    Licitações: responsável pela descrição de licitações
    """
    queryset = Licitacao.objects.all().order_by('id')
    serializer_class = LicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
       return Response(data)

class DocumentoViewSet(viewsets.ModelViewSet):
    """
    Documentos: responsável pela vinculação de documentos à licitação
    """
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)

class RecolhimentoViewSet(viewsets.ModelViewSet):
    """
    Recolhimento: responsável pelo recolhimento de licitações
    """
    queryset = Recolhimento.objects.all().order_by('id')
    serializer_class = RecolhimentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)

class PublicacaoViewSet(viewsets.ModelViewSet):
    """
    Publicação: responsável pela publicação de licitações
    """
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)

class ContatoViewSet(viewsets.ModelViewSet):
    """
    Contato: responsável pelos contatos da licitações
    """
    queryset = Contato.objects.all().order_by('id')
    serializer_class = ContatoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)

class LinkViewSet(viewsets.ModelViewSet):
    """
    Contato: responsável pelos links da licitações
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_paginated_response(self, data):
       return Response(data)