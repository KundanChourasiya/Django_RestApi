from django.shortcuts import render
from rest_framework import viewsets
from Pagination_App.models import Emp
from .serializers import EmpSerializer

class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


