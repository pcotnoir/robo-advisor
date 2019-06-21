# app/robo_advisor.py

import requests
import json

#Info Inputs

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(url)
#print(response.status_code) #> 200
#print(type(response)) #> <class 'requests.models.Response'>
#print(response.text)

parsed_response = json.loads(response.text)

breakpoint()

#Info Outputs

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")