from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='productimages')
    category=models.CharField(max_length=25)

class Cart(models.Model):
    id = models.UUIDField(default= uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # ID=models.ForeignKey(User,on_delete=models.CASCADE)
    #productID=models.ForeignKey(product,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)

    # quantity=models.IntegerField()
    def __str__(self):
      return str(self.id)

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total   

    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity       


class Cartitem(models.Model):
    product= models.ForeignKey(product,on_delete=models.CASCADE,related_name='items')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cartitems')
    quantity=models.IntegerField(default=0)  
    
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return self.product.name

    @property
    def price(self):
     new_price =self.product.price * self.quantity
     return new_price
