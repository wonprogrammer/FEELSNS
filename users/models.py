from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserModel(AbstractUser):

    class Meta:
        db_table = "user"
   
    nickname = models.TextField(max_length=16, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    user_images = models.ImageField(null=True, upload_to="images", blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
