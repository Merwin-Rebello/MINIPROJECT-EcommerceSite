from django.contrib import admin
from .models import Products
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['prd_name','product_id','price','image']