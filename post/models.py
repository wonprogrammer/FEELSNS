from django.db import models
from users.models import UserModel


class Post(models.Model):

    class Meta:
        db_table = "post"

    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.TextField(max_length=16, null=True, default='')
    post = models.TextField(max_length=10000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_images = models.ImageField(null=True, upload_to="", blank=True)


class Comment(models.Model):

    class Meta:
        db_table = "Comment"

    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.TextField(max_length=3000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    