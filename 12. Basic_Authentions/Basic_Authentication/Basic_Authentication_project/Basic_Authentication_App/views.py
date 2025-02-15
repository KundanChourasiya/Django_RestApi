from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Emp
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Empviewset(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
