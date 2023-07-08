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

import unittest

from modules.data.parser import path_utils


class TestPathUtils(unittest.TestCase):
    def setUp(self):
        # This path should point to the location of the 'exilecraft.db' file
        self.correct_abs_path = r"\data\exilecraft.db"

        # This is the base directory from which the relative path to the 'exilecraft.db' file will be calculated
        self.base_dir = r"ExileCraft"

    def test_get_rel_path_to_db(self):
        rel_path = path_utils.get_rel_path_to_file(self.base_dir)
        self.assertEqual(rel_path, r"data\exilecraft.db")

    def test_get_abs_path(self):
        # This should be the path to the script that's calling get_abs_path
        script_path = "main.py"
        abs_path = path_utils.get_abs_path(script_path)
        self.assertEqual(abs_path, self.correct_abs_path)


if __name__ == '__main__':
    unittest.main()
