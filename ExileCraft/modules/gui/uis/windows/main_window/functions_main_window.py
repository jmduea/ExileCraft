# ##############################################################################
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
# ##############################################################################
import os
import re

from PySide6 import QtGui
from PySide6.QtCore import (
    QEasingCurve,
    QObject,
    QParallelAnimationGroup,
    QPropertyAnimation,
    Qt,
    Signal,
)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QPushButton

from modules import BASE_ITEMS_CACHE
from modules.data.models.item_models import Item, ITEM_RARITY
from modules.data.web.mod_requests import get_mod_stat_text_raw_by_id
from modules.gui.core.functions import Functions
from modules.gui.uis.windows.main_window.ui_mainwindow import UiMainWindow
from modules.shared.config.constants import ITEM_CLASS_SUFFIXES, subtype_tags_map
from modules.shared.config.gui_constants import (
    BTN_CLOSE_LEFT_COLUMN,
    BTN_HOME,
    BTN_INFO,
    BTN_PAGE_2,
    BTN_PAGE_3,
    BTN_SETTINGS,
    BTN_TOP_SETTINGS,
)


class MainFunctions:
    """
    A class used to control the main functions of the UI.

    ...

    Attributes
    ----------
    ui : object
        An instance of the UI_MainWindow class.


    Methods
    -------
    set_page(page)
        Sets the current widget to the given page.
    set_left_column_menu(menu, title, icon_path)
        Sets the current widget of the left column menu, updates the title and icon.
    left_column_is_visible()
        Returns a boolean indicating if the left column is visible.
    right_column_is_visible()
        Returns a boolean indicating if the right column is visible.
    set_right_column_menu(menu)
        Sets the current widget of the right column menu.
    get_title_bar_btn(object_name)
        Returns the QPushButton with the given object name in the title bar.
    get_left_menu_btn(object_name)
        Returns the QPushButton with the given object name in the left menu.
    toggle_left_column()
        Toggles the visibility of the left column.
    toggle_right_column()
        Toggles the visibility of the right column.
    start_box_animation(left_box_width, right_box_width, direction)
        Starts the animation for the left and right boxes.
    """

    def __init__(self):
        """Initializes an instance of the MainFunctions class."""
        super().__init__()
        self.ui = UiMainWindow()

    def set_page(self, page):
        """Sets the current widget to the given page."""
        self.ui.load_pages.pages.setCurrentWidget(page)

    @staticmethod
    def select_menu_and_load_page(self, btn, page):
        """Select Menu And Load Page"""
        self.ui.left_menu.select_only_one(btn.objectName())
        MainFunctions.set_page(self, page)

    def set_left_column_menu(self, menu, title, icon_path):
        """
        Sets the current widget of the left column menu, updates the title and icon.

        Parameters:
        menu (QWidget): The widget to set as the current widget.
        title (str): The title to set for the left column menu.
        icon_path (str): The path to the icon for the left column menu.
        """
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    def left_column_is_visible(self):
        """Returns a boolean indicating if the left column is visible."""
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def right_column_is_visible(self):
        """Returns a boolean indicating if the right column is visible."""
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def set_right_column_menu(self, menu):
        """Sets the current widget of the right column menu."""
        self.ui.right_column.menus.setCurrentWidget(menu)

    def toggle_left_column(self):
        """Toggles the visibility of the left column."""
        # Get columns actual size
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        """Toggles the visibility of the right column."""
        # Get columns actual size
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        """
        Starts the animation for the left and right boxes.

        Parameters:
        left_box_width (int): The current width of the left box.
        right_box_width (int): The current width of the right box.
        direction (str): The direction of the animation ("left" or "right").
        """
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


