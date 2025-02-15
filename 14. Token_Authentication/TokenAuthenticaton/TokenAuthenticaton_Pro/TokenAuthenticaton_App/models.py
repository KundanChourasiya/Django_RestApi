from django.db import models

class Emp(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=200)
    empsal = models.DecimalField(max_digits=10,decimal_places=2)
    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
