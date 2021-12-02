# Create your views here.
from rest_framework import viewsets, generics

from .models import (
    Children,
    Activity,
    VaccinationLogs,
    DiaperChangeLogs,
    SleepLogs,
    GrowthLogs,
)
from .serializers import (
    ChildrenSerializers,
    ActivitySerializer,
    VaccineLogsSerializer,
    DiaperChangeLogsSerializer,
    SleepLogsSerializer,
    GrowthLogsSerializer,
)


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ChildrenViewSet(viewsets.ModelViewSet):
    serializer_class = ChildrenSerializers
    queryset = Children.objects.all()


class VaccinationLogsViewSet(viewsets.ModelViewSet):
    serializer_class = VaccineLogsSerializer
    queryset = VaccinationLogs.objects.all()


class DiaperChangeLogsViewSet(viewsets.ModelViewSet):
    serializer_class = DiaperChangeLogsSerializer
    queryset = DiaperChangeLogs.objects.all()


class SleepLogsViewSet(viewsets.ModelViewSet):
    serializer_class = SleepLogsSerializer
    queryset = SleepLogs.objects.all()


class GrowthLogsViewSet(viewsets.ModelViewSet):
    serializer_class = GrowthLogsSerializer
    queryset = GrowthLogs.objects.all()


class VaccinationLogsByChild(generics.ListAPIView):
    serializer_class = VaccineLogsSerializer

    def get_queryset(self):
        child_id = self.request.query_params.get("child_id")
        return VaccinationLogs.objects.filter(child=child_id)


class SleepLogsByChild(generics.ListAPIView):
    serializer_class = SleepLogsSerializer

    def get_queryset(self):
        child_id = self.request.query_params.get("child_id")
        return SleepLogs.objects.filter(child=child_id)


class GrowthLogsByChild(generics.ListAPIView):
    serializer_class = GrowthLogsSerializer

    def get_queryset(self):
        child_id = self.request.query_params.get("child_id")
        return GrowthLogs.objects.filter(child=child_id)


class DiaperLogsByChild(generics.ListAPIView):
    serializer_class = DiaperChangeLogsSerializer

    def get_queryset(self):
        child_id = self.request.query_params.get("child_id")
        return DiaperChangeLogs.objects.filter(child=child_id)


class ChildrenByUser(generics.ListAPIView):
    serializer_class = ChildrenSerializers

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        return Children.objects.filter(parent_id=user_id)
