from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='productimages')
    category=models.CharField(max_length=25)

class cart(models.Model):
    ID=models.ForeignKey(User,on_delete=models.CASCADE)
    productID=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
