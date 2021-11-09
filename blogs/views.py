from .serializers import BlogSerializer
from rest_framework import generics
from .models import Blog


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
