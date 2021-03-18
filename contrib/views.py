from .models import MeioEnvio, Tecnologia, Tipo  
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MeioEnvioSerializer, TecnologiaSerializer, TipoSerializer


# Create your views here.
class MeioEnvioViewSet(viewsets.ModelViewSet):
    """
    Meio de envio: responsável pela descrição dos meios de envio de alertas
    """
    queryset = MeioEnvio.objects.all().order_by('dataCriacao')
    serializer_class = MeioEnvioSerializer
    permission_classes = [permissions.IsAuthenticated]


class TecnologiaViewSet(viewsets.ModelViewSet):
    """
    Tecnologias: responsável pela descrição das tecnologias a serem utilizadas nas licitações
    """
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    permission_classes = [permissions.IsAuthenticated]

class TipoViewSet(viewsets.ModelViewSet):
    """
    Tipo: responsável pela descrição dos tipos de documentos
    """
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    permission_classes = [permissions.IsAuthenticated]