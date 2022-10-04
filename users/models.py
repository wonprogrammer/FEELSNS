from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserModel(models.Model):

    class Meta:
        db_table = "user"

    login_id = models.CharField(max_length=16, null=False)
    nickname = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=256, null=False)
    password2 = models.CharField(max_length=256, null=False)


class ProfileModel(models.Model):

    class Meta:
        db_table = "profile"

    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    user_images = models.ImageField(null=True, upload_to="", blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')