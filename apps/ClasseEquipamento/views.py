from django.shortcuts import render
from .models import ClasseEquipamento 
from rest_framework import viewsets
from .serializer import ClasseEquipamentoSerializer

# Create your views here.

class ClasseEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = ClasseEquipamento.objects.all()
    serializer_class = ClasseEquipamentoSerializer