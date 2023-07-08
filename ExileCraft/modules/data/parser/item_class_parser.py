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

from modules.config.constants import item_class_whitelist
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'item_classes.min.json'))


def insert_item_classes_into_db(db_manager):
    with open(abs_path_to_json) as json_file:
        data = json.load(json_file)
        
    with db_manager.transaction() as session:
        for item_class, item_data in data.items():
            if item_class in item_class_whitelist:
                item_class_dict = {
                    "name": item_class,
                    "display_name": item_data.get("name")
                }
                db_manager.add_item_classes(item_class_dict, session)
