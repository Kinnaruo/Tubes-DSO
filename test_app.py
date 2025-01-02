import unittest
from app import create_user, read_users, update_user, delete_user, close_connection
import sqlite3

class TestCRUD(unittest.TestCase):

    def setUp(self):
        # Establish a fresh connection before each test
        self.conn = sqlite3.connect('simple_crud.db')
        self.cursor = self.conn.cursor()

        # Membersihkan semua data sebelum setiap tes
        users = read_users()
        for user in users:
            delete_user(user[0])

    def test_create_user(self):
        create_user("John", 25)
        users = read_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], "John")
        self.assertEqual(users[0][2], 25)

    def test_update_user(self):
        create_user("Jane", 28)
        users = read_users()
        user_id = users[0][0]
        update_user(user_id, "Jane Doe", 29)
        updated_users = read_users()
        self.assertEqual(updated_users[0][1], "Jane Doe")
        self.assertEqual(updated_users[0][2], 29)

    def test_delete_user(self):
        create_user("Mike", 35)
        users = read_users()
        self.assertEqual(len(users), 1)
        delete_user(users[0][0])
        users_after_delete = read_users()
        self.assertEqual(len(users_after_delete), 0)

    def tearDown(self):
        # Tutup koneksi setelah semua tes selesai
        self.conn.close()

if __name__ == "__main__":
    unittest.main()
