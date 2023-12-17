
api_url='https://www.iforbet.pl/rest/market/categories/multi/29994/events?gamesClass=major'
import requests
import pandas as pd
import json
from utils import *

def forbet_scraper(api_url):
    datetime_list=[]
    gospodarze_name_list=[]
    gospodarze_odds_list=[]
    remis_name_list=[]
    remis_odds_list=[]
    goscie_name_list=[]
    goscie_odds_list=[]


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")

    data=response['data'] #each element of data list == match
    for match in data:
        competition=match['category3Name']
        datetime_list.append(match['eventStart'])
        data2=match['eventGames']
        data2=data2[0]
        typ=data2['gameName']
        data2=data2['outcomes']
        for result in data2:
            
            if result==data2[0]:
                gospodarze_name=result['outcomeName']
                gospodarze_odds=result['outcomeOdds']
                gospodarze_name_list.append(gospodarze_name)
                gospodarze_odds_list.append(gospodarze_odds)
            if result==data2[1]:
                remis_name='Remis'
                remis_odds=result['outcomeOdds']
                remis_name_list.append(remis_name)
                remis_odds_list.append(remis_odds)
            if result==data2[2]:
                goscie_name=result['outcomeName']
                goscie_odds=result['outcomeOdds']
                goscie_name_list.append(goscie_name)
                goscie_odds_list.append(goscie_odds)                
    df=raw_to_df(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
            typ,datetime_list,competition
            ,'forbet')
    return df

