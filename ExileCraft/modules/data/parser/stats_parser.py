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
import logging
import os

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'stats.min.json'))


class StatParser:
    def __init__(self):
        self._data = self.parse_json()
        self.abs_path_to_json = abs_path_to_json
    
    def parse_json(self):
        if not hasattr(self, '_data'):
            with open(abs_path_to_json) as json_file:
                self._data = json.load(json_file)
        return self._data
    
    def get_all_stats(self):
        data = self._data
        stat_list = []
        for stat_name, stat_data in data.items():
            # alias_string = ""
            # alias = alias_string.join(stats.get("alias"))
            stats_dict = {
                "name": stat_name,
                "is_aliased": stat_data.get("is_aliased", False),
                "is_local": stat_data.get("is_local", False)
            }
            stat_list.append(stats_dict)
        return stat_list
            