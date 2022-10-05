from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserModel(AbstractUser):

    class Meta:
        db_table = "user"
   
    nickname = models.TextField(max_length=16, null=False)
    bio = models.CharField(max_length=500, blank=True)
    # user_images = models.ImageField(null=True, upload_to="", blank=True)
    # follow = models.ManyToMan\login_page\yField(settings.AUTH_USER_MODEL, related_name='followee')
        
    def __str__(self):
        return self.username