# Generated by Django 4.1.2 on 2022-10-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usermodel_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
