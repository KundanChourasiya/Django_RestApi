from django.shortcuts import render
from rest_framework import viewsets
from Hyperlink_Serializer_App.models import Emp
from .serializers import EmpSerializer

class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


