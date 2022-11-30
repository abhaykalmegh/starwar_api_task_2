import requests

params = {
  'access_key': 'ec9c5a64a5c778d9ff5d21ce00ce0414'
}

api_result = requests.get('https://api.marketstack.com/v1/tickers/aapl/eod', params)

api_response = api_result.json()
print(api_response)
for stock_data in api_response['data']:
    print(
      stock_data['symbol'],
      stock_data['high'],
      stock_data['date']
    )
