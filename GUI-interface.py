import streamlit as st
from yellow_page_scraper import YellowPageScraper


def main():
    st.title('Yellow Page Listing Scraper')
    st.markdown("🌐[Yellow Page website](https://www.yellowpages.com/)")
    st.image('yp-website.png')

    search_terms = st.text_input('Enter search terms:')
    geo_location_terms = st.text_input('Enter geo location terms:')
    start_page = st.number_input('Enter start page number:', value=1)
    filename = st.text_input('Enter CSV filename (without extension):')
    filename = f'{filename}.csv'

    if st.button('Scrape Data'):
        with st.spinner('Scraping data...'):
            scraper = YellowPageScraper(
                search_terms, geo_location_terms, start_page, filename)
            scraper.scrape_all_pages()
        st.success('Scraping completed successfully!')

        # Show the number of pages scraped
        st.write(
            f'Number of pages scraped: {scraper.current_page - start_page}')

        # Provide a button to download the CSV file
        st.write('Download CSV File:')

        with open(filename, "rb") as file:
            btn = st.download_button(
                label="Download csv",
                data=file,
                file_name=filename,
                mime='text/csv'
            )


if __name__ == '__main__':
    main()
