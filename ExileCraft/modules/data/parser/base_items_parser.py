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

from modules.shared.config.constants import one_hand_weapon_types, two_hand_weapon_types, flask_types, \
    item_class_whitelist, armour_subtypes, domain_whitelist
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'base_items.min.json'))


class ItemParser:
    
    def __init__(self):
        self.abs_path_to_json = abs_path_to_json
    
    @staticmethod
    def parse_json():
        with open(abs_path_to_json) as json_file:
            _data = json.load(json_file)
        return _data
    
    def get_item_data_by_key(self, key):
        data = self.parse_json()
        item_data_list = []
        for item, item_data in data.items():
            if item_data.get("item_class") not in item_class_whitelist:
                continue
            item_data_value = item_data.get(key, '')
            item_data_dict = {'metadata_id': item, key: item_data_value}
            if item_data_dict not in item_data_list:
                item_data_list.append(item_data_dict)
        return item_data_list
    
    def create_item_data_list(self):
        data = self.parse_json()
        item_data_list = []
        for metadata_id, item_data in data.items():
            if item_data.get("domain") not in domain_whitelist:
                continue
            drop_level = item_data.get("drop_level")
            visual_identity = item_data.get("visual_identity").get("id")
            item_domain = item_data.get("domain")
            item_class = item_data.get("item_class")
            name = item_data.get("name")
            
            # Create the tags list
            tag_list = [tag for tag in item_data.get("tags")]
            
            # Create the implicit list
            implicit_list = [implicit for implicit in item_data.get("implicits")]
            
            # Create the item_requirements_dict with the get_item_requirements method
            item_requirements_dict = self.get_item_requirements(item_data) if item_data.get("requirements") else None
            
            # Create the item_properties_dict with the get_item_properties method
            item_properties_dict = self.get_item_properties(item_data) if item_data.get("properties") else None
            
            item_class_subtype = self.get_item_class_subtype(item_class, tag_list)
            
            item_data_dict = {
                'metadata_id': metadata_id,
                'drop_level': drop_level,
                'name': name,
                'item_domain': item_domain,
                'item_class': item_class,
                'visual_identity': visual_identity,
                'tag_list': tag_list,
                'implicit_list': implicit_list,
                'item_requirements_dict': item_requirements_dict,
                'item_properties_dict': item_properties_dict,
                'item_class_subtype': item_class_subtype,
                'release_state': item_data.get("release_state")
            }
            if item_data_dict not in item_data_list:
                item_data_list.append(item_data_dict)
        return item_data_list
    
    @staticmethod
    def get_item_class_subtype(item_class, tag_list):
        # Get the set of subtypes for this item_class
        possible_subtypes = armour_subtypes.get(item_class)
        if possible_subtypes:
            # Find the first tag in the tag_list that is in the set of possible subtypes
            for tag in tag_list:
                if tag in possible_subtypes:
                    return tag
        # if no subtype was found
        elif item_class in one_hand_weapon_types:
            return 'one_hand_weapon'
        elif item_class in two_hand_weapon_types:
            return 'two_hand_weapon'
        elif item_class in flask_types:
            return 'flask'
        else:
            return 'other'
    
    @staticmethod
    def get_item_requirements(item_data):
        if item_data.get("requirements") != {}:
            name = item_data.get("name")
            level = item_data.get("requirements").get("level", item_data.get("drop_level"))
            strength = item_data.get("requirements").get("strength", 0)
            dexterity = item_data.get("requirements").get("dexterity", 0)
            intelligence = item_data.get("requirements").get("intelligence", 0)
            item_requirements_dict = {"name": name,
                                      "requirements": {
                                          "level": level,
                                          "strength": strength,
                                          "dexterity": dexterity,
                                          "intelligence": intelligence
                                      }}
            return item_requirements_dict
        else:
            return {}
    
    @staticmethod
    def get_item_properties(item_data):
        item_properties_dict = {}
        if item_data.get("properties") != {}:
            properties = item_data.get("properties", {})
            for _property, value in properties.items():
                item_properties_dict[_property] = value
            return item_properties_dict
        else:
            return {}
    
    def get_all_items(self):
        data = self._data
        item_list = []
        for item, item_data in data.items():
            item_dict = {
                item: item_data
            }
            if item_dict not in item_list:
                item_list.append(item_dict)
        return item_list


if __name__ == "__main__":
    item_parser = ItemParser()
    item_data_list = item_parser.create_item_data_list()
    print(item_data_list)
