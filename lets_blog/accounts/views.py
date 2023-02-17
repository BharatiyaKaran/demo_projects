from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from accounts.serializers import UserCreateSerializer, UserViewSerializer

# Create your views here.

class UserList(APIView):
    """
    List all users or create a new user
    """

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserViewSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User created successfully!", status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """ 
    Retrieve, update or delete a user
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserViewSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserCreateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User updated successfully!")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
