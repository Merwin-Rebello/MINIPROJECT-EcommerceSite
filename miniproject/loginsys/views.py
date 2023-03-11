from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import product, Cart, Cartitem
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from django.views.generic.base import TemplateView
from .models import *
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY
# from cart.cart import Cart

def login(request):
    if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            a=product.objects.filter(category="featuredindex")
            return render(request,'index.html',{'name':username,'objects':a})
        else:
            return render(request,'login.html',{'text':' SORRRY!! cannot login'})
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        # list=feats.objects.all()
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if (password==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return render(request,'register.html',{'error':"Account already exists!!!"})
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)  
                key=0 
                user.save()
                user1=auth.authenticate(username=username,password=password)
                auth.login(request,user1)
                a=product.objects.filter(category="featuredindex")
                return render(request,'index.html',{'name':username,'objects':a})
        else:
            messages.info(request,'Password Not Same')
            return redirect('register')
    return render(request,'register.html')

def index (request):
    
    a=product.objects.filter(category="featuredindex")
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)    
    # context = {"products":product, "cart": cart}
    return render(request,'index.html',{'objects':a})

def home(request):
    return redirect('index')

def category(request,value):
    a=product.objects.filter(category=value)
    context = {"products":a, "cart": cart,'objects':a,'category':value.capitalize()}
    return render(request,'category.html',context)


def logout(request):
    auth.logout(request)
    return redirect('index')

def carthome(request):
    return redirect('index')

def cart(request):

    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart,created=Cart.objects.get_or_create(user=request.user,completed=False)
        cartitems = cart.cartitems.all()

         
    context = {"cart":cart, "items":cartitems}
    return render(request,'cart.html',context)


def add_to_cart(request):
    data= json.loads(request.body)
    product_id= data["id"]
    product1= product.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        print(cart)
        cartitem, created =Cartitem.objects.get_or_create(cart=cart, product=product1)
        cartitem.quantity += 1
        cartitem.save()

        num_of_item = cart.num_of_items

        print(cartitem)
        
    return JsonResponse(num_of_item,safe=False)

# class indexview(TemplateView):
#     template_name='index.html'

#     def get_context_data(self, **kwargs):
#       context= super().get_context_data(**kwargs)
#       context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#       return context

# def charge(request):
#     if request.method == 'POST':
#             charge = stripe.Charge.create(
#             amount=500,
#             currency='inr',
#             description='Payment gateway',
#             source=request.POST['stripeToken']
#         )
#     return render(request,'charge.html')

def delete_item(request, id):
    cart = Cart.objects.get(id)
    cart.quantity -=1
    #cart.completed = True
    cart.save()
    #messages.success(request, "Payment made successfully")
    return redirect("cart.html")