from django.urls import path
from smsapi import views

urlpatterns = [
    path('helloworld/', views.hello_world, name='helloworld')
]