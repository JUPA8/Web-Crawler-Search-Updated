import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime
from collections import defaultdict

class Crawler:
    def __init__(self, start_url, max_pages=100, max_depth=3):
        """
        Initialize the crawler.
        Args:
            start_url (str): The starting URL for the crawl.
            max_pages (int): Maximum number of pages to crawl.
            max_depth (int): Maximum crawl depth.
        """
        self.start_url = start_url
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.visited_urls = set()
        self.index = defaultdict(list)
        self.base_domain = urlparse(start_url).netloc
        self.stats = {"pages_crawled": 0, "errors": 0, "skipped": 0}

    def is_valid_url(self, url):
        """
        Check if URL belongs to the same domain and is HTML.
        """
        parsed = urlparse(url)
        return (
            parsed.netloc == self.base_domain and
            parsed.scheme in ['http', 'https']
        )

    def extract_metadata(self, html, url):
        """
        Extract metadata like title, snippet, and domain from HTML.
        """
        soup = BeautifulSoup(html, 'html.parser')

        # Extract title
        title = soup.title.string.strip() if soup.title else "No Title"

        # Extract snippet
        text = soup.get_text(separator=" ", strip=True)
        snippet = text[:150] + "..." if len(text) > 150 else text

        # Domain and date
        domain = urlparse(url).netloc
        date = datetime.now().strftime('%Y-%m-%d')

        return title, snippet, domain, date

    def extract_links(self, html, base_url):
        """
        Extract all valid links from the page.
        """
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for link in soup.find_all('a', href=True):
            href = urljoin(base_url, link['href'])
            if self.is_valid_url(href):
                links.append(href)
        return links

    def crawl(self):
        """
        Start crawling from the start URL.
        """
        urls_to_visit = [(self.start_url, 0)]  # (URL, depth)

        while urls_to_visit and self.stats["pages_crawled"] < self.max_pages:
            url, depth = urls_to_visit.pop(0)

            if depth > self.max_depth or url in self.visited_urls:
                self.stats["skipped"] += 1
                continue

            try:
                response = requests.get(url, timeout=5)
                if 'text/html' not in response.headers.get('Content-Type', ''):
                    self.stats["skipped"] += 1
                    continue

                self.visited_urls.add(url)
                self.stats["pages_crawled"] += 1

                title, snippet, domain, date = self.extract_metadata(response.text, url)

                # Add to the index
                self.index[title].append({
                    "url": url,
                    "title": title,
                    "snippet": snippet,
                    "domain": domain,
                    "date": date
                })

                # Extract and queue new links
                links = self.extract_links(response.text, url)
                for link in links:
                    if link not in self.visited_urls:
                        urls_to_visit.append((link, depth + 1))

            except Exception as e:
                self.stats["errors"] += 1
                print(f"Error crawling {url}: {e}")

    def get_stats(self):
        """
        Return crawl statistics.
        """
        return self.stats
