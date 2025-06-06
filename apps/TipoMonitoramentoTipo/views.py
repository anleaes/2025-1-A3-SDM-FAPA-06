from django.shortcuts import render
from .models import TipoMonitoramentoTipo
from rest_framework import viewsets
from .serializer import TipoMonitoramentoTipoSerializer


# Create your views here.

class TipoMonitoramentoTipoViewSet(viewsets.ModelViewSet):
    queryset = TipoMonitoramentoTipo.objects.all()
    serializer_class = TipoMonitoramentoTipoSerializer  
