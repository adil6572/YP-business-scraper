# Yellow Pages Scraper

Yellow Pages Scraper: A Python tool to extract business information from Yellow Pages, offering command-line and Streamlit interfaces for seamless data retrieval."

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line](#command-line)
  - [Streamlit Interface](#streamlit-interface)
  - [Examples](#examples)
- [Options](#options)
- [Output Format](#output-format)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script allows you to scrape business data from Yellow Pages. It provides both command-line and Streamlit interface options for ease of use.

## Features

- Scrape business data based on search terms and geographical location.
- Choose starting page number for scraping.
- Save the scraped data to a CSV file.
- Streamlit interface for interactive usage.

## Installation

Clone the repository:

```bash
git clone https://github.com/adil6572/YP-business-scraper.git
cd YP-business-scraper
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line

Run the scraper from the command line using the following syntax:

```bash
python CLI-interface.py "search terms" "location terms" --start_page 2 --filename output.csv
```

Replace `"search terms"`, `"location terms"`, and `output.csv` with your desired parameters.

### Streamlit Interface

Run the Streamlit interface:

```bash
streamlit run GUI-interface.py
```

Visit the provided URL in your web browser to use the interactive interface.

### Examples

Run the scraper from the command line:

```bash
python CLI-interface.py "roofing" "Ravenswood, Chicago, IL" --start_page 2 --filename roofing.csv
```

Run the Streamlit interface:

```bash
streamlit run GUI-interface.py
```

## Options

- `search_terms`: Search terms for scraping (required).
- `geo_location_terms`: Geographical location terms for scraping (required).
- `--start_page`: Start page number for scraping (default: 1).
- `--filename`: CSV filename for output (default: business_data.csv).

## Output Format

The scraped data is saved to a CSV file with the following columns:

- `Rank`
- `Business Name`
- `Phone Number`
- `Business Page`
- `Website`
- `Category`
- `Rating`
- `Street Name`
- `Locality`
- `Region`
- `Zipcode`

## Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please follow these guidelines:

1. **Fork the Repository:** Fork the project on GitHub and clone your fork.

2. **Create a New Branch:** Create a new branch for your contribution using a descriptive name. For example:

   ```bash
   git checkout -b feature/new-feature
   ```

3. **Make Changes:** Make your changes or additions to the code.

4. **Commit Changes:** Commit your changes with a clear and concise commit message.

   ```bash
   git commit -m "Add new feature"
   ```

5. **Push Changes:** Push your changes to your fork on GitHub.

   ```bash
   git push origin feature/new-feature
   ```

6. **Create a Pull Request:** Open a pull request on the main repository. Provide a clear title and description of your changes.

### Reporting Issues

If you encounter any issues or have suggestions, please [create an issue](https://github.com/adil6572/YP-business-scraper/issues) on GitHub. When reporting issues, please include:

- A clear and descriptive title.
- A detailed description of the issue, including steps to reproduce.
- The version of the software you are using.
- Any relevant error messages or screenshots.

We appreciate your help in improving this project!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Happy Scraping! 🌟

Thank you for exploring our Yellow Pages Scraper. We hope you find it useful and enjoyable! If you have any feedback, suggestions, or just want to say hello, feel free to [reach out](mailto:adilshaikh6572@gmail.com).

Happy scraping and have a fantastic day! 🚀✨
