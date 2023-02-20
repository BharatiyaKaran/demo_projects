from rest_framework import serializers
from .models.blog import Blog
from accounts.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Blog
        fields = ['id', 'title', 'owner', 'body', 'status']
        extra_kwargs = {'id': {'read_only': True} }

class BlogDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta: 
        model = Blog
        fields = ['id', 'title', 'owner', 'body', 'status']
        extra_kwargs = {'id': {'read_only': True} }