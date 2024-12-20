# Generated by Django 5.1.3 on 2024-12-13 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
