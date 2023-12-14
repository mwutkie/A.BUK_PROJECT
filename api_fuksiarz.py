
api_url='https://fuksiarz.pl/rest/market/categories/multi/319/events'
import requests
import pandas as pd


def fuksiarz_scraper(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")
    data=response['data'] #each element of data list == match
    for match in data:
        competition=match['category3Name']
        data2=match['eventGames']
        data2=data2[0]
        data2=data2['outcomes']
        for result in data2:
            
            if result==data2[0]:
                gospodarze_name=result['outcomeName']
                gospodarze_odds=result['outcomeOdds']
            if result==data2[1]:
                remis_name='remis'
                remis_odds=result['outcomeOdds']
            if result==data2[2]:
                goscie_name=result['outcomeName']
                goscie_odds=result['outcomeOdds']
fuksiarz_scraper(api_url)