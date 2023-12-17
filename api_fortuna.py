import requests
from bs4 import BeautifulSoup
import pandas as pd
# Replace 'your_url_here' with the URL of the website you want to scrape
url = 'https://www.efortuna.pl/zaklady-bukmacherskie/pilka-nozna/ekstraklasa-polska'

def stanarisation_fortuna(input_df):
    input_df=input_df.replace('ekstraklasa-polska','Ekstraklasa')
    return input_df


def scraper_fortuna(url):
    dict_start={

        'teamy':[],
        'gospodarze_ods_fortuna':[],
        'remis_odds_fortuna':[],
        'goscie_ods_fortuna':[],
    }

    master_df=pd.DataFrame(dict_start)
    # Send an HTTP request to the URL
    response = requests.get(url)
    name=url.split('/')
    name=name[-1]
    print(name)
    odds_list=[]
    match_lis=[]
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        market_name_spans = soup.find_all('span', class_='market-name')
        matches_list=[]
        for market_name_span in market_name_spans:
            string=market_name_span.text
            modified_string = string.replace('\n', '')
            matches_list.append(modified_string)


        col_odds_td_elements = soup.find_all('td', class_='col-odds')
        temp_odds=[]
        for col_odds_td in col_odds_td_elements:
            string=col_odds_td.text
            modified_string = string.replace('\n', '')
            temp_odds.append(modified_string)

        sublists = [temp_odds[i:i+6] for i in range(0, len(temp_odds), 6)]




        sublists=sublists[3:23] # do wywalenia
        true_list=[]
        for i in range(len(sublists)):
            temp_list=[]
            temp_list.append(matches_list[i])
            for ele in sublists[i]:
                temp_list.append(ele)
            true_list.append(temp_list)
        
        modified_list = [inner_list[:4] for inner_list in true_list]
        for small_list in modified_list:
            master_df = master_df.append(pd.Series(small_list, index=master_df.columns), ignore_index=True)
        temp_data=master_df['teamy'].str.split(' - ',expand=True)
        temp_data.columns=['gospodarze_name_fortuna','goscie_name_fortuna']
        master_df=pd.concat([master_df,temp_data],axis=1)
        master_df['liga_fortuna']=name
        master_df['typ_fortuna']='1X2'
        master_df['remis_name_fortuna']='Remis'
        del master_df['teamy']
        master_df=stanarisation_fortuna(master_df)
        return master_df


        





    


