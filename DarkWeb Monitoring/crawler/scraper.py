import requests
from bs4 import BeautifulSoup
from alerts import store_result

def fetch_onion_page(url):
    # Fetches a .onion page using a Tor proxy.
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_titles(content):
    soup = BeautifulSoup(content, 'html.parser')
    titles = [h1.text.strip() for h1 in soup.find_all('h1')]
    return titles

def extract_links(content):
    # Extracts all valid HTTP/HTTPS links from the page.
    soup = BeautifulSoup(content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("http")]
    return links

def scrape_and_store(url):
    content = fetch_onion_page(url)
    if content:
        titles = extract_titles(content)
        for title in titles:
            store_result(title, "Title extracted from page", "N/A")
        links = extract_links(content)
        for link in links:
            store_result(link, "Link extracted from page", "N/A")