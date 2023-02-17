from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.blog import Blog
from blogs.serializers import BlogCreateSerializer, BlogViewSerializer

# Create your views here.

class BlogList(APIView):
    """
    List all users or create a new user
    """

    def get(self, request, format=None):
        users = Blog.objects.all()
        serializer = BlogViewSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Blog created successfully!", status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    """ 
    Retrieve, update or delete a user
    """

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk = pk)
        except Blog.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlogCreateSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlogCreateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Blog updated successfully!")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)