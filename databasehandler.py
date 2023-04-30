import sqlite3
import json

ITEM_CLASS_WHITELIST = {
    "LifeFlask",
    "ManaFlask",
    "HybridFlask",
    "Amulet",
    "Ring",
    "Claw",
    "Dagger",
    "Rune Dagger",
    "Wand",
    "One Hand Sword",
    "Thrusting One Hand Sword",
    "One Hand Axe",
    "One Hand Mace",
    "Bow",
    "Staff",
    "Warstaff",
    "Two Hand Sword",
    "Two Hand Axe",
    "Two Hand Mace",
    "Quiver",
    "Belt",
    "Gloves",
    "Boots",
    "Body Armour",
    "Helmet",
    "Shield",
    "Sceptre",
    "UtilityFlask",
    "UtilityFlaskCritical",
    "Jewel",
    "AbyssJewel",

}

ITEM_CLASS_BLACKLIST = {
    "LabyrinthTrinket",
    "MiscMapItem",
    "Leaguestone",
    "LabyrinthItem",
    "PantheonSoul",
    "UniqueFragment",
    "IncursionItem",
    "MetamorphosisDNA",
    "HideoutDoodad",
    "LabyrinthMapItem",
    "Incubator",
    "Microtransaction",
    "HarvestInfrastructure",
    "HarvestSeed",
    "HarvestPlantBooster",
    "Trinket",
    "HeistObjective",
    "HiddenItem",
    "ArchnemesisMod",
    "MemoryLine",
    "HeistContract",
    "HeistBlueprint",
    "HeistEquipmentWeapon",
    "HeistEquipmentTool",
    "HeistEquipmentUtility",
    "HeistEquipmentReward",
    "DivinationCard",
    "Map",
    "MapFragment",
    "AtlasRegionUpgradeItem",
    "ExpeditionLogbook",
    "IncubatorStackable",
    "AtlasUpgradeItem",
    "SentinelDrone",
    "DelveStackableSocketableCurrency",
    "DelveSocketableCurrency",
    "QuestItem",
    "StackableCurrency",
    "Active Skill Gem",
    "Support Skill Gem",
    "Currency",
    'FishingRod',
}

tags_map = {
    "Body Armour": {
        "Body Armour (dex)": ["armour", "dex_armour"],
        "Body Armour (dex/int)": ["armour", "dex_int_armour"],
        "Body Armour (dex/str)": ["armour", "dex_str_armour"],
        "Body Armour (dex/str/int)": ["armour", "dex_str_int_armour"],
        "Body Armour (str)": ["armour", "str_armour"],
        "Body Armour (str/int)": ["armour", "str_int_armour"],
        "Body Armour (int)": ["armour", "int_armour"],
    },
    # Define tags map for other item classes
}


