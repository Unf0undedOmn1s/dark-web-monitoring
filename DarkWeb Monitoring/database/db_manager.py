# db_manager.py
import sqlite3
from datetime import datetime

# Create the database and the results table if they don't exist
def create_database():
    conn = sqlite3.connect('darkweb_monitor.db')
    c = conn.cursor()
    
    # Create the 'results' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY, 
                  title TEXT, 
                  description TEXT, 
                  keyword TEXT, 
                  timestamp TEXT)''')
    
    conn.commit()
    conn.close()
    print("Database and table created successfully.")

# Insert a record into the 'results' table
def insert_data(title, description, keyword, timestamp):
    conn = sqlite3.connect('darkweb_monitor.db')
    c = conn.cursor()

    # Insert the data into the table
    c.execute('''INSERT INTO results (title, description, keyword, timestamp)
                 VALUES (?, ?, ?, ?)''', (title, description, keyword, timestamp))
    
    conn.commit()
    conn.close()
    print(f"Data inserted: {title}, {description}, {keyword}, {timestamp}")

# Fetch all the data from the 'results' table
def fetch_data():
    conn = sqlite3.connect('darkweb_monitor.db')
    c = conn.cursor()

    # Fetch all records from the table
    c.execute('SELECT * FROM results')
    rows = c.fetchall()
    
    # Print each row (or you could return it for further processing)
    for row in rows:
        print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Keyword: {row[3]}, Timestamp: {row[4]}")
    
    conn.close()

# Example usage:
# Uncomment to test
# create_database()
# insert_data('Test Title', 'Test Description', 'Test Keyword', str(datetime.now()))
# fetch_data()
