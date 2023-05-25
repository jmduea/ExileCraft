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
