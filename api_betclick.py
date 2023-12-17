import requests
import pandas as pd
from utils import *

api_url='https://offer.cdn.begmedia.com/api/pub/v3/competitions/221?application=2048&countrycode=pl&forceCompetitionInfo=true&language=pa&markettypeId=1365&sitecode=plpa'
        #https://offer.cdn.begmedia.com/api/pub/v3/competitions/3?application=2048&countrycode=pl&forceCompetitionInfo=true&language=pa&markettypeId=1365&sitecode=plpa

def adjust(input_df):
    input_df=input_df.replace('Werder','Werder Brema')
    return input_df



def api_betclick_scraper(api_url):
    datetime_list=[]
    gospodarze_name_list=[]
    gospodarze_odds_list=[]
    remis_name_list=[]
    remis_odds_list=[]
    goscie_name_list=[]
    goscie_odds_list=[]
    competition=None
    response = requests.get(api_url)
    if response.status_code == 200:
        response=response.json() 
    else:
        print(f"Error: {response.status_code}")
    hehe=response['matches']
    for i in range(len(hehe)): 
       
        for key,value in hehe[i].items():
            if competition==None:
                competition=hehe[i]['competition']['name']
            

            if key=='date':
                datetime=value
                datetime_list.append(datetime)
            if key=='grouped_markets':
                for key2,value2 in value[0].items():
                    if key2=='markets':
                        for i in value2:
                            
                            for key3,value3 in i.items():
                                typ=i['name']
                                if key3=='selections':
                                    gospodarze=value3[0]
                                    remis=value3[1]
                                    goscie=value3[2]
                                
                                    gospodarze=gospodarze[0]
                                    goscie=goscie[0]
                                    remis=remis[0]
            
                                    gospodarze_name=gospodarze['name']
                                    gospodarze_odds=gospodarze['odds']
                                    remis_name='Remis'
                                    remis_odds=remis['odds']
                                    goscie_name=goscie['name']
                                    goscie_odds=goscie['odds']

                                    gospodarze_name_list.append(gospodarze_name)
                                    gospodarze_odds_list.append(gospodarze_odds)
                                    remis_name_list.append(remis_name)
                                    remis_odds_list.append(remis_odds)
                                    goscie_name_list.append(goscie_name)
                                    goscie_odds_list.append(goscie_odds)
    typ='1X2'
    master_df=raw_to_df_betclick(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
              typ,datetime_list,competition
              ,'betclick')
    master_df=adjust(master_df)
    return master_df

