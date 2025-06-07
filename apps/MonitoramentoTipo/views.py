from django.shortcuts import render
from .models import MonitoramentoTipo
from rest_framework import viewsets
from .serializer import MonitoramentoTipoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class MonitoramentoTipoViewSet(viewsets.ModelViewSet):
    queryset = MonitoramentoTipo.objects.all()
    serializer_class = MonitoramentoTipoSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quantity', 'description', 'rate_security']