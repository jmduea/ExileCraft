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

from modules.config.constants import one_hand_weapon_types, two_hand_weapon_types, armour_types, flask_types, \
    item_class_whitelist, armour_subtypes, domain_whitelist
from modules.data.models.item_models import VisualIdentity, Item
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'base_items.min.json'))


def insert_visual_identities_into_db(db_manager):
    # Load the JSON file
    with open(abs_path_to_json) as json_file:
        data = json.load(json_file)
    
    with db_manager.transaction() as session:
        for metadata_id, item_data in data.items():
            if item_data.get("item_class") in item_class_whitelist and item_data.get("release_state") == "released" \
                    and item_data.get("domain") in domain_whitelist:
                visual_identity = session.query(VisualIdentity).filter_by(visual_identity=data[metadata_id]
                ['visual_identity']['id']).first()
                if not visual_identity:
                    visual_identity = VisualIdentity(visual_identity=data[metadata_id]['visual_identity']['id'])
                    session.add(visual_identity)
        session.commit()


def get_class_subtype(item_class, tag_list):
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


def get_item_requirements(item_data):
    if item_data.get("requirements"):
        level = item_data.get("requirements").get("level")
        strength = item_data.get("requirements").get("strength")
        dexterity = item_data.get("requirements").get("dexterity")
        intelligence = item_data.get("requirements").get("intelligence")
        item_requirements_dict = {
            "level": level,
            "strength": strength,
            "dexterity": dexterity,
            "intelligence": intelligence
        }
        return item_requirements_dict
    else:
        item_requirements_dict = {
            "level": item_data.get("drop_level"),
            "strength": 0,
            "dexterity": 0,
            "intelligence": 0
        }
        return item_requirements_dict


def get_item_properties(item_class, item_data):
    if item_class in armour_types:
        item_properties = {
            "armour_min": item_data.get("properties", {}).get("armour", {}).get('min'),
            "armour_max": item_data.get("properties", {}).get("armour", {}).get('max'),
            "evasion_min": item_data.get("properties", {}).get("evasion", {}).get('min'),
            "evasion_max": item_data.get("properties", {}).get("evasion", {}).get('max'),
            "energy_shield_min": item_data.get("properties", {}).get("energy_shield", {}).get('min'),
            "energy_shield_max": item_data.get("properties", {}).get("energy_shield", {}).get('max'),
            "ward_min": item_data.get("properties", {}).get("ward", {}).get('min'),
            "ward_max": item_data.get("properties", {}).get("ward", {}).get('max'),
            "block": item_data.get("properties", {}).get("block"),
            "movement_penalty": item_data.get("properties", {}).get("movement_speed")
        }
        return item_properties
    elif item_class in one_hand_weapon_types or item_class in two_hand_weapon_types:
        item_properties = {
            "attack_time": item_data.get("properties", {}).get("attack_time"),
            "critical_strike_chance": item_data.get("properties", {}).get("critical_strike_chance"),
            "physical_damage_min": item_data.get("properties", {}).get("physical_damage_min"),
            "physical_damage_max": item_data.get("properties", {}).get("physical_damage_max"),
            "range": item_data.get("properties", {}).get("range")
        }
        return item_properties
    elif item_class in flask_types:
        item_properties = {
            "buff_id": item_data.get("grants_buff", {}).get('id'),
            "buff_stat": item_data.get("grants_buff", {}).get('stat'),
            "implicits": f'{item_data.get("implicits")}',
            "charges_max": item_data.get("properties", {}).get("charges_max"),
            "charges_per_use": item_data.get("properties", {}).get("charges_per_use"),
            "duration": item_data.get("properties", {}).get("duration"),
            "life_per_use": item_data.get("properties", {}).get("life_per_use"),
            "mana_per_use": item_data.get("properties", {}).get("mana_per_use")
        }
        return item_properties
    else:
        item_properties = None
        return item_properties


def get_item_info(db_manager):
    with open(abs_path_to_json) as json_file:
        data = json.load(json_file)
    for metadata_id, item_data in data.items():
        # Check that the item is one that we want to insert into the db based off item_class and release_state
        if item_data.get("item_class") in item_class_whitelist and item_data.get("release_state") == "released" and \
                item_data.get("domain") in domain_whitelist:
            drop_level = item_data.get("drop_level")
            visual_identity = item_data.get("visual_identity").get("id")
            item_domain = item_data.get("domain")
            item_class = item_data.get("item_class")
            name = item_data.get("name")
            
            # Create the tags list
            tag_list = []
            for tag in item_data.get("tags"):
                tag_list.append(tag)
            
            # Create the implicit list
            implicit_list = []
            for implicit in item_data.get("implicits"):
                implicit_list.append(implicit)
            
            # Create the item_requirements_dict with the get_item_requirements method
            item_requirements_dict = get_item_requirements(item_data)
            
            # Create the item_properties_dict with the get_item_properties method
            item_properties_dict = get_item_properties(item_class, item_data)
            
            item_class_subtype = get_class_subtype(item_class, tag_list)
            
            insert_base_items_into_db(db_manager, metadata_id, drop_level, name, item_domain, item_class,
                                      visual_identity,
                                      tag_list, implicit_list, item_requirements_dict, item_properties_dict,
                                      item_class_subtype)


def insert_base_items_into_db(db_manager, metadata_id, drop_level, name, item_domain, item_class, visual_identity,
                              tag_list,
                              implicit_list, item_requirements_dict, item_properties_dict, item_class_subtype):
    with db_manager.transaction() as session:
        # Get the domain_id
        domain_id = db_manager.get_domain(session, item_domain)
        
        # Get the item_class_id
        item_class_id = db_manager.get_item_class(session, item_class)
        
        # Get the item_class_subtype_id using the item_class_id and subtype name from item_class_subtype
        item_class_subtype_id = db_manager.get_item_class_subtype(session, item_class_id, item_class_subtype)
        
        # Get the visual_identity_id
        visual_identity_id = db_manager.get_visual_identity_id(session, visual_identity)
        
        item_class_dict = {
            "visual_identity_id": visual_identity_id,
            "name": name,
            "meta_data_id": metadata_id,
            "item_class_id": item_class_id,
            "item_class_subtype_id": item_class_subtype_id,
            "domain_id": domain_id,
            "drop_level": drop_level,
            "rarity": 'Normal',
            "is_corrupted": False
        }
        item = Item(**item_class_dict)
        session.add(item)
        session.commit()
        item_id = item.id
        
        db_manager.insert_item_tags(session, tag_list, item_id)
        db_manager.insert_item_implicits(session, implicit_list, item_id)
        db_manager.insert_item_properties(session, item_id, item_class_id, item_class_subtype,
                                          item_class_subtype_id, item_properties_dict, item_requirements_dict)
