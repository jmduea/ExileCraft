from game_data import base_items_objects

allowed_base_types = [
    "AbyssJewel", "Amulet", "Belt", "Body Armour", "Boots", "Bow", "Claw",
    "Dagger", "Gloves", "Helmet", "HybridFlask", "Jewel", "LifeFlask",
    "ManaFlask", "One Hand Axe", "One Hand Mace", "One Hand Sword", "Quiver",
    "Rune Dagger", "Sceptre", "Shield", "Staff", "Thrusting One Hand Sword",
    "Two Hand Axe", "Two Hand Mace", "Two Hand Sword", "UtilityFlask", "Wand", "Warstaff"
]

base_type_to_tag = {
    "Amulet": "amulet",
    "Talisman": "talisman",
    "Belt": "belt",
    "Body Armour": "body_armour",
    "Boots": "boots",
    "Bow": "bow",
    "Claw": "claw",
    "Dagger": "dagger",
    "Gloves": "gloves",
    "Helmet": "helmet",
    "HybridFlask": "hybrid_flask",
    "Jewel": "jewel",
    "LifeFlask": "life_flask",
    "ManaFlask": "mana_flask",
    "One Hand Axe": "onehand",
    "One Hand Mace": "onehand",
    "One Hand Sword": "onehand",
    "Quiver": "quiver",
    "Rune Dagger": "rune_dagger",
    "Sceptre": "sceptre",
    "Shield": "shield",
    "Staff": "staff",
    "Thrusting One Hand Sword": "onehand",
    "Two Hand Axe": "twohand",
    "Two Hand Mace": "twohand",
    "Two Hand Sword": "twohand",
    "UtilityFlask": "utility_flask",
    "Wand": "wand",
    "Warstaff": "warstaff",
}


class ItemBaseSelector:
    def convert_tag_to_readable_format(self, tag):
        tag_readable_format = {
            "dex_armour": "Armour (dex)",
            "str_armour": "Armour (str)",
            "int_armour": "Armour (int)",
            "str_dex_armour": "Armour (str/dex)",
            "str_int_armour": "Armour (str/int)",
            "dex_int_armour": "Armour (dex/int)",
            "str_dex_int_armour": "Armour (str/dex/int)",
            "talisman": "Talisman",
            # Add more conversion rules here if needed
        }

        return tag_readable_format.get(tag, "")

    def convert_readable_format_to_tag(self, readable_format):
        readable_format_to_tag = {
            "Armour (dex)": "dex_armour",
            "Armour (str)": "str_armour",
            "Armour (int)": "int_armour",
            "Armour (str/dex)": "str_dex_armour",
            "Armour (str/int)": "str_int_armour",
            "Armour (dex/int)": "dex_int_armour",
            "Armour (str/dex/int)": "str_dex_int_armour",
        }

        return readable_format_to_tag.get(readable_format, "")

    def get_unique_base_types(self):
        base_types = set()
        for base_item in base_items_objects:
            if base_item.item_class in allowed_base_types:
                base_types.add(base_item.item_class)
        return sorted(base_types)

    def populate_base_type_dropdown(self):
        for base_type in self.base_types:
            self.base_type_box.addItem(base_type)

    def get_base_subtypes(self, base_type):
        subtypes = set()
        for base_item in base_items_objects:
            if base_item.item_class == base_type:
                tag = base_type_to_tag.get(base_type)
                if tag in base_item.tags:
                    for tag in base_item.tags:
                        if tag.endswith('_armour'):
                            readable_tag = self.convert_tag_to_readable_format(tag)
                            subtypes.add(readable_tag)
        return sorted(subtypes)

    def get_unique_subtypes(self, base_type, subtype):
        items = set()
        for base_item in base_items_objects:
            if base_item.item_class == base_type:
                tag = base_type_to_tag.get(base_type)
                if tag in base_item.tags:
                    subtype_tag = self.convert_readable_format_to_tag(subtype)
                    if subtype_tag in base_item.tags:
                        items.add(base_item.name)
        return sorted(items)

    def get_items_for_subtype(self, base_type, subtype):
        items = set()
        subtype_tag = self.convert_readable_format_to_tag(subtype)

        for base_item in base_items_objects:
            if base_item.item_class == base_type:
                if subtype_tag in base_item.tags:
                    items.add(base_item.name)

        return sorted(items)

    def populate_subtype_dropdown(self):
        selected_base_type = self.base_type_box.currentText()
        self.subtypes = self.get_base_subtypes(selected_base_type)
        if self.subtypes:
            self.base_item_box.clear()
            self.base_item_box.hide()
            self.base_item_box.setEnabled(False)
            self.base_subtype_box.clear()
            self.base_subtype_box.addItems(self.subtypes)
            self.base_subtype_box.show()
            self.base_subtype_box.setEnabled(True)
        elif not self.subtypes:
            self.base_subtype_box.clear()
            self.base_subtype_box.setEnabled(False)
            self.populate_base_item_box_with_base_type(selected_base_type)

    def populate_base_item_box_with_base_type(self, base_type):
        items = set()
        for base_item in base_items_objects:
            if base_item.item_class == base_type:
                items.add(base_item.name)
        self.base_subtype_box.clear()
        self.base_subtype_box.setEnabled(False)
        self.base_subtype_box.hide()
        self.base_item_box.clear()
        self.base_item_box.addItems(sorted(items))
        self.base_item_box.show()
        self.base_item_box.setEnabled(True)

    def populate_base_item_box(self):
        selected_base_type = self.base_type_box.currentText()
        selected_subtype = self.base_subtype_box.currentText()

        # Populate the base item box if a subtype is selected
        if selected_subtype:
            self.items = self.get_unique_subtypes(selected_base_type, selected_subtype)
            self.base_item_box.clear()
            self.base_item_box.addItems(self.items)
            self.base_item_box.show()
            self.base_item_box.setEnabled(True)
        # Populate the base item box if there are no subtypes for the base type
        elif not self.subtypes:
            self.items = self.get_unique_subtypes(selected_base_type, None)
            self.base_item_box.clear()
            self.base_item_box.addItems(self.items)
            self.base_item_box.show()
            self.base_item_box.setEnabled(True)
        # Clear the base item box if a subtype is required but not selected
        else:
            self.base_item_box.clear()
            self.base_item_box.setEnabled(False)




