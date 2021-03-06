from rest_framework.serializers import ModelSerializer

from .models import Exchange


class ExchangeSerializer(ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('user', 'valute1', 'valute2')

