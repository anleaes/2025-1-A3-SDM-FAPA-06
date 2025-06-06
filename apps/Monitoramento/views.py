from django.shortcuts import render
from .models import Monitoramento
from rest_framework import viewsets
from .serializer import MonitoramentoSerializer

# Create your views here.

class MonitoramentoViewSet(viewsets.ModelViewSet):
    queryset = Monitoramento.objects.all()
    serializer_class = MonitoramentoSerializer  