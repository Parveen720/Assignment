import sqlite3
import hashlib
import getpass  # For hiding password input

# Connect to DB


conn = sqlite3.connect("exam2.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    login_status INTEGER DEFAULT 0
)
""")
conn.commit()

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Register user
def register():
    username = input("Enter new username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("User already registered. Please choose a different username.")
        return

    try:
        password = getpass.getpass("Enter password: ").strip()
    except Exception:
        print("Error reading password input. Try running in a proper terminal.")
        return

    if not password:
        print("Password cannot be empty.")
        return

    hashed = hash_password(password)

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    print("Registration successful.")


# Login user
def login():
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()
    hashed = hash_password(password)

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if not row:
        print("User not found.")
        return

    stored_pass = row[0]

    if hashed == stored_pass:
        # Force logout all users before logging in new user
        cursor.execute("UPDATE users SET login_status = 0")
        cursor.execute("UPDATE users SET login_status = 1 WHERE username = ?", (username,))
        conn.commit()
        print(f"Login successful. Welcome, {username}! (All other users logged out.)")
    else:
        print("Incorrect password.")


# Logout user
def logout():
    username = input("Enter username to logout: ").strip()
    cursor.execute("SELECT login_status FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if not row:
        print("User not found.")
        return

    if row[0] == 0:
        print("User is already logged out.")
        return

    cursor.execute("UPDATE users SET login_status = 0 WHERE username = ?", (username,))
    conn.commit()
    print(f"{username} logged out.")


def logout1(username):
    cursor.execute("UPDATE users SET login_status = 0 WHERE username = ?", (username,))
    conn.commit()
    print(f"{username} logged out successfully.")


# Change password
def change_password():
    username = input("Enter your username: ").strip()
    cursor.execute("SELECT password, login_status FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    if not row:
        print("User not found.")
        return

    current_hash, status = row

    if status == 0:
        print("User must be logged in to change password.")
        return

    current_input = getpass.getpass("Enter current password: ").strip()
    if hash_password(current_input) != current_hash:
        print("Incorrect current password.")
        return

    new_pass = getpass.getpass("Enter new password: ").strip()
    confirm_pass = getpass.getpass("Confirm new password: ").strip()

    if new_pass != confirm_pass:
        print("Passwords do not match.")
        return

    new_hash = hash_password(new_pass)
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_hash, username))
    conn.commit()
    print("Password changed successfully.")
    logout1(username)

# --- Menu ---
while True:
    print("\n--- USER PORTAL ---")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Change Password")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        logout()
    elif choice == "4":
        change_password()
    elif choice == "5":
        cursor.execute("UPDATE users SET login_status = 0")
        conn.commit()
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Close DB
conn.close()
