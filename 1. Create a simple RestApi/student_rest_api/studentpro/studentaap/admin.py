from django.contrib import admin
from .models import Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','semail','sfee','sloc']

admin.site.register(Student,AdminStudent)