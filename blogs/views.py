from .serializers import BlogSerializer
from rest_framework import generics, viewsets
from .models import Blog


# class BlogList(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer

