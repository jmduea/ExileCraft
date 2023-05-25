import json
import os

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'base_items.json'))


def find_items(item_class, tag):
    """
    Searches through a JSON file of item data and returns the names of items
    that match a specified class and have a specified tag.

    This function opens a JSON file containing item data and iterates through
    all items. If an item's 'item_class' key matches the provided item_class
    parameter and the provided tag exists in the item's 'tags' list, the item's
    name is added to a list. This list of matching item names is returned.

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
        if item_data.get('item_class') == item_class and tag in item_data.get('tags', []):
            matching_items.append(item_data['name'])
    return matching_items


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
