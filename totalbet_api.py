api_url='https://totalbet.pl/rest/market/categories/multi/7485/events'
import requests
import pandas as pd
import json
def sts_scraper(api_url):


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")

    print(response)
    return response

sts_scraper(api_url)

