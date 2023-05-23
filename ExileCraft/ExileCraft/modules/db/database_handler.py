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
#

import json
import sqlite3

from ..emu import CraftingProject
from ..parser import path_utils

rel_path_to_db = "data/exilecraft.db"  # replace this with the correct relative path
db_path = path_utils.get_abs_path(__file__, rel_path_to_db)


class DatabaseHandler:

    def update_item_influences(self, influence_btns):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        for button in influence_btns.buttons():
            # Get the column name from the button text, converted to lowercase and replacing spaces with underscores
            column_name = button.text().lower().replace(' ', '_') + '_item'

            # Check if this button is checked
            value = button.isChecked()

            # Update the SQLite database
            cursor.execute(
                f'UPDATE crafting_project SET {column_name} = ? WHERE id = (SELECT MAX(id) FROM crafting_project)',
                (value,))

        conn.commit()

    def get_crafting_project_data(self):
        conn = self.conn
        conn.row_factory = self.dict_factory
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crafting_project")
        crafting_project_data = cursor.fetchone()
        conn.close()
        if crafting_project_data:
            return CraftingProject(crafting_project_data)
        else:
            return None

    def get_last_crafting_project_base_item_id(self):
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute('SELECT base_item_id FROM crafting_project ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()

        conn.close()

        if result is not None:
            return result[0]  # Return the base_item_id of the most recently added row
        else:
            return None  # Return None if the table is empty

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def update_crafting_project(self, crafting_project):
        self.cursor.execute("""
            UPDATE crafting_project
            SET item_class_id = ?,
                rarity = ?,
                name = ?,
                base_item_id = ?,
                quality = ?,
                item_level = ?,
                sockets = ?,
                enchant = ?,
                physical_damage_min = ?,
                physical_damage_max = ?,
                cold_damage_min = ?,
                cold_damage_max = ?,
                fire_damage_min = ?,
                fire_damage_max = ?,
                lightning_damage_min = ?,
                lightning_damage_max = ?,
                chaos_damage_min = ?,
                chaos_damage_max = ?,
                critical_strike_chance = ?,
                attacks_per_second = ?,
                requirements_level = ?,
                requirements_str = ?,
                requirements_dex = ?,
                requirements_int = ?,
                prefix_modifier_1 = ?,
                prefix_modifier_2 = ?,
                prefix_modifier_3 = ?,
                suffix_modifier_1 = ?,
                suffix_modifier_2 = ?,
                suffix_modifier_3 = ?,
                shaper_item = ?,
                elder_item = ?,
                hunter_item = ?,
                redeemer_item = ?,
                crusader_item = ?,
                warlord_item = ?,
                synthesis_item = ?,
                implicits = ?,
                item_tags = ?,
                properties_armour = ?,
                properties_evasion = ?,
                properties_energy_shield = ?,
                properties_movement_speed = ?,
                properties_block = ?,
                properties_range = ?
            WHERE id = ?
        """, (
            crafting_project.item_class_id, crafting_project.rarity, crafting_project.name,
            crafting_project.base_item_id,
            crafting_project.quality,
            crafting_project.item_level, crafting_project.sockets, crafting_project.enchant,
            crafting_project.physical_damage_min, crafting_project.physical_damage_max,
            crafting_project.cold_damage_min, crafting_project.cold_damage_max, crafting_project.fire_damage_min,
            crafting_project.fire_damage_max,
            crafting_project.lightning_damage_min, crafting_project.lightning_damage_max,
            crafting_project.chaos_damage_min,
            crafting_project.chaos_damage_max,
            crafting_project.critical_strike_chance, crafting_project.attacks_per_second,
            crafting_project.requirements_level, crafting_project.requirements_str,
            crafting_project.requirements_dex, crafting_project.requirements_int, crafting_project.prefix_modifier_1,
            crafting_project.prefix_modifier_2,
            crafting_project.prefix_modifier_3, crafting_project.suffix_modifier_1, crafting_project.suffix_modifier_2,
            crafting_project.suffix_modifier_3,
            crafting_project.shaper_item, crafting_project.elder_item, crafting_project.hunter_item,
            crafting_project.redeemer_item, crafting_project.crusader_item,
            crafting_project.warlord_item, crafting_project.synthesis_item, crafting_project.implicits,
            crafting_project.item_tags, crafting_project.properties_armour,
            crafting_project.properties_evasion, crafting_project.properties_energy_shield,
            crafting_project.properties_movement_speed, crafting_project.properties_block,
            crafting_project.properties_range, crafting_project.id))

        self.conn.commit()
        self.close()

    @staticmethod
    def update_item_class_id(item_class_id):
        conn = sqlite3.connect('data/exilecraft.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT OR REPLACE INTO crafting_project (item_class_id)
                            VALUES (?)''', (item_class_id,))
        conn.commit()
        conn.close()

    def fetch_item_stats(self, base_item):
        conn = self.conn
        c = conn.cursor()
        c.execute('''SELECT drop_level, implicits, name, properties_attack_time,
                            properties_critical_strike_chance,properties_physical_damage_min,
                            properties_physical_damage_max, requirements_strength, requirements_dexterity,
                            requirements_intelligence, requirements_level, properties_armour, properties_evasion,
                            properties_energy_shield, properties_movement_speed, properties_block, properties_range
                         FROM base_items WHERE name = ?''', (base_item,))
        item_stats = c.fetchone()
        conn.close()
        return item_stats

    def insert_base_item_into_crafting_project(self, base_item_name):
        conn = self.conn
        cursor = conn.cursor()

        cursor.execute('''with base_item as
                        (SELECT item_class_id,
                         name,
                         properties_physical_damage_min,
                         properties_physical_damage_max,
                         properties_critical_strike_chance,
                         properties_attack_time,
                         requirements_level,
                         requirements_strength,
                         requirements_dexterity,
                         requirements_intelligence,
                         implicits,
                         tags,
                         properties_armour,
                         properties_evasion,
                         properties_energy_shield,
                            properties_movement_speed,
                            properties_block,
                            properties_range
                        FROM base_items
                        WHERE name = ?)
        INSERT or REPLACE INTO crafting_project (
                        item_class_id,
                        base_item_id,
                        physical_damage_min,
                        physical_damage_max,
                        critical_strike_chance,
                        attacks_per_second,
                        requirements_level,
                        requirements_str,
                        requirements_dex,
                        requirements_int,
                        implicits,
                        item_tags,
                        properties_armour,
                        properties_evasion,
                        properties_energy_shield,
                        properties_movement_speed,
                        properties_block,
                        properties_range
                    )
                    select *
                    from base_item
        ''', (base_item_name,))
        conn.commit()
        conn.close()

    def insert_stat_translations(self, json_file):
        with open(json_file) as f:
            data = json.load(f)

        for translation_obj in data:
            print("Inserting translation objects..")
            # Insert the translation object
            translation_object_id = self.insert_translation_object(translation_obj.get("hidden", False))

            # Insert stat ids
            print("Inserting stat_id..")
            for stat_id in translation_obj["ids"]:
                self.insert_stat_id(translation_object_id, stat_id)

            # Insert translation info
            print("Inserting translation_info")
            for translation_info in translation_obj["English"]:
                translation_info_id = self.insert_translation_info(translation_object_id)

                # Insert conditions if they exist
                print("Inserting Conditions..")
                if "conditions" in translation_info:
                    for condition in translation_info["condition"]:
                        self.insert_condition(translation_info_id, condition.get("min"), condition.get("max"),
                                              condition.get("negated", False))
                print("inserting formatting info")
                # Insert formatting info
                self.insert_formatting_info(translation_info_id, translation_info["string"], translation_info["format"],
                                            translation_info["index_handlers"])

        # Commit the changes
        self.conn.commit()

    def get_base_items_by_item_class(self, item_class):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT base_items.name
                FROM base_items
                JOIN tags ON base_items.tags = tags.id
                WHERE base_items.item_class_id = ?
            ''', (item_class,))
            base_items = c.fetchall()
        return base_items

    def get_tags(self):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT * FROM tags
            ''')
            tags = c.fetchall()
        return tags

    @staticmethod
    def load_tags_from_json(db_handler, file_path):
        with open(file_path, 'r') as file:
            tag_names = json.load(file)

        tags = {tag_name: tag_name for tag_name in tag_names}

        for tag_key, tag_name in tags.items():
            db_handler.insert_tag(tag_name)

    def insert_tag(self, tag_name):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                INSERT OR IGNORE INTO tags (name)
                VALUES (?)
            ''', (tag_name,))
            conn.commit()
        print(tag_name)

    @staticmethod
    def load_base_items():
        with open('../../data/json/base_items.json', 'r') as f:
            data = json.load(f)

            base_items = []
            for base_item_id, base_item in data.items():
                if base_item['item_class'] in ITEM_CLASS_BLACKLIST:
                    # Skip base items that are not equippable items
                    continue

                item_class = base_item['item_class']
                tag_map = tags_map.get(item_class)

                if tag_map:
                    item_tags = set(base_item.get('tags', []))
                    filtered_tags = [tag for tag in item_tags if tag in tag_map.values()]
                    filtered_tags.sort(key=lambda tag: list(tag_map.values()).index(tag))
                    base_item['tags_map'] = {key: key in filtered_tags for key in tag_map.keys()}

                base_item_row = [
                    base_item_id,
                    base_item.get('drop_level'),
                    json.dumps(base_item.get('implicits')),
                    base_item.get('inventory_height'),
                    base_item.get('inventory_width'),
                    base_item.get('item_class'),
                    base_item.get('name'),
                    json.dumps(base_item.get('tags')),
                    base_item.get('visual_identity', {}).get('id'),
                    base_item.get('visual_identity', {}).get('dds_file'),
                    base_item.get('requirements', {}).get('strength') if base_item.get(
                        'requirements') is not None else None,
                    base_item.get('requirements', {}).get('dexterity') if base_item.get(
                        'requirements') is not None else None,
                    base_item.get('requirements', {}).get('intelligence') if base_item.get(
                        'requirements') is not None else None,
                    base_item.get('requirements', {}).get('level') if base_item.get(
                        'requirements') is not None else None,
                    json.dumps(base_item.get('properties', {}).get('armour')),
                    json.dumps(base_item.get('properties', {}).get('evasion')),
                    json.dumps(base_item.get('properties', {}).get('energy_shield')),
                    base_item.get('properties', {}).get('movement_speed'),
                    base_item.get('properties', {}).get('block'),
                    base_item.get('properties', {}).get('life_per_use'),
                    base_item.get('properties', {}).get('mana_per_use'),
                    base_item.get('properties', {}).get('duration'),
                    base_item.get('properties', {}).get('charges_max'),
                    base_item.get('properties', {}).get('charges_per_use'),
                    base_item.get('properties', {}).get('critical_strike_chance'),
                    base_item.get('properties', {}).get('attack_time'),
                    base_item.get('properties', {}).get('physical_damage_max'),
                    base_item.get('properties', {}).get('physical_damage_min'),
                    base_item.get('properties', {}).get('range'),
                    base_item.get('properties', {}).get('stack_size'),
                    base_item.get('properties', {}).get('stack_size_currency_tab'),
                    base_item.get('properties', {}).get('directions'),
                    base_item.get('properties', {}).get('description'),
                    base_item.get('properties', {}).get('full_stack_turns_into'),
                    base_item.get('grants_buff', {}).get('id'),
                    json.dumps(base_item.get('grants_buff', {}).get('stats')),
                    base_item.get('domain'),
                ]
                base_items.append(base_item_row)

            conn = self.conn
            c = conn.cursor()
            # Insert a row only if the id is not already present in the table
            c.execute("SELECT id FROM base_items WHERE id=?", (base_item_id,))
            res = c.fetchone()
            if res is None:
                c.execute(
                    'INSERT INTO base_items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                    ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', base_item_row)
            conn.commit()
            conn.close()

            return base_items

    @staticmethod
    def insert_ids_to_database(json_filename, database_name):
        # Connect to the SQLite database
        conn = self.conn

        # Create a cursor object to execute SQL statements
        c = conn.cursor()

        # Create the stat_translations table if it doesn't already exist
        c.execute('CREATE TABLE IF NOT EXISTS stat_translations (id TEXT PRIMARY KEY)')

        # Load the data from the JSON file
        with open(json_filename) as f:
            data = json.load(f)

        # Extract the "ids" field from each object and insert the values into the table
        for obj in data:
            ids = obj.get('ids')
            if ids:
                for id in ids:
                    c.execute('INSERT OR IGNORE INTO stat_translations (id) VALUES (?)', (id,))

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

    @staticmethod
    def populate_stat_translations_table(json_file_path, db_file_path, table_name):
        # Open the JSON file and load the data
        with open(json_file_path) as f:
            data = json.load(f)

        # Connect to the SQLite database
        conn = self.conn

        # Create a cursor object to execute SQL statements
        c = conn.cursor()

        # Loop through the objects in the JSON data
        for obj in data:
            # Get the id and string fields from the object
            _id = obj.get('ids', [])[0]
            string = obj.get('English', [])[0].get('string')

            # Update the string field in the specified table for the given id
            c.execute(f'UPDATE {table_name} SET string = ? WHERE id = ?', (string, _id))

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

    @staticmethod
    def insert_resolved_stats():
        def find_translation_text(stat_id, stat_translations_data):
            for translation in stat_translations_data:
                if stat_id in translation.get("ids", []):
                    for language in translation:
                        if language != "ids":
                            for translation_obj in translation[language]:
                                if "string" in translation_obj:
                                    return translation_obj["string"]
            return None

        with open("../../data/json/stats.json", "r") as f:
            stats_data = json.load(f)

        with open("../../data/json/stat_translations.json", "r") as f:
            stat_translations_data = json.load(f)

        conn = self.conn
        cursor = conn.cursor()

        # Query the mod_stats table
        cursor.execute("SELECT mod_id, stat_id, min, max FROM mod_stats")
        rows = cursor.fetchall()

        # Resolve the stat ids and convert them to text
        for row in rows:
            mod_id, stat_id, min_value, max_value = row
            stat_info = stats_data.get(stat_id)
            if stat_info:
                translation_text = find_translation_text(stat_id, stat_translations_data)
                if translation_text:
                    print(
                        f"mod_id: {mod_id}, stat_id: {stat_id}, stat_info: {stat_info}, translation_text: {translation_text}")
                    cursor.execute("""
                        INSERT INTO resolved_mod_stats (mod_id, stat_id, min, max, stat_name, translation_text)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        mod_id,
                        stat_id,
                        min_value,
                        max_value,
                        stat_info.get("name"),
                        translation_text
                    ))
                    print(f"Rows affected: {cursor.rowcount}")
                else:
                    print(f"No translation found for stat_id: {stat_id}")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def import_item_classes(self, json_file):
        with open(json_file) as f:
            item_classes_data = json.load(f)

        for item_class_id, item_class_data in item_classes_data.items():
            self.cursor.execute(
                "INSERT INTO item_classes (id, name) VALUES (?, ?)",
                (item_class_id, item_class_data["name"])
            )

        self.conn.commit()

    def load_mods_json(json_file):
        with open(json_file, "r") as f:
            data = json.load(f)
        return data

    def insert_mods_to_db(conn, mods_data):
        cursor = conn.cursor()

        for mod_id, mod_data in mods_data.items():
            cursor.execute(
                '''
                INSERT INTO modifiers (id, name, required_level, stats, grants_effects, adds_tags, domain, generation_type, groups, is_essence_only, spawn_weights, generation_weights, type, implicit_tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    mod_id,
                    mod_data.get("name", ""),
                    mod_data.get("required_level", 0),
                    json.dumps(mod_data.get("stats", [])),
                    json.dumps(mod_data.get("grants_effects", [])),
                    json.dumps(mod_data.get("adds_tags", [])),
                    mod_data.get("domain", ""),
                    mod_data.get("generation_type", ""),
                    json.dumps(mod_data.get("groups", [])),
                    mod_data.get("is_essence_only", False),
                    json.dumps(mod_data.get("spawn_weights", [])),
                    json.dumps(mod_data.get("generation_weights", [])),
                    mod_data.get("type", ""),
                    json.dumps(mod_data.get("implicit_tags", []))
                )
            )
        conn.commit()

    def get_translation_text_by_id(self, stat_id):
        query = "SELECT translation_text FROM resolved_mod_stats WHERE stat_id = ?"
        self.cursor.execute(query, (stat_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None


def populate_modifiers_tags_table():
    conn = DatabaseHandler.conn
    c = conn.cursor()

    # Get all the tags from the tags table
    c.execute("SELECT * FROM tags")
    tags = c.fetchall()

    # Loop through each tag
    for tag in tags:
        tag_id = tag[0]
        tag_name = tag[1]

        # Get all mods that have a positive spawn weight for this tag
        c.execute("""
            SELECT DISTINCT modifiers.*
            FROM modifiers, json_each(modifiers.spawn_weights)
            WHERE json_extract(json_each.value, '$.tag') = ?
            AND json_extract(json_each.value, '$.weight') > 0
        """, (tag_name,))

        mods = c.fetchall()

        # Loop through each mod and insert a record into the modifiers_tags table
        for mod in mods:
            mod_id = mod[0]

            c.execute("""
                INSERT INTO modifiers_tags (modifier_id, tag_id)
                VALUES (?, ?)
            """, (mod_id, tag_id))

    conn.commit()
    conn.close()


# Use this function to store the translations in the SQLite database
def store_translations(conn, stat_translations):
    cursor = conn.cursor()

    for tr in stat_translations:
        # Insert stat_translation entry
        cursor.execute("INSERT INTO stat_translation (ids, hidden) VALUES (?, ?)",
                       (' '.join(tr['ids']), int(tr.get('hidden', False))))
        stat_translation_id = cursor.lastrowid

        for eng in tr['English']:
            # Insert translation entry
            conditions = eng['condition']
            cursor.execute(
                "INSERT INTO translation (stat_translation_id, condition_min, condition_max, condition_negated, string, format, index_handlers) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (stat_translation_id,
                 ' '.join([str(c.get('min', '')) for c in conditions]),
                 ' '.join([str(c.get('max', '')) for c in conditions]),
                 ' '.join([str(int(c.get('negated', False))) for c in conditions]),
                 eng['string'],
                 ' '.join(eng['format']),
                 ' '.join([' '.join(h) for h in eng['index_handlers']])))
    conn.commit()


def _convert_tags(n_ids, tags, tags_types):
    f = ["ignore" for _ in range(n_ids)]
    for tag, tag_type in zip(tags, tags_types):
        if tag_type == "+d":
            f[tag] = "+#"
        elif tag_type == "d":
            f[tag] = "#"
        elif tag_type == "":
            f[tag] = "#"
        else:
            print("Unknown tag type:", tag_type)
    return f


def _convert_range(translation_range):
    rs = []
    for r in translation_range:
        r_dict = {}
        if r.min is not None:
            r_dict["min"] = r.min
        if r.max is not None:
            r_dict["max"] = r.max
        if r.negated:
            r_dict["negated"] = True
        rs.append(r_dict)
    return rs


def _convert_handlers(n_ids, index_handlers):
    hs = [[] for _ in range(n_ids)]
    for handler_name, ids in index_handlers.items():
        for i in ids:
            # Indices in the handler dict are 1-based
            hs[i - 1].append(handler_name)
    return hs


def _convert(tr, tag_set):
    ids = tr.ids
    n_ids = len(ids)
    english = []
    for s in tr.get_language("English").strings:
        tags = _convert_tags(n_ids, s.tags, s.tags_types)
        tag_set.update(tags)
        english.append(
            {
                "condition": _convert_range(s.range),
                "string": s.as_format_string,
                "format": tags,
                "index_handlers": _convert_handlers(n_ids, s.quantifier.index_handlers),
            }
        )
    return {"ids": ids, "English": english}


def get_stat_translation(conn, ids, stat_values):
    cursor = conn.cursor()

    # Query the stat_translation table
    cursor.execute("SELECT id, hidden FROM stat_translation WHERE ids = ?", (' '.join(ids),))
    stat_translation_data = cursor.fetchone()

    if stat_translation_data is None:
        return None

    stat_translation_id, hidden = stat_translation_data

    # Query the translation table
    cursor.execute("SELECT condition_min, condition_max, condition_negated, string, format, index_handlers FROM "
                   "translation WHERE stat_translation_id = ?", (stat_translation_id,))
    translations = cursor.fetchall()

    for translation in translations:
        condition_min, condition_max, condition_negated, string, format_str, index_handlers = translation
        condition_min = [float(v) if v else float('-inf') for v in condition_min.split()]
        condition_max = [float(v) if v else float('inf') for v in condition_max.split()]
        condition_negated = [bool(condition_negated)]
        format_list = format_str.split()
        index_handlers = [handler.split() for handler in index_handlers.split()]

        all_conditions_met = True
        for i, (min_value, max_value, negated, value) in enumerate(
                zip(condition_min, condition_max, condition_negated, stat_values)):
            condition_met = min_value <= value <= max_value
            if negated:
                condition_met = not condition_met
            if not condition_met:
                all_conditions_met = False
                break

        if all_conditions_met:
            # Build the translated string
            translated_string = string
            for i, (value, fmt, handlers) in enumerate(zip(stat_values, format_list, index_handlers)):
                for handler in handlers:
                    # Apply index_handlers here if any
                    pass

                if fmt == "#":
                    formatted_value = str(value)
                elif fmt == "+#":
                    formatted_value = f"+{value}" if value >= 0 else str(value)
                else:  # ignore
                    continue

                translated_string = translated_string.replace(f"{{{i}}}", formatted_value)

            return translated_string, hidden

    return None
