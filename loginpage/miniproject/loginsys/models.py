from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.IntegerField()
    user_name= models.CharField(max_length=15,default=None)