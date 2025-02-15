from django.contrib import admin
from .models import Feedback

class AdminFeedback(admin.ModelAdmin):
    list_display = ['user_id','name','email','subject','message','created','modefied']

admin.site.register(Feedback,AdminFeedback)
