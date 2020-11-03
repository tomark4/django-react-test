from blog.models import Post
from django.shortcuts import render
from rest_framework import generics
from blogapi.serializer import PostSerializer

# Create your views here.

class ListView(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class DetailView(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
