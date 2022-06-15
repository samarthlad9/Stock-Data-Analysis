# Stock-Data-Analysis
To get stock data from google/Yahoo Finance API. The application provides near real time / historical stock data and provide alerts.
import json
#import sys
import yfinance as yf
import datetime as dt
import pandas as pd

# Our goal is to get per-hour stock price data for a time range for identified stocks.
# Further, calling the static info api for the stocks to get their current 52WeekHigh and 52WeekLow values.
# Crafting individual data records with information about the stockid, price, price timestamp, 52WeekHigh and 52WeekLow values and storing it in file

#stocks = ["MSFT", "MVIS", "GOOG", "SPOT", "INO", "OCGN", "ABML", "RLLCF", "JNJ", "PSFE"]
stocks = ["JNJ","GOOG"]
today = dt.date.today()
yesterday = dt.date.today() - dt.timedelta(1)
print (yesterday)
## Code to pull the specified duration data for the identified stocks using yfinance API
df_list = list()
i = 0
for stock in stocks:
    print(i)
    data = pd.DataFrame()
    print(stocks[i])
    #data = yf.download(stock, start= yesterday, end= today, interval = '1h' )
    data = yf.download(tickers=stocks[i], period="5d",interval="1h",group_by='ticker',auto_adjust=True,prepost=True)
    print(data)
    data.reset_index(level=0, inplace=True)
    data.insert(1, "stock", stocks[i])
    print(type(data))
    df_list.append(data)
    i =i+1
    ###################################################
#print("writing into csv file")
#df.to_csv('stocks.csv', encoding='utf-8', index = True)
