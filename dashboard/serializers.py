from rest_framework import serializers

from .models import Children, Activity


class ChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ("name", "dob", "weight", "parent")


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("type", "child")
