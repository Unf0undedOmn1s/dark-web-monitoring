import sqlite3
import os

DATABASE_NAME = 'darkweb_monitoring.db'
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

# Function to create the database and table
def create_database():
    # Check if database exists, if not create it
    if not os.path.exists(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        create_table(cursor)
        
        conn.commit()
        conn.close()

# Function to create the table if it doesn't exist
def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        description TEXT,
                        keywords TEXT,
                        timestamp TEXT)''')

# Function to insert data into the table
def insert_data(title, description, keywords, timestamp):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO results (title, description, keywords, timestamp)
                      VALUES (?, ?, ?, ?)''', (title, description, keywords, timestamp))
    
    conn.commit()
    conn.close()

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Keywords: {row[3]}, Timestamp: {row[4]}")
    
    conn.close()
