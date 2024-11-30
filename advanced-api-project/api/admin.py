from django.contrib import admin

from .models import Author, Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Configures the display and management of the Author model in the Django admin interface.

    Features:
        - Filters authors by name.
        - Provides search functionality for author names.
    """

    list_filter = ['name']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Configures the display and management of the Book model in the Django admin interface.

    Features:
        - Displays the book title and author in the list view.
        - Enables search functionality by book title.
        - Filters books by publication year.
    """

    list_display = ['title', 'author']
    search_fields = ['title']
    list_filter = ['publication_year']
