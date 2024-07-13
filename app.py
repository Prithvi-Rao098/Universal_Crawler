from firecrawl import FirecrawlApp
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import pandas as ad
import datetime


def scrape_data(url):
    load_dotenv()

    # Intialize FireCrawler
    app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))
    
    # scrape the url
    scrape_data = app.scrape_url(url)

    # make sure the data has a 'markdown' key
    if 'markdown' in scrape_data:
        return scrape_data['markdown']
    else:
        raise KeyError("the url does not have scraped down data that can be marked down")

# saving the data
def save_data(raw_data, timestamp, output_folder = 'outputs'):
    output_path = os.path.join(output_folder, f'raw_Data_{timestamp}.md')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(raw_data)

    print(f"the data from the website is saved to {output_path}")           