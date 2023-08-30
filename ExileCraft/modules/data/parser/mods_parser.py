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

from modules.data.parser.path_utils import (
    get_abs_path,
    get_base_dir,
    MOD_FAMILY_JSON_PATH,
    MOD_TYPES_JSON_PATH,
)
from modules.shared.config.constants import domain_whitelist

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(
    base_dir, os.path.join(r"ExileCraft\modules\data", "json", "mods.json")
)


class ModParser:
    def __init__(self):
        super().__init__()
        self.abs_path_to_json = abs_path_to_json

    def parse_mods_json(self):
        with open(abs_path_to_json) as json_file:
            return json.load(json_file)

    def parse_mod_types_json(self):
        with open(MOD_TYPES_JSON_PATH) as json_file:
            return json.load(json_file)

    def parse_mod_family_json(self):
        with open(MOD_FAMILY_JSON_PATH) as json_file:
            return json.load(json_file)

    def get_all_mod_data_for_key(self, key):
        mod_data_list = []
        for mod_data in self.bounded_data.values():
            if mod_data not in mod_data_list:
                mod_data_list.append({key: mod_data.get(key, None)})
        return mod_data_list

    @property
    def bounded_data(self):
        return {
            mod: mod_data
            for mod, mod_data in self._data.items()
            if self.is_data_valid(mod_data)
        }

    @staticmethod
    def is_data_valid(data):
        return (
            data.get("domain") in domain_whitelist
            and data.get("generation_type") != "<unknown>"
        )

    @staticmethod
    def get_mod_data_by_key(mod_data, key):
        return {key: mod_data.get(key)}

    def get_all_mod_generation_types(self):
        mod_generation_types_list = self.get_all_mod_data_for_key("generation_type")
        return mod_generation_types_list

    @staticmethod
    def get_mod_generation_type(mod_data):
        mod_generation_type = mod_data.get("generation_type")
        return mod_generation_type

    def get_all_mod_domains(self):
        mod_domains_list = self.get_all_mod_data_for_key("domain")
        return mod_domains_list

    @staticmethod
    def get_mod_domain(mod_data):
        mod_domain = mod_data.get("domain")
        return mod_domain

    @staticmethod
    def get_mod_type(mod_data):
        mod_type = mod_data.get("type")
        return mod_type

    def get_all_mod_groups(self):
        return [
            {"groups": group["groups"][0]}
            for group in self.get_all_mod_data_for_key("groups")
        ]

    @staticmethod
    def get_mod_group(mod_data):
        mod_group = mod_data.get("groups")
        group = mod_group[0]
        return group

    def get_all_mods(self):
        return [
            self.get_mod_data(mod, mod_data)
            for mod, mod_data in self.bounded_data.items()
        ]

    @staticmethod
    def extract_weight_data(weight_data):
        return {"tag": weight_data.get("tag"), "weight": weight_data.get("weight")}

    def get_all_mod_dicts(self):
        data = self._data
        mod_dicts = {}
        for mod, mod_data in data.items():
            if mod_data.get("domain") not in domain_whitelist:
                continue
            mod_dict = self.get_mod_data(mod, mod_data)
            mod_dicts.update(mod_dict)
        return mod_dicts

    @staticmethod
    def get_added_tags(mod_data):
        return mod_data.get("adds_tags", [])

    @staticmethod
    def get_implicit_tags(mod_data):
        return mod_data.get("implicit_tags", [])

    def get_spawn_weights(self, mod_data):
        return [
            self.extract_weight_data(weight_data)
            for weight_data in mod_data.get("spawn_weights", [])
        ]

    @staticmethod
    def get_stats(mod_data):
        return [
            {
                "stat": stat.get("id"),
                "values": {"min": stat.get("min"), "max": stat.get("max")},
            }
            for stat in mod_data.get("stats", [])
        ]

    def get_mod_data(self, mod, mod_data):
        return {
            "mod_name": mod,
            "level_req": mod_data.get("required_level"),
            "name": mod_data.get("name"),
            "is_essence_only": mod_data.get("is_essence_only"),
            "domain": mod_data.get("domain"),
            "generation_type": mod_data.get("generation_type"),
            "group": mod_data.get("groups")[0],
            "type": mod_data.get("type"),
            "added_tags_list": self.get_added_tags(mod_data),
            "implicit_tags_list": self.get_implicit_tags(mod_data),
            "spawn_weights_list": self.get_spawn_weights(mod_data),
            "stats_list": self.get_stats(mod_data),
        }


if __name__ == "__main__":
    mod_parser = ModParser()
    mod_list = mod_parser.parse_mods_json()
    print(mod_list)
