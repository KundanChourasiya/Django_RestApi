from django.contrib import admin
from TokenAuthenticaton_App.models import Emp

class AdminEmp(admin.ModelAdmin):
    list_display = ['empid','empname','empsal','created','modified']

admin.site.register(Emp,AdminEmp)
