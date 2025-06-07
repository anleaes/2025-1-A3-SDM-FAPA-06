from django.shortcuts import render
from .models import Monitoramento
from rest_framework import viewsets
from .serializer import MonitoramentoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class MonitoramentoViewSet(viewsets.ModelViewSet):
    queryset = Monitoramento.objects.all()
    serializer_class = MonitoramentoSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event', 'date_time', 'status']