from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name="login"),
    path('',views.register,name="register"),
    path('register',views.register,name="register"),
    
]