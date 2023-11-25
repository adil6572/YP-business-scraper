import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode, quote_plus
import math
import argparse


class YellowPageScraper:

    def __init__(self, search_terms, geo_location_terms, start_page=1, file_path='business_data.csv'):
        self.search_terms = search_terms
        self.geo_location_terms = geo_location_terms
        self.start_page = start_page
        self.file_path = file_path
        self.base_url = 'https://www.yellowpages.com'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.yellowpages.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

        self.current_page = start_page
        self.max_page = 1

    def extract_business_listing(self, card):
        # Extracting attributes
        rank = card.select_one('.info-primary h2')
        rank = rank.text.strip().split('. ')[0] if rank else ''

        business_name = card.select_one('.business-name span')
        business_name = business_name.text.strip() if business_name else ''

        phone_number = card.select_one('.phones')
        phone_number = phone_number.text.strip() if phone_number else ''

        business_page = card.select_one('.business-name')
        business_page = self.base_url + \
            business_page['href'] if business_page else ''

        website = card.select_one(".track-visit-website")
        website = website['href'] if website else ''

        category = card.select('.categories a')
        category = ', '.join(a.text.strip()
                             for a in category) if category else ''

        rating = card.select_one('.ratings .count')
        rating = rating.text.strip('()') if rating else ''

        street_name = card.select_one('.street-address')
        street_name = street_name.text.strip() if street_name else ''

        locality = card.select_one('.locality')
        locality = locality.text.strip() if locality else ''

        if locality:
            locality, region = locality.split(
                ",") if ',' in locality else (locality, '')
            region, zipcode = region.strip().split() if ' ' in region.strip() else ('', '')
        else:
            locality, region, zipcode = '', '', ''

        business_info = {
            "Rank": rank,
            "Business Name": business_name,
            "Phone Number": phone_number,
            "Business Page": business_page,
            "Website": website,
            "Category": category,
            "Rating": rating,
            "Street Name": street_name,
            "Locality": locality,
            "Region": region,
            'Zipcode': zipcode
        }

        return business_info
        # Your existing extract_business_info function

    def save_to_csv(self, data_list):
        fieldnames = ["Rank", "Business Name", "Phone Number", "Business Page",
                      "Website", "Category", "Rating", "Street Name", "Locality", "Region", "Zipcode"]

        # Check if the file exists
        file_exists = False
        try:
            with open(self.file_path, 'r', encoding='utf-8'):
                file_exists = True
        except FileNotFoundError:
            pass

        with open(self.file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if the file is new
            if not file_exists:
                writer.writeheader()

            # Write data
            writer.writerows(data_list)

    def parse_page(self, content):
        soup = BeautifulSoup(content, "html.parser")
        all_cards = soup.select(".organic .srp-listing")
        result_count = soup.select_one('.showing-count')
        result_count = int(result_count.text.strip().split(
            ' ')[-1]) if result_count else 0

        # print('Result count:', result_count)
        self.max_page = math.ceil(result_count/30)
        # print('Max page:', self.max_page)
        data_list = []

        if all_cards:
            for item in all_cards:
                result = self.extract_business_listing(item)
                data_list.append(result)

            # Save data to CSV
            self.save_to_csv(data_list)

    def fetch_html_content(self, page):
        params = {
            'search_terms': self.search_terms,
            'geo_location_terms': self.geo_location_terms,
            'page': page
        }

        url = 'https://www.yellowpages.com/search?' + \
            urlencode(params, quote_via=quote_plus)
        for _ in range(5):
            response = requests.get(url, verify=False, headers=self.headers)
            if response.status_code == 200:
                return response.content
        return None

    def scrape_all_pages(self):
        self.current_page = self.start_page
        while self.current_page <= self.max_page:
            print(f'Scraping data for page {self.current_page}')

            html_content = self.fetch_html_content(self.current_page)
            if html_content is None:
                print("No html content for page {self.current_page}")
            else:
                self.parse_page(html_content)
                print(f'Page {self.current_page} scraped successfully.')
                self.current_page += 1

