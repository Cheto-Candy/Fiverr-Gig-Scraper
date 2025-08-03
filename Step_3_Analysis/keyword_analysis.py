"""
Step 3: Keyword Frequency Analysis
----------------------------------
Analyzes the titles from CSV data extracted previously.
Determines the frequency of each keyword appearing across gig titles.

Required Libraries:
- pandas (Data analysis)

Input Directory: output_csv/
Output Directory: analysis_results/
"""


import pandas as pd
import os


def load_keywords(file_name): 
    """
    Load keywords from a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file containing keywords.

    Returns:
    pd.DataFrame: A DataFrame containing the keywords.
    """
    keywords_count = {}
    titles=pd.read_csv(file_name)
    # print(f"Loaded {len(titles)} keywords from {file_name}")
    # git full titles column
    title_col= titles['title'].tolist()
    # print(title_col[0])
    for title in title_col:
        title = title.lower()  # Convert to lowercase
        title = title.strip()
        # Remove punctuation
        title = title.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
        # Split the title into keywords
        keywords = title.split(' ')
        for keyword in keywords:
            keyword = keyword.strip() # Remove any leading/trailing whitespace
            print(f"Processing keyword: {keyword}")
            if keyword in keywords_count.keys() :
                keywords_count[keyword] += 1
            else:
                keywords_count.update({keyword: 1})
           
    os.makedirs('Step_3_Analysis/output_csv', exist_ok=True)  # Create directory if it doesn't exist
    # Create a DataFrame from the keywords count dictionary
    df= pd.DataFrame(list(keywords_count.items()), columns=['keyword', 'count'])
    df.sort_values(by='count', ascending=False, inplace=True)
    df.to_csv('Step_3_Analysis/output_csv/keywords_GP.csv', index=False)
    print(f"Keywords saved to keywords.csv with {len(df)} unique keywords.")

load_keywords("Step_2_Cleaning/output_csv/gigs_GP.csv")