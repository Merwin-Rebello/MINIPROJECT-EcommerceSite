from django.contrib import admin
from .models import product,Cart,Cartitem
# Register your models here.
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(Cartitem)