import json
import os
import sqlite3

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
print(script_path)
base_dir = get_base_dir(script_path)
print(base_dir)
abs_path_to_db = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'exilecraft.db'))
# Connect to SQLite database
print(abs_path_to_db)
conn = sqlite3.connect(abs_path_to_db)
c = conn.cursor()

# Load JSON data
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'fossils.json'))

with open(abs_path_to_json, 'r') as f:
    data = json.load(f)

# Iterate over each fossil in the data
for fossil_key, fossil in data.items():
    # Insert into fossils table
    c.execute("""
        INSERT INTO fossils (fossil_key, changes_quality, corrupted_essence_chance, enchants, mirrors, name, rolls_lucky,
         rolls_white_sockets)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (fossil_key, fossil['changes_quality'], fossil['corrupted_essence_chance'], fossil['enchants'], fossil['mirrors'], fossil['name'], fossil['rolls_lucky'], fossil['rolls_white_sockets']))

    # Get the id of the fossil we just inserted
    fossil_id = c.lastrowid

    # Insert into other tables
    for table, values in {
        'added_mods': fossil['added_mods'],
        'allowed_tags': fossil['allowed_tags'],
        'blocked_descriptions': fossil['blocked_descriptions'],
        'descriptions': fossil['descriptions'],
        'forbidden_tags': fossil['forbidden_tags'],
        'forced_mods': fossil['forced_mods'],
        'sell_price_mods': fossil['sell_price_mods']
    }.items():
        for value in values:
            c.execute(f"INSERT INTO {table} (fossil_id, {table[:-1]}) VALUES (?, ?)", (fossil_id, value))

    for weight in fossil['negative_mod_weights']:
        c.execute("INSERT INTO negative_mod_weights (fossil_id, tag, weight) VALUES (?, ?, ?)", (fossil_id, weight['tag'], weight['weight']))

    for weight in fossil['positive_mod_weights']:
        c.execute("INSERT INTO positive_mod_weights (fossil_id, tag, weight) VALUES (?, ?, ?)", (fossil_id, weight['tag'], weight['weight']))

# Commit changes and close connection
conn.commit()
conn.close()
