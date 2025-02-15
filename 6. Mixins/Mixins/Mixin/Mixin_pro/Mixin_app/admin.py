from django.contrib import admin
from .models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['Product_id','Product_name','Product_price','Product_color']

admin.site.register(Product,AdminProduct)
