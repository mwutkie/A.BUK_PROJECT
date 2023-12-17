import pandas as pd 
from merge import *
df=merge()

df['stake']=100
df['total']= (1/df['top_remis_odds'])+(1/df['top_gospodarze_odds'])+(1/df['top_goscie_odds'])
df['prob1']=(1 / df['top_remis_odds']) / df['total']
df['prob2']=(1 / df['top_gospodarze_odds']) / df['total']
df['prob3']=(1 / df['top_goscie_odds']) / df['total']
df['in_stake1']=df['stake']*df['prob1']
df['in_stake2']=df['stake']*df['prob2']
df['in_stake3']=df['stake']*df['prob3']
df['adj_in_stake1']=df['in_stake1']-(df['in_stake1']*0.12)
df['adj_in_stake2']=df['in_stake2']-(df['in_stake2']*0.12)
df['adj_in_stake3']=df['in_stake3']-(df['in_stake3']*0.12)
df['profit']=df['adj_in_stake3']*df['top_goscie_odds']



