#https://production-superbet-offer-pl.freetls.fastly.net/v2/pl-PL/events/by-date?offerState=prematch&startDate=2023-12-16+17:35:00&endDate=2024-12-17+08:00:00

api_url='https://production-superbet-offer-pl.freetls.fastly.net/v2/pl-PL/events/by-date?offerState=prematch&startDate=2023-12-16+17:35:00&endDate=2024-12-17+08:00:00'
import requests
import pandas as pd
import json
def superbet_scraper(api_url):


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")
    data1=response['data']
    for data2 in data1:
        date_dt=data2['matchDate']
        game=data2['matchName']
        print(game)
        data3=data2['odds']

        if data3==None: 
            continue
        if len(data3)!=3:
            continue
    
        data4=data3[0]
        gospodarze_name=data4['info']
        gospodarze_odds=data4['price']
        data4=data3[1]
        remis_name='remis'
        remis_odds=data4['price']
        data4=data3[2]
        goscie_name=data4['info']
        goscie_odds=data4['price']
      
    return response

superbet_scraper(api_url)