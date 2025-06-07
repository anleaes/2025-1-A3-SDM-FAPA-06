from django.shortcuts import render
from .models import Cliente
from rest_framework import viewsets
from .serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['firt_name', 'address', 'cell_phone', 'email']
    