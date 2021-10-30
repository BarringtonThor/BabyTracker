from django.db import models
from django.contrib.auth.models import User


class Children(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    weight = models.DecimalField(decimal_places=2)
    parent = models.ForeignKey(User)


class Activity(models.Model):
    type = models.CharField(max_length=10)
    datetime_of_activity = models.DateTimeField(auto_now=True)
    child = models.ForeignKey(Children)
