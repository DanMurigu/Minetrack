from django.shortcuts import render
from rest_framework import viewsets
from .models import DispatchRecord
from .serializers import DispatchRecordSerializer

# Create your views here.
class DispatchRecordViewSet(viewsets.ModelViewSet):
    queryset = DispatchRecord.objects.all()
    serializer_class = DispatchRecordSerializer