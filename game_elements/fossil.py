import json


class Fossil:
    def __init__(self, data):
        self.added_mods = data.get('added_mods', [])
        self.allowed_tags = data.get('allowed_tags', [])
        self.blocked_descriptions = data.get('blocked_descriptions', [])
        self.changes_quality = data.get('changes_quality', False)
        self.corrupted_essence_chance = data.get('corrupted_essence_chance', 0)
        self.descriptions = data.get('descriptions', [])
        self.enchants = data.get('enchants', False)
        self.forbidden_tags = data.get('forbidden_tags', [])
        self.forced_mods = data.get('forced_mods', [])
        self.mirrors = data.get('mirrors', False)
        self.name = data.get('name', '')
        self.negative_mod_weights = data.get('negative_mod_weights', [])
        self.positive_mod_weights = data.get('positive_mod_weights', [])
        self.rolls_lucky = data.get('rolls_lucky', False)
        self.rolls_white_sockets = data.get('rolls_white_sockets', False)
        self.sell_price_mods = data.get('sell_price_mods', [])


def load_fossils_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    fossils = {}
    for key, data in json_data.items():
        fossils[key] = Fossil(data)

    return fossils
