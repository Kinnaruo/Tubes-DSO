import sqlite3

# Fungsi untuk membuat dan mengembalikan koneksi baru
def get_db_connection():
    conn = sqlite3.connect('simple_crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Fungsi untuk membuat pengguna
def create_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

# Fungsi untuk membaca semua pengguna
def read_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Fungsi untuk memperbarui data pengguna
def update_user(conn, user_id, new_name, new_age):
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (new_name, new_age, user_id))
    conn.commit()

# Fungsi untuk menghapus pengguna
def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

# Fungsi untuk menutup koneksi
def close_connection(conn):
    conn.close()

# Jika ingin menguji, gunakan contoh di bawah ini
if __name__ == "__main__":
    conn = get_db_connection()
    create_user(conn, "Alice", 30)
    print(read_users(conn))
    update_user(conn, 1, "Alice Updated", 31)
    print(read_users(conn))
    delete_user(conn, 1)
    print(read_users(conn))
    close_connection(conn)
