import sqlite3
import re
import json
import random

from PySide6 import QtCore

from ..parser import path_utils

db_path = path_utils.get_abs_path(__file__)



def fetch_item_stats(base_item_name):
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


def calculate_quality(quality_text):
    if quality_text is None or quality_text == '':
        quality_value = int(0)
    else:
        quality_value = int(quality_text)
    return quality_value


def extract_values_from_string(s):
    values = re.findall(r'(\d+)', s)
    if len(values) == 2:
        min_val, max_val = map(int, values)
        return min_val, max_val
    return None, None


def compute_avg_value(min_value, max_value, quality_value):
    if min_value is not None and max_value is not None:
        avg_value = ((min_value + max_value) // 2) * ((100 + quality_value) / 100)
        return round(avg_value)
    return None


def compute_physical_damage(physical_damage_min, physical_damage_max, quality_value):
    min_physical_damage, max_physical_damage = (int(physical_damage_min) * ((100 + quality_value) / 100)), \
        (int(physical_damage_max) * ((100 + quality_value) / 100))
    return round(min_physical_damage), round(max_physical_damage)


def compute_item_level(item_level):
    if item_level is None or item_level == '':
        item_level = int(0)
    else:
        item_level = int(item_level)
    return item_level


def extract_mods(implicits_list, mods_data):
    # Connect to the database
    cursor = conn.cursor()

    # Create lists to store min and max value ranges
    min_value_ranges = []
    max_value_ranges = []

    # Iterate over the mod_ids in the implicits_list
    for mod_id in [mod.strip('\"[]') for mod in implicits_list]:
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
    conn.close()

    return min_value_ranges, max_value_ranges



def update_item_stats(self, base_item_name, quality_text=None):
    """
    Updates the statistics of an item given its base name and quality.

    This function retrieves the base item's details from the 'exilecraft.db' SQLite database,
    and updates various statistics of the item based on its quality. The updated statistics are then
    displayed on the UI labels.

    The method also updates the implicit mods of the base item, if any are available. It reads
    the 'mods.json' file, retrieves the implicit mods from the database, and parses them. A random
    number is chosen if a range is available for the mod values.

    :param self: Reference to the instance of the class.
    :param base_item_name: The name of the base item to update.
    :param quality_text: The quality of the item as a string. Default is None.
    """
    item_stats = fetch_item_stats(base_item_name)

    if not item_stats:
        return

    if item_stats:
        drop_level, implicits, name, attack_time, critical_strike_chance, physical_damage_min, \
            physical_damage_max, req_strength, req_dexterity, req_intelligence, req_level, \
            armour, evasion, energy_shield, movement_speed, block, range = item_stats
        self.item_header_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_header_text_label.setText(
            '<div style="text-align:center;">'
            '<font face="Fontin" font-weight="bold" color="white">Crafting Project</font><br>'
            '<font face="Fontin" font-weight="bold" color="white">{}</font></div>'.format(name)
        )

        quality_value = calculate_quality(quality_text)
        properties_list = [f'Quality: <span style="color:#8787fe;">{quality_text}</span>%']

        if block:
            properties_list.append(f'Block: {block}')

        if armour:
            min_armour, max_armour = extract_values_from_string(armour)
            avg_armour = compute_avg_value(min_armour, max_armour, quality_value)
            if avg_armour is not None:
                properties_list.append(f'Armour: <span style="color:#8787fe;">{avg_armour}</span>')

        if evasion:
            min_evasion, max_evasion = extract_values_from_string(evasion)
            avg_evasion = compute_avg_value(min_evasion, max_evasion, quality_value)
            if avg_evasion is not None:
                properties_list.append(f'Evasion: <span style="color:#8787fe;">{avg_evasion}</span>')

        if energy_shield:
            min_energy_shield, max_energy_shield = extract_values_from_string(energy_shield)
            avg_energy_shield = compute_avg_value(min_energy_shield, max_energy_shield, quality_value)
            if avg_energy_shield is not None:
                properties_list.append(f'Energy Shield: <span style ="color:#8787fe;">'
                                       f'{avg_energy_shield}</span>')

        if physical_damage_min and physical_damage_max:
            min_physical_damage, max_physical_damage = (int(physical_damage_min) * ((100 + quality_value) / 100)),
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

        item_level = calculate_item_level(item_level)

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
                min_value_ranges, max_value_ranges = fetch_mods(implicits_list)

                formatted_values = format_values(min_value_ranges, max_value_ranges)

                if formatted_values:
                    final_parsed_string = generate_final_string(formatted_values)

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

        if implicits:
            implicits_list = implicits.split('|')
            if implicits_list and len(implicits_list) > 0 and not (
                    len(implicits_list) == 1 and implicits_list[0] == '[]'):
                print(implicits_list)

                # Load the mods.json file
                with open(abs_file_path, 'r') as f:
                    mods_data = json.load(f)

                # Connect to the database
                conn = sqlite3.connect('exilecraft.db')
                cursor = conn.cursor()

                # Create lists to store min and max value ranges
                min_value_ranges = []
                max_value_ranges = []

                # Iterate over the mod_ids in the implicits_list
                for mod_id in [mod.strip('\"[]') for mod in implicits_list]:
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
                    pass

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
