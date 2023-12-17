api_url='https://offer.lvbet.pl/client-api/v4/matches/competition-view/?lang=pl&sports_groups_ids=37425'
import requests
import pandas as pd
import json
def lvbet_scraper(api_url):


    response = requests.get(api_url,)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")
    date_data=response['matches']
    date_data=date_data[0]
    date=date_data['date']


    data=response['primary_column_markets']

    for data2 in data:

        typ=data2['name']
        if typ=='Zwycięzca meczu':
            data3=data2['selections']
            
            for  data4 in data3:
                
                if data4==data3[0]:    
                    gospodarze_name=data4['name']
                    gospodarze_odds=data4['rate']
                    gospodarze_odds=gospodarze_odds['decimal']
                if data4==data3[1]:
              
                    remis_name='remis'
                    remis_odds=data4['rate']
                    remis_odds=remis_odds['decimal']
                if data4==data3[2]:
          
                    goscie_name=data4['name']
                    goscie_odds=data4['rate']
                    goscie_odds=goscie_odds['decimal']




lvbet_scraper(api_url)