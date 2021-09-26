from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

import requests
import json

response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false')

list = json.loads(response.text)

top = int(input("Which top do you want to get? Please Enter: "))

for i in range(top):
    print(list[i]['market_cap_rank'], list[i]['name'], list[i]['market_cap'])