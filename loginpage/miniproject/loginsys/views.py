from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'login.html',{'text':'sucessfully logged in'})
        else:
            return render(request,'login.html',{'text':'bad input'})
    return render(request,'login.html')