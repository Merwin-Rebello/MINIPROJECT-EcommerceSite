from django.contrib import admin
from .models import products
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display =['user_name','product_id','amount']
    
admin.site.register(products,AdminProduct)