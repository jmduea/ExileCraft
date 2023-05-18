import sqlite3
import json
from ..parser import path_utils
def get_mods_for_item_class(self, item_name):
    """
        Retrieves and returns the modifiers for a selected item class from the SQLite database 'exilecraft.db'.

        The method executes multiple SQL queries to retrieve and filter the modifiers based on the item tags.
        Temporary tables are used to keep track of valid and non-valid modifier IDs.

        The final list of modifiers is unique and only includes those that are valid for the item class,
        belong to the 'item' domain, and have a generation type of either 'prefix', 'suffix', 'eater_implicit',
        or 'exarch_implicit'.

        :param self: Reference to the instance of the class.

        :param item_name: Reference to the current crafting project's item name.

        :return: A list of unique modifiers for the selected item class. Each modifier is a tuple
                 with the structure defined in the 'modifiers' table of the 'exilecraft.db' database.
                 Returns an empty list if no modifiers are found or if no item is selected.
        """
    db_path = path_utils.get_abs_path(__file__)
    print(f"Database Path: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    item_tags = []
    cursor.execute("""
        SELECT
            tags
        FROM
            base_items
        WHERE
            name = ?
    """, (item_name,))
    item_tags_result = cursor.fetchall()
    if item_tags_result is None or not item_tags_result:
        return []
    item_tags_string = item_tags_result[0][0]

    item_tags = json.loads(item_tags_string)
    cursor.execute("""CREATE TEMPORARY TABLE valid_mod_ids (mod_id TEXT PRIMARY KEY, weight INTEGER);""")
    cursor.execute("""CREATE TEMPORARY TABLE not_valid_mod_ids (mod_id TEXT PRIMARY KEY);""")
    mods_data = []
    for tag in item_tags:
        # Query to get mod_ids with a spawn weight of 0
        cursor.execute("""
        WITH modpool AS (
        SELECT spawn_weights.mod_id,
            (CASE
                WHEN spawn_weights.tag_id = ? AND spawn_weights.weight = 0
                THEN 'not_valid_mod'
                ELSE NULL
            END) AS not_valid_mod,
            (CASE
                WHEN spawn_weights.tag_id = ? AND spawn_weights.weight > 0
                THEN 'valid_mod'
                ELSE NULL
            END) AS valid_mod
        FROM spawn_weights)
        INSERT OR IGNORE INTO not_valid_mod_ids (mod_id)
        SELECT modpool.mod_id
        FROM modpool
        WHERE modpool.not_valid_mod IS NOT NULL;
        """, (tag, tag))

        cursor.execute("""
        WITH modpool AS (
            SELECT spawn_weights.mod_id, spawn_weights.weight,
                (CASE
                    WHEN spawn_weights.tag_id = ? AND spawn_weights.weight = 0
                    THEN 'not_valid_mod'
                    ELSE NULL
                END) AS not_valid_mod,
                (CASE
                    WHEN spawn_weights.tag_id = ? AND spawn_weights.weight > 0
                    THEN 'valid_mod'
                    ELSE NULL
                END) AS valid_mod
            FROM spawn_weights)
        INSERT OR REPLACE INTO valid_mod_ids (mod_id, weight)
        SELECT modpool.mod_id,
            (SELECT MAX(weight) FROM modpool mp WHERE mp.mod_id = modpool.mod_id AND mp.valid_mod IS NOT NULL)
             AS max_weight
        FROM modpool
        WHERE modpool.valid_mod IS NOT NULL;
        """, (tag, tag))

        cursor.execute("""
        SELECT
            modifiers.*
        FROM
            modifiers
        JOIN
            valid_mod_ids ON valid_mod_ids.mod_id = modifiers.id
        LEFT JOIN
            not_valid_mod_ids ON not_valid_mod_ids.mod_id = modifiers.id
        WHERE
            not_valid_mod_ids.mod_id IS NULL
            AND modifiers.domain = 'item'
            AND (modifiers.generation_type IN ('prefix', 'suffix', 'eater_implicit', 'exarch_implicit'));
        """)
        results = cursor.fetchall()
        mods_data.extend(results)
    mods_data = list(set(mods_data))
    cursor.execute("DROP TABLE valid_mod_ids;")
    cursor.execute("DROP TABLE not_valid_mod_ids;")

    return mods_data
