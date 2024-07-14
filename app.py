from firecrawl import FirecrawlApp
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import pandas as ad
from datetime import datetime

# scrape the raw data from the url
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

# format the data and use the GPT AI to analyze
#ef format_data(data, fields = none):
    #load_dotenv

    #integrate OpenAI client
    #client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


#def save_data_formatted():
    p#rint("save the data from the OpenAI analysis")

# get the data fields that need to be analyzed 
def get_fields():
    fields = []
    done = False
    field_n = 1

    while not done:
        fields.append(input(f"please enter field {field_n} that you would like to analyze: "))
        
        field_n += 1

        #check to see if the use is done with inputting fields
        user_done = input("if you are done inputting fields please type exit or just click enter to contiue: ")
        if user_done.lower() == 'exit':
            done = True
        


    print(f"there are your fields: {fields}")
           

if __name__  == "__main__":

    #get the url from the user to scrape
    url = input("What url would you like to scrape")

    #get the fields that you would like to extract from the urls
    fields = get_fields()

    try:
        #generate time stamp to save the data
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')     # year, month _ hour, mintute second


        raw_data = scrape_data(url)    # scrape the url for the raw data 

        #save the data from the scape
        save_data(raw_data, timestamp)

        #fomat the data usinf OpenAI
        #format_data()       ## GOTTA FINISH THIS

        # THEN SAVE THE DATA, DONT HAVE THIS YET
    
    except Exception as e:
        print(f"there is an error: {e}")


