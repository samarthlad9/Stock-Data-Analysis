import datetime as dt
import StockDataAcquisition
import SaveToJson
import FiftyTwoWeekStockData

# Our goal is to get per-hour stock price data for a time range for identified stocks.
# Further, calling the static info api for the stocks to get their current 52WeekHigh and 52WeekLow values.
# Storing stock information (stockid, price, price timestamp, 52WeekHigh and 52WeekLow values) in a json file for further analysis

#Stocks to be considered for this excercise 
stocks = ["JNJ", "GOOG"]

#Getting per-hour stock price data for specified duration i.e. 5days
df_list = StockDataAcquisition.GetStockData(stocks, "5d", "1h")

#Storing fetched stock information to json file for further analysis
df = SaveToJson.SaveToJsonFile(df_list)

#Getting 52Week Stock data of the specified stocks
data1 = FiftyTwoWeekStockData.Get52WeekStockData(stocks)

#Preparing 52Week Stock data of the specified stocks
stockdata = FiftyTwoWeekStockData.prepare52WeekData('stocks.json', data1)

#Displaying/printing consolidated Stock data (closing price and 52weekhigh-low values)
print(stockdata[0])

#print sample json record