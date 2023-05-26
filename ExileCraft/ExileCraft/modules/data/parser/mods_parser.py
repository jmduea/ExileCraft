import json
import os

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'mods.json'))


def find_mod(mod_id):
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    return data.get(mod_id)


def get_mod_stats(mod_key):
    """ Searches through a JSON file of mod data and returns the stats for a specified mod key.

    Parameters:
    mod_key (str): The key of the mod to search for. E.g. 'SpellDamageImplicitArmour1'.

    Returns:
    list: A list of dictionaries containing the stats for the specified mod key, or None if the key was not found.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    mod_data = data.get(mod_key)
    if mod_data:
        return mod_data.get('stats')
    else:
        return None
