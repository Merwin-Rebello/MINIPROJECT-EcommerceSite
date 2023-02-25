from django.db import models




# Create your models here.
class products(models.Model):
    user_name= models.CharField(max_length=15,default=None)
    product_id = models.IntegerField()
    amount= models.IntegerField(default=0)
