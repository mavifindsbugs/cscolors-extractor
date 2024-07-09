import os

SKINS_URL = "https://bymykel.github.io/CSGO-API/api/en/skins.json"
STICKERS_URL = "https://bymykel.github.io/CSGO-API/api/en/stickers.json"
GRAFFITI_URL = "https://bymykel.github.io/CSGO-API/api/en/graffiti.json"
CRATES_URL = "https://bymykel.github.io/CSGO-API/api/en/crates.json"

SB_URL: str | None = os.environ.get("SUPABASE_URL")
SB_KEY: str | None = os.environ.get("SUPABASE_KEY")
