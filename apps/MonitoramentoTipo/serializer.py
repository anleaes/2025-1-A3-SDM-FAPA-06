from .models import MonitoramentoTipo
from rest_framework import serializers

class MonitoramentoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoramentoTipo
        fields = '__all__'
        