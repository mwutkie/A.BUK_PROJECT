from api_betfan import *
from api_fuksiarz import *
from api_totalbet import *
from api_etoto import *
from api_betclick import *
from api_forbet import *
def merge():
    etoto=api_url='https://api.etoto.pl/rest/market/categories/multi/847/events'
    totalbet=api_url='https://totalbet.pl/rest/market/categories/multi/7226/events'
    fuksiarz=api_url='https://fuksiarz.pl/rest/market/categories/multi/236/events'
    betfan=api_url='https://api-v2.betfan.pl/api/v1/market/categories/264/events?date=&hours='
    betclick=api_url='https://offer.cdn.begmedia.com/api/pub/v3/competitions/'+'5'+'?application=2048&countrycode=pl&forceCompetitionInfo=true&language=pa&markettypeId=1365&sitecode=plpa'
    forbet=api_url='https://www.iforbet.pl/rest/market/categories/multi/29994/events?gamesClass=major'


    df_list=[etoto_scraper(etoto),fuksiarz_scraper(fuksiarz),totalbet_scraper(totalbet),betfan_scraper(betfan),api_betclick_scraper(betclick),forbet_scraper(forbet)]
    columns_suffix_list=['etoto','fuksiarz','totalbet','betfan','betclick','forbet']
    for i in range(len(columns_suffix_list)):
        if i==0:
            master_df=df_list[i]
            continue
        master_df=master_df.merge(df_list[i],how='outer'
                                  ,left_on=['datetime_'+columns_suffix_list[i-1],'gospodarze_name_'+columns_suffix_list[i-1],'typ_'+columns_suffix_list[i-1],'liga_'+columns_suffix_list[i-1]],
                                  right_on=['datetime_'+columns_suffix_list[i],'gospodarze_name_'+columns_suffix_list[i],'typ_'+columns_suffix_list[i],'liga_'+columns_suffix_list[i]])

    master_df=find_highest(master_df,'remis_odds')
    master_df=find_highest(master_df,'gospodarze_odds')
    master_df=find_highest(master_df,'goscie_odds')

    return master_df






