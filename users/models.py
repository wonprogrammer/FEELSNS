from django.db import models


class UserModel(models.Model):

    class Meta:
        db_table = "user"

    login_id = models.TextField(max_length=16, null=False)
    nickname = models.TextField(max_length=16, null=False)
    password = models.CharField(max_length=256, null=False)
    password2 = models.CharField(max_length=256, null=False)


class ProfileModel(models.Model):

    class Meta:
        db_table = "profile"

    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    bio = models.CharField(max_length=256, blank=True)    # 필드에 blank = True widget(양식) 유효성 검사에서 빈 값을 입력 할 수 있다.
    user_images = models.ImageField(null=True, upload_to="", blank=True)
