from rest_framework.test import APITestCase
from rest_framework.reverse import reverse


class LoginViewTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.login_url = reverse('rest_framework:login')
        cls.books_list_url = reverse('list of books')
        cls.authors_list_url = reverse('authors-list')
        cls.user_data = {
            'username':'enam',
            'password':'root1234'
        }

    def test_login_page_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_booklist_page_get(self):
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, 200)

    def test_authorlist_page_get(self):
        response = self.client.get(self.authors_list_url)
        self.assertEqual(response.status_code, 200)