from rest_framework import viewsets

from forum.models import Post, PostComment
from .serializers import ForumSerializer, CommentSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = ForumSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all().order_by("id")
    serializer_class = CommentSerializer
