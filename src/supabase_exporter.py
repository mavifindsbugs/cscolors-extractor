import json

from supabase.client import Client, create_client
from config import SB_URL, SB_KEY

supabase: Client = create_client(SB_URL, SB_KEY)


def export_items(filename: str, table: str):
    with open(filename, "r") as file:
        items = json.loads(file.read())
        supabase.table(table).upsert(items, on_conflict="id").execute()
        print(f"Exporting items from {filename} to table {table}")
