from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ClienteSerializer
from .models import Cliente

# Create your views here.

class ClienteView(viewsets.ModelViewSet):
    """
    Clientes: responsável pelos clientes
    """

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticated]

    def get_paginated_response(self, data):
       return Response(data)

