import pandas as pd
import yfinance as yf
import json
import datetime as dt

#stocks = ["JNJ", "GOOG"]
#Get 52WeekHigh and 52WeekLow using yfinance API
def Get52WeekStockData(stocks):
    data1 = pd.DataFrame(columns=['stock', 'fiftytwoweekhigh', 'fiftytwoweeklow'])
    for stock in stocks:
        stock_object = yf.Ticker(stock)
        print(stock_object)
        # get stock info
        print(stock_object.info)
        fiftytwoweekhigh  = stock_object.info['fiftyTwoWeekHigh']
        fiftytwoweeklow = stock_object.info['fiftyTwoWeekLow']
        data1 = data1.append({'stock': stock, 'fiftytwoweekhigh': fiftytwoweekhigh, 'fiftytwoweeklow': fiftytwoweeklow}, ignore_index=True)
    print(data1)
    return data1

##################################################
## Prepare data records to be pushed into file.

def prepare52WeekData(file, data1):
    stockdata = []
    i = 0
    df = pd.read_json(file, orient='split', compression = 'infer')
    for index, row in df.iterrows():
        print(row['index'])
        print(row['stock'])
        date_and_time = dt.datetime.fromtimestamp(int(row['index'])/1000).strftime('%Y-%m-%d %H:%M:%S')
        #fiftytwoweekhigh = data1.loc[data1['stock'] == row['stock']]['fiftytwoweekhigh'].values
        fiftytwoweekhigh = data1[data1['stock'] == row['stock']].loc[:, 'fiftytwoweekhigh'].values[0]
        fiftytwoweeklow = data1[data1['stock'] == row['stock']].loc[:, 'fiftytwoweeklow'].values[0]
        to_append = {'stock': row['stock'], 'timestamp': date_and_time, 'stockvalue': str(row['Close']), 'fiftytwoweekhigh': str(fiftytwoweekhigh), 'fiftytwoweeklow': str(fiftytwoweeklow)}
        stockdata.append(to_append)
        print(f'to_append is \n {to_append}')
        i = i + 1
    #Data = pd.merge_asof(df_stockdata_dict, data1, on="stock")
    #Data = json.dumps(stockdata)
    return stockdata

    #print(stockdata[0])
    #print sample json record