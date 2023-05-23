from modules.db.constants import ITEM_CLASS_SUBTYPES, SUBTYPE_DISPLAY_NAMES


class ComboboxUpdater:
    def __init__(self, base_group_combobox, base_combobox, base_item_combobox):
        super().__init__()
        self.base_group_combobox = base_group_combobox
        self.base_combobox = base_combobox
        self.base_item_combobox = base_item_combobox
        self.ITEM_CLASS_SUBTYPES = ITEM_CLASS_SUBTYPES
        self.SUBTYPE_DISPLAY_NAMES = SUBTYPE_DISPLAY_NAMES

    def update_base_combobox(self, index):
        print("update_base_combobox called")
        # Get the selected group
        group = self.base_group_combobox.itemText(index)

        # Clear the base combobox
        self.base_combobox.clear()
        self.base_combobox.setEnabled(True)
        # Add the corresponding base items to the base combobox
        for base_item in self.ITEM_CLASS_SUBTYPES.get(group, []):
            display_name = self.SUBTYPE_DISPLAY_NAMES.get(base_item, base_item)
            self.base_combobox.addItem(display_name.format(group))
        self.update_base_item_combobox(self.base_combobox.itemText(index))

    def update_base_item_combobox(self, index):
        item_class_id = self.base_combobox.itemText(index)
        pass
