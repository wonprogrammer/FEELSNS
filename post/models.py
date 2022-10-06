from django.db import models
from users.models import UserModel


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):

    class Meta:
        db_table = "Comment"

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.TextField(max_length=3000, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment