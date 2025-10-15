from rest_framework import serializers
from .models import TransportCost

class TransportCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCost
        fields = '__all__'