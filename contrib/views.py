from .models import MeioEnvio, Tecnologia, Tipo  
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import MeioEnvioSerializer, TecnologiaSerializer, TipoSerializer


# Create your views here.
class MeioEnvioViewSet(viewsets.ModelViewSet):
    """
    Meio de envio: responsável pela descrição dos meios de envio de alertas
    """
    class Meta:
        ordering = ['-id']
    queryset = MeioEnvio.objects.all().order_by('dataCriacao')
    serializer_class = MeioEnvioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
       return Response(data)


class TecnologiaViewSet(viewsets.ModelViewSet):
    """
    Tecnologias: responsável pela descrição das tecnologias a serem utilizadas nas licitações
    """
    class Meta:
        ordering = ['-id']
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
       return Response(data)

class TipoViewSet(viewsets.ModelViewSet):
    """
    Tipo: responsável pela descrição dos tipos de documentos
    """
    queryset = Tipo.objects.all().order_by('id')
    serializer_class = TipoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
       return Response(data)