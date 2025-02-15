from django.db import models

class Emp(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=20)
    empsal = models.DecimalField(max_digits=10,decimal_places=2)

