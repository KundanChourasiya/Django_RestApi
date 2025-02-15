from django.shortcuts import render
from rest_framework import generics
from .import serializers
from productapp import models

class ListProduct(generics.ListCreateAPIView):
    queryset = models.ProductInfo.objects.all()
    serializer_class = serializers.ProductInfoSerializer