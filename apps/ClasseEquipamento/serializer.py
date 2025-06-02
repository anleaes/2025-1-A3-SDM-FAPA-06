from .models import ClasseEquipamento
from rest_framework import serializers

class ClasseEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseEquipamento
        fields = '__all__'
        

        