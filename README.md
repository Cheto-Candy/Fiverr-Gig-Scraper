 🚀 Fiverr Gig Scraper & Keyword Analyzer

This Python-based project automates the process of scraping Fiverr gig details and performing keyword analysis from gig titles.

---

 📌 Overview

The project is divided into three clear steps:

 1. Web Scraping (`scrape_gigs.py`)
- Searches Fiverr gigs based on provided keywords.
- Saves each gig's HTML content into separate HTML files.

 2. Data Extraction & Cleaning (`clean_gigs_data.py`)
- Parses saved HTML files to extract structured information:
  - Gig Title
  - Gig URL
  - Seller Level
  - Rating
  - Price
- Outputs this data into a CSV file.

3.Keyword Frequency Analysis (`keyword_analysis.py`)
- Analyzes extracted gig titles from CSV.
- Counts the frequency of each keyword appearing in gig titles.
- Exports keyword frequency data into a separate CSV file.

---

 🛠️ Tech Stack

- Python
- BeautifulSoup
- Pandas
- Requests
- Undetected Chromedriver

---

 📂 Project Structure

