from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title