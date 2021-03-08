from django.shortcuts import render
from rest_framework import viewsets
from .serializers import licitaSerializer
from .models import Licitacoes

# Create your views here.

class licitaView(viewsets.ModelViewSet):
    serializer_class = licitaSerializer
    queryset = Licitacoes.objects.all()
