# main.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from database.db_manager import create_database, insert_data, fetch_data

# Defining the list of target URLs to scrape
TARGET_URLS = [
    "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/",
    "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
    "http://g66ol3eb5ujdckzqqfmjsbpdjufmjd5nsgdipvxmsh7rckzlhywlzlqd.onion/",
    "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/",
    "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page"]

# Keywords to search for
KEYWORDS=[
    "darknet marketplace", "hacking tools", "exploit database", "ransomware attack", 
    "data breach tool", "stolen credentials", "credit card theft", "password cracking", 
    "trojan", "backdoor access", "stealth malware", "DDoS for hire", "fraudulent services", 
    "fake bank accounts", "unlicensed pharmaceuticals", "money mule", "blackhat", 
    "exploit kits", "malicious scripts", "cybercriminals", "fraudulent tax returns", 
    "crypto theft", "illegal bitcoins", "stolen data sales", "data anonymization", 
    "private keys", "counterfeit documents", "hacker forums", "web shell", "cybersecurity breach", 
    "malicious payload", "false advertising", "dark web forums", "illegal streaming", "fake reviews", 
    "DDoS-as-a-service", "infected links", "unethical hacking", "identity spoofing", "fake diplomas", 
    "smuggling route", "illegal animal trade", "cloned apps", "data extraction", "vpn for dark web", 
    "software piracy", "SIM card cloning", "bot farms", "deep web hacking", "IP spoofing", "trojan virus", 
    "underground hacking", "keylogger", "data for sale", "black web", "VPN bypass", "spam email list", 
    "traffic diversion", "trojan horse", "email harvesting", "bounty programs", "cyber espionage", 
    "darknet marketplace links", "government data leaks", "insider threats", "cyber surveillance", 
    "encrypted messaging", "hidden wiki", "illegal auction", "mugshot extortion", "fake charities", 
    "money laundering site", "phishing kit", "cracked software", "fileless malware", "web scraping tool", 
    "password dumps", "DOX", "botnet controller", "cloning hardware", "underground chat rooms", 
    "hidden services", "hoax", "anonymous browsing", "illegal downloads", "flood attack", 
    "fake social media accounts", "credential stuffing", "drug smuggling", "ransomware victim", 
    "cyber blackmail", "man-in-the-middle", "fake charity donations", "steganography", "password reuse", 
    "dark net hacking", "SQL injection", "APT attack", "Phantom bot", "decryption tools", 
    "network penetration testing", "scamming software", "botnet operators", "fraudulent insurance", 
    "digital extortion", "RAT malware", "deceptive marketing", "false advertisement", "online fraud", 
    "hacked content", "carding forum", "spyware", "C&C server", "webshells", "underground forums"
]

# Function to scrape the content from the URL
def scrape_url(url):
    try:
        # Send a request to the URL
        response = requests.get(url, proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"})
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title and description (example)
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', {'name': 'description'})
        description = description['content'] if description else 'No description found'

        # Check for any matching keywords
        matched_keywords = [keyword for keyword in KEYWORDS if keyword.lower() in (title + description).lower()]

        # Store the data in the database
        timestamp = str(datetime.now())
        insert_data(title, description, ', '.join(matched_keywords), timestamp)

        # Print the results
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Keywords found: {', '.join(matched_keywords) if matched_keywords else 'N/A'}")
        print(f"Timestamp: {timestamp}")
        print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Main function to run the scan
def run_scan():
    create_database()  # Ensure database and table are created
    for url in TARGET_URLS:
        print(f"Scanning: {url}")
        scrape_url(url)
    print("Scan complete and results stored.")

# Function to display the fetched data (optional)
def display_results():
    fetch_data()

# Run the scan when this script is executed
if __name__ == "__main__":
    run_scan()  # Start scanning
    display_results()  # Optionally display the results after the scan
