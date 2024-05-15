from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
def home(request):

    return render(request,'home.html')

#API views


# List of blogs
class BlogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Create a new blog
class BlogCreate(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Retrieve a single blog
class BlogRetrieve(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Update the existing blog
class BlogUpdate(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Destroy the existing blog
class BlogDelete(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
