import pandas as pd

def SaveToJsonFile(df_list):
    # storing/reading/displaying the data in JSON format
    df1 = pd.concat(df_list, ignore_index= 'true')
    #print(df1)
    df1.to_json('stocks.json', orient = 'split', compression = 'infer', index = 'true')
    df = pd.read_json('stocks.json', orient='split', compression = 'infer')
    print(f'data in stocks.json file \n {df}')
    return df