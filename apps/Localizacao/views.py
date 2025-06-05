from django.shortcuts import render
from .models import Localizacao
from rest_framework import viewsets
from .serializer import LocalizacaoSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer 

    