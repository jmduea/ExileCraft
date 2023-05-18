import sqlite3
from ..parser import path_utils


def get_base_item_stats(base_item_name):
    """
    Fetches the base item statistics from a SQLite database given a base item name.

    Parameters:
    base_item_name (str): The name of the base item to retrieve statistics for.

    Returns:
    tuple: Contains the following base item statistics:
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

    Note:
    The function uses the SQLite3 module to interact with the database and uses parameterized queries
    to prevent SQL injection attacks. Assumes the 'base_items' table exists in the 'exilecraft.db' database.
    """
    db_path = path_utils.get_abs_path(__file__)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''SELECT drop_level, implicits, name, properties_attack_time,
                        properties_critical_strike_chance,properties_physical_damage_min,
                        properties_physical_damage_max, requirements_strength, requirements_dexterity,
                        requirements_intelligence, requirements_level, properties_armour, properties_evasion,
                        properties_energy_shield, properties_movement_speed, properties_block, properties_range
                     FROM base_items WHERE name = ?''', (base_item_name,))
    item_stats = c.fetchone()
    conn.close()
    return item_stats
