import pandas as pd

def raw_to_df(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
              typ,datetime_dt,competition
              ,buk):
    export_df=pd.DataFrame()

    export_df['gospodarze_name_'+buk]=gospodarze_name_list
    export_df['gospodarze_odds_'+buk]=gospodarze_odds_list
    export_df['remis_name_'+buk]=remis_name_list
    export_df['remis_odds_'+buk]=remis_odds_list
    export_df['goscie_name_'+buk]=goscie_name_list
    export_df['goscie_odds_'+buk]=goscie_odds_list
    export_df['typ_'+buk]=typ
    export_df['datetime_'+buk]=datetime_dt
    export_df['datetime_'+buk] = pd.to_datetime(export_df['datetime_'+buk], unit='ms', utc=True).dt.date
    export_df['liga_'+buk]=competition

    export_df['remis_odds_'+buk]=pd.to_numeric(export_df['remis_odds_'+buk])

    return export_df

def raw_to_df_betclick(gospodarze_name_list,gospodarze_odds_list,remis_name_list,remis_odds_list,goscie_name_list,goscie_odds_list,
              typ,datetime_dt,competition
              ,buk):
    export_df=pd.DataFrame()

    export_df['gospodarze_name_'+buk]=gospodarze_name_list
    export_df['gospodarze_odds_'+buk]=gospodarze_odds_list
    export_df['remis_name_'+buk]=remis_name_list
    export_df['remis_odds_'+buk]=remis_odds_list
    export_df['goscie_name_'+buk]=goscie_name_list
    export_df['goscie_odds_'+buk]=goscie_odds_list
    export_df['typ_'+buk]=typ
    export_df['datetime_'+buk]=datetime_dt
    export_df['datetime_'+buk] = pd.to_datetime(export_df['datetime_'+buk]).dt.date
    export_df['liga_'+buk]=competition

    export_df['remis_odds_'+buk]=pd.to_numeric(export_df['remis_odds_'+buk])

    return export_df


def find_highest(df,identifier):
# Filter columns that include "hehe" in their names
    hehe_columns = [col for col in df.columns if identifier in col]
    print(hehe_columns)
    # Define a function to get both the max value and column name
    def max_value_and_column(row):
        hehe_values = pd.to_numeric(row[hehe_columns], errors='coerce')  # Convert to numeric

        max_col = hehe_values.idxmax()
        max_val = row[max_col]
        print(max_val)
        print(max_col)
        return pd.Series({'top_'+identifier: max_val, 'top_buk': max_col})

    # Apply the function row-wise and concatenate the result to the DataFrame
    
    result_df = pd.concat([df, df.apply(max_value_and_column, axis=1)], axis=1)


    return result_df

