import json
import requests

def get_prices():
    prices = {}
    res = requests.get("https://prices.csgotrader.app/latest/prices_v6.json")
    content = res.content
    i = 0
    for item, data in json.loads(content).items():
        item = item.replace("\u2605 ", "")
        item = item.replace("\u2122", "")
        prices[item] = data

    with open("prices.json", "w") as file:
        file.write(json.dumps(prices))