from pyexpat import model

from rest_framework import serializers

from .models import Children, Activity, SleepLogs, VaccinationLogs, DiaperChangeLogs, GrowthLogs


class ChildrenSerializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ("id", "name", "dob", "weight", "height", "parent", "gender")


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("id", "type", "child")


class SleepLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepLogs
        fields = ("id", "date", "start", "end", "child")


class VaccineLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationLogs
        fields = (
            "id",
            "date",
            "name",
            "number_of_doses",
            "number_of_doses_taken",
            "child",
        )


class GrowthLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthLogs
        fields = ("id", "datetime", "height", "child")



class DiaperChangeLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaperChangeLogs
        fields = ("id", "datetime", "description", "child")