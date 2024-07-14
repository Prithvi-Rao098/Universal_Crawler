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
def format_data(data, fields):
    load_dotenv

    #integrate OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # set the fields
    if fields == None:
        format_data(data, get_fields())

    # define the system message: this will give the chat bot spefic commands to be able to get the correct inforamtion
    system_message = f"Your task is to convert structured information from the given text and convert it into a pure JSON format. The JSON file should only contain
                       stuctured data extracted from the text, with no additional commentary, explainations, or extraneous informatin.
                       You could encounter cases where you cant find the data of the fields provided or the data will be in a different language. In the case 
                       of no relevent data, just output a JSON with no information. In the case of the differnt langauage, please proccess the text and provide an 
                       output in pure JSON format with no words before or after the JSON."
    
    # define the statement to extract the correct information
    inquiry_message = f"Extract the following information from the provided text: \n this is the provided content: {data} \n \n This is the information you need to extract: {fields}" 

    #CREATE THE CHAT RESPONSE
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-1106"
        response_format={"type": "json_obect"},
        messages=[
            # define the role of OpenAI
            {
                "role": "system",
                "content": system_message
            },
            # define the inquiry
            {
                "role": "user",
                "content": inquiry_message
            }
        ]
    )

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
        timestamp = datetime.now().strftime('%Y%:m:%d_%H:%M:%S')     # year, month _ hour, mintute second


        raw_data = scrape_data(url)    # scrape the url for the raw data 

        #save the data from the scape

        save_data(raw_data, timestamp)

        #fomat the data usinf OpenAI
        #format_data()       ## GOTTA FINISH THIS

        # THEN SAVE THE DATA, DONT HAVE THIS YET
    
    except Exception as e:
        print(f"there is an error: {e}")


