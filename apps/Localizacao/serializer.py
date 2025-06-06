from .models import Localizacao
from rest_framework import serializers

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'
        