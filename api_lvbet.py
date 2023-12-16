api_url='https://offer.lvbet.pl/client-api/v4/matches/competition-view/?lang=pl&sports_groups_ids=37425'
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