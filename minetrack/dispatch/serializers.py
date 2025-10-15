from rest_framework import serializers
from .models import DispatchRecord

class DispatchRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchRecord
        fields = '__all__'