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

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir,
                                os.path.join(r'ExileCraft\modules\data', 'json', 'stat_translations.min.json'))


class StatTranslationParser:
    def __init__(self):
        self.abs_path_to_json = abs_path_to_json

    @staticmethod
    def parse_json():
        with open(abs_path_to_json) as json_file:
            _data = json.load(json_file)
        return _data

    def create_translation_objects(self):
        data = self.parse_json()
        translation_list = []
        for item in data:
            translation_list.append({'ids': item.get('ids', []), 'translations': item.get(
                'English', []), 'hidden': item.get('hidden', False)})
        return translation_list

    @staticmethod
    def find_stat_translation(data, mod_id):
        for translation in data:
            if mod_id in translation['ids']:
                return translation

        return None


def get_stat_translation_string(_stat_translation_data, average_stat):
    """
    Determines the appropriate translation string for a given stat based on its average value.

    This function iterates through a list of possible translations, each with a condition
    specifying a minimum and/or maximum value. If the average stat value meets the condition
    of a translation, that translation's string is returned, with the average stat value
    inserted at the appropriate place.

    If no suitable translation is found, an empty string is returned.

    Args:
        _stat_translation_data (list): A list of dictionaries, each representing a possible
                                      translation. Each dictionary should contain a 'condition'
                                      key (itself a dictionary with 'min' and/or 'max' keys)
                                      and a 'string' key.
        average_stat (float): The average value of the stat for which a translation is needed.

    Returns:
        str: The appropriate translation string with the average stat value inserted, or an
             empty string if no suitable translation is found.
    """
    for translation in _stat_translation_data:
        condition = translation.get('condition', [{}])[0]
        min_condition = condition.get('min', None)
        max_condition = condition.get('max', None)

        # Check if average_stat meets the condition
        if (min_condition is not None and average_stat >= min_condition) or \
                (max_condition is not None and average_stat <= max_condition):
            return translation.get('string', '').format(average_stat)
    return ''


if __name__ == "__main__":
    stat_translation_parser = StatTranslationParser()
    stat_translation_data = stat_translation_parser.create_translation_objects()
    for translation_data in stat_translation_data:
        print(translation_data)
    print(stat_translation_data)
