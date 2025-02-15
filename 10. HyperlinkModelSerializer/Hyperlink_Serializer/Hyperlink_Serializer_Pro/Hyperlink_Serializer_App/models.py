from django.db import models

class Emp(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
