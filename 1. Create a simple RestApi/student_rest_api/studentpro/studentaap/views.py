from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

def studentlist(request):
    s=Student.objects.all()
    data={"result":list(s.values('sno','sname','semail','sfee','sloc'))}
    return JsonResponse(data)
