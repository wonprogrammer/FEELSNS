# Generated by Django 4.1.1 on 2022-10-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]