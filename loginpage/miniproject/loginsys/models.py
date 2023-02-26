from django.db import models
# Create your models here.

class Products(models.Model):
    prd_name=models.CharField(max_length=100,default=None)
    product_id= models.IntegerField()
    price= models.IntegerField(default=0)
    image=models.ImageField(upload_to='productimage/')


