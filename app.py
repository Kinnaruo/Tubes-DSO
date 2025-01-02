import tkinter as tk
from tkinter import messagebox
import os
import json

# Path to the JSON file to store the registration data
DATA_FILE = "registrations.json"

# Check if the data file exists, if not, create an empty file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def create_user(name, email):
    data = load_data()
    data.append({"name": name, "email": email})
    save_data(data)
    messagebox.showinfo("Success", "User registered successfully")

def read_users():
    return load_data()

def update_user(old_email, new_name, new_email):
    data = load_data()
    for user in data:
        if user['email'] == old_email:
            user['name'] = new_name
            user['email'] = new_email
            save_data(data)
            messagebox.showinfo("Success", "User updated successfully")
            return
    messagebox.showwarning("Not Found", "User not found")

def delete_user(email):
    data = load_data()
    data = [user for user in data if user['email'] != email]
    save_data(data)
    messagebox.showinfo("Success", "User deleted successfully")

def show_users():
    data = load_data()
    user_list = "\n".join([f"Name: {user['name']}, Email: {user['email']}" for user in data])
    messagebox.showinfo("Registered Users", user_list)

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        create_user(name, email)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

def update_form():
    old_email = email_entry.get()
    new_name = name_entry.get()
    new_email = email_entry.get()
    if new_name and new_email:
        update_user(old_email, new_name, new_email)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def delete_form():
    email = email_entry.get()
    if email:
        delete_user(email)
    else:
        messagebox.showwarning("Input Error", "Please enter the email of the user to delete.")

# Set up the main UI
app = tk.Tk()
app.title("Registration App")

name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

email_label = tk.Label(app, text="Email:")
email_label.grid(row=1, column=0)

email_entry = tk.Entry(app)
email_entry.grid(row=1, column=1)

submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=2, column=0)

update_button = tk.Button(app, text="Update", command=update_form)
update_button.grid(row=2, column=1)

delete_button = tk.Button(app, text="Delete", command=delete_form)
delete_button.grid(row=3, column=0)

show_button = tk.Button(app, text="Show Users", command=show_users)
show_button.grid(row=3, column=1)

app.mainloop()
