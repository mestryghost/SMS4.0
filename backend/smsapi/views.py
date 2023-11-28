from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from smsapi.models import User, Teacher, Student
from smsapi.serializers import UserSerializer, StudentSerializer, TeacherSerializer
from django.shortcuts import get_object_or_404

# Function Based Views

# Simple Hello World API
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

# Admin SignUp API View
@api_view(['POST', 'GET'])
def adminSignup(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.save()
        return Response({"user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Login API View
@api_view(['POST'])
def adminLogin(request):

    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(instance=user)
    return Response({"user": serializer.data})

# Teacher SignUp API View
@api_view(['POST', 'GET'])
def teacherRegister(request):

    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.save()
        return Response({"user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Teacher Login API View
@api_view(['POST'])
def teacherLogin(request):

    user = get_object_or_404(Teacher, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = TeacherSerializer(instance=user)
    return Response({"user": serializer.data})

# Student SignUp API View
@api_view(['POST', 'GET'])
def studentRegister(request):

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.save()
        return Response({"user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Login API View
@api_view(['POST'])
def studentLogin(request):

    user = get_object_or_404(Student, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(instance=user)
    return Response({"user": serializer.data})



# Class Based Views

# Admin ID Lookup
class adminDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

adminDetailView = adminDetailAPIView.as_view()

# Student ID Lookup
class studentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

studentDetailView = studentDetailAPIView.as_view()

# Teacher ID Lookup
class teacherDetailAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

teacherDetailView = teacherDetailAPIView.as_view()