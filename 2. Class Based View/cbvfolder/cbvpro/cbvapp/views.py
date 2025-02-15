from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class Instituteclass(APIView):
    def get(self,request):
        databases=[
            {
                'oracle':1000,
                'mysql':1500,
                'sql server':1000
            }
        ]

        languages = [
            {
                'c':1000,
                'c++':2000,
                'python':2000
            }
        ]
        fees = [
            {
                'sai': 1000,
                'satya': 2000,
                'Ramu': 5000
            }
        ]
        return Response(
            {
                'databases':databases,
                'languages':languages,
                'fees':fees

            }
        )