import os
import django
import sqlite3
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

try:
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Create a new user
    username = 'testuser'
    password = make_password('password')
    email = 'testuser@example.com'

    # Insert the new user into the auth_user table
    cursor.execute("INSERT INTO auth_user (username, password, email, is_superuser, is_staff, is_active, date_joined) VALUES (?, ?, ?, 0, 0, 1, CURRENT_TIMESTAMP)", (username, password, email))
    conn.commit()

    print(f"User '{username}' created successfully.")

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
