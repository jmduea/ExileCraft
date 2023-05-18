
# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock
from ExileCraft.ExileCraft.modules.db import get_base_item_stats

"""
Code Analysis

Objective:
The objective of the 'get_base_item_stats' function is to retrieve the statistics of a base item from a SQLite database given its name. The function returns a tuple containing various statistics of the base item.

Inputs:
- base_item_name (str): The name of the base item to retrieve statistics for.

Flow:
1. Connect to the 'exilecraft.db' database using the sqlite3 module.
2. Create a cursor object to execute SQL queries.
3. Execute a parameterized SQL query to retrieve the statistics of the base item with the given name from the 'base_items' table.
4. Fetch the result of the query and store it in the 'item_stats' variable.
5. Close the database connection.
6. Return the 'item_stats' tuple.

Outputs:
- tuple: Contains the following base item statistics:
    - drop_level
    - implicits
    - name
    - properties_attack_time
    - properties_critical_strike_chance
    - properties_physical_damage_min
    - properties_physical_damage_max
    - requirements_strength
    - requirements_dexterity
    - requirements_intelligence
    - requirements_level
    - properties_armour
    - properties_evasion
    - properties_energy_shield
    - properties_movement_speed
    - properties_block
    - properties_range

Additional aspects:
- The function uses parameterized queries to prevent SQL injection attacks.
- The function assumes that the 'base_items' table exists in the 'exilecraft.db' database.
"""


class TestGetBaseItemStats:
    #  Tests that the function returns the correct statistics for a valid base item name. Tags: [happy path]
    SQLITE3_CONNECT = 'sqlite3.connect'
    BASE_ITEM_NAME = 'Shabby Jerkin'

    def test_happy_path_get_base_item_stats(self, mocker):
        # Setup
        expected_stats = (1, "test implicits", "test name", 1.0, 5.0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 0, 5)
        mocker.patch("sqlite3.connect")
        mocker.patch("sqlite3.Cursor.execute", return_value=expected_stats)
        # Exercise
        result = get_base_item_stats("test name")
        # Verify
        assert result == expected_stats

    def test_edge_case_get_base_item_stats_invalid_name(self, mocker):
        # Setup
        mocker.patch("sqlite3.connect")
        mocker.patch("sqlite3.Cursor.execute", return_value=None)
        # Exercise
        result = get_base_item_stats("invalid name")
        # Verify
        assert result is None