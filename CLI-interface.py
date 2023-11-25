
import argparse
from yellow_page_scraper import YellowPageScraper


def main():
    parser = argparse.ArgumentParser(description='Yello Page Listing Scraper')
    parser.add_argument('search_terms', type=str,
                        help='Search terms for scraping')
    parser.add_argument('geo_location_terms', type=str,
                        help='Geographical location terms for scraping')
    parser.add_argument('--start_page', type=int, default=1,
                        help='Start page number (default: 1)')
    parser.add_argument('--filename', type=str, default='business_data.csv',
                        help='CSV filename (default: business_data.csv)')

    args = parser.parse_args()

    scraper = YellowPageScraper(
        args.search_terms, args.geo_location_terms, args.start_page, args.filename)
    scraper.scrape_all_pages()


if __name__ == '__main__':
    main()
