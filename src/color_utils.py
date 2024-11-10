import time
from typing import List
import urllib.request

import webcolors

from css3_colors import CSS3_NAMES_TO_HEX
from colorthief import ColorThief

from models import Item, Color


def fetch_image(url: str) -> ColorThief | None:
    try:
        return ColorThief(urllib.request.urlopen(url))
    except Exception as e:
        print(f"Error when fetching image: {e}")
        return None


def closest_colour(requested_colour):
    min_colours = {}
    for name, hex in CSS3_NAMES_TO_HEX.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(hex)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colors(item: Item) -> List[Color]:
    colorthief: ColorThief | None = None
    for _ in range(3):
        colorthief = fetch_image(item.image)
        if colorthief is not None:
            break
        time.sleep(2)

    if colorthief is None:
        print(f"Could not fetch image for {item}, setting colors to empty")
        return []

    colors = colorthief.get_palette(10, 1)
    web_colors = {}
    color_objs = []

    for r, g, b in colors:
        web_color = closest_colour((int(r), int(g), int(b)))
        if web_color == "darkslategray":
            continue
        if web_color not in web_colors:
            web_colors[web_color] = 1
        else:
            web_colors[web_color] += 1

    for color, count in web_colors.items():
        color_obj = Color(color, count, webcolors.name_to_hex(color))
        color_objs.append(color_obj)
    return color_objs


def convert_to_basic_colors(colors: List[Color]) -> List[str]:
    base_colors = [
        "red",
        "green",
        "blue",
        "yellow",
        "red",
        "white",
        "black",
        "gray",
        "brown",
    ]
    res = []
    for color in colors:
        for base_color in base_colors:
            if base_color in color.name:
                res.append(base_color)
    res = set(res)
    return list(res)
