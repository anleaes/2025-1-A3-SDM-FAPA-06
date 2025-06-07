from django.shortcuts import render
from .models import EquipamentoItem 
from rest_framework import viewsets
from .serializer import  EquipamentoItemSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class EquipamentoItemViewSet(viewsets.ModelViewSet):
    queryset = EquipamentoItem.objects.all()
    serializer_class = EquipamentoItemSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['unitary_price'] 

    