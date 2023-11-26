from rest_framework import serializers
from smsapi.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'email']