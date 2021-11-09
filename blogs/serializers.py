# TODO: Serializer for the blog data
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "body", "author")
