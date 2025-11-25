from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a normal user for testing authenticated access
        self.user = User.objects.create_user(username="testuser", password="pass1234")

        # Create an admin user for testing admin permissions
        self.admin = User.objects.create_superuser(username="admin", password="admin1234")

        # Create test author and books
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer At Ease",
            publication_year=1960,
            author=self.author
        )

        self.client = APIClient()

    # -----------------------------
    # Test LIST VIEW (GET /books/)
    # -----------------------------
    def test_list_books_requires_authentication(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_books_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -----------------------------
    # Test DETAIL VIEW (GET /books/<id>/)
    # -----------------------------
    def test_get_single_book(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    # -----------------------------
    # Test CREATE VIEW (POST /books/create/)
    # -----------------------------
    def test_create_book_admin_only(self):
        # Not logged in → forbidden
        response = self.client.post("/api/books/create/", {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Logged in as normal user → still forbidden
        self.client.login(username="testuser", password="pass1234")
        response = self.client.post("/api/books/create/", {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Logged in as admin → allowed
        self.client.login(username="admin", password="admin1234")
        response = self.client.post("/api/books/create/", {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # -----------------------------
    # Test UPDATE VIEW (PUT /books/update/<id>/)
    # -----------------------------
    def test_update_book(self):
        self.client.login(username="admin", password="admin1234")
        response = self.client.put(f"/api/books/update/{self.book1.id}/", {
            "title": "Updated Title",
            "publication_year": 1958,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # -----------------------------
    # Test DELETE VIEW (DELETE /books/delete/<id>/)
    # -----------------------------
    def test_delete_book(self):
        self.client.login(username="admin", password="admin1234")
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # TEST FILTERING (title, author, year)
    # -----------------------------
    def test_filter_books_by_title(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/api/books/?title=Things Fall Apart")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -----------------------------
    # TEST SEARCH
    # -----------------------------
    def test_search_books_by_title(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/api/books/?search=Things")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -----------------------------
    # TEST ORDERING
    # -----------------------------
    def test_order_books(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "No Longer At Ease")
