from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an Author in the database library.

    Attributes:
        name (str): The name of the Author
    """
    name = models.CharField(max_length=75, unique=True)

    class Meta:
        """
        Meta options for Author Model.

        Attributes:
            permissions (list[tuple[str, str]]): Defines custom permissions for managing 
            Author instances, including creating and deleting.
        """
        permissions = [
        ('can_create_author', 'Permission to create new author instances'),
        ('can_delete_author', 'Permission to delete a author instance'),]

    def __str__(self) -> str:
        """Returns the Name of the author"""
        return self.name

class Book(models.Model):
    """
    Represents a book in the database library.

    Attributes:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (Author): A foreign key to the Author model, representing the book's author.
    
    Notes:
        This class is designed to store book-related data and establish a 
        relationship with the Author model.
    """

    title = models.CharField(max_length=150)
    publication_year = models.IntegerField() #assigned as integer field to make validation elsewhere easier
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        """Returns the title of the book object as a str"""
        return self.title
    
class Meta:
    """
    Meta options for the Book model.

    Attributes:
        ordering (list[str]): Specifies the default ordering of books, first by title 
            and then by publication year.
        permissions (list[tuple[str, str]]): Defines custom permissions for managing 
            book instances, including creating, editing, and deleting.
    """
    ordering = ['title', 'publication_year']
    permissions = [
        ('can_edit_book', 'Permission to edit the title, author, and publication year'),
        ('can_create_book', 'Permission to create new book instances'),
        ('can_delete_book', 'Permission to delete a book instance'),
    ]

