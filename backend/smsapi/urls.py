from django.urls import path
from smsapi import views

urlpatterns = [
    path('helloworld/', views.hello_world, name='helloworld'),
    path('adminsignup/', views.adminSignup, name='signup'),
    path('adminlogin/', views.adminLogin, name='login')
]