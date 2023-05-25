import json
import os
import sqlite3

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_db = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'exilecraft.db'))
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'json', 'stats.json'))
conn = sqlite3.connect(abs_path_to_db)
c = conn.cursor()

with open(abs_path_to_json, 'r') as f:
    data = json.load(f)

for stat_key, stat in data.items():
    # Insert into stats table
    c.execute("""
        INSERT INTO stats (stat_key, is_aliased, is_local)
        VALUES (?, ?, ?)
    """, (stat_key, stat['is_aliased'], stat['is_local']))

    # Get the id of the stat we just inserted
    stat_id = c.lastrowid

    # Insert aliases
    for alias_key, alias_value in stat['alias'].items():
        c.execute("""
            INSERT INTO alias (stat_id, alias_key, alias_value)
            VALUES (?, ?, ?)
        """, (stat_id, alias_key, alias_value))

conn.commit()
conn.close()
