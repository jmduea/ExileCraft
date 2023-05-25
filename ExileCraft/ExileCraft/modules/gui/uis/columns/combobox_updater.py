from modules.config.constants import ITEM_CLASS_SUBTYPES, REVERSED_SUBTYPE_DISPLAY_NAMES, SUBTYPE_DISPLAY_NAMES, \
    SUBTYPE_TAGS_MAP

from modules.data.parser import base_items_parser, path_utils

from modules.gui.widgets.py_window import *

rel_path_to_db = "modules/data/exilecraft.db"
db_path = path_utils.get_abs_path(__file__, rel_path_to_db)


class ComboboxUpdater:
    """
    This class is responsible for updating the QComboBox objects in the GUI. It takes in several QComboBox
    objects and QSpinBox objects, and updates their values based on the user's selections.

    Attributes:
        base_group_combobox (QComboBox): A combobox that displays the available base item groups.
        base_combobox (QComboBox): A combobox that displays the available bases.
        base_item_combobox (QComboBox): A combobox that displays the available base item types.
        item_level_spinbox (QSpinBox): A spinbox that allows the user to select an item level.
        item_quality_spinbox (QSpinBox): A spinbox that allows the user to select an item quality level.
    """

    def __init__(self, base_group_combobox, base_combobox, base_item_combobox, item_level_spinbox,
                 item_quality_spinbox):
        super().__init__()
        self.window = PyWindow(self)
        self.base_group_combobox = base_group_combobox
        self.base_combobox = base_combobox
        self.base_item_combobox = base_item_combobox
        self.item_level_spinbox = item_level_spinbox
        self.item_quality_spinbox = item_quality_spinbox
        self.ITEM_CLASS_SUBTYPES = ITEM_CLASS_SUBTYPES
        self.SUBTYPE_DISPLAY_NAMES = SUBTYPE_DISPLAY_NAMES
        self.SUBTYPE_TAGS_MAP = SUBTYPE_TAGS_MAP
        self.group = None
        self.base_item = None
        self.REVERSED_SUBTYPE_DISPLAY_NAMES = REVERSED_SUBTYPE_DISPLAY_NAMES
        self.base_combobox.currentIndexChanged.connect(self.get_base_items_for_combobox)

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
