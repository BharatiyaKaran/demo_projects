from rest_framework import generics
from .models import Blog
from blogs.serializers import BlogSerializer, BlogDetailSerializer
from .permissions import IsBlogOwner

# Create your views here.
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = []

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsBlogOwner]