from .models import TipoMonitoramentoTipo
from rest_framework import serializers

class TipoMonitoramentoTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMonitoramentoTipo
        fields = '__all__'
