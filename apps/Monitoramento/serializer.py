from .models import Monitoramento
from rest_framework import serializers

class MonitoramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoramento
        fields = '__all__'
        