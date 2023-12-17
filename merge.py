from api_betfan import *
from api_fuksiarz import *
from api_totalbet import *
from api_etoto import *
from api_betclick import *
from api_forbet import *
def merge():
    etoto=api_url=''
    totalbet=api_url=''
    fuksiarz=api_url=''
    betfan=api_url=''
    betclick=api_url=''
    forbet=api_url=''


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






