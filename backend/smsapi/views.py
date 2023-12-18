from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import Group, Permission
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from smsapi.models import User, Teacher, Student, Subject, Term, Test, studentPerformance, studentScore
from smsapi.serializers import UserSerializer, StudentSerializer, TeacherSerializer, SubjectSerializer, TermSerializer, StudentPerformanceSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import time

# Function Based Views

# Simple Hello World API
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello World!'})

# Admin SignUp API View
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def adminSignup(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.is_active = True
        user_instance.save()

        # Token Generated during SignUp
        token, created = Token.objects.get_or_create(user=user_instance)


        # Add Admin to Admin Group
        admin_group, _ = Group.objects.get_or_create(name="admins")
        user_instance.groups.add(admin_group)

        # Add Admin to Admin Permissions
        permissions = Permission.objects.filter(name__icontains="admin_users")
        user_instance.user_permissions.add(*permissions)

        return Response({"message" : "Success, BaseUser Registered!","token" : token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin Login API View
@api_view(['POST'])
@permission_classes([AllowAny])
def adminLogin(request):

    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    if user:
        if user.is_active:
            return Response({"message" : "Success, BaseUser Logged In", "token" : token.key, "user": serializer.data})
        return Response({"message" : f"{str(user.username)} is not Active"})
    return Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)

# Teacher SignUp API View
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def teacherRegister(request):

    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.save()

        # Token Generated during SignUp
        # token, created = Token.objects.get_or_create(user=user_instance)

        # Add Teacher to Teacher Group
        teacher_group, _ = Group.objects.get_or_create(name="teachers")
        user_instance.groups.add(teacher_group)

        # Add Teacher to Teacher Permissions
        permissions = Permission.objects.filter(name__icontains="teacher_users")
        user_instance.user_permissions.add(*permissions)

        return Response({"message" : "Success, TeacherUser Registered!", "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Teacher Login API View
@api_view(['POST'])
@permission_classes([AllowAny])
def teacherLogin(request):

    user = get_object_or_404(Teacher, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    # token, created = Token.objects.get_or_create(user=user)
    serializer = TeacherSerializer(instance=user)
    if user:
        if user.is_active:
            return Response({"message" : "Success, TeacherUser Logged In!", "user": serializer.data})
        return Response({"message" : f"{str(user.username)} is not Active"})
    return Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)

# Student SignUp API View
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def studentRegister(request):

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        user_instance = serializer.save()
        user_instance.set_password(request.data['password'])
        user_instance.save()

        # Token Generated during SignUp
        # token, created = Token.objects.get_or_create(user=user_instance)

        # Add Teacher to Student Group
        student_group, _ = Group.objects.get_or_create(name="students")
        user_instance.groups.add(student_group)

        # Add Teacher to Student Permissions
        permissions = Permission.objects.filter(name__icontains="student_users")
        user_instance.user_permissions.add(*permissions)

        return Response({"message" : "Success, StudentUser Registered!", "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Login API View
@api_view(['POST'])
@permission_classes([AllowAny])
def studentLogin(request):

    user = get_object_or_404(Student, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
    # token, created = Token.objects.get_or_create(user=user)
    serializer = StudentSerializer(instance=user)
    if user:
        if user.is_active:
            return Response({"message" : "Success, StudentUser Logged In!", "user": serializer.data})
        return Response({"message" : f"{str(user.username)} is not Active"})
    return Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)

# User LogOut
@action(detail=False, methods=['post'])
def UserLogout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass

    logout(request)
    return Response(status=status.HTTP_200_OK)

# Class Based Views

# Admin ID Lookup
class adminDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

adminDetailView = adminDetailAPIView.as_view()

# Student ID Lookup
class studentDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

studentDetailView = studentDetailAPIView.as_view()

# Teacher ID Lookup
class teacherDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

teacherDetailView = teacherDetailAPIView.as_view()

class SubjectCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        term = serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
subjectCreateView = SubjectCreateView.as_view()

class TermCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Term.objects.all()
    serializer_class = TermSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        term = serializer.save()

        # Generaing tests for created terms
        self.generate_tests_for_term(term)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def generate_tests_for_term(self, term):
        # Assuming a list of subjects is in place
        subjects = Subject.objects.all()

        for subject in subjects:
            for test_number in range(1, 3):
                test_name = f"{subject.name} {chr(ord('A') + test_number - 1)}"
                Test.objects.create(term=term, subject=subject, name=test_name)

termCreateView = TermCreateView.as_view()

class StudentPerformanceView(generics.CreateAPIView):
    queryset = studentPerformance.objects.all()
    serializer_class = StudentPerformanceSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of request.data
        mutable_data = request.data.copy()

        # Logic to assign grades based on the score
        score = mutable_data.get('score', 0)
        if score < 10:
            mutable_data['grade'] = 'F'
        elif score < 20:
            mutable_data['grade'] = 'E'
        elif score < 40:
            mutable_data['grade'] = 'D'
        elif score < 60:
            mutable_data['grade'] = 'C'
        elif score < 80:
            mutable_data['grade'] = 'B'
        else:
            mutable_data['grade'] = 'A'

        # Use the mutable copy for further processing
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201)

studentPerformanceView = StudentPerformanceView.as_view()