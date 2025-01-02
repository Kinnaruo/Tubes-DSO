from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

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

@app.route('/')
def home():
    conn = get_db_connection()
    users = read_users(conn)
    close_connection(conn)
    return render_template('home.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    conn = get_db_connection()
    create_user(conn, name, age)
    close_connection(conn)
    return jsonify({"message": "User added successfully!"})

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user_route(user_id):
    new_name = request.form['name']
    new_age = request.form['age']
    conn = get_db_connection()
    update_user(conn, user_id, new_name, new_age)
    close_connection(conn)
    return jsonify({"message": "User updated successfully!"})

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    conn = get_db_connection()
    delete_user(conn, user_id)
    close_connection(conn)
    return jsonify({"message": "User deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
