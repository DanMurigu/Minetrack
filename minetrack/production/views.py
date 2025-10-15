from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductionRecord
from .serializers import ProductionRecordSerializer

# Create your views here.
class ProductionRecordViewSet(viewsets.ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductionRecordSerializer


