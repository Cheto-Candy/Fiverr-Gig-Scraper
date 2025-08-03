"""
Step 1: Fiverr Gig Scraper
--------------------------
This script scrapes Fiverr gig cards based on multiple search keywords.
Each gig's HTML content is saved into separate HTML files for further data extraction.

Required Libraries:
- undetected_chromedriver (Bypass bot detection)
- BeautifulSoup (HTML Parsing)
- time (Page loading delays)

Output Directory: gigs_html/
"""


import time
from bs4 import BeautifulSoup
import pandas as pd
import os

URL="https://www.fiverr.com/search/gigs?query=python%20automation%20script"




import undetected_chromedriver as uc

def open_fiverr():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36")
    
    driver = uc.Chrome(options=options)
    return driver


def get_html(driver,keyword):
    keyword = keyword.replace(' ','%20')  # URL encode the keyword
    driver.get(f'https://www.fiverr.com/search/gigs?query={keyword}')
    time.sleep(5)  # Wait for the page to load
    html = driver.page_source
    return html

def parse_html(count,Keywords):
    driver = open_fiverr()
    for keyword in Keywords:
        html = get_html(driver, keyword)
        time.sleep(2)
        # save in csv file 
        soup = BeautifulSoup(html, 'html.parser')

        gigs = soup.find_all('div', class_='gig-card-layout')
        if not gigs:
            print("No gigs found. Please check the keyword or the page structure.")
            continue
        
        number_of_gigs = len(gigs)
        print(f"Number of gigs found: {number_of_gigs}")

        os.makedirs('Step_1_Scraping/gigs_html', exist_ok=True)  # Create directory if it doesn't exist
        for gig in gigs:
            # Save each gig's HTML content to a file
            with open(f'Step_1_Scraping/gigs_html/fiverr{count}.html', 'w', encoding='utf-8') as file:
                file.write(gig.prettify())
            count += 1



keywords = ["guest posting service",
"high da guest post",
"guest posting da 90",
"guest post backlinks",
"manual guest posting",
"guest post outreach",
"white hat guest posting",
"guest post link building",
"do follow guest post",
"seo guest posting",
"high authority guest posting",
"guest blogging service",
"guest post on high authority sites",
"da 90 guest posting",
"guest post submission",
"high da backlinks",
"authority backlink building",
"guest post website ranking",
"high quality guest post",
"guest post sites list"
]
count = 1
parse_html(count, keywords)    