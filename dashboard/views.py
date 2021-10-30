# Create your views here.
from rest_framework import generics

from .models import Children, Activity
from .serializers import ChildrenSerializers, ActivitySerializer


class ChildrenList(generics.ListCreateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializers


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ChildrenUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChildrenSerializers
    queryset = Children.objects.all()
