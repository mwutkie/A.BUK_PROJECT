import pandas as pd 

df=pd.DataFrame({'bet1':[1.2,3.4,3.5],'bet2':[7.2,2.4,4.5],'bet3':[2.2,3.4,8.5]})
df['stake']=100
df['total']= (1/df['bet1'])+(1/df['bet2'])+(1/df['bet3'])
df['prob1']=(1 / df['bet1']) / df['total']
df['prob2']=(1 / df['bet2']) / df['total']
df['prob3']=(1 / df['bet3']) / df['total']
df['in_stake1']=df['stake']*df['prob1']
df['in_stake2']=df['stake']*df['prob2']
df['in_stake3']=df['stake']*df['prob3']
df['adj_in_stake1']=df['in_stake1']-(df['in_stake1']*0.12)
df['adj_in_stake2']=df['in_stake2']-(df['in_stake2']*0.12)
df['adj_in_stake3']=df['in_stake3']-(df['in_stake3']*0.12)
df['in_profit1']=df['adj_in_stake1']*df['bet1']-df['stake']
print(df)