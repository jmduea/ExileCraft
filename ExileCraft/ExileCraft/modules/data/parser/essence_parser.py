import json
import os
import sqlite3

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_db = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'exilecraft.db'))
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'json', 'essences.json'))

conn = sqlite3.connect(abs_path_to_db)
c = conn.cursor()

with open(abs_path_to_json, 'r') as f:
    data = json.load(f)

for essence_id, essence in data.items():
    c.execute(
        """
        INSERT INTO Essence (id, name, spawn_level_min, spawn_level_max, level, item_level_restriction, is_corruption_only, tier) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            essence_id,
            essence.get('name'),
            essence.get('spawn_level_min'),
            essence.get('spawn_level_max'),
            essence.get('level'),
            essence.get('item_level_restriction'),
            int(essence.get('type').get('is_corruption_only')),
            essence.get('type').get('tier'),
        ),
    )
    for item_class, mod in essence.get('mods').items():
        c.execute(
            """
            INSERT INTO EssenceMods (essence_id, item_class, mod)
            VALUES (?, ?, ?)
            """,
            (
                essence_id,
                item_class,
                mod,
            ),
        )

conn.commit()
conn.close()
