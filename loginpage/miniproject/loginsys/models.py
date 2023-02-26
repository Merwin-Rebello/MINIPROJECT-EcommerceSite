from django.db import models

class product(models.Model):
    name= models.CharField(max_length=100,default=0)
    price= models.IntegerField(default=0)
    image= models.ImageField(upload_to='productimages/')