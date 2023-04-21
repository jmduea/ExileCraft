from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout

from game_data import base_items_objects, mods, BaseItem, Mod, stat_translations
from item_base_selector import ItemBaseSelector, allowed_base_types


class ItemModFinder:
    def __init__(self, base_items_objects, mods, base_item_box, mods_tabs):
        self.prefixes = {}
        self.suffixes = {}
        self.implicits = {}
        self.mods_tabs = mods_tabs
        self.base_item_box = base_item_box
        self.mods = []
        self.mod_types = []
        self.tag = []
        self.base_items = []
        self.base_items_to_mods = {}
        self.mod_groups_to_base_items = {}
        self.mods_trees = {}

        # create three tabs for prefixes, suffixes, and implicits
        self.tab_types = ["prefix", "suffix", "implicit"]
        for tab_type in self.tab_types:
            tree = QTreeWidget()
            tree.setHeaderLabels(["Modifier", "ILvl", "StatRange", "Weight", "Tag"])
            self.mods_trees[tab_type] = tree
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(tree)
            mods_tabs.addTab(tab, tab_type.capitalize())

        self.map_mod_groups_to_base_items(base_items_objects, mods)

        # connect signals
        self.connect_signals()
        self.populate_mods_tree()

    def connect_signals(self):
        self.base_item_box.currentIndexChanged.connect(self.find_mods)
        self.base_item_box.currentIndexChanged.connect(self.populate_mods_tree)

    def mod_applicable_to_base_item(self, base_item, mod):

        if mod.required_level >= base_item.drop_level:
            return False

        # Check if the item and mod share a domain
        if base_item.domain != mod.domain:
            return False

        # Add more conditions here if needed

        return True

    def map_mod_groups_to_base_items(self, base_items_objects, mods):
        self.base_items = [item.name for item in base_items_objects]
        self.mods = mods

        # create a dictionary of mod groups to base items
        self.mod_groups_to_base_items = {}
        for item in base_items_objects:
            for group in item.mod_groups:
                if group not in self.mod_groups_to_base_items:
                    self.mod_groups_to_base_items[group] = []
                self.mod_groups_to_base_items[group].append(item)

    def find_mods(self):
        selected_base_item_name = self.base_item_box.currentText()

        selected_base_item = self.base_item_box.currentText()
        for base_item in base_items_objects:
            if base_item.name == selected_base_item_name:
                selected_base_item = base_item
                break

        if selected_base_item:
            prefixes, suffixes, implicits = self.get_mods_for_base_item(selected_base_item)

            combined_mods = {
                "prefixes": prefixes,
                "suffixes": suffixes,
                "implicits": implicits,
            }
            return combined_mods
        else:
            print("Base item not found.")
            return None

    def get_mods_for_base_item(self, selected_base_item):
        prefixes = {}
        suffixes = {}
        implicits = {}

        base_item_groups = selected_base_item.groups

        for mod_id, mod in mods.items():
            if self.mod_applicable_to_base_item(selected_base_item, mod):
                mod_info = {"required_level": mod.required_level, "stats": mod.stats}
                if mod.generation_type == "prefix":
                    if mod.groups[0] not in prefixes:
                        prefixes[mod.groups[0]] = []
                    prefixes[mod.groups[0]].append(Mod(mod_id, mod.adds_tags, mod.domain, mod.generation_type,
                                                        mod.generation_weights, mod.grants_effects, mod.groups,
                                                        mod.implicit_tags, mod.is_essence_only, mod.name,
                                                        mod.required_level, mod.spawn_weights, mod.stats,
                                                        mod.type))
                elif mod.generation_type == "suffix":
                    if mod.groups[0] not in suffixes:
                        suffixes[mod.groups[0]] = []
                    suffixes[mod.groups[0]].append(Mod(mod_id, mod.adds_tags, mod.domain, mod.generation_type,
                                                        mod.generation_weights, mod.grants_effects, mod.groups,
                                                        mod.implicit_tags, mod.is_essence_only, mod.name,
                                                        mod.required_level, mod.spawn_weights, mod.stats,
                                                        mod.type))
                elif mod.generation_type == "implicit":
                    if mod.groups[0] not in implicits:
                        implicits[mod.groups[0]] = []
                    implicits[mod.groups[0]].append(Mod(mod_id, mod.adds_tags, mod.domain, mod.generation_type,
                                                         mod.generation_weights, mod.grants_effects, mod.groups,
                                                         mod.implicit_tags, mod.is_essence_only, mod.name,
                                                         mod.required_level, mod.spawn_weights, mod.stats,
                                                         mod.type))

        return prefixes, suffixes, implicits

    def map_mod_groups_to_QTreeWidgets(self):
        self.mods_trees = {mod_group: tree for mod_group, tree in self.mods_trees.items()}



    def populate_mods_tree(self):
        print("populate_mods_tree called")
        def get_readable_mod_string(mod):
            for stat in mod.stats:
                for translation in stat_translations:
                    if stat['id'] in translation.ids:
                        stat_translation = translation
                        break
                else:
                    continue

                formatted_values = []
                for index, format_str in enumerate(stat_translation.format):
                    formatted_value = format_str.replace("#", f"{stat['min']}-{stat['max']}")
                    formatted_values.append(formatted_value)

                formatted_stat = stat_translation.string.format(*formatted_values)
                return f"{mod.name}: {formatted_stat}", f"({stat['min']}-{stat['max']})"
            return "", ""  # default to empty strings if no matching stat translation is found

        for tab_type, tree in self.mods_trees.items():
            if tree.layout() is None:
                print(f"Mods tree widget for {tab_type} has not been added to a layout")

        mod_groups = {}
        for mod_id, mod in mods.items():
            if mod.generation_type in self.tab_types:
                tab_type = mod.generation_type
                group_name = mod.groups[0]

                if group_name not in mod_groups:
                    mod_groups[group_name] = []

                mod_groups[group_name].append(mod)

        selected_base_item_name = self.base_item_box.currentText()
        selected_base_item = next((item for item in base_items_objects if item.name == selected_base_item_name), None)

        for group_name, group_mods in mod_groups.items():
            group_item = QTreeWidgetItem([group_name, "", "", "", "", ""])
            child_count = 0

            for mod in group_mods:
                if selected_base_item.item_class not in allowed_base_types:
                    continue

                if mod.domain != "item":
                    continue

                tab_type = mod.generation_type
                tree = self.mods_trees[tab_type]
                mod_tag = ""
                if mod.name.endswith(("_shaper", "_elder", "_crusader", "_hunter", "_warlord", "_redeemer")):
                    mod_tag = mod.name.split("_")[-1]
                weight_str = ', '.join([f"{entry['tag']}:{entry['weight']}" for entry in mod.spawn_weights])

                matching_weights = [entry for entry in mod.spawn_weights if
                                    entry['tag'] in selected_base_item.tags and entry['weight'] > 0]

                if matching_weights:
                    readable_mod_name, stat_range = get_readable_mod_string(mod)
                    mod_item = QTreeWidgetItem([readable_mod_name, str(mod.required_level), stat_range,
                                                "", "", ""])
                    group_item.addChild(mod_item)
                    child_count += 1

            if child_count > 0:
                tree.addTopLevelItem(group_item)
                print(f"Added mod group {group_name} to tree for {tab_type}")


