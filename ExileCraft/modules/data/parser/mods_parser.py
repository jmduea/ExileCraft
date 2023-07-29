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
from modules.shared.config.constants import domain_whitelist

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'mods.min.json'))


class ModParser:
    def __init__(self):
        self._data = self.parse_json()
        self.abs_path_to_json = abs_path_to_json
        self.mod_list = self.get_all_mods()

    def parse_json(self):
        if not hasattr(self, '_data'):
            with open(abs_path_to_json) as json_file:
                self._data = json.load(json_file)
        return self._data

    def get_all_mod_data_for_key(self, key):
        data = self._data
        mod_data_list = []
        for mod, mod_data in data.items():
            if mod_data.get("domain") not in domain_whitelist:
                continue
            if mod_data.get("generation_type") == "<unknown>":
                continue
            mod_data_value = mod_data.get(key, None)
            mod_data_dict = {
                key: mod_data_value if mod_data_value is not None else None
            }
            if mod_data_dict not in mod_data_list:
                mod_data_list.append(mod_data_dict)
        return mod_data_list

    @staticmethod
    def get_mod_data_by_key(mod_data, key):
        mod_data_value = mod_data.get(key)
        value_dict = {key: mod_data_value}
        return value_dict

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

    def get_all_mod_types(self):
        types_list = self.get_all_mod_data_for_key("type")
        mod_types_list = []
        for _type in types_list:
            if _type not in mod_types_list:
                mod_types_list.append(_type)
        return mod_types_list

    @staticmethod
    def get_mod_type(mod_data):
        mod_type = mod_data.get("type")
        return mod_type

    def get_all_mod_groups(self):
        mod_groups_list = self.get_all_mod_data_for_key("groups")
        groups_list = []
        for group in mod_groups_list:
            group_dict = {
                "groups": group["groups"][0]
            }
            if group_dict not in groups_list:
                groups_list.append(group_dict)
        return groups_list

    @staticmethod
    def get_mod_group(mod_data):
        mod_group = mod_data.get("groups")
        group = mod_group[0]
        return group

    def get_all_mods(self):
        data = self._data
        _mod_list = []
        for mod, mod_data in data.items():
            if mod_data.get("domain") not in domain_whitelist:
                continue
            if mod_data.get("generation_type") == "<unknown>":
                continue
            if mod not in _mod_list:
                mod_dict = {
                    'mod_name': mod,
                    'level_req': mod_data.get("required_level"),
                    'name': mod_data.get("name"),
                    'is_essence_only': mod_data.get("is_essence_only"),
                    'domain': mod_data.get('domain'),
                    'generation_type': mod_data.get('generation_type'),
                    'group': mod_data.get('groups')[0],
                    'mod_type': mod_data.get('type'),
                    'added_tags_list': self.get_added_tags(mod_data),
                    'implicit_tags_list': self.get_implicit_tags(mod_data),
                    'spawn_weights_list': self.get_spawn_weights(mod_data),
                    'stats_list': self.get_stats(mod_data)
                }
                _mod_list.append(mod_dict)
        return _mod_list

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
        added_tags_list = [tag for tag in mod_data.get("adds_tags", [])]
        return added_tags_list

    @staticmethod
    def get_implicit_tags(mod_data):
        implicit_tags_list = [tag for tag in mod_data.get("implicit_tags", [])]
        return implicit_tags_list

    @staticmethod
    def get_spawn_weights(mod_data):
        spawn_weights_list = []
        spawn_weights_data = mod_data.get("spawn_weights", [])
        for weight_data in spawn_weights_data:
            tag_dict = {
                "tag": weight_data.get("tag"),
                "weight": weight_data.get("weight")
            }
            spawn_weights_list.append(tag_dict)
        return spawn_weights_list

    @staticmethod
    def get_stats(mod_data):
        stats_list = []
        stats_data = mod_data.get("stats", [])
        for stat in stats_data:
            stat_data_dict = {
                'stat': stat.get("id"),
                'values': {'min': stat.get("min"), 'max': stat.get("max")},
                # 'stat_min_value': stat_data.get("min"),
                # 'stat_max_value': stat_data.get("max")
            }
            stats_list.append(stat_data_dict)
        return stats_list

    def get_mod_data(self, mod, mod_data):
        mod_dict = {
            'mod_name': mod,
            'level_req': mod_data.get("required_level"),
            'name': mod_data.get("name"),
            'is_essence_only': mod_data.get("is_essence_only"),
            'domain': mod_data.get('domain'),
            'generation_type': mod_data.get('generation_type'),
            'group': mod_data.get('groups')[0],
            'type': mod_data.get('type'),
            'added_tags_list': self.get_added_tags(mod_data),
            'implicit_tags_list': self.get_implicit_tags(mod_data),
            'spawn_weights_list': self.get_spawn_weights(mod_data),
            'stats_list': self.get_stats(mod_data)
        }
        return mod_dict


if __name__ == "__main__":
    mod_parser = ModParser()
    mod_list = mod_parser.get_all_mods()
    print(mod_list)
