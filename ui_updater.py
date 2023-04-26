import json
import sqlite3
import re
import random
import builtins

class UIUpdater:
    def __init__(self, item_class_combobox, item_subtype_combobox, base_item_combobox, base_item_level_combobox,
                 base_item_quality_combobox, base_item_influence_combobox, item_header_text_label,
                 ItemProperties, ItemRequirements, ItemImplicits, ItemSpacer3, Modifiers):
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
        self.all_subtypes = {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                             "str_dex_int_armour", "str_int_armour"}
        self.subtype_display_names = {
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

    def limit_selection(self):
        max_selections = 2
        selected_items = self.base_item_influence_combobox.selectedItems()

        if len(selected_items) > max_selections:
            last_selected_item = selected_items[-1]
            last_selected_item.setSelected(False)

    def populate_item_class_combobox(self):
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        c.execute('''SELECT DISTINCT item_class FROM base_items ORDER BY item_class''')
        item_classes = c.fetchall()
        conn.close()
        self.item_class_combobox.clear()

        for item_class in item_classes:
            self.item_class_combobox.addItem(item_class[0])
        return self.item_class_combobox.currentText()

    def on_item_class_combobox_changed(self):
        item_class = self.item_class_combobox.currentText()

        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()

        if item_class == "Amulet":
            c.execute('''SELECT name FROM base_items WHERE item_class = ? AND tags NOT LIKE ?''',
                      (item_class, '%"talisman"%'))
        else:
            c.execute('''SELECT name FROM base_items WHERE item_class = ?''', (item_class,))

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

    def filter_item_subtypes(self, selected_item_class, all_subtypes):
        selected_item_class = self.item_class_combobox.currentText()
        item_class_subtypes = {
            'Body Armour': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                            "str_dex_int_armour", "str_int_armour"},
            'Boots': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"},
            'Gloves': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"},
            'Helmet': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"},
            'Shield': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"}
            # Add other item class to subtype mappings here
        }

        filtered_subtypes = item_class_subtypes.get(selected_item_class, set())
        filtered_subtypes.discard("not_for_sale")
        print(filtered_subtypes)
        return filtered_subtypes

    def populate_item_subtype_combobox(self):
        selected_item_class = self.item_class_combobox.currentText()

        # Get valid subtypes for the selected item class
        valid_subtypes = self.filter_item_subtypes(selected_item_class, self.all_subtypes)
        print(valid_subtypes)
        # Connect to the database
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()

        # Execute a query to obtain the unique tags associated with the items from the selected item class
        c.execute('''SELECT DISTINCT tags FROM base_items WHERE item_class = ?''', (selected_item_class,))
        tags = c.fetchall()
        print(tags)
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
        selected_item_class = self.item_class_combobox.currentText()

        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        c.execute('''SELECT name FROM base_items WHERE item_class = ? AND tags LIKE ? ORDER BY drop_level ASC''',
                  (selected_item_class, f'%"{item_subtype}"%'))
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
        print(base_items)

    def create_mods_dict(base_item_name):
        # Load base_items.json and mods.json files
        with open('data/json/base_items.json', 'r') as f:
            base_items = json.load(f)
        with open('data/json/mods.json', 'r') as f:
            mods = json.load(f)

        # Find the base item in base_items.json
        base_item = base_items.get(base_item_name)
        if not base_item:
            return {}

        # Extract the tags for the base item
        tags = base_item.get('tags')
        if not tags:
            return {}

        # Find all mods that can spawn on the base item
        mods_dict = {}
        for mod_name, mod_data in mods.items():
            spawn_weights = mod_data.get('spawn_weights')
            if not spawn_weights:
                continue
            for spawn_weight in spawn_weights:
                if spawn_weight['tag'] in tags:
                    mods_dict[mod_name] = mod_data
                    break
        return mods_dict

    def update_item_stats(self, base_item_name, quality_text=None):
        conn = sqlite3.connect('exilecraft.db')
        c = conn.cursor()
        c.execute('''SELECT drop_level, implicits, name, properties_attack_time, properties_critical_strike_chance, properties_physical_damage_min,
                          properties_physical_damage_max, requirements_strength, requirements_dexterity,
                          requirements_intelligence, requirements_level, properties_armour, properties_evasion,
                          properties_energy_shield, properties_movement_speed, properties_block, properties_range
                     FROM base_items WHERE name = ?''', (base_item_name,))
        item_stats = c.fetchone()
        conn.close()

        if item_stats:
            drop_level, implicits, name, attack_time, critical_strike_chance, physical_damage_min, physical_damage_max, \
                req_strength, req_dexterity, req_intelligence, req_level, armour, evasion, energy_shield,\
                movement_speed, block, range = item_stats
            self.item_header_text_label.setText(f'Crafting Project \n {name}')

            quality_text = self.base_item_quality_combobox.currentText()
            if quality_text is None or quality_text == '':
                quality_value = int(self.base_item_quality_combobox.currentText() or 0)
            else:
                quality_value = int(quality_text)

            properties_list = [f'Quality: {quality_text}%']

            if block:
                properties_list.append(f'Block: {block}')
            if armour:
                armour_values = re.findall(r'(\d+)', armour)
                if len(armour_values) == 2:
                    min_armour, max_armour = map(int, armour_values)
                    avg_armour = ((min_armour + max_armour) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_armour = round(avg_armour)
                    properties_list.append(f'Armour: {rounded_avg_armour}')
            if evasion:
                evasion_values = re.findall(r'(\d+)', evasion)
                if len(evasion_values) == 2:
                    min_evasion, max_evasion = map(int, evasion_values)
                    avg_evasion = ((min_evasion + max_evasion) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_evasion = round(avg_evasion)
                    properties_list.append(f'Evasion: {rounded_avg_evasion}')
            if energy_shield:
                energy_shield_values = re.findall(r'(\d+)', energy_shield)
                if len(energy_shield_values) == 2:
                    min_energy_shield, max_energy_shield = map(int, energy_shield_values)
                    avg_energy_shield = ((min_energy_shield + max_energy_shield) // 2) * ((100 + quality_value) / 100)
                    rounded_avg_energy_shield = round(avg_energy_shield)
                    properties_list.append(f'Energy Shield: {rounded_avg_energy_shield}')
            if physical_damage_min and physical_damage_max:
                min_physical_damage, max_physical_damage = (int(physical_damage_min) * ((100 + quality_value) / 100)),\
                    (int(physical_damage_max) * ((100 + quality_value) / 100))
                adjusted_min_physical_damage = round(min_physical_damage)
                adjusted_max_physical_damage = round(max_physical_damage)
                properties_list.append(
                    f'{adjusted_min_physical_damage} To {adjusted_max_physical_damage} Physical Damage')

            if critical_strike_chance:
                properties_list.append(f'Critical Strike Chance: {critical_strike_chance / 100:.2f}%')
            if attack_time:
                properties_list.append(f'Attacks Per Second: {1000 / attack_time:.2f}' if attack_time else '')

            self.ItemProperties.setText('\n'.join(properties_list))

            item_level = self.base_item_level_combobox.currentText()
            if item_level is None or item_level == '':
                item_level = int(self.base_item_level_combobox.currentText() or 0)
            else:
                item_level = int(item_level)

            requirements_list = [f'Item Level: {item_level} \n']

            if req_level:
                requirements_list.append(f'Requires Level: {req_level},')
            if req_strength:
                requirements_list.append(f'{req_strength} Str')
            if req_dexterity:
                requirements_list.append(f'{req_dexterity} Dex')
            if req_intelligence:
                requirements_list.append(f'{req_intelligence} Int')

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

                        # Query the resolved_mod_stats table to get the min_translation_text, max_translation_text, min, and max values
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

                    if len(formatted_values) == 1:
                        random_number = random_numbers[0]
                        final_parsed_string = translation_text.format(f"{random_number}{formatted_values[0]}")
                    elif len(formatted_values) == 2:
                        random_number1 = random_numbers[0]
                        random_number2 = random_numbers[1]
                        final_parsed_string = translation_text.format(f"{random_number1}{formatted_values[0]}",
                                                                      f"{random_number2}{formatted_values[1]}")
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


