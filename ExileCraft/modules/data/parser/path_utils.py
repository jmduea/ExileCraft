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


def get_base_dir(script_path):
    """Return the base directory, which is the project root directory."""
    base_dir = os.path.dirname(script_path)
    while os.path.basename(base_dir) != "ExileCraft":
        base_dir = os.path.dirname(base_dir)
    return base_dir


def get_rel_path_to_file(base_dir, dir_path, filename):
    """Return the relative path from the base directory to the given file."""
    return os.path.relpath(os.path.join(dir_path, filename), base_dir)


def get_abs_path(script_path, rel_path):
    """Return the absolute path to the given file."""
    base_dir = get_base_dir(script_path)
    return os.path.join(base_dir, rel_path)


def get_json_path(base_dir, sub_dir):
    return get_abs_path(base_dir, os.path.join(sub_dir, "json"))


def parse_json(abs_path):
    with open(abs_path, "r") as file:
        data = json.load(file)
    return data


base_dir = get_base_dir(os.path.realpath(__file__))
sub_dir = r"ExileCraft\modules\data"

MOD_TYPES_JSON_PATH = get_abs_path(
    get_base_dir(os.path.realpath(__file__)),
    os.path.join(r"ExileCraft\modules\data", "json", "mod_types.json"),
)

MOD_FAMILY_JSON_PATH = get_abs_path(
    get_base_dir(os.path.realpath(__file__)),
    os.path.join(r"ExileCraft\modules\data", "json", "mod_family.json"),
)

TRADE_MARKET_CATEGORY_GROUPS_JSON_PATH = get_abs_path(
    get_base_dir(os.path.realpath(__file__)),
    os.path.join(
        r"ExileCraft\modules\data", "json", "trade_market_category_groups.json"
    ),
)

TRADE_MARKET_CATEGORIES_JSON_PATH = get_abs_path(
    get_base_dir(os.path.realpath(__file__)),
    os.path.join(r"ExileCraft\modules\data", "json", "trade_market_categories.json"),
)

if __name__ == "__main__":
    pass
