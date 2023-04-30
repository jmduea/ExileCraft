import json
import sqlite3
import re
import random

from PyQt5 import QtGui
from PyQt5.QtCore import Qt



class UIUpdater:
    def __init__(self, item_class_combobox, item_subtype_combobox, base_item_combobox, base_item_level_combobox,
                 base_item_quality_combobox, base_item_influence_combobox, item_header_text_label,
                 ItemProperties, ItemRequirements, ItemImplicits, ItemSpacer3, Modifiers, item_img_box, main_window):
        self.item_img_box = item_img_box
        self.set_item_view_box_background = self.set_item_view_box_background
        self.item_header_text_label = item_header_text_label
        self.ItemProperties = ItemProperties
        self.ItemRequirements = ItemRequirements
        self.ItemImplicits = ItemImplicits
        self.ItemSpacer3 = ItemSpacer3
        self.ItemSpacer3.setVisible(False)
        self.ItemSpacer3.setEnabled(False)
        self.Modifiers = Modifiers
        self.Modifiers.setVisible(False)
        self.Modifiers.setEnabled(False)
        self.item_class_combobox = item_class_combobox
        self.item_subtype_combobox = item_subtype_combobox
        self.base_item_combobox = base_item_combobox
        self.base_item_level_combobox = base_item_level_combobox
        self.base_item_quality_combobox = base_item_quality_combobox
        self.base_item_influence_combobox = base_item_influence_combobox
        self.main_window = main_window
        self.Prefixes = main_window.Prefixes
        self.all_subtypes = {"armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                             "str_dex_int_armour", "str_int_armour"}
        self.subtype_display_names = {
            "armour": "Armour",
            "dex_armour": "Armour(dex)",
            "dex_int_armour": "Armour(dex/int)",
            "int_armour": "Armour(int)",
            "str_armour": "Armour(str)",
            "str_dex_armour": "Armour(str/dex)",
            "str_dex_int_armour": "Armour(str/dex/int)",
            "str_int_armour": "Armour(str/int)",
            "amulet": "Amulet",
        }
        self.subtype_original_names = {v: k for k, v in self.subtype_display_names.items()}
        self.base_item_influence_combobox.itemSelectionChanged.connect(self.limit_selection)
        self.item_class_combobox.currentTextChanged.connect(self.on_item_class_combobox_changed)
        self.item_subtype_combobox.currentTextChanged.connect(self.on_item_subtype_combobox_changed)
        self.item_class_combobox.setPlaceholderText("Select an item class")
        self.populate_item_class_combobox()
        self.base_item_combobox.currentTextChanged.connect(self.update_item_stats)
        self.base_item_quality_combobox.currentTextChanged.connect(
            lambda quality_text: self.update_item_stats(self.base_item_combobox.currentText(), quality_text)
        )
        self.base_item_level_combobox.currentTextChanged.connect(
            lambda item_level: self.update_item_stats(self.base_item_combobox.currentText(),
                                                      self.base_item_quality_combobox.currentText())
        )
        self.base_item_combobox.currentTextChanged.connect(self.set_item_view_box_background)
        self.base_item_combobox.currentTextChanged.connect(self.get_mods_for_item_class)
        base_item_combobox.currentTextChanged.connect(self.update_mods_data)

    def get_mods_for_item_class(self):
        conn = sqlite3.connect("exilecraft.db")
        cursor = conn.cursor()
        if self.base_item_combobox.currentText() is not None:
            item_name = self.base_item_combobox.currentText()
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
                    (SELECT MAX(weight) FROM modpool mp WHERE mp.mod_id = modpool.mod_id AND mp.valid_mod IS NOT NULL) AS max_weight
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
            print(mods_data)
            cursor.execute("DROP TABLE valid_mod_ids;")
            cursor.execute("DROP TABLE not_valid_mod_ids;")

            return mods_data

    def update_mods_data(self):
        mods_data = self.get_mods_for_item_class()
        generation_type = "prefix"
        # self.main_window.base_modpool_prefixes.clear()
        # self.main_window.base_modpool_prefixes.populate_with_mod_data(mods_data, generation_type)

    def set_item_view_box_background(self):
        current_base_item = self.base_item_combobox.currentText().replace(' ', '_').lower()
        image_path = f"assets/images/items/{current_base_item}.png"
        pixmap = QtGui.QPixmap(image_path)
        self.item_img_box.setPixmap(pixmap)
        self.item_img_box.setAlignment(Qt.AlignCenter)
        self.item_img_box.setScaledContents(False)

    def limit_selection(self):
        max_selections = 2
        selected_items = self.base_item_influence_combobox.selectedItems()

        if len(selected_items) > max_selections:
            last_selected_item = selected_items[-1]
            last_selected_item.setSelected(False)

    def populate_item_class_combobox(self):
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        c.execute('''SELECT DISTINCT base_items.item_class_id, item_classes.name 
                     FROM base_items 
                     JOIN item_classes ON base_items.item_class_id = item_classes.id 
                     ORDER BY base_items.item_class_id''')
        item_classes = c.fetchall()
        conn.close()
        self.item_class_combobox.clear()

        for item_class in item_classes:
            self.item_class_combobox.addItem(item_class[1])
        return self.item_class_combobox.currentText()

    def on_item_class_combobox_changed(self):
        item_class_name = self.item_class_combobox.currentText()
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()

        # Get the item_class_id from the item_classes table using the human-readable name
        c.execute('''SELECT id FROM item_classes WHERE name = ?''', (item_class_name,))
        item_class_id = c.fetchone()[0]

        if item_class_name == "Amulets":
            c.execute('''SELECT name FROM base_items WHERE item_class_id = ? AND tags NOT LIKE ?''',
                      (item_class_id, '%"talisman"%'))
        else:
            c.execute('''SELECT name FROM base_items WHERE item_class_id = ?''', (item_class_id,))

        base_items = c.fetchall()

        conn.close()
        self.populate_item_subtype_combobox()

        if self.item_subtype_combobox.currentIndex() == -1:
            self.item_subtype_combobox.setEnabled(False)
            self.item_subtype_combobox.setVisible(False)
            self.base_item_combobox.clear()
            self.base_item_combobox.setEnabled(True)
            self.base_item_combobox.setVisible(True)

            for base_item in base_items:
                self.base_item_combobox.addItem(base_item[0])
            self.base_item_level_combobox.setVisible(True)
            self.base_item_level_combobox.setEnabled(True)
            self.base_item_quality_combobox.setVisible(True)
            self.base_item_quality_combobox.setEnabled(True)
            self.base_item_influence_combobox.setVisible(True)
            self.base_item_influence_combobox.setEnabled(True)

    def filter_item_subtypes(self, selected_item_class_name, all_subtypes):
        selected_item_class_name = self.item_class_combobox.currentText()
        item_class_subtypes = {
            'Body Armours': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                             "str_dex_int_armour", "str_int_armour"},
            'Boots': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                      "str_int_armour"},
            'Gloves': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                       "str_int_armour"},
            'Helmets': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                        "str_int_armour"},
            'Shields': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"}
            # Add other item class to subtype mappings here
        }

        filtered_subtypes = item_class_subtypes.get(selected_item_class_name, set())
        filtered_subtypes.discard("not_for_sale")
        return filtered_subtypes

    def populate_item_subtype_combobox(self):
        selected_item_class_name = self.item_class_combobox.currentText()

        # Get valid subtypes for the selected item class
        valid_subtypes = self.filter_item_subtypes(selected_item_class_name, self.all_subtypes)
        # Connect to the database
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()

        # Get the item_class_id from the item_classes table using the human-readable name
        c.execute('''SELECT id FROM item_classes WHERE name = ?''', (selected_item_class_name,))
        item_class_id = c.fetchone()[0]
        # Execute a query to obtain the unique tags associated with the items from the selected item class
        c.execute('''SELECT DISTINCT tags FROM base_items WHERE item_class_id = ?''', (item_class_id,))
        tags = c.fetchall()
        # Close the database connection
        conn.close()

        # Populate the item subtype combobox with the filtered tags
        self.item_subtype_combobox.clear()
        for subtype in valid_subtypes:
            display_name = self.subtype_display_names.get(subtype, subtype)
            self.item_subtype_combobox.addItem(display_name)

        self.item_subtype_combobox.setVisible(True)
        self.item_subtype_combobox.setEnabled(True)

    def on_item_subtype_combobox_changed(self):
        item_subtype_display_name = self.item_subtype_combobox.currentText()
        item_subtype = self.subtype_original_names.get(item_subtype_display_name, item_subtype_display_name)
        self.base_item_combobox.clear()
        self.populate_base_item_combobox(item_subtype)
        self.base_item_combobox.setEnabled(True)
        self.base_item_combobox.setVisible(True)

    def populate_base_item_combobox(self, item_subtype):
        selected_item_class_name = self.item_class_combobox.currentText()

        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        # Get the item_class_id from the item_classes table using the human-readable name
        c.execute('''SELECT id FROM item_classes WHERE name = ?''', (selected_item_class_name,))
        item_class_id = c.fetchone()[0]
        c.execute('''SELECT name FROM base_items WHERE item_class_id = ? AND tags LIKE ? ORDER BY drop_level ASC''',
                  (item_class_id, f'%"{item_subtype}"%'))
        base_items = c.fetchall()
        self.base_item_combobox.clear()
        conn.close()

        for base_item in base_items:
            self.base_item_combobox.addItem(base_item[0])

        self.base_item_combobox.setVisible(True)
        self.base_item_combobox.setEnabled(True)
        self.base_item_level_combobox.setVisible(True)
        self.base_item_level_combobox.setEnabled(True)
        self.base_item_quality_combobox.setVisible(True)
        self.base_item_quality_combobox.setEnabled(True)
        self.base_item_influence_combobox.setVisible(True)
        self.base_item_influence_combobox.setEnabled(True)
        self.get_mods_for_item_class()

    def update_item_stats(self, base_item_name, quality_text=None):
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        c.execute('''SELECT drop_level, implicits, name, properties_attack_time,
                        properties_critical_strike_chance,properties_physical_damage_min,
                        properties_physical_damage_max, requirements_strength, requirements_dexterity,
                        requirements_intelligence, requirements_level, properties_armour, properties_evasion,
                        properties_energy_shield, properties_movement_speed, properties_block, properties_range
                     FROM base_items WHERE name = ?''', (base_item_name,))
        item_stats = c.fetchone()
        conn.close()

        if item_stats:
            drop_level, implicits, name, attack_time, critical_strike_chance, physical_damage_min,\
                physical_damage_max, req_strength, req_dexterity, req_intelligence, req_level,\
                armour, evasion, energy_shield, movement_speed, block, range = item_stats
            self.item_header_text_label.setText(f'Crafting Project \n {name}')

            quality_text = self.base_item_quality_combobox.currentText()
            if quality_text is None or quality_text == '':
                quality_value = int(self.base_item_quality_combobox.currentText() or 0)
            else:
                quality_value = int(quality_text)

            properties_list = [f'Quality: <span style="color:#8787fe;">{quality_text}</span>%']

            if block:
                properties_list.append(f'Block: {block}')
            if armour:
                armour_values = re.findall(r'(\d+)', armour)
                if len(armour_values) == 2:
                    min_armour, max_armour = map(int, armour_values)
                    avg_armour = ((min_armour + max_armour) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_armour = round(avg_armour)
                    properties_list.append(f'Armour: <span style="color:#8787fe;">{rounded_avg_armour}</span>')
            if evasion:
                evasion_values = re.findall(r'(\d+)', evasion)
                if len(evasion_values) == 2:
                    min_evasion, max_evasion = map(int, evasion_values)
                    avg_evasion = ((min_evasion + max_evasion) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_evasion = round(avg_evasion)
                    properties_list.append(f'Evasion: <span style="color:#8787fe;">{rounded_avg_evasion}</span>')
            if energy_shield:
                energy_shield_values = re.findall(r'(\d+)', energy_shield)
                if len(energy_shield_values) == 2:
                    min_energy_shield, max_energy_shield = map(int, energy_shield_values)
                    avg_energy_shield = ((min_energy_shield + max_energy_shield) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_energy_shield = round(avg_energy_shield)
                    properties_list.append(f'Energy Shield: <span style="color:#8787fe;">'
                                           f'{rounded_avg_energy_shield}</span>')
            if physical_damage_min and physical_damage_max:
                min_physical_damage, max_physical_damage = (int(physical_damage_min) * ((100 + quality_value) / 100)),\
                    (int(physical_damage_max) * ((100 + quality_value) / 100))
                adjusted_min_physical_damage = round(min_physical_damage)
                adjusted_max_physical_damage = round(max_physical_damage)
                properties_list.append(
                    f'<span style="color:#8787fe;">{adjusted_min_physical_damage}</span> To'
                    f' <span style="color:#8787fe;">{adjusted_max_physical_damage}</span> Physical Damage')

            if critical_strike_chance:
                properties_list.append(f'Critical Strike Chance: <span style="color:#FFF;">'
                                       f'{critical_strike_chance / 100:.2f}%</span>')
            if attack_time:
                properties_list.append(f'Attacks Per Second: <span style="color:#FFF;">{1000 / attack_time:.2f}</span>'
                                       if attack_time else '')

            self.ItemProperties.setText('<br>'.join(properties_list))

            item_level = self.base_item_level_combobox.currentText()
            if item_level is None or item_level == '':
                item_level = int(self.base_item_level_combobox.currentText() or 0)
            else:
                item_level = int(item_level)

            requirements_list = [f'Item Level: <span style="color:#FFF;">{item_level}</span><br>']

            if req_level:
                requirements_list.append(f'Requires Level: <span style="color:#FFF;">{req_level}</span>,')
            if req_strength:
                requirements_list.append(f'<span style="color:#FFF;">{req_strength}</span> Str')
            if req_dexterity:
                requirements_list.append(f'<span style="color:#FFF;">{req_dexterity}</span> Dex')
            if req_intelligence:
                requirements_list.append(f'<span style="color:#FFF;">{req_intelligence}</span> Int')

            self.ItemRequirements.setText(' '.join(requirements_list))

            self.ItemImplicits.setText('')
            self.ItemImplicits.setEnabled(False)
            self.ItemImplicits.setVisible(False)
            self.ItemSpacer3.setEnabled(False)
            self.ItemSpacer3.setVisible(False)

            if implicits:
                implicits_list = implicits.split('|')
                if implicits_list and len(implicits_list) > 0 and not (
                        len(implicits_list) == 1 and implicits_list[0] == '[]'):
                    print(implicits_list)

                    # Load the mods.json file
                    with open('data/json/mods.json', 'r') as f:
                        mods_data = json.load(f)

                    # Connect to the database
                    conn = sqlite3.connect('exilecraft.db')
                    cursor = conn.cursor()

                    # Create lists to store min and max value ranges
                    min_value_ranges = []
                    max_value_ranges = []

                    # Iterate over the mod_ids in the implicits_list
                    for mod_id in [mod.strip('\"[]') for mod in implicits_list]:
                        # Retrieve the mod data from mods_data
                        mod_data = mods_data[mod_id]

                        # Query the resolved_mod_stats table to get the min_translation_text,
                        # max_translation_text, min, and max values
                        cursor.execute(
                            "SELECT id, translation_text, min, max FROM resolved_mod_stats WHERE mod_id = ?",
                            (mod_id,))
                        rows = cursor.fetchall()

                        # Iterate over the rows
                        for row in rows:
                            id_, translation_text, min_value_range, max_value_range = row

                            # Split the string range into min and max values
                            if "-" in str(min_value_range):
                                min_value = [int(x) for x in str(min_value_range).split('-')]
                            else:
                                min_value = [int(min_value_range)]

                            if "-" in str(max_value_range):
                                max_value = [int(x) for x in str(max_value_range).split('-')]
                            else:
                                max_value = [int(max_value_range)]

                            # Add the min and max value ranges to their respective lists
                            min_value_ranges.append(f"{min_value[0]}" if len(min_value) > 1 else str(min_value[0]))
                            max_value_ranges.append(f"{max_value[0]}" if len(max_value) > 1 else str(max_value[0]))

                    # Format the final string
                    formatted_values = []
                    for min_val, max_val in zip(min_value_ranges, max_value_ranges):
                        if min_val == max_val:
                            formatted_values.append(min_val)
                        else:
                            formatted_values.append(f"({min_val}-{max_val})")
                            random_numbers = []

                            for value in formatted_values:
                                if '-' in value:
                                    min_val, max_val = value.strip('()').split('-')
                                    min_val, max_val = int(min_val), int(max_val)
                                    random_number = random.randint(min_val, max_val)
                                else:
                                    random_number = int(value)

                                random_numbers.append(random_number)

                            print(random_numbers)

                    if len(formatted_values) == 1 and min_val != max_val:
                        random_number = random_numbers[0]
                        final_parsed_string = translation_text.format(f"{random_number}{formatted_values[0]}")
                    elif len(formatted_values) == 1:
                        final_parsed_string = translation_text.format(f"{formatted_values[0]}")
                    elif len(formatted_values) == 2:
                        final_parsed_string = translation_text.format(f"{formatted_values[0]}",
                                                                      f"{formatted_values[1]}")
                    else:
                        # Handle other cases if necessary
                        pass

                    print(final_parsed_string)

                    if final_parsed_string:
                        self.ItemImplicits.setText(final_parsed_string)
                        self.ItemImplicits.setEnabled(True)
                        self.ItemImplicits.setVisible(True)
                        self.ItemSpacer3.setEnabled(True)
                        self.ItemSpacer3.setVisible(True)
                    else:
                        self.ItemImplicits.setText('')
                        self.ItemImplicits.setEnabled(False)
                        self.ItemImplicits.setVisible(False)
                        self.ItemSpacer3.setEnabled(False)
                        self.ItemSpacer3.setVisible(False)

                    conn.close()
