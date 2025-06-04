from .models import EquipamentoItem 
from rest_framework import serializers

class EquipamentoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipamentoItem
        fields = '__all__'

        