class DatabaseHandler:
    def __init__(self, db_name='exilecraft.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def close(self):
        self.conn.close()

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
                        self.insert_condition(translation_info_id, condition.get("min"), condition.get("max"), condition.get("negated", False))
                print("inserting formatting info")
                # Insert formatting info
                self.insert_formatting_info(translation_info_id, translation_info["string"], translation_info["format"], translation_info["index_handlers"])

        # Commit the changes
        self.conn.commit()

    def create_tables(self):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                    CREATE TABLE IF NOT EXISTS tags (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mods (
                        mod_id TEXT PRIMARY KEY,
                        name TEXT,
                        required_level INTEGER,
                        domain INTEGER,
                        generation_type INTEGER,
                        is_essence_only BOOLEAN,
                        type TEXT
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_stats (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        stat_id TEXT,
                        min INTEGER,
                        max INTEGER,
                        FOREIGN KEY (mod_id) REFERENCES mods (id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_grants_effects (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        granted_effect_id TEXT,
                        level INTEGER,
                        FOREIGN KEY (mod_id) REFERENCES mods (id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_adds_tags (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        tag TEXT,
                        FOREIGN KEY (mod_id) REFERENCES mods (id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_groups (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        group_name TEXT,
                        FOREIGN KEY (mod_id) REFERENCES mods (id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_spawn_weights (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        tag TEXT,
                        weight INTEGER,
                        FOREIGN KEY (mod_id) REFERENCES mods (id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_generation_weights (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        tag TEXT,
                        weight INTEGER,
                        FOREIGN KEY (mod_id) REFERENCES mods (mod_id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS mod_implicit_tags (
                        id INTEGER PRIMARY KEY,
                        mod_id TEXT,
                        tag TEXT,
                        FOREIGN KEY (mod_id) REFERENCES mods (mod_id)
                    )
                ''')
            c.execute('''
                    CREATE TABLE IF NOT EXISTS resolved_mod_stats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        mod_id TEXT NOT NULL,
                        stat_id TEXT NOT NULL,
                        min INTEGER,
                        max INTEGER,
                        stat_name TEXT,
                        translation_object_id INTEGER,
                        FOREIGN KEY (mod_id) REFERENCES mods (mod_id),
                        FOREIGN KEY (stat_id) REFERENCES stat_ids (stat_id),
                        FOREIGN KEY (translation_object_id) REFERENCES translation_objects(id)
                    )
                ''')
            c.execute('''CREATE TABLE IF NOT EXISTS stat_translations
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              stat_id TEXT,
                              language TEXT,
                              condition TEXT,
                              format TEXT,
                              index_handlers TEXT,
                              translation TEXT,
                              formatting_info_id INTEGER,
                              FOREIGN KEY (stat_id) REFERENCES stat_ids (stat_id))''')
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='base_items'")
            if not c.fetchone():
                c.execute('''CREATE TABLE if NOT EXISTS base_items
                                 (id TEXT PRIMARY KEY,
                                  drop_level INTEGER,
                                  implicits TEXT,
                                  inventory_height INTEGER,
                                  inventory_width INTEGER,
                                  item_class TEXT,
                                  name TEXT,
                                  tags TEXT,
                                  visual_identity_id TEXT,
                                  visual_identity_dds_file TEXT,
                                  requirements_strength INTEGER,
                                  requirements_dexterity INTEGER,
                                  requirements_intelligence INTEGER,
                                  requirements_level INTEGER,
                                  properties_armour INTEGER,
                                  properties_evasion INTEGER,
                                  properties_energy_shield INTEGER,
                                  properties_movement_speed INTEGER,
                                  properties_block INTEGER,
                                  properties_life_per_use INTEGER,
                                  properties_mana_per_use INTEGER,
                                  properties_duration INTEGER,
                                  properties_charges_max INTEGER,
                                  properties_charges_per_use INTEGER,
                                  properties_critical_strike_chance INTEGER,
                                  properties_attack_time INTEGER,
                                  properties_physical_damage_max INTEGER,
                                  properties_physical_damage_min INTEGER,
                                  properties_range INTEGER,
                                  properties_stack_size INTEGER,
                                  properties_stack_size_currency_tab INTEGER,
                                  properties_directions TEXT,
                                  properties_description TEXT,
                                  properties_full_stack_turns_into TEXT,
                                  grants_buff_id TEXT,
                                  grants_buff_stats TEXT,
                                  domain TEXT,
                                  tag_id INTEGER REFERENCES tags(id)
                                  )
                            ''')
            conn.commit()

    def get_base_items_by_item_class(self, item_class):
        with self._connect() as conn:
            c = conn.cursor()
            c.execute('''
                SELECT base_items.name
                FROM base_items
                JOIN tags ON base_items.tag_id = tags.id
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

    def load_tags_from_json(self, db_handler, file_path):
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
        with open('data/json/base_items.json', 'r') as f:
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

            conn = sqlite3.connect('exilecraft.db')
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

    def insert_ids_to_database(self, json_filename, database_name):
        # Connect to the SQLite database
        conn = sqlite3.connect(database_name)

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

    def populate_stat_translations_table(self, json_file_path, db_file_path, table_name):
        # Open the JSON file and load the data
        with open(json_file_path) as f:
            data = json.load(f)

        # Connect to the SQLite database
        conn = sqlite3.connect(db_file_path)

        # Create a cursor object to execute SQL statements
        c = conn.cursor()

        # Loop through the objects in the JSON data
        for obj in data:
            # Get the id and string fields from the object
            id = obj.get('ids', [])[0]
            string = obj.get('English', [])[0].get('string')

            # Update the string field in the specified table for the given id
            c.execute(f'UPDATE {table_name} SET string = ? WHERE id = ?', (string, id))

        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

    def insert_resolved_stats(self):
        def find_translation_text(stat_id, stat_translations_data):
            for translation in stat_translations_data:
                if stat_id in translation.get("ids", []):
                    for language in translation:
                        if language != "ids":
                            for translation_obj in translation[language]:
                                if "string" in translation_obj:
                                    return translation_obj["string"]
            return None

        with open("data/json/stats.json", "r") as f:
            stats_data = json.load(f)

        with open("data/json/stat_translations.json", "r") as f:
            stat_translations_data = json.load(f)

        conn = sqlite3.connect("exilecraft.db")
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


import sqlite3
import json

def populate_modifiers_tags_table():
    conn = sqlite3.connect('exilecraft.db')
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
            cursor.execute("INSERT INTO translation (stat_translation_id, condition_min, condition_max, condition_negated, string, format, index_handlers) VALUES (?, ?, ?, ?, ?, ?, ?)",
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


def _get_stat_translations(tag_set, translations, custom_translations):
    previous = set()
    root = []
    for tr in translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            print("Duplicate id", tr.ids)
            continue
        previous.add(id_str)
        root.append(_convert(tr, tag_set))
    for tr in custom_translations:
        id_str = " ".join(tr.ids)
        if id_str in previous:
            continue
        previous.add(id_str)
        result = _convert(tr, tag_set)
        result["hidden"] = True
        root.append(result)
    return root

def get_stat_translation(conn, ids, stat_values):
    cursor = conn.cursor()

    # Query the stat_translation table
    cursor.execute("SELECT id, hidden FROM stat_translation WHERE ids = ?", (' '.join(ids),))
    stat_translation_data = cursor.fetchone()

    if stat_translation_data is None:
        return None

    stat_translation_id, hidden = stat_translation_data

    # Query the translation table
    cursor.execute("SELECT condition_min, condition_max, condition_negated, string, format, index_handlers FROM translation WHERE stat_translation_id = ?", (stat_translation_id,))
    translations = cursor.fetchall()

    for translation in translations:
        condition_min, condition_max, condition_negated, string, format_str, index_handlers = translation
        condition_min = [float(v) if v else float('-inf') for v in condition_min.split()]
        condition_max = [float(v) if v else float('inf') for v in condition_max.split()]
        condition_negated = [bool(condition_negated)]
        format_list = format_str.split()
        index_handlers = [handler.split() for handler in index_handlers.split()]

        all_conditions_met = True
        for i, (min_value, max_value, negated, value) in enumerate(zip(condition_min, condition_max, condition_negated, stat_values)):
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

if __name__ == "__main__":
    ids = ["local_physical_damage_+% local_weapon_no_physical_damage"]
    stat_values = [4]  # Use the appropriate stat values for the given ids
    conn = sqlite3.connect('exilecraft.db')
    translated_string, hidden = get_stat_translation(conn, ids, stat_values)
    if translated_string is not None:
        print(translated_string, "(Hidden)" if hidden else "")
    else:
        print("No translation found.")
