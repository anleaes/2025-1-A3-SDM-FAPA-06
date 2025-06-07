from django.shortcuts import render
from .models import ClasseEquipamento 
from rest_framework import viewsets
from .serializer import ClasseEquipamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ClasseEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = ClasseEquipamento.objects.all()
    serializer_class = ClasseEquipamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','description'] # Neste campo coloque somente.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]