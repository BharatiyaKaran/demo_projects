from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from .models.user_profile import UserProfile

class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        user = User.objects.create(**validate_data)
        UserProfile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class UserViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class UserProfileViewSerializer(serializers.ModelSerializer):
    user = UserViewSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'about', 'profile_pic_url', 'user']

class UserProfileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['about', 'profile_pic_url']
    
    def save(self):
        about = self.validated_data['about']