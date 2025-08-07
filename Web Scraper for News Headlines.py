#!/usr/bin/env python3
"""
News Headlines Web Scraper
Scrapes top headlines from a news website and saves them to a text file.
"""

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os

class NewsHeadlineScraper:
    def __init__(self):
        # Headers to mimic a real browser request
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def scrape_bbc_news(self):
        """Scrape headlines from BBC News"""
        url = "https://www.bbc.com/news"
        headlines = []
        
        try:
            print(f"Fetching headlines from {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # BBC uses various selectors for headlines
            selectors = [
                'h2[data-testid="card-headline"]',  # Main story cards
                'h3[data-testid="card-headline"]',  # Secondary stories
                'h2.sc-4fedabc7-3',                # Alternative selector
                'h3.sc-4fedabc7-3'                 # Alternative selector
            ]
            
            for selector in selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    if headline and len(headline) > 10 and headline not in headlines:
                        headlines.append(headline)
            
            print(f"Found {len(headlines)} headlines from BBC News")
            return headlines
            
        except requests.RequestException as e:
            print(f"Error fetching BBC News: {e}")
            return []

    def scrape_reuters(self):
        """Scrape headlines from Reuters"""
        url = "https://www.reuters.com"
        headlines = []
        
        try:
            print(f"Fetching headlines from {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Reuters headline selectors
            selectors = [
                'a[data-testid="Heading"]',
                'h2 a',
                'h3 a',
                '.story-title a'
            ]
            
            for selector in selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    if headline and len(headline) > 10 and headline not in headlines:
                        headlines.append(headline)
            
            print(f"Found {len(headlines)} headlines from Reuters")
            return headlines
            
        except requests.RequestException as e:
            print(f"Error fetching Reuters: {e}")
            return []

    def scrape_hacker_news(self):
        """Scrape headlines from Hacker News (more reliable for testing)"""
        url = "https://news.ycombinator.com"
        headlines = []
        
        try:
            print(f"Fetching headlines from {url}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Hacker News uses consistent structure
            title_links = soup.select('span.titleline > a')
            
            for link in title_links:
                headline = link.get_text(strip=True)
                if headline and headline not in headlines:
                    headlines.append(headline)
            
            print(f"Found {len(headlines)} headlines from Hacker News")
            return headlines
            
        except requests.RequestException as e:
            print(f"Error fetching Hacker News: {e}")
            return []

    def scrape_generic_news_site(self, url, site_name="News Site"):
        """Generic scraper for news websites"""
        headlines = []
        
        try:
            print(f"Fetching headlines from {site_name}...")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Common headline selectors used by news sites
            common_selectors = [
                'h1', 'h2', 'h3',
                '.headline', '.title', '.story-title',
                'article h1', 'article h2', 'article h3',
                '[class*="headline"]', '[class*="title"]'
            ]
            
            for selector in common_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    # Filter out very short or very long text that might not be headlines
                    if headline and 10 <= len(headline) <= 200 and headline not in headlines:
                        headlines.append(headline)
            
            # Remove duplicates while preserving order
            headlines = list(dict.fromkeys(headlines))
            print(f"Found {len(headlines)} headlines from {site_name}")
            return headlines
            
        except requests.RequestException as e:
            print(f"Error fetching {site_name}: {e}")
            return []

    def save_headlines_to_file(self, headlines, filename=None):
        """Save headlines to a text file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_headlines_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"News Headlines - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
                
                for i, headline in enumerate(headlines, 1):
                    f.write(f"{i:3d}. {headline}\n")
                
                f.write(f"\nTotal Headlines: {len(headlines)}\n")
            
            print(f"Headlines saved to: {filename}")
            return filename
            
        except IOError as e:
            print(f"Error saving file: {e}")
            return None

    def run_scraper(self):
        """Main method to run the scraper"""
        print("Starting News Headlines Scraper...")
        print("-" * 40)
        
        all_headlines = []
        
        # Scrape from multiple sources
        sources = [
            ("Hacker News", self.scrape_hacker_news),
            ("BBC News", self.scrape_bbc_news),
            ("Reuters", self.scrape_reuters)
        ]
        
        for source_name, scraper_func in sources:
            headlines = scraper_func()
            if headlines:
                all_headlines.extend([(headline, source_name) for headline in headlines])
            time.sleep(1)  # Be respectful with requests
        
        if all_headlines:
            # Format headlines with source information
            formatted_headlines = [f"{headline} [{source}]" for headline, source in all_headlines]
            
            print(f"\nTotal headlines collected: {len(formatted_headlines)}")
            
            # Save to file
            filename = self.save_headlines_to_file(formatted_headlines)
            
            # Display first 10 headlines
            print("\nFirst 10 headlines:")
            print("-" * 30)
            for i, headline in enumerate(formatted_headlines[:10], 1):
                print(f"{i:2d}. {headline}")
            
            if len(formatted_headlines) > 10:
                print(f"... and {len(formatted_headlines) - 10} more headlines")
            
            return filename
        else:
            print("No headlines were collected.")
            return None

def main():
    """Main function to demonstrate the scraper"""
    scraper = NewsHeadlineScraper()
    
    # Option 1: Run the full scraper
    scraper.run_scraper()
    
    # Option 2: Scrape a specific site
    print("\n" + "=" * 50)
    print("Scraping specific site example:")
    
    # Example with a specific URL
    custom_headlines = scraper.scrape_generic_news_site(
        "https://news.ycombinator.com", 
        "Hacker News Custom"
    )
    
    if custom_headlines:
        custom_filename = scraper.save_headlines_to_file(
            custom_headlines, 
            "custom_headlines.txt"
        )

if __name__ == "__main__":
    main()