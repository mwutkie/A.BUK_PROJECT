
api_url='https://www.iforbet.pl/rest/market/categories/multi/29994/events?gamesClass=major'
import requests
import pandas as pd
import json
def totalbet_scraper(api_url):


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")

    data=response['data'] #each element of data list == match
    for match in data:
        competition=match['category3Name']
        time_dt=match['eventStart']
        data2=match['eventGames']
        data2=data2[0]
        typ=data2['gameName']
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
                print(goscie_odds)
    return response

totalbet_scraper(api_url)

