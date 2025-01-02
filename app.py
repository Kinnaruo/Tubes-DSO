
import sqlite3

# Koneksi ke database SQLite
conn = sqlite3.connect('simple_crud.db')
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

def read_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def update_user(user_id, new_name, new_age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (new_name, new_age, user_id))
    conn.commit()

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

# Jangan lupa menutup koneksi setelah selesai
def close_connection():
    conn.close()

# Jika ingin menguji fungsi langsung, gunakan yang di bawah ini
if __name__ == "__main__":
    # Contoh penggunaan
    create_user("Alice", 30)
    print(read_users())
    update_user(1, "Alice Updated", 31)
    print(read_users())
    delete_user(1)
    print(read_users())
