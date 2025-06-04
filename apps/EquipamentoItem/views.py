from django.shortcuts import render
from .models import EquipamentoItem 
from rest_framework import viewsets
from .serializer import  EquipamentoItemSerializer

# Create your views here.

class EquipamentoItemViewSet(viewsets.ModelViewSet):
    queryset = EquipamentoItem.objects.all()
    serializer_class = EquipamentoItemSerializer  

    