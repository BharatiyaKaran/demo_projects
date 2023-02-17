from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        user = User.objects.create(**validate_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']