class ButtonFunctions:
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.main_functions = MainFunctions()
        self.button_handlers = {
            BTN_HOME: self.handle_home_btn,
            BTN_PAGE_2: self.handle_page_2_btn,
            BTN_PAGE_3: self.handle_page_3_btn,
            BTN_INFO: lambda: self.handle_info_and_settings_btn(
                BTN_INFO, "Item Settings", "icon_info.svg"
            ),
            BTN_SETTINGS: lambda: self.handle_info_and_settings_btn(
                BTN_SETTINGS, "Settings Left Column", "icon_settings.svg"
            ),
            BTN_TOP_SETTINGS: self.handle_top_settings_btn,
            BTN_CLOSE_LEFT_COLUMN: self.handle_close_left_column_btn,
        }

    @staticmethod
    def set_button_active(button):
        """Set Button Active"""
        button.set_active(True)

    def get_title_bar_btn(self, object_name):
        """
        Returns the QPushButton with the given object name in the title bar.

        Parameters:
        object_name (str): The object name of the QPushButton.
        """
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    def get_left_menu_btn(self, object_name):
        """
        Returns the QPushButton with the given object name in the left menu.

        Parameters:
        object_name (str): The object name of the QPushButton.
        """
        return self.ui.left_menu.findChild(QPushButton, object_name)

    def handle_home_btn(self):
        """Handles the event when the home button is clicked."""
        self.main_functions.select_menu_and_load_page(
            self, BTN_HOME, self.ui.load_pages.crafting_emu_page
        )

    def handle_page_2_btn(self):
        pass

    def handle_page_3_btn(self):
        self.main_functions.select_menu_and_load_page(
            self, BTN_PAGE_3, self.ui.load_pages.crafting_calc_page
        )

    def handle_info_and_settings_btn(self, button_name, title, icon):
        menu_visible = (
            self.ui.left_column.menus.menu_1.isVisibile()
            if button_name == BTN_SETTINGS
            else (self.ui.left_column.menus.menu_2.isVisible())
        )
        if not self.main_functions.left_column_is_visible() or menu_visible:
            self.main_functions.toggle_left_column()
            self.ui.left_menu.select_only_one_tab(button_name)
        elif button_name != BTN_CLOSE_LEFT_COLUMN:
            self.ui.left_menu.select_only_one_tab(button_name)
            self.main_functions.set_left_column_menu(
                menu=self.ui.left_column.menus.menu_1
                if button_name == BTN_SETTINGS
                else self.ui.left_column.menus.menu_2,
                title=title,
                icon_path=Functions.set_svg_icon(icon),
            )


