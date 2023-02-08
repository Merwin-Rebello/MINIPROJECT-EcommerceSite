from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('shoppage',views.shop,name="shoppage"),
    path('bakingoods',views.baking,name="bakingoods"),
    path('snacks',views.snacks,name="snacks"),
]