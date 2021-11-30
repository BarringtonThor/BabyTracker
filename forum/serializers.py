from rest_framework import serializers
from .models import Post, PostComment


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "post_title",
            "post_body",
            "post_author",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ("id", "comment", "comment_author", "comment_post")
