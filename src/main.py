import json

from items import process_items
from config import SKINS_URL, STICKERS_URL

res = process_items(SKINS_URL, poolsize=10)

with open("skins.json", "w") as file:
    items = sorted(res, key=lambda item: item['name'].lower())
    file.write(json.dumps(items))

res = process_items(STICKERS_URL, poolsize=10)

with open("stickers.json", "w") as file:
    items = sorted(res, key=lambda item: item['name'].lower())
    file.write(json.dumps(items))

