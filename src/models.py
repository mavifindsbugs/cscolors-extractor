# type: ignore

from dataclasses import dataclass
from typing import List


@dataclass
class Color(object):
    name: str = None
    count: int = None
    hex: str = None

    def from_dict(self, dic):
        if dic is not None:
            for key, value in dic.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} {self.count}"


@dataclass
class Collection(object):
    id: str = None
    name: str = None
    image: str = None

    def from_dict(self, dic):
        if dic is not None:
            for key, value in dic.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} {self.image}"


@dataclass
class Crate(object):
    id: str = None
    name: str = None
    image: str = None

    def from_dict(self, dic):
        if dic is not None:
            for key, value in dic.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} {self.image}"


@dataclass
class Item(object):
    id: str = None
    name: str = None
    description: str = None
    weapon: str = None
    category: str = None
    pattern: str = None
    min_float: int = None
    max_float: int = None
    rarity: str = None
    stattrak: bool = None
    souvenir: bool = None
    paint_index: str = None
    image: str = None

    collections: List[str] = None
    crates: List[str] = None

    colors: List[Color] = None
    base_colors: List[str] = None

    type: str = None

    def from_dict(self, dic):
        if dic is not None:
            for key, value in dic.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.id} {self.category} {self.name} "
