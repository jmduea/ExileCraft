import sqlite3
import json
import os

from modules.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_db = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'exilecraft.db'))
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\data', 'json', 'essences.json'))
conn = sqlite3.connect(abs_path_to_db)
c = conn.cursor()

with open(abs_path_to_json, 'r') as f:
    data = json.load(f)

conn.commit()
conn.close()
