# Generated by Django 5.1.3 on 2024-11-30 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'permissions': [('can_create_author', 'Permission to create new author instances'), ('can_delete_author', 'Permission to delete a author instance')]},
        ),
    ]
