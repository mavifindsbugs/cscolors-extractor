import json

def sort_file(filename: str):
    items = {}
    with open(filename, "r") as file:
        items = json.loads(file.read())
        items = sorted(items, key=lambda item: item['name'].lower())

    with open(filename, "w") as file:
        file.write(json.dumps(items))