from django.test import TestCase
from api.models import Author, Book

# Create your tests here.
class AuthorModelTest(TestCase):
    """This is to test the Author model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = Author.objects.create(name='Chinua Achebe')
        cls.book = Book.objects.create(title='Things Fall Apart', publication_year=1956, author=cls.author)
    
    def test_object_str_repr(self):
        self.assertEqual(str(self.author), f'{self.author.name}')
    
    def test_reverse_relationship(self):
        author_books = self.author.books.all()
        books_by_author = Book.objects.filter(author=self.author)
        self.assertQuerySetEqual(author_books, books_by_author)
    
    def test_name_field_max_length_uniqueness(self):
        name_field = self.author._meta.get_field('name')
        self.assertTrue(name_field.unique, "The 'name' field should have 'unique=True'.")
        self.assertEqual(name_field.max_length, 75,"The 'name' field should have a max_length of 75.")

class BookModelTestCase(TestCase):
    """For testing the methods and attributes of the Book model"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = Author.objects.create(name='Chinua Achebe')
        cls.book = Book.objects.create(title='Things Fall Apart', publication_year=1956, author=cls.author)

    def test_book_str_repr(self):
        self.assertEqual(str(self.book), f'{self.book.title}')

    def test_book_forward_relationship(self):
        self.assertEqual(self.author, self.book.author)

    def test_book_in_dbtable(self):
        self.assertIn(self.book, Book.objects.all())