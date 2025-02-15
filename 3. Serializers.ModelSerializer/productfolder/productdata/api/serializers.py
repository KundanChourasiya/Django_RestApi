from rest_framework import serializers
from productapp import models

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'pno',
            'pname',
            'pcost',
            'pdese'
        )

        model = models.ProductInfo