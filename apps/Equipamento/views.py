from django.shortcuts import render
from .models import Equipamento
from rest_framework import viewsets
from .serializer import EquipamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['description', 'modelo', 'price']

