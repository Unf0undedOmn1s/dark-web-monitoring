import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

import sqlite3

def store_result(title, description, keyword):
    conn = sqlite3.connect("darkweb_results.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO alerts (title, description, keyword) VALUES (?, ?, ?)", 
                   (title, description, keyword))

    conn.commit()
    conn.close()

def scan_keywords_and_store(data, keywords):
    for record in data:
        title = record[1]
        description = record[2]

        for keyword in keywords:
            if keyword.lower() in title.lower() or keyword.lower() in description.lower():
                print(f"Found keyword: {keyword}")
                
                # Store result in SQLite
                store_result(title, description, keyword)

    print("Scan complete and results stored.")

def scan_keywords_and_notify(data, keywords):
    for record in data:
        title = record[1]
        description = record[2]

        for keyword in keywords:
            if keyword.lower() in title.lower() or keyword.lower() in description.lower():
                print(f"Found keyword: {keyword}")
                
                # Notify (you can implement your notification logic here)
                logging.info(f"Notification: Found keyword '{keyword}' in title '{title}' or description '{description}'")

    print("Scan complete and notifications sent.")