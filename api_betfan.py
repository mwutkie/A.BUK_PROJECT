api_url='https://api-v2.betfan.pl/api/v1/market/categories/294/events?date=&hours='
from utils import *
import requests
import pandas as pd
import json
def betfan_scraper(api_url):
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

    response=response['data']
    response=response['categories']
    response=response[0]
    response=response['events']
    for part in response:
        datetime_list.append(part['eventStart'])
        competition=part['categoryName']
        data=part['games']
        data=data[0]
        typ=data['gameName']
        data2=data['outcomes']
        for part2 in data2:
            if part2==data2[0]:
                gospodarze_name=part2['outcomeName']
                gospodarze_odds=part2['outcomeOdds']
                gospodarze_name_list.append(gospodarze_name)
                gospodarze_odds_list.append(gospodarze_odds)
            if part2==data2[1]:
                remis_name='remis'
                remis_odds=part2['outcomeOdds']
                remis_name_list.append(remis_name)
                remis_odds_list.append(remis_odds)
            if part2==data2[2]:
                goscie_name=part2['outcomeName']
                goscie_odds=part2['outcomeOdds']    
                goscie_name_list.append(goscie_name)
                goscie_odds_list.append(goscie_odds)
    typ='1X2'
    df=raw_to_df(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
              typ,datetime_list,competition
              ,'betfan')
    return df



