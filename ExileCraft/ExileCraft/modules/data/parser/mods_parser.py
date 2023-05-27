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


def get_mods_by_domain(domain):
    """ Fetches all mods from a JSON file where the domain matches the specified domain.

    Parameters:
    domain (str): The domain to match. E.g. 'item'.

    Returns:
    dict: A dictionary containing all mods where the domain matches the specified domain.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    matching_mods = {mod_key: mod_data for mod_key, mod_data in data.items() if mod_data.get('domain') == domain}

    return matching_mods


def get_mods_by_generation_type(generation_type):
    """ Fetches all mods from a JSON file where the generation type matches the specified generation type.

    Parameters:
    generation_type (str): The generation type to match. E.g. 'prefix', 'suffix'.

    Returns:
    dict: A dictionary containing all mods where the generation type matches the specified generation type.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    matching_mods = {mod_key: mod_data for mod_key, mod_data in data.items() if mod_data.get('generation_type') == generation_type}

    return matching_mods


generation_type = "prefix"
modlist = get_mods_by_generation_type(generation_type)
print(modlist)
