import json

import requests

from supabase_exporter import export_items, export_prices, update_prices

from items import get_items, process_items
from config import GRAFFITI_URL, SKINS_URL, STICKERS_URL, CRATES_URL
from prices import get_prices

res = process_items(SKINS_URL, poolsize=10, skip_colors=False)

with open("skins.json", "w") as file:
    items = sorted(res, key=lambda item: item['name'].lower())
    file.write(json.dumps(items))

# export_items("skins.json", "Items")

res = process_items(STICKERS_URL, poolsize=10, skip_colors=False)

with open("stickers.json", "w") as file:
     items = sorted(res, key=lambda item: item['name'].lower())
     file.write(json.dumps(items))

# export_items("stickers.json", "Items")

res = process_items(GRAFFITI_URL, poolsize=5)

with open("graffiti.json", "w") as file:
    items = sorted(res, key=lambda item: item['name'].lower())
    file.write(json.dumps(items))


get_prices()
# export_prices("prices.json", "Prices")
# update_prices()
