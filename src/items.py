from functools import partial
import json
from typing import List
import requests
import warnings

from color_utils import get_colors, convert_to_basic_colors
from models import Item
from multiprocessing.pool import ThreadPool
from tqdm.rich import tqdm

from tqdm import TqdmExperimentalWarning

bar: tqdm
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)


def chunks(list, n):
    for i in range(0, len(list), n):
        yield list[i : i + n]


def get_items(url: str) -> List[Item]:
    res = requests.get(url)
    items = json.loads(res.content)

    items_objs = []
    for item in items:
        item_obj = Item()
        item_obj.from_dict(item)
        if item.get("max_float", None) is not None:
            item_obj.max_float = int(item["max_float"] * 100)
            item_obj.min_float = int(item["min_float"] * 100)
        item_obj.type = item_obj.id.split("-")[0]
        item_obj.rarity = item["rarity"]["name"]
        
        item_obj.category = item.get("category")
        if item_obj.category is not None:
            item_obj.category = item_obj.category["name"]
        item_obj.weapon = item.get("weapon")
        if item_obj.weapon is not None:
            item_obj.weapon = item_obj.weapon["name"]
        item_obj.pattern = item.get("pattern", None)
        if item_obj.pattern is not None:
            item_obj.pattern = item_obj.pattern["name"]
        
        if "collections" in item:
            item_obj.collections = [i["name"] for i in item["collections"]]
        item_obj.crates = [i["name"] for i in item["crates"]]

        items_objs.append(item_obj)
    return items_objs


def process_items(url: str, count: int = -1, poolsize: int = 10, skip_colors: bool = False, filename: str = "items.json"):
    items = get_items(url)
    if count != -1:
        items = items[:count]

    total = len(items)
    pool = ThreadPool(poolsize)
    global bar
    bar = tqdm(total=total)

    print(f"Processing {total} items.")
    part_func = partial(process_items_async, skip_colors)
    chunked = chunks(items, poolsize)
    processed_items = pool.map(part_func, chunked)

    pool.close()
    pool.join()
    bar.close()

    result = []
    for pi in processed_items:
        result.extend(pi)

    with open(filename, "w") as file:
        items = sorted(result, key=lambda item: item['name'].lower())
        file.write(json.dumps(items))

    return result


def process_items_async(skip: bool, items: List[Item]):
    if skip:
        return [i.__dict__ for i in items]
    
    values = []
    for item in items:
        # print(f"Processing {item}")
        item.colors = get_colors(item)
        item.base_colors = convert_to_basic_colors(item.colors)
        item_dict = item.__dict__
        item_dict["colors"] = [color.__dict__ for color in item.colors]
        values.append(item_dict)
        global bar
        bar.update()
    return values
