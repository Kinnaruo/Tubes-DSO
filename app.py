import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

# Koneksi ke database SQLite
def get_db_connection():
    conn = sqlite3.connect('simple_crud.db')
    conn.row_factory = sqlite3.Row  # For easier access to rows as dictionaries
    return conn

# Membuat tabel jika belum ada
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# CRUD Functions
def create_user(name, age):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()

def read_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(user_id, new_name, new_age):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (new_name, new_age, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

# Routes for web UI
@app.route('/')
def index():
    users = read_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        create_user(name, age)
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()
    conn.close()

    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        update_user(id, name, age)
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    delete_user(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()  # Create the table if not exists
    app.run(debug=True)
