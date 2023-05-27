import json
import os

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'stat_translations.json'))


def find_stat_translation(mod_id):
    """ Searches through a JSON file of stat translations and returns the translation for a specified mod_id.

    Parameters:
    mod_id (str): The mod_id to search for.

    Returns:
    dict: A dictionary containing the stat translation for the specified mod_id, or None if the mod_id was not found.
    """
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)

    for translation in data:
        if mod_id in translation['ids']:
            return translation

    return None


def get_stat_translation_string(stat_translation_data, average_stat):
    """
    Determines the appropriate translation string for a given stat based on its average value.

    This function iterates through a list of possible translations, each with a condition
    specifying a minimum and/or maximum value. If the average stat value meets the condition
    of a translation, that translation's string is returned, with the average stat value
    inserted at the appropriate place.

    If no suitable translation is found, an empty string is returned.

    Args:
        stat_translation_data (list): A list of dictionaries, each representing a possible
                                      translation. Each dictionary should contain a 'condition'
                                      key (itself a dictionary with 'min' and/or 'max' keys)
                                      and a 'string' key.
        average_stat (float): The average value of the stat for which a translation is needed.

    Returns:
        str: The appropriate translation string with the average stat value inserted, or an
             empty string if no suitable translation is found.
    """
    for translation in stat_translation_data:
        condition = translation.get('condition', [{}])[0]
        min_condition = condition.get('min', None)
        max_condition = condition.get('max', None)

        # Check if average_stat meets the condition
        if (min_condition is not None and average_stat >= min_condition) or \
                (max_condition is not None and average_stat <= max_condition):
            return translation.get('string', '').format(average_stat)
    return ''
