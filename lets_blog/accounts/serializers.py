from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from .models.user_profile import UserProfile

class UserSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        user = User.objects.create(**validate_data)
        UserProfile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}, 
                           'id': {'read_only': True} }


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['about', 'profile_pic_url', 'user']
        extra_kwargs = {'user': {'read_only': True}}