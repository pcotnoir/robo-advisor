# app/robo_advisor.py

import requests
import json

#Info Inputs

def moneyformat(price):
    return '${:,.2f}'.format(price) 

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(url)
#print(response.status_code) #> 200
#print(type(response)) #> <class 'requests.models.Response'>
#print(response.text)

parsed_response = json.loads(response.text)
time_series = parsed_response["Time Series (Daily)"]
date = list(time_series.keys())
last_day = date[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = time_series[last_day]["4. close"]

large_prices = []

for chosen_date in date:
    large_price = time_series[chosen_date]["2. high"]
    large_prices.append(float(large_price))

latest_high = max(large_prices)

#breakpoint()

#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #DO ON OWN
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {moneyformat(float(latest_close))}")
print(f"RECENT HIGH: {moneyformat(float(latest_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")