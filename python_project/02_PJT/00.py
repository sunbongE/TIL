import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url)
D = response.json()
print(D.get('data').get('prev_closing_price'))
# print(response.json().get('data').get('prev_closing_price'))

