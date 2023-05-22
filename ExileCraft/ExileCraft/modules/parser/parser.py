import json


def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


file_path = 'item_classes.json'
data = parse_json(file_path)

for key, value in data.items():
    print(f'Key: {key} - Value: {value}')
