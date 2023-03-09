from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import product, Cart, Cartitem
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
# from cart.cart import Cart

def login(request):
    if request.method=='POST': 
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html',{'name':username})
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
                return render(request,'index.html',{'name':username})
        else:
            messages.info(request,'Password Not Same')
            return redirect('index')
    return render(request,'register.html')

def index ( request):
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        
    context = {"products":product, "cart": cart}
    return render(request,'index.html',context)

def home(request):
    return render(request,'index.html')

def category(request,value):
    print(value)
    a=product.objects.filter(category=value)
    context = {"products":a, "cart": cart}
    return render(request,'category.html',{'objects':a,'category':value.capitalize()})


def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def carthome(request):
    return render(request,'index.html')

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
        print(cartitem)
    return JsonResponse("it is working upp",safe=False)

class indexview(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
      context= super().get_context_data(**kwargs)
      context['key'] = settings.STRIPE_PUBLISHABLE_KEY
      return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment gateway',
            source=request.POST['stripeToken']
        )
    return render(request,'charge.html')

