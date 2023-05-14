# from PyQt5 import QtGui
# from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from ExileCraft.item_mods_retriever import get_mods_for_item_class
from ExileCraft.item_stats_updater import update_item_stats
# from ExileCraft.item_mods_retriever import get_mods_for_item_class
from constants import SUBTYPE_DISPLAY_NAMES, ALL_SUBTYPES

class UiUpdater:
    """

    """
    def __init__(self, item_header_text_label, ItemProperties, ItemRequirements, ItemImplicits, ItemSpacer3, Modifiers,
                 item_img_box, main_window):
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
        self.main_window = main_window
        self.Prefixes = main_window.Prefixes
        self.all_subtypes = ALL_SUBTYPES
        self.subtype_display_names = SUBTYPE_DISPLAY_NAMES
        self.subtype_original_names = {v: k for k, v in self.subtype_display_names.items()}

    def set_item_view_box_background(self, base_item_name):
        """

        """
        base_item_name = base_item_name.replace(' ', '_').lower()
        print(base_item_name)
        image_path = f"ui/assets/images/items/{base_item_name}.png"
        print(image_path)
        pixmap = QtGui.QPixmap(image_path)
        self.item_img_box.setPixmap(pixmap)
        self.item_img_box.setAlignment(Qt.AlignCenter)
        self.item_img_box.setScaledContents(False)

    # def limit_selection(self):
    #     """
    #
    #     """
    #     max_selections = 2
    #     selected_items = self.base_item_influence_combobox.selectedItems()
    #
    #     if len(selected_items) > max_selections:
    #         last_selected_item = selected_items[-1]
    #         last_selected_item.setSelected(False)

    def update_item_stats(self, base_item_name, quality_text=None):
        update_item_stats(self, base_item_name, quality_text)

    def get_mods_for_item_class(self):
        return get_mods_for_item_class(self)

    def filter_item_subtypes(self, selected_item_class_name, all_subtypes):
        return self.filter_item_subtypes(self, selected_item_class_name, all_subtypes)