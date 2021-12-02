from rest_framework import viewsets, generics

from forum.models import Post, PostComment
from .serializers import ForumSerializer, CommentSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = ForumSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all().order_by("id")
    serializer_class = CommentSerializer

class CommentByForum(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.request.query_params.get("post_id")
        return PostComment.objects.filter(comment_post=post_id)