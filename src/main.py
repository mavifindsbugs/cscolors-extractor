from supabase_exporter import export_items

from items import get_items, process_items
from config import GRAFFITI_URL, SKINS_URL, STICKERS_URL, CRATES_URL

res = process_items(SKINS_URL, poolsize=20, skip_colors=False, filename="skins.json")

export_items("skins.json", "Items")

res = process_items(STICKERS_URL, poolsize=20, skip_colors=False, filename="stickers.json")

export_items("stickers.json", "Items")

res = process_items(GRAFFITI_URL, poolsize=20, skip_colors=False, filename="graffiti.json")

export_items("graffiti.json", "Items")

