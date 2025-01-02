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

def close_connection():
    conn.close()

# Function to take manual input
def input_user():
    print("Choose an option:")
    print("1. Create User")
    print("2. Read Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        create_user(name, age)
        print(f"User {name} added successfully.")
    
    elif choice == "2":
        users = read_users()
        print("Current Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    
    elif choice == "3":
        user_id = int(input("Enter user ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        update_user(user_id, new_name, new_age)
        print(f"User ID {user_id} updated successfully.")
    
    elif choice == "4":
        user_id = int(input("Enter user ID to delete: "))
        delete_user(user_id)
        print(f"User ID {user_id} deleted successfully.")
    
    elif choice == "5":
        close_connection()
        print("Exiting program.")
        return False
    
    else:
        print("Invalid choice. Please try again.")
    
    return True

if __name__ == "__main__":
    while True:
        if not input_user():
            break
