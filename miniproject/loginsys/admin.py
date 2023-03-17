from django.contrib import admin
from .models import product,Cart,Cartitem
from .  import  models
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(product)
admin.site.register(Cart)
# admin.site.register(Cartitem)

class cartitemadmin(ImportExportModelAdmin, admin.ModelAdmin):
      ...
admin.site.register(models.Cartitem,cartitemadmin)      