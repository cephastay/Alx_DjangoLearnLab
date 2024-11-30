from django.test import TestCase
from api.serializers import AuthorSerializer, BookSerializer
from api.models import Author, Book

class BookSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an author and book instance for testing
        cls.author = Author.objects.create(name='Chinua Achebe')
        cls.book = Book.objects.create(
            title='Things Fall Apart',
            author=cls.author,
            publication_year=1956
        )
        cls.book_serializer = BookSerializer(cls.book)

    def test_book_serializer_contains_expected_fields(self):
        # Ensure the serializer includes the correct fields
        data = self.book_serializer.data
        self.assertEqual(
            set(data.keys()),
            {'id', 'title', 'publication_year', 'author'}
        )

    def test_book_serializer_field_content(self):
        # Ensure the serialized data matches the instance data
        data = self.book_serializer.data
        self.assertEqual(data['title'], 'Things Fall Apart')
        self.assertEqual(data['publication_year'], 1956)
        self.assertEqual(data['author'], self.author.id)

class AuthorSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an author and books for testing
        cls.author = Author.objects.create(name='Chinua Achebe')
        cls.book1 = Book.objects.create(
            title='Things Fall Apart',
            author=cls.author,
            publication_year=1956
        )
        cls.book2 = Book.objects.create(
            title='Arrow of God',
            author=cls.author,
            publication_year=1964
        )
        cls.author_serializer = AuthorSerializer(cls.author)

    def test_author_serializer_contains_expected_fields(self):
        # Ensure the serializer includes the correct fields
        data = self.author_serializer.data
        self.assertEqual(set(data.keys()), {'name', 'books'})

    def test_author_serializer_nested_books(self):
        # Test that the nested books are serialized correctly
        data = self.author_serializer.data
        self.assertEqual(len(data['books']), 2)
        self.assertEqual(data['books'][0]['title'], 'Arrow of God')
        self.assertEqual(data['books'][1]['title'], 'Things Fall Apart')


