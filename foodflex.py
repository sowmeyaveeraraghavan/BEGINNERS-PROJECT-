import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the database and user table
def create_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY, 
                    password TEXT)''')
    conn.commit()
    conn.close()

# Function for user registration
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            register_window.destroy()  # Close registration window after successful registration
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        conn.close()
    else:
        messagebox.showerror("Error", "Both fields are required.")

# Function to handle user login
def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()
    if username and password:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        if user:
            messagebox.showinfo("Success", f"Welcome {username}!")
            login_window.destroy()  # Close login window on successful login
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        conn.close()
    else:
        messagebox.showerror("Error", "Both fields are required.")

# Registration window
def register_window():
    global entry_username, entry_password
    register_win = tk.Toplevel()
    register_win.title("Register")
    register_win.geometry("350x300")
    register_win.config(bg="#F5F5F5")

    # Title label
    tk.Label(register_win, text="Register", font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#333").pack(pady=20)

    # Username label and entry
    tk.Label(register_win, text="Username", font=("Arial", 12), bg="#F5F5F5", fg="#333").pack(pady=5)
    entry_username = tk.Entry(register_win, font=("Arial", 12), width=30)
    entry_username.pack(pady=5)

    # Password label and entry
    tk.Label(register_win, text="Password", font=("Arial", 12), bg="#F5F5F5", fg="#333").pack(pady=5)
    entry_password = tk.Entry(register_win, font=("Arial", 12), width=30, show="*")
    entry_password.pack(pady=5)

    # Register button
    tk.Button(register_win, text="Register", font=("Arial", 12), width=20, height=2, bg="#4CAF50", fg="white", command=register_user).pack(pady=20)

# Login window
def login_window():
    global entry_login_username, entry_login_password
    global login_win

    login_win = tk.Toplevel()
    login_win.title("Login")
    login_win.geometry("350x300")
    login_win.config(bg="#F5F5F5")

    # Title label
    tk.Label(login_win, text="Login", font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#333").pack(pady=20)

    # Username label and entry
    tk.Label(login_win, text="Username", font=("Arial", 12), bg="#F5F5F5", fg="#333").pack(pady=5)
    entry_login_username = tk.Entry(login_win, font=("Arial", 12), width=30)
    entry_login_username.pack(pady=5)

    # Password label and entry
    tk.Label(login_win, text="Password", font=("Arial", 12), bg="#F5F5F5", fg="#333").pack(pady=5)
    entry_login_password = tk.Entry(login_win, font=("Arial", 12), width=30, show="*")
    entry_login_password.pack(pady=5)

    # Login button
    tk.Button(login_win, text="Login", font=("Arial", 12), width=20, height=2, bg="#4CAF50", fg="white", command=login_user).pack(pady=20)

# Main window with buttons to login and register
def main_window():
    window = tk.Tk()
    window.title("Main Window")
    window.geometry("350x250")
    window.config(bg="#F5F5F5")

    # Title label
    tk.Label(window, text="Welcome to the App", font=("Arial", 18, "bold"), bg="#F5F5F5", fg="#333").pack(pady=20)

    # Login button
    tk.Button(window, text="Login", font=("Arial", 12), width=20, height=2, bg="#4CAF50", fg="white", command=login_window).pack(pady=10)

    # Register button
    tk.Button(window, text="Register", font=("Arial", 12), width=20, height=2, bg="#FF9800", fg="white", command=register_window).pack(pady=10)

    window.mainloop()

# Create the database and table when the app starts
create_db()

# Start the main window
main_window()
