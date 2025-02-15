from django.contrib import admin
from . models import ProductInfo

class AdminProductInfo(admin.ModelAdmin):
    list_display = ['pno','pname','pcost','pdese']


admin.site.register(ProductInfo,AdminProductInfo)
