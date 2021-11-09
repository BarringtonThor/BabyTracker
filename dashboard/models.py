from django.db import models


class Children(models.Model):
    name = models.CharField(max_length=60)
    dob = models.DateField()
    weight = models.DecimalField(decimal_places=2,max_digits=2)
    parent = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return f"Name={self.name} of parent {self.parent.username}"


class Activity(models.Model):
    type = models.CharField(max_length=10)
    datetime_of_activity = models.DateTimeField(auto_now=True)
    child = models.ForeignKey(Children,on_delete=models.CASCADE)

    def __str__(self):
        return self.type
