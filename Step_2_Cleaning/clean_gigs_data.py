"""
Step 2: Gig Data Cleaning and Extraction
----------------------------------------
Processes HTML files saved by the scraper and extracts relevant data:
- Gig Title
- Gig URL
- Price
- Seller Level
- Rating

Required Libraries:
- BeautifulSoup (HTML Parsing)
- pandas (Data handling)

Input Directory: gigs_html/
Output Directory: output_csv/
"""


from bs4 import BeautifulSoup
import os
import pandas as pd
def clean_html(file_path):
    """
    Cleans the HTML content by removing all HTML tags and returning plain text.
    
    Args:
        html_content (str): The HTML content to be cleaned.
        
    Returns:
        str: The cleaned text without any HTML tags.
    """
    # check the numer of gigs in the directory
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return
    if not os.path.isdir(file_path):
        print(f"The path {file_path} is not a directory.")
        return
    
    df={'title':[], 'rating': [], 'level': [], 'price': [], 'link': []}
    # Assuming the file_path is a directory, count the number of gigs
    gigs = os.listdir(file_path)
    print(f"Number of gigs in the directory: {len(gigs)}")
    for gig in gigs:
        print(f"Processing gig: {gig}")
        with open(os.path.join(file_path, gig), 'r', encoding='utf-8') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            # find by elements with calss
            title = soup.find('p', class_='f2YMuU6').get_text()
            title = title.replace('\n', '').replace('  ', '')
            # print(f"Cleaned text for {title}:")
            link ="https://www.fiverr.com/"+ soup.find('a').get('href')
            # print(link)
            price = soup.find('span', class_='text-bold co-grey-1200').find('span').text
            price = price.replace('\n', '').replace(' ', '')
            # print(f"Price: {price}")
            try:
                level = soup.find('p', class_='_1qwbi7a2').text
                level = level.replace('\n', '').replace('  ', '')
                # print(f"Level: {type(level)}")
            except AttributeError:
                level = "N/A"
            try:
                rating = f"{soup.find('strong','rating-score').text}/{soup.find('span','rating-count-number').text}"
                rating = rating.replace('\n', '').replace(' ', '')
                # print(f"Rating: {rating}")
            except AttributeError:
                rating = "N/A"
            df['title'].append(title)
            df['rating'].append(rating)
            df['level'].append(level)
            df['price'].append(price)
            df['link'].append(link)
            # print(df)
            # df.to_csv('gigs.csv', index=False)
            # print(f"Level: {level}")
    os.makedirs('Step_2_Cleaning/output_csv', exist_ok=True)  # Create directory if it doesn't exist
    df = pd.DataFrame(df)
    df.to_csv('Step_2_Cleaning/output_csv/gigs_GP.csv', index=False)
    print("Data cleaned and saved to gigs.csv")
    



file_path = "Step_1_Scraping/gigs_html"

clean_html(file_path)