class GUIUpdater(QObject):
    item_class_selected = Signal(str)
    item_changed = Signal(bool)

    def __init__(self, parent: QMainWindow):
        super().__init__()
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        self.ui = parent.ui
        self.mods_widget = None
        self.base_item_cache = BASE_ITEMS_CACHE.cache
        self.item_cache = None
        self.item_level = 0
        self.item_class = None
        self.current_item = None
        self.item_rarity = ITEM_RARITY.NORMAL
        self.item_quality = 0
        self.influences = []
        self.combo_map = {
            "One Hand Weapons": "OneHandWeapons",
            "Two Hand Weapons": "TwoHandWeapons",
            "Body Armours": "BodyArmours",
            "Helmets": "Helmets",
            "Gloves": "Gloves",
            "Boots": "Boots",
            "Shields": "Shields",
            "Offhands": "Quivers",
            "Flasks": "Flasks",
            "Jewellery": ["Amulets", "Rings", "Belts"],
            "Jewels": "Jewel",
        }
        self.base_to_key_map = {
            "Body Armour (dex)": "BodyDex",
            "Body Armour (dex/int)": "BodyDexInt",
            "Body Armour (int)": "BodyInt",
            "Body Armour (str)": "BodyStr",
            "Body Armour (str/dex)": "BodyStrDex",
            "Body Armour (str/dex/int)": "BodyStrDexInt",
            "Body Armour (str/int)": "BodyStrInt",
            "Helmet (dex)": "HelmetDex",
            "Helmet (dex/int)": "HelmetDexInt",
            "Helmet (int)": "HelmetInt",
            "Helmet (str)": "HelmetStr",
            "Helmet (str/dex)": "HelmetStrDex",
            "Helmet (str/dex/int)": "HelmetStrDexInt",
            "Helmet (str/int)": "HelmetStrInt",
            "Helmet (ward)": "HelmetExpedition",
            "Gloves (dex)": ["GlovesDex", "GlovesAtlasDex", "GlovesDexRitual"],
            "Gloves (dex/int)": "GlovesDexInt",
            "Gloves (int)": ["GlovesInt", "GlovesAtlasInt", "GlovesIntRitual"],
            "Gloves (str)": ["GlovesStr", "GlovesAtlasStr", "GlovesStrRitual"],
            "Gloves (str/dex)": "GlovesStrDex",
            "Gloves (str/dex/int)": "GlovesStrDexInt",
            "Gloves (str/int)": ["GlovesStrInt", "GlovesAtlasStrInt"],
            "Gloves (ward)": "GlovesExpedition",
            "Boots (dex)": ["BootsDex", "BootsDexRitual"],
            "Boots (dex/int)": ["BootsDexInt", "BootsAtlas1", "BootsAtlas4"],
            "Boots (int)": "BootsInt",
            "Boots (str)": "BootsStr",
            "Boots (str/dex)": ["BootsStrDex", "BootsAtlas2"],
            "Boots (str/dex/int)": "BootsStrDexInt",
            "Boots (str/int)": ["BootsStrInt", "BootsAtlas3"],
            "Boots (ward)": "BootsExpedition",
        }

    def update_base_combobox(self):
        """
        Updates the base combobox based on the currently selected item_class in the base group combobox.
        """

        search_strings = self.combo_map[
            self.ui.left_column.menus.base_group_combobox.currentText()
        ]
        if not isinstance(search_strings, list):
            search_strings = [search_strings]
        matching_keys = [
            k for k in self.base_item_cache.keys() for s in search_strings if s in k
        ]
        item_classes = [
            self.base_item_cache[k]["item_class"]
            for k in matching_keys
            if "item_class" in self.base_item_cache[k]
        ]
        unique_item_classes = list(set(item_classes))

        self.ui.left_column.menus.base_combobox.clear()
        self.ui.left_column.menus.base_combobox.setEnabled(True)

        for item_class in unique_item_classes:
            if item_class in ITEM_CLASS_SUFFIXES:
                for suffix in ITEM_CLASS_SUFFIXES[item_class]:
                    self.ui.left_column.menus.base_combobox.addItem(item_class + suffix)
            else:
                self.ui.left_column.menus.base_combobox.addItem(item_class)

    def update_base_item_combobox(self, index):
        subtype_display_name = self.ui.left_column.menus.base_combobox.currentText()
        self.item_cache = {}
        if subtype_display_name is not None:
            # Extracting subtype and item_class from display name
            subtype = re.findall(r"\((.*?)\)", subtype_display_name)
            if subtype:
                subtype = subtype[0]  # Taking the first match
            else:
                subtype = None

            # Extracting item_class from display name
            item_class = re.sub(r" \((.*?)\)", "", subtype_display_name)
            self.mods_widget.update_mod_tabs(subtype_display_name)
            # Fetching corresponding tag
            subtype_tag = subtype_tags_map.get(subtype, None)

            if subtype_tag is not None:
                # Fetching matching items from cache
                matching_items = [
                    item
                    for item in self.base_item_cache.values()
                    if subtype_tag in item["tags"] and item["item_class"] == item_class
                ]
            else:
                matching_items = [
                    item
                    for item in self.base_item_cache.values()
                    if item["item_class"] == item_class
                ]

            matching_items = sorted(matching_items, key=lambda x: x["drop_level"])
            self.ui.left_column.menus.base_item_combobox.clear()
            self.ui.left_column.menus.base_item_combobox.setEnabled(True)

            if matching_items:
                for item in matching_items:
                    base_item_dict = {item["name"]: item}
                    self.item_cache.update(base_item_dict)
                    self.ui.left_column.menus.base_item_combobox.addItem(item["name"])

        self.ui.left_column.menus.item_level_spinbox.setEnabled(True)
        self.ui.left_column.menus.item_quality_spinbox.setEnabled(True)

    def set_current_item(self):
        """
        Sets the current item based on the currently selected item in the base item combobox.
        """
        item_name = self.ui.left_column.menus.base_item_combobox.currentText()
        if item_name != "":
            self.current_item = Item(self.item_cache.get(item_name))
            self.ui.left_column.menus.item_level_spinbox.setValue(0)
            self.set_item_level()
            self.set_item_quality()
            self.set_item_influences()

    def set_item_influences(self):
        if self.influences is not None:
            self.current_item.add_influence(iter(self.influences))

    def set_item_rarity(self, value):
        self.current_item.rarity = value
        self.item_rarity = value

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

        current_item = self.current_item

        if current_item is None:
            return
        visual_identity = current_item.visual_identity

        if "shaper" in self.influences:
            self.ui.load_pages.item_img_label.setStyleSheet(
                "QLabel{background-image: url(:/images/images/shaper_item_box.png);\
            opacity: 0.8;}"
            )
        else:
            self.ui.load_pages.item_img_label.setStyleSheet(
                "QLabel{background-image: url(:/images/images/item_box.png);\
            opacity: 0.8;}"
            )

        current_file_path = "modules/gui/assets/images/items"
        image_path = os.path.join(current_file_path, visual_identity + ".png")

        try:
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image at {image_path}")
            else:
                self.ui.load_pages.item_img_label.setPixmap(pixmap)
                self.ui.load_pages.item_img_label.setAlignment(Qt.AlignCenter)
                self.ui.load_pages.item_img_label.setScaledContents(False)
        except Exception as e:
            print(f"Error loading image: {e}")

    def clear_item_view_box_background(self):
        """
        Clears the background image of a label widget assigned to the item_img_label attribute of the load_pages
        object in the current instance of a class.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        self.ui.load_pages.item_img_label.setPixmap(QPixmap())

    def set_item_header_label(self):
        """
         Update the item header label in the load_pages object by retrieving the currently selected item from the
         base_item_combobox object in the left_column object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        item_name = self.current_item.name
        if not item_name:
            return
        item_name_str = f"Crafting Project:\n{item_name}"
        if self.item_rarity == ITEM_RARITY.MAGIC:
            self.ui.load_pages.item_header_label.setStyleSheet(
                "QLabel {\
                                                                                background-image:\
                                                                                url("
                ":/images/images/item-header-magic.png);\
                                                                                }\
                                                                            "
            )
        elif self.item_rarity == ITEM_RARITY.RARE:
            self.ui.load_pages.item_header_label.setStyleSheet(
                "QLabel {\
                                                                                background-image:\
                                                                                url(\
                :/images/images/item-header-rare.png);\
                                                                                }\
                                                                            "
            )
        else:
            self.ui.load_pages.item_header_label.setStyleSheet(
                "QLabel {\
                                                                                background-image:\
                                                                                url(\
                :/images/images/item-header-normal.png);\
                                                                                }\
                                                                            "
            )
        self.ui.load_pages.item_header_label.setText(item_name_str)

    def set_item_level(self):
        """
        Sets the item level value from the item_level_spinbox object in the left_column object and updates the HTML
        formatted label to display the item level in the load_pages object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        current_item = self.current_item
        self.item_level = self.ui.left_column.menus.item_level_spinbox.value()

        if current_item:
            current_item.item_level = self.item_level
            item_level = str(current_item.item_level)
            item_html = (
                f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Item Level: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_level}</span></p>'
            )
            self.ui.load_pages.item_level_label.setText(item_html)
        else:
            return

    def set_item_quality(self):
        """
        Sets the item quality value from the item_quality_spinbox object in the left_column object and updates the
        HTML formatted label to display the item quality percentage in the load_pages object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        item_quality_value = self.ui.left_column.menus.item_quality_spinbox.value()
        self.item_quality = self.ui.left_column.menus.item_quality_spinbox.value()
        current_item = self.current_item
        if current_item:
            current_item.quality = self.item_quality
            item_quality = str(item_quality_value)
            quality_html = (
                f'<p align="center"><span style=" font-size:11pt; margin:0; color:#827a6c;">Quality: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_quality}%</span></p>'
            )
            self.ui.load_pages.item_quality_label.setText(quality_html)
            self.ui.load_pages.item_properties_label.setText(
                current_item.formatted_properties()
            )
        else:
            return

    def set_influence(self, influence):
        if not self.current_item:
            self.influences.append(influence)
            return
        else:
            self.current_item.add_influence(influence)
            self.influences.append(influence)
            self.set_item_view_box_background()
            print(f"Setting influence to {influence}")

    def remove_influence(self, influence):
        if not self.current_item:
            self.influences.remove(influence)
            return
        else:
            self.current_item.remove_influence(influence)
            self.influences.remove(influence)
            self.set_item_view_box_background()
            print(f"Removing influence {influence}")

    @staticmethod
    def format_implicit_string(current_item):
        """
        Formats the implicit properties of an item for display in the GUI.

        This method takes a string of implicit properties, calculates the average stat for each property, and formats
        these properties into an HTML string that can be displayed in the GUI.

        Args:
            current_item (object): An instance of an item.

        Returns:
            str: A string containing the formatted implicit properties, ready to be displayed in the GUI.
        """

        item_implicits = current_item.implicits
        if not item_implicits:
            return ""
        else:
            stat_translation_strings = ""
            for implicit in item_implicits:
                translation_string = get_mod_stat_text_raw_by_id(implicit)
                split_strings = translation_string.split("&lt;br&gt;")
                stat_translation_strings = split_strings

            # Format each implicit string
            implicit_formatted_list = [
                (
                    f'<p style="line-height:1; margin:0; padding-bottom:0;" align="center">'
                    f'<span style=" font-size:10.5pt; color:#8787fe;">'
                    f"{single_translation_string}</span></p>"
                )
                for single_translation_string in stat_translation_strings
            ]

            # Join all formatted strings together
            return "".join(implicit_formatted_list)

    def update_implicit_label(self, current_item):
        if current_item:
            implicit_formatted = self.format_implicit_string(current_item)

            if implicit_formatted != "":
                # Set the text of the implicit label
                self.ui.load_pages.item_spacer_3.setEnabled(True)
                self.ui.load_pages.item_spacer_3.show()
                self.ui.load_pages.item_implicits.setEnabled(True)
                self.ui.load_pages.item_implicits.show()
                self.ui.load_pages.item_implicits_label.setEnabled(True)
                self.ui.load_pages.item_implicits_label.show()
                self.ui.load_pages.item_implicits_label.setText(implicit_formatted)
            else:
                self.ui.load_pages.item_spacer_3.hide()
                self.ui.load_pages.item_implicits_label.hide()

    def update_labels(self):
        current_item = self.current_item
        if current_item is None:
            return
        self.ui.load_pages.item_requirements_label.setText(
            current_item.formatted_requirements()
        )
        self.ui.load_pages.item_properties_label.setText(
            current_item.formatted_properties()
        )
        self.update_implicit_label(current_item)

    def clear_labels(self):
        """
        Clears the text of the item requirements, properties, and implicits labels,
        and hides the implicits container and spacer.
        """
        self.ui.load_pages.item_requirements_label.clear()
        self.ui.load_pages.item_properties_label.clear()
        self.ui.load_pages.item_implicits_label.clear()
        self.ui.load_pages.item_implicits.hide()
        self.ui.load_pages.item_spacer_3.hide()
