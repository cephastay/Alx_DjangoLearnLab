# Generated by Django 5.1.3 on 2024-12-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='comment'),
        ),
    ]
