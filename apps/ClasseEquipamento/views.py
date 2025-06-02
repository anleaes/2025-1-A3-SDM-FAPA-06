from django.shortcuts import render
from .models import ClasseEquipamento 
from rest_framework import viewsets
from .serializer import ClassEquipamentSerializer

# Create your views here.

class ClassEquipamentViewSet(viewsets.ModelViewSet):
    queryset = ClasseEquipamento.objects.all()
    serializer_class = ClassEquipamentSerializer