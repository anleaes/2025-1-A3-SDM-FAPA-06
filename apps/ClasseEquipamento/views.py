from django.shortcuts import render
from .models import ClasseEquipamento 
from rest_framework import viewsets
from .serializer import ClasseEquipamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ClasseEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = ClasseEquipamento.objects.all()
    serializer_class = ClasseEquipamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','description'] # Neste campo coloque somente.