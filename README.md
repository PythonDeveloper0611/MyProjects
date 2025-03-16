# Web Scraping & Data Extraction

## Project Description
This project demonstrates how to scrape Amazon product details (title, price, reviews, availability) using Selenium and BeautifulSoup. It includes implementing CAPTCHA solving techniques and automated login with cookies. The extracted data is stored in an SQLite database for analysis.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup4
- SQLite (built-in with Python)

## Setup
1. Install the required Python packages:
```bash
pip install selenium beautifulsoup4
```

2. Download and install the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)).

3. Update the `config.py` file with your Amazon login details.

## Usage
Run the `scraper.py` script to start scraping and storing the data in the SQLite database:
```bash
python scraper.py
```

## Files
- `config.py`: Configuration file containing Amazon login credentials.
- `scraper.py`: Main script to perform web scraping and store data in the SQLite database.
- `analyze_data.py`: Script to analyze and visualize the scraped data.
- `export_data.py`: Script to export the scraped data to a CSV file.
- `app.py`: Simple Flask web dashboard to display the scraped data.

## Example Usage
### Analyzing and Visualizing Data
Run the `analyze_data.py` script to analyze and visualize the data:
```bash
python analyze_data.py
```

### Exporting Data to CSV
Run the `export_data.py` script to export the data to a CSV file:
```bash
python export_data.py
```

### Running the Flask Web Dashboard
Run the `app.py` script to start the Flask web dashboard:
```bash
python app.py
```

Access the web dashboard at `http://127.0.0.1:5000/`.