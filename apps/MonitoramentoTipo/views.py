from django.shortcuts import render
from .models import MonitoramentoTipo
from rest_framework import viewsets
from .serializer import MonitoramentoTipoSerializer

# Create your views here.

class MonitoramentoTipoViewSet(viewsets.ModelViewSet):
    queryset = MonitoramentoTipo.objects.all()
    serializer_class = MonitoramentoTipoSerializer  