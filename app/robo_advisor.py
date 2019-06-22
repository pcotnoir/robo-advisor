# app/robo_advisor.py

#imports

import time
import requests
import json
import csv
import os
from dotenv import load_dotenv
load_dotenv()

#functions

def moneyformat(price):
    return '${:,.2f}'.format(price) 

    #URLs: adapted from https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# while True:
#     try:
#         api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#         stock_symbol = input("Please input the stock ticker you would like information on: ")
#         url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
#         user_input = requests.get(url)
#         parsed_response = json.loads(user_input.text)
#         last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#     except KeyError:
#         print("You entered the ticker incorrectly. Expecting a properly-formed stock symbol like 'MSFT'. Please try again: ")
#         continue
#     else:
#         break


while True:
    try:
        api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
        stock_symbol = input("Please input the stock ticker you would like information on: ")
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
        user_input = requests.get(url)
        parsed_response = json.loads(user_input.text)
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    except KeyError:
            if len(stock_symbol) >=5:
                print("You entered the ticker incorrectly with too many characters. Expecting a properly-formed stock symbol like 'MSFT'. Please try again: ")
                continue
            elif not stock_symbol.isalpha():
                print("You entered the ticker incorrectly with a number. Expecting a properly-formed stock symbol like 'MSFT'. Please try again: ")
                continue
    else:
        break


   # api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
   # while True:
   #     stock_symbol = input("Please input the stock ticker you would like information on: ")
   #     if not stock_symbol.isalpha():
   #         print("You entered the ticker incorrectly. Please try again: ")
   #     else:
   #         url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
   #         user_input = requests.get(url)
   #         #user_input = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}")
   #         if "Error" in user_input.text:
   #             print("You entered the ticker incorrectly. Please try again: ")
   #         else:
   #             break

#stock_symbol = "MSFT" #TO DO: accept user input

#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
#response = requests.get(url)

#print(response.status_code) #> 200
#print(type(response)) #> <class 'requests.models.Response'>
#print(response.text)

#Info Inputs

parsed_response = json.loads(user_input.text)
time_series = parsed_response["Time Series (Daily)"]
date = list(time_series.keys())
last_day = date[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = time_series[last_day]["4. close"]

large_prices = []
small_prices = []

for chosen_date in date:
    large_price = time_series[chosen_date]["2. high"]
    large_prices.append(float(large_price))
    small_price = time_series[chosen_date]["3. low"]
    small_prices.append(float(small_price))

latest_high = max(large_prices)
latest_low = min(small_prices)

#breakpoint()

#Info Outputs

#csv_file_path = "data/stock_prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    for chosen_date in date:
        everyday_prices = time_series[chosen_date]
        writer.writerow({
            "timestamp": chosen_date, 
            "open": everyday_prices["1. open"], 
            "high": everyday_prices["2. high"], 
            "low": everyday_prices["3. low"], 
            "close": everyday_prices["4. close"], 
            "volume": everyday_prices["5. volume"] 
            })

print("-------------------------")
print("SELECTED SYMBOL:", stock_symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", time.strftime("%Y-%m-%d"), time.strftime("%H:%M:%S"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {moneyformat(float(latest_close))}")
print(f"RECENT HIGH: {moneyformat(float(latest_high))}")
print(f"RECENT LOW: {moneyformat(float(latest_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!") #if statements required
print("RECOMMENDATION REASON: TODO") #TO DO
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
