from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models.user_profile import UserProfile
from accounts.serializers import (
    UserCreateSerializer, 
    UserViewSerializer, 
    UserProfileViewSerializer, 
    UserProfileCreateSerializer)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import timedelta

# Create your views here.

class UserList(APIView):
    """
    List all users
    """
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserViewSerializer(users, many=True)
        return Response(serializer.data)

class SignUp(APIView):
    """
    Sign Up - Create new
    """

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        response_data = {
            "errors": None,
            "data": None
        }

        if serializer.is_valid():
            serializer.save()
            # JWT 
            refresh = RefreshToken.for_user(request.user)
            access_token = refresh.access_token
            # set access token expiry as 1 day
            access_token.set_exp(lifetime=timedelta(days=1))
            response_data["data"] = {
                'refresh': str(refresh),
                'access': str(access_token),
            }
            response_status=status.HTTP_201_CREATED
        else:
            response_data["errors"] = serializer.errors
            print(serializer.errors)
            response_status = status.HTTP_400_BAD_REQUEST
        
        return Response(response_data, status=response_status)

class UserDetail(APIView):
    """ 
    Retrieve, update or delete a user
    """
    #permission_classes = [IsAuthenticated]

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
        response_data = {
            "errors": None,
            "data": None
        }
        if serializer.is_valid():
            serializer.save()
            response_status = status.HTTP_201_CREATED
        else:
            response_data["errors"] = serializer.errors
            response_status = status.HTTP_204_NO_CONTENT
        
        return Response(response_data, status=response_status)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileList(APIView):

    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        print(request.user)
        users = UserProfile.objects.all()
        serializer = UserProfileViewSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProfileDetail(APIView):

    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk = pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def get(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
        except Exception:
            return Response("Object does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileViewSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        try:
            user = self.get_object(pk)
        except Exception:
            return Response("Object does not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileCreateSerializer(instance=request.user, data=request.data)
        print(request.user)
        response_data = {
            "errors": None,
            "data": None
        }
        if serializer.is_valid():
            user_profile = serializer.save()
            print(user_profile)
            response_data["data"] = UserProfileCreateSerializer(instance=user_profile).data
            response_status = status.HTTP_200_OK
        else:
            response_data["errors"] = serializer.errors
            response_status = status.HTTP_204_NO_CONTENT
        
        return Response(response_data, status=response_status)

    def delete(self, request, pk):
        try:
            user = self.get_object(pk)
        except Exception:
            return Response("Object does not exist", status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk, format=None):
        # TODO : Complete this !
        return Response("No change", status=status.HTTP_200_OK)
    
