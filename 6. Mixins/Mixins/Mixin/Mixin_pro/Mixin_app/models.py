from django.db import models

class Product(models.Model):
    Product_id = models.IntegerField(primary_key=True)
    Product_name = models.CharField(max_length=20)
    Product_price = models.IntegerField()
    Product_color = models.CharField(max_length=20)
