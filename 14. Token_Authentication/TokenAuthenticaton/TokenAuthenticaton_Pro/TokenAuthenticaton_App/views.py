from django.shortcuts import render,redirect
from .serializers import EmpSerializer
from .models import Emp
from rest_framework import viewsets
from django.contrib.auth import authenticate,login

def login_form(request):
    return render(request,'login.html')

def login_user(request):
    username = request.POST['uname']
    password = request.POST['pwd']
    user = authenticate(username=username,password=password)
    print(user)
    print("=====     ======")
    if user is not None:
        login(request,user)
        return redirect('/api')
    else:
        return redirect('/auth')

class EmpViewset(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer