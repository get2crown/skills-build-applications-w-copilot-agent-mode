import sqlite3

try:
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Print the table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
