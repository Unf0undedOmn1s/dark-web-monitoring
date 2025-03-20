import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database.db_manager import create_database, insert_data, fetch_data

# Defining the list of target URLs to scrape
TARGET_URLS = [
    "http://darkwebcrawling.com", "http://darkwebcrawling.com/page2",
    "http://darkwebcrawling.com/page3", "http://darkwebcrawling.com/page4",
    "http://darkwebcrawling.com/page5",
]

# Keywords to search for
KEYWORDS = [
    "darknet marketplace", "hacking tools", "exploit database", "ransomware attack",
]

# Function to scrape the content from the URL
def scrape_url(url):
    try:
        # Sending a request to the URL
        response = requests.get(url, proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"})
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parsing the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting title and description
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', {'name': 'description'})
        description = description['content'] if description else 'No description found'

        # Checking for any matching keywords
        matched_keywords = [keyword for keyword in KEYWORDS if keyword.lower() in (title + description).lower()]

        # Store the data in the database
        timestamp = str(datetime.now())
        insert_data(title, description, ', '.join(matched_keywords), timestamp)

        print("URL: {}".format(url))
        print("Title: {}".format(title))
        print("Description: {}".format(description))
        print("Keywords found: {}".format(', '.join(matched_keywords) if matched_keywords else 'N/A'))
        print("Timestamp: {}".format(timestamp))
        print("-" * 50)

    except requests.exceptions.RequestException as e:
        print("Error fetching {}: {}".format(url, e))

# Main function to run the scan
def run_scan():
    create_database()  # Ensure database and table are created
    for url in TARGET_URLS:
        print("Scanning: %s" % url)
        scrape_url(url)
    print("Scan complete and results stored.")

# Function to display the fetched data 
def display_results():
    fetch_data()

# Run the scan when this script is executed
if __name__ == "__main__":
    run_scan()
    display_results()
