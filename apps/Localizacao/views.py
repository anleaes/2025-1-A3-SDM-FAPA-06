from django.shortcuts import render
from .models import Localizacao
from rest_framework import viewsets
from .serializer import LocalizacaoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['address', 'Location']

    