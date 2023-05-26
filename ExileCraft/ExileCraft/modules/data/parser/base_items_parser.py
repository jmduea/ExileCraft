import json
import os

from modules.config.constants import ITEM_CLASS_WHITELIST
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'base_items.json'))


def find_items(item_class, tag):
    """ Searches through a JSON file of item data and returns the names of items that match a specified class and have a specified tag. Only items with a class in the ITEM_CLASS_WHITELIST set, with a 'release_state' of 'released', without 'Talisman' in their name, and without the 'not_for_sale' tag are considered.
    This function opens a JSON file containing item data and iterates through
    all items. If an item's 'item_class' key matches the provided item_class
    parameter, the item_class is in the ITEM_CLASS_WHITELIST set, the provided
    tag exists in the item's 'tags' list, the item's 'release_state' is 'released',
    the item's name does not contain 'Talisman', and the item's tags do not contain
    'not_for_sale', the item's name is added to a list. This list of matching item
    names is returned.

    Parameters:
    item_class (str): The class of items to search for. E.g. 'Amulet'.
    tag (str): The tag that matching items must contain. E.g. 'default'.

    Returns:
    list: A list of names of items that match the specified class and tag.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    matching_items = []
    for item_data in data.values():
        item_class_in_data = item_data.get('item_class')
        item_name = item_data.get('name', '')
        item_tags = item_data.get('tags', [])
        if (item_class_in_data == item_class
                and item_class_in_data in ITEM_CLASS_WHITELIST
                and tag in item_tags
                and item_data.get('release_state') == 'released'
                and 'Talisman' not in item_name
                and 'demigods' not in item_tags):
            matching_items.append(item_data)

    # Sort the list of matching items by drop level
    matching_items = sorted(matching_items, key=lambda item: item.get('drop_level', 0))

    # Return a list of item names
    return [item['name'] for item in matching_items]


def find_item_info(item_name):
    """
    Retrieves the details of an item with a specified name from a JSON file of item data.

    This function opens a JSON file containing item data and iterates through all items.
    If an item's 'name' key matches the provided item_name parameter, the item's data
    is added to a list. This list of matching item data is returned.

    Parameters:
    item_name (str): The name of the item to search for. E.g. 'Jade Amulet'.

    Returns:
    list: A list of dictionaries containing the data of items that match the specified name.
    Each dictionary represents one item and contains key-value pairs for different item attributes.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    item_info = []
    for item_data in data.values():
        if item_data.get('name') == item_name:
            item_info.append(item_data)
    return item_info


def extract_item_info(item_info):
    """
    Extracts specified attributes from a list of item information dictionaries.

    This function iterates through a list of item information dictionaries,
    where each dictionary represents the data of a particular item. It extracts
    the values of specified attributes (such as 'domain', 'implicits', etc.)
    and stores these values in a new dictionary. The new dictionaries are
    added to a list, which is then returned.

    Parameters:
    item_info (list): A list of dictionaries, where each dictionary contains
                      data of a specific item.

    Returns:
    list: A list of dictionaries, where each dictionary contains the extracted
          information for a specific item.
    """
    extracted_info = []
    for item_data in item_info:
        item_details = {
            'domain': item_data.get('domain'),
            'implicits': item_data.get('implicits'),
            'item_class': item_data.get('item_class'),
            'name': item_data.get('name'),
            'properties': item_data.get('properties'),
            'requirements': item_data.get('requirements'),
            'tags': item_data.get('tags')
        }
        extracted_info.append(item_details)
    return extracted_info
