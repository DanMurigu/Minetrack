from django.shortcuts import render
from rest_framework import viewsets
from .models import TransportCost
from .serializers import TransportCostSerializer

# Create your views here.

class TransportCostViewSet(viewsets.ModelViewSet):
    queryset = TransportCost.objects.all()
    serializer_class = TransportCostSerializer