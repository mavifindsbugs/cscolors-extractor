import json

from postgrest import APIResponse
from supabase.client import Client, create_client
from config import SB_URL, SB_KEY

supabase: Client = create_client(SB_URL, SB_KEY)


def export_items(filename: str, table: str):
    with open(filename, "r") as file:
        items = json.loads(file.read())
        supabase.table(table).upsert(items, on_conflict="id").execute()
        print(f"Exporting items from {filename} to table {table}")


def export_prices(filename: str, table: str):
    values = []
    with open(filename, "r") as file:
        prices = json.loads(file.read())
        for name, price in prices.items():
            steam = price.get("steam", None)
            if steam:
                steam = steam.get("last_30d", None)
            if steam == 0:
                steam = None

            skinport = price.get("skinport", None)
            if skinport:
                skinport = skinport.get("suggested_price", None)
            buff = price.get("buff163", None)
            if buff:
                buff = buff.get("highest_order", None)
            if buff:
                buff = buff.get("price", None)
            values.append({"name": name, "steam": steam, "skinport": skinport, "buff": buff})
        # print(values)
        supabase.table(table).upsert(values, on_conflict="name").execute()
        print(f"Exporting prices from {filename} to table {table}")


def update_prices():
    res = supabase.rpc("update_item_prices", params={}).execute()
    print(res)

