import unittest
from app import app
import json

class LibraryManagementSystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_book(self):
        response = self.app.post("/books", json={"title": "Book1", "author": "Author1"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("title", response.json)

    def test_get_books(self):
        response = self.app.get("/books?page=1&per_page=10")
        self.assertEqual(response.status_code, 200)

    def test_add_member(self):
        response = self.app.post("/members", json={"name": "John Doe"}, headers={"Authorization": "user-token"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("name", response.json)

    def test_token_required(self):
        response = self.app.post("/members", json={"name": "Jane Doe"})
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
