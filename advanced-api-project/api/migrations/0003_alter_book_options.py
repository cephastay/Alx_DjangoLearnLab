# Generated by Django 5.1.3 on 2024-11-30 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'publication_year'], 'permissions': [('can_edit_book', 'Permission to edit the title, author, and publication year'), ('can_create_book', 'Permission to create new book instances'), ('can_delete_book', 'Permission to delete a book instance')]},
        ),
    ]
