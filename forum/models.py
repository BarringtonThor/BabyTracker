from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_body = models.TextField()
    post_author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post with title {self.post_title}"


class PostComment(models.Model):
    comment = models.TextField()
    comment_author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment of post {self.comment_post} by user {self.comment_author}"
