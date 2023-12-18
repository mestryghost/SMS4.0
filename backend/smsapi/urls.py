from django.urls import path
from smsapi import views

urlpatterns = [
    path('helloworld/', views.hello_world, name='helloworld'),
    path('adminsignup/', views.adminSignup, name='adminsignup'),
    path('adminlogin/', views.adminLogin, name='adminlogin'),
    path('studentsignup/', views.studentRegister, name='studentsignup'),
    path('studentlogin/', views.studentLogin, name='studentlogin'),
    path('teachersignup/', views.teacherRegister, name='teachersignup'),
    path('teacherlogin/', views.teacherLogin, name='teacherlogin'),
    path('logout/', views.UserLogout, name='logout'),
    path('admindetail/<int:pk>/', views.adminDetailView, name='admindetail'),
    path('studentdetail/<int:pk>/', views.studentDetailView, name='studentdetail'),
    path('subjectcreate/', views.subjectCreateView, name='subjectcreate'),
    path('termcreate/', views.termCreateView, name='termcreate')
]