from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente

# Create your views here.

class ClienteView(viewsets.ModelViewSet):
    """
    Clientes: responsável pelos clientes
    """
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
