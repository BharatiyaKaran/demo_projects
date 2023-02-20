from rest_framework import serializers
from .models.blog import Blog
from accounts.serializers import UserSerializer

class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Blog
        fields = ['title', 'owner', 'body', 'status']

class BlogViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'owner', 'body', 'slug']