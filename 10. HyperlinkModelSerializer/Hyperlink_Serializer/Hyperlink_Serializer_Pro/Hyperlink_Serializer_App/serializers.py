from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emp
        fields = ('__all__')