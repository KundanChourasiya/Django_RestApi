from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer

class ViewSet_Feedback(viewsets.ViewSet):
    def list(self,request):
        queryset = Feedback.objects.all()
        serializer= FeedbackSerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        queryset=Feedback.objects.get(pk=pk)
        serializer=FeedbackSerializer(queryset)
        return Response(serializer.data)

    def update(self,request,pk):
        queryset = Feedback.objects.get(pk=pk)
        serializer = FeedbackSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        queryset = Feedback.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

