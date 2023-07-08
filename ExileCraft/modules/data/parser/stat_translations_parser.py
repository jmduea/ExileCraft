# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################

import json
import os

from modules.data.models.stat_models import StatTranslation, EnglishTranslation, StatCondition, StatFormat, \
    StatIndexHandler
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'stat_translations.min.json'))


def insert_stat_translations_into_db(db_manager):
    with open(abs_path_to_json, 'r') as f:
        data = json.load(f)
    
    with db_manager.transaction() as session:
        for entry in data:
            stat_translation = StatTranslation(stat_id=entry['ids'][0])
            if 'hidden' in entry:
                stat_translation.hidden = entry['hidden']
            
            for english in entry['English']:
                english_translation = EnglishTranslation(stat_string=english['string'])
                english_translation.stat_translation = stat_translation
                
                for condition in english['condition']:
                    stat_condition = StatCondition(min=condition.get('min'), max=condition.get('max'),
                                                    negated=condition.get('negated', False))
                    english_translation.conditions.append(stat_condition)
                
                for format in english['format']:
                    stat_format = StatFormat(format=format)
                    english_translation.formats.append(stat_format)
                
                for index_handler in english['index_handlers']:
                    for handler in index_handler:  # assuming 'index_handlers' is a list of lists
                        stat_index_handler = StatIndexHandler(handler=handler)
                        english_translation.index_handlers.append(stat_index_handler)
                
                stat_translation.english_translations.append(english_translation)
            
            session.add(stat_translation)
            
            session.commit()


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
