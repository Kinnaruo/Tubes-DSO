import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Users List", response.data)  # Check for text in response

    def test_add_user(self):
        response = self.client.post('/add', data=dict(name="John", age=25))
        self.assertEqual(response.status_code, 302)  # Redirect after adding user
        self.assertIn(b"John", response.data)  # Check if user is in the response data

if __name__ == '__main__':
    unittest.main()
