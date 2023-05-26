from PySide6 import QtGui

from modules.config.constants import ITEM_CLASS_SUBTYPES, REVERSED_SUBTYPE_DISPLAY_NAMES, SUBTYPE_DISPLAY_NAMES, \
    SUBTYPE_TAGS_MAP
from modules.data.parser import base_items_parser, mods_parser
from qt_core import *
from .ui_mainwindow import *


# TODO: fix string formatting for properties, lines should be more closely spaced
# TODO: fix filtering for two-toned boots
# TODO: stat translations for implicits
# TODO: properly clear labels when switching base_groups, bases
# TODO: properly calculate item stats with quality factored in


class MainFunctions:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    def set_left_column_menu(
            self,
            menu,
            title,
            icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)

    def toggle_left_column(self):
        # Get columns actual size
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # Get columns actual size
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values        
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values        
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()


class ComboboxUpdater:
    """
    This class is responsible for updating the QComboBox and QSpinBox objects in the GUI. It takes in several QComboBox
    and QSpinBox objects, and updates their values based on the user's selections. It also handles the display of item
    images, properties, requirements, and implicits.

    Attributes:
        base_group_combobox (QComboBox): A combobox that displays the available base item groups.
        base_combobox (QComboBox): A combobox that displays the available bases.
        base_item_combobox (QComboBox): A combobox that displays the available base item types.
        item_level_spinbox (QSpinBox): A spinbox that allows the user to select an item level.
        item_quality_spinbox (QSpinBox): A spinbox that allows the user to select an item quality level.
        item_img_label (QLabel): A label that displays the image of the selected item.
        item_properties_label (QLabel): A label that displays the properties of the selected item.
        item_requirements_label (QLabel): A label that displays the requirements of the selected item.
        item_level_label (QLabel): A label that displays the selected item level.
        item_quality_label (QLabel): A label that displays the selected item quality level.
        item_header_label (QLabel): A label that displays the header of the selected item.
        item_implicits_container (QWidget): A container that holds the implicits label.
        item_implicits_label (QLabel): A label that displays the implicits of the selected item.
        item_spacer_3 (QSpacerItem): A spacer item used for layout purposes.
    """

    def __init__(self, base_group_combobox, base_combobox, base_item_combobox, item_level_spinbox,
                 item_quality_spinbox, item_img_label, item_properties_label, item_requirements_label, item_level_label,
                 item_quality_label, item_header_label, item_implicits_container, item_implicits_label, item_spacer_3):
        super().__init__()
        self.window = PyWindow
        self.base_group_combobox = base_group_combobox
        self.base_group_combobox.setCurrentIndex(-1)
        self.base_combobox = base_combobox
        self.base_item_combobox = base_item_combobox
        self.item_level_spinbox = item_level_spinbox
        self.item_quality_spinbox = item_quality_spinbox
        self.item_img_label = item_img_label
        self.item_properties_label = item_properties_label
        self.item_requirements_label = item_requirements_label
        self.item_level_label = item_level_label
        self.item_quality_label = item_quality_label
        self.item_header_label = item_header_label
        self.item_implicits_container = item_implicits_container
        self.item_implicits_label = item_implicits_label
        self.item_spacer_3 = item_spacer_3
        self.ITEM_CLASS_SUBTYPES = ITEM_CLASS_SUBTYPES
        self.SUBTYPE_DISPLAY_NAMES = SUBTYPE_DISPLAY_NAMES
        self.SUBTYPE_TAGS_MAP = SUBTYPE_TAGS_MAP
        self.group = None
        self.base_item = None
        self.item_level = ""
        self.item_quality = ""
        self.REVERSED_SUBTYPE_DISPLAY_NAMES = REVERSED_SUBTYPE_DISPLAY_NAMES

    def update_base_combobox(self):
        """
        Updates the base combobox based on the currently selected group in the base group combobox.
        """
        self.group = self.base_group_combobox.currentText()
        # Clear the base combobox
        self.base_combobox.clear()
        self.base_combobox.setEnabled(True)
        # Add the corresponding base items to the base combobox
        for base_item in self.ITEM_CLASS_SUBTYPES.get(self.group, []):
            display_name = self.SUBTYPE_DISPLAY_NAMES.get(base_item, base_item)
            self.base_combobox.addItem(display_name.format(self.group))

    # Take the info from the base_group_combobox and the base_combobox and return the current_base_item_type
    # and tag that specifies what subtype of base item to search for (if any)
    def get_base_items_for_combobox(self, index):
        """
        Retrieves the base items for the combobox based on the selected index.

        Args:
            index (int): The index of the selected item in the base combobox.
        """
        if self.base_combobox.itemText(index) is not None:
            group = self.group
            tag = ""
            if group == "Two Handed Weapons":
                current_base_item_type = self.base_combobox.itemText(index)
                current_base_item_type = current_base_item_type.title()
                tag = "two_hand_weapon"
            elif group == "One Handed Weapons":
                current_base_item_type = self.base_combobox.itemText(index)
                current_base_item_type = current_base_item_type.title()
                tag = "one_hand_weapon"
            elif group == "Jewellery":
                current_base_item_type = self.base_combobox.itemText(index)
                tag = self.REVERSED_SUBTYPE_DISPLAY_NAMES.get(current_base_item_type)
            elif group == "Flasks":
                current_base_item_type = self.base_combobox.itemText(index).replace(' ', '')
                current_base_type_tag = self.base_combobox.itemText(index)
                tag = self.REVERSED_SUBTYPE_DISPLAY_NAMES.get(current_base_type_tag)
            else:
                current_base_item_type = group
                current_base_type_tag = self.base_combobox.itemText(index)
                current_base_type_tag = current_base_type_tag.replace(self.group, '').strip()
                tag = SUBTYPE_TAGS_MAP.get(current_base_type_tag)
            self.update_base_item_combobox(current_base_item_type, tag)

    def update_base_item_combobox(self, current_base_item_type, tag):
        """
        Updates the base item combobox based on the current base item type and tag.

        Args:
            current_base_item_type (str): The current base item type selected in the base combobox.
            tag (str): The tag associated with the current base item type.
        """
        self.base_item_combobox.clear()
        self.base_item_combobox.setEnabled(True)
        self.base_item_combobox.show()
        matching_items = base_items_parser.find_items(current_base_item_type, tag)
        for base_item in matching_items:
            self.base_item_combobox.addItem(base_item)
        self.item_level_spinbox.setEnabled(True)
        self.item_quality_spinbox.setEnabled(True)

    def set_item_view_box_background(self):
        """
        Sets the background of the item view box to the image of the currently selected item.

        This method fetches the name of the currently selected item from the base item combo box,
        modifies the name to match the naming convention of the item images, constructs the path to
        the image, and then attempts to load and display the image in the item view box.

        If the image fails to load or an error occurs during the process, a message is printed to
        the console. If the image is loaded successfully, it is displayed in the item view box and
        is centered and not scaled.

        Raises:
        Exception: If an error occurs when loading the image.
        """
        base_item_name = self.base_item_combobox.currentText()
        base_item = base_item_name.replace(' ', '_').lower()
        image_path = os.path.abspath(
            os.path.join('F:', 'modules', 'gui', 'assets', 'images', 'items',
                         base_item + '.png'))
        print(image_path)
        try:
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image at {image_path}")
            else:
                self.item_img_label.setPixmap(pixmap)
                self.item_img_label.setAlignment(Qt.AlignCenter)
                self.item_img_label.setScaledContents(False)
        except Exception as e:
            print(f"Error loading image: {e}")

    def clear_item_view_box_background(self):
        """
        Clears the background image of a label widget assigned to the item_img_label attribute of the load_pages object in the current instance of a class.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        self.item_img_label.setPixmap(QPixmap())

    def set_item_header_label(self):
        """
           Update the item header label in the load_pages object by retrieving the currently selected item from the base_item_combobox object in the left_column object.

           Args:
               self: The current instance of the class where the method is called.

           Returns:
               None
           """
        item_name = self.base_item_combobox.currentText()
        item_name_str = f'Crafting Project:\n{item_name}'
        self.item_header_label.setText(item_name_str)

    def set_item_level(self):
        """
            Sets the item level value from the item_level_spinbox object in the left_column object and updates the HTML formatted label to display the item level in the load_pages object.

            Args:
                self: The current instance of the class where the method is called.

            Returns:
                None
            """
        item_level_value = self.item_level_spinbox.value()
        self.item_level = self.item_level_spinbox.value()
        item_level = str(item_level_value)
        item_html = f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Item Level: </span>' \
                    f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_level}</span></p>'
        self.item_level_label.setText(item_html)

    def set_item_quality(self):
        """
            Sets the item quality value from the item_quality_spinbox object in the left_column object and updates the HTML formatted label to display the item quality percentage in the load_pages object.

            Args:
                self: The current instance of the class where the method is called.

            Returns:
                None
            """
        item_quality_value = self.item_quality_spinbox.value()
        self.item_quality = self.item_quality_spinbox.value()
        item_quality = str(item_quality_value)
        quality_html = f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Quality: </span>' \
                       f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_quality}%</span></p>'
        self.item_quality_label.setText(quality_html)

    def get_base_item_info(self):
        item_name = self.base_item_combobox.currentText()
        if item_name:
            item_info = base_items_parser.find_item_info(item_name)
            if item_info:
                item_info = item_info[0]  # Assuming you only have one item in the list
                domain = item_info.get('domain', '')
                drop_level = str(item_info.get('drop_level', ''))
                implicits = ', '.join(item_info.get('implicits', []))
                inventory_height = str(item_info.get('inventory_height', ''))
                inventory_width = str(item_info.get('inventory_width', ''))
                item_class = item_info.get('item_class', '')
                name = item_info.get('name', '')
                release_state = item_info.get('release_state', '')
                tags = ', '.join(item_info.get('tags', []))
                visual_identity = item_info.get('visual_identity', {}).get('dds_file', '')

                # Extracting properties
                properties = item_info.get('properties', {})
                armour_min = properties.get('armour', {}).get('min', '')
                armour_max = properties.get('armour', {}).get('max', '')
                block = str(properties.get('block', ''))
                energy_shield_min = properties.get('energy_shield', {}).get('min', '')
                energy_shield_max = properties.get('energy_shield', {}).get('max', '')
                evasion_min = properties.get('evasion', {}).get('min', '')
                evasion_max = properties.get('evasion', {}).get('max', '')
                ward_min = properties.get('ward', {}).get('min', '')
                ward_max = properties.get('ward', {}).get('max', '')
                movement_speed = str(properties.get('movement_speed', ''))
                attack_time = properties.get('attack_time', '')
                critical_strike_chance = properties.get('critical_strike_chance', '')
                physical_damage_min = properties.get('physical_damage_min', '')
                physical_damage_max = properties.get('physical_damage_max', '')
                _range = str(properties.get('range', ''))

                # Calculate averages if values are not empty
                average_armour = round((armour_min + armour_max) / 2) if armour_min and armour_max else ''
                average_energy_shield = round((energy_shield_min + energy_shield_max) / 2) \
                    if energy_shield_min and energy_shield_max else ''
                average_evasion = round((evasion_min + evasion_max) / 2) if evasion_min and evasion_max else ''
                average_ward = round((ward_min + ward_max) / 2) if ward_min and ward_max else ''

                # Convert averages to strings for consistency
                average_armour = str(average_armour)
                average_energy_shield = str(average_energy_shield)
                average_evasion = str(average_evasion)
                average_ward = str(average_ward)

                # Calculate aps, crit chance
                attack_time = round((1000 / float(attack_time)), 2) \
                    if attack_time else ''
                critical_strike_chance = round((float(critical_strike_chance) / 100), 3) \
                    if critical_strike_chance else ''

                # Convert to strings for consistency
                attacks_per_second = str(attack_time)
                critical_strike_chance = str(critical_strike_chance)

                # Extracting requirements
                requirements = item_info.get('requirements', {})
                dexterity = str(requirements.get('dexterity', ''))
                intelligence = str(requirements.get('intelligence', ''))
                level = str(requirements.get('level', ''))
                strength = str(requirements.get('strength', ''))

                return domain, drop_level, implicits, inventory_height, inventory_width, item_class, name, release_state, \
                    tags, visual_identity, average_armour, block, average_energy_shield, average_evasion, average_ward, \
                    movement_speed, attacks_per_second, critical_strike_chance, \
                    physical_damage_max, physical_damage_min, _range, \
                    requirements, dexterity, intelligence, level, strength

    def update_labels(self):
        # Get the item info
        item_info = self.get_base_item_info()
        if item_info:
            # Get the implicit string
            implicit_str = item_info[2] if item_info[2] and item_info[2] != "" else ""
            if implicit_str != "":
                stats = mods_parser.get_mod_stats(implicit_str)
                for stat in stats:
                    stat_id = stat.get("id", "")
                    stat_min = stat.get("min", "")
                    stat_max = stat.get("max", "")

                # Format the implicit string
                implicit_formatted = (
                    f'<p style="line-height:0.8; padding-bottom:1em;" align="center">'
                    f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{implicit_str}</span></p>'
                ) if implicit_str else ""

                if implicit_formatted != "":
                    # Set the text of the implicit label
                    self.item_spacer_3.setEnabled(True)
                    self.item_spacer_3.show()
                    self.item_implicits_container.setEnabled(True)
                    self.item_implicits_container.show()
                    self.item_implicits_label.setEnabled(True)
                    self.item_implicits_label.show()
                    self.item_implicits_label.setText(implicit_formatted)
            else:
                self.item_spacer_3.hide()
                self.item_implicits_label.hide()

            # Format the properties string
            properties_list = [
                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Armour: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[10]}</span></p>'
                if item_info[10] and item_info[10] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Block: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[11]}</span></p>'
                if item_info[11] and item_info[11] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Energy Shield: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[12]}</span></p>'
                if item_info[12] and item_info[12] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Evasion: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[13]}</span></p>'
                if item_info[13] and item_info[13] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Ward: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[14]}</span></p>'
                if item_info[14] and item_info[14] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[19]} </span>'
                f'<span style=" font-size:11pt; color:#827a6c;">To </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_info[18]} </span>'
                f'<span style=" font-size:11pt; color:#827a6c;">Physical Damage</span></p>'
                if item_info[18] and item_info[18] != "0" and item_info[19] and item_info[19] != "0" else "",

                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Critical Strike Chance: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[17]}</span></p>'
                if item_info[17] and item_info[17] != "0" else "",
                f'<p style="line-height:0.8; padding-bottom:0.2em;" align="center">'
                f'<span style=" font-size:11pt; color:#827a6c;">Attacks Per Second: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[16]}</span></p>'
                if item_info[16] and item_info[16] != "0" else "",

                f"Range: {item_info[20]}" if item_info[20] and item_info[23] != "0" else ""
            ]
            properties_str = "".join(filter(None, properties_list))  # filter out empty strings
            self.item_properties_label.setText(properties_str)

            # Format the requirements string
            requirements_list = [
                f'<span style=" font-size:11pt; color:#827a6c;">Requires Level: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[24]}</span>'
                if item_info[24] and item_info[24] != "0" else "",
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[22]} </span>'
                f'<span style =" font-size:11pt; color:#827a6c;"> DEX </span>'
                if item_info[22] and item_info[22] != "0" else "",
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[23]} </span>'
                f'<span style =" font-size:11pt; color:#827a6c;"> INT </span>'
                if item_info[23] and item_info[23] != "0" else "",
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_info[25]} </span>'
                f'<span style =" font-size:11pt; color:#827a6c;"> STR </span>'
                if item_info[25] and item_info[25] != "0" else ""
            ]
            requirements_str = '<p align="center">' + ", ".join(
                filter(None, requirements_list)) + '</p>'  # filter out empty strings
            self.item_requirements_label.setText(requirements_str)
