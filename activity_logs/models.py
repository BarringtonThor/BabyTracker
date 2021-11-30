from django.db import models
from django.utils.translation import gettext_lazy as _


class Children(models.Model):
    class Gender(models.TextChoices):
        MALE = "ML", _("Male")
        FEMALE = "FM", _("Female")
        OTHER = "OT", _("Other")

    name = models.CharField(max_length=60)
    dob = models.DateField()
    weight = models.FloatField()
    height = models.IntegerField(default=0)
    parent = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.MALE,
    )

    def __str__(self):
        return f"Name={self.name} of parent {self.parent.username}"


class Activity(models.Model):
    type = models.CharField(max_length=10)
    datetime_of_activity = models.DateTimeField(auto_now=True)
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return self.child.name


class SleepLogs(models.Model):
    date = models.DateField(auto_now=True)
    start = models.TimeField()
    end = models.TimeField()
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return self.child.name


class VaccinationLogs(models.Model):
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=60)
    number_of_doses = models.IntegerField()
    number_of_doses_taken = models.IntegerField()
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return self.child.name


class DiaperChangeLogs(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=250)
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class GrowthLogs(models.Model):
    datetime = models.DateField(auto_now=True)
    height = models.IntegerField()
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    def __str__(self):
        return self.child.name
