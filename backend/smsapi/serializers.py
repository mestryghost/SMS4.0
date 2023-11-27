from rest_framework import serializers
from smsapi.models import User, Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Teacher
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Student
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']