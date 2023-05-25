from modules.config.constants import ITEM_CLASS_SUBTYPES, REVERSED_SUBTYPE_DISPLAY_NAMES, SUBTYPE_DISPLAY_NAMES, \
    SUBTYPE_TAGS_MAP
from modules.data.parser import base_items_parser, path_utils
from modules.gui.widgets import *

rel_path_to_db = "modules/data/exilecraft.db"
db_path = path_utils.get_abs_path(__file__, rel_path_to_db)


class ComboboxUpdater:
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
        if self.base_combobox.itemText(index) is not None:
            group = self.group
            tag = ""
            if group == "Two Handed Weapons":
                current_base_item_type = self.base_combobox.itemText(index)
                current_base_item_type = current_base_item_type.title()
                tag = "two_hand_weapon"
            elif group == "One Handed Weapons":
                current_base_item_type = self.base_combobox.itemText(index)
                if current_base_item_type == "Convoking Wand":
                    current_base_type_tag = current_base_item_type
                    tag = self.REVERSED_SUBTYPE_DISPLAY_NAMES.get(current_base_type_tag)
                    current_base_item_type = "Wand"
            else:
                current_base_item = group
                current_base_item_type = current_base_item
                current_base_type_tag = self.base_combobox.itemText(index)
                current_base_type_tag = current_base_type_tag.replace(self.group, '').strip()
                tag = SUBTYPE_TAGS_MAP.get(current_base_type_tag)
                print(current_base_item_type)
            self.update_base_item_combobox(current_base_item_type, tag)

    def update_base_item_combobox(self, current_base_item_type, tag):
        self.base_item_combobox.clear()
        self.base_item_combobox.setEnabled(True)
        self.base_item_combobox.show()
        matching_items = base_items_parser.find_items(current_base_item_type, tag)
        for base_item in matching_items:
            self.base_item_combobox.addItem(base_item)
        self.item_level_spinbox.setEnabled(True)
        self.item_quality_spinbox.setEnabled(True)
