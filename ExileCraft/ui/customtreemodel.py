import json

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt

from ..ui.customtreeitem import TreeItem
from ..db.database_handler import DatabaseHandler


class CustomTreeModel(QAbstractItemModel):
    def __init__(self, headers, item_name, all_results, generation_type):
        super().__init__()
        self.db_handler = DatabaseHandler()
        self.headers = headers
        self.item_name = item_name
        self.root_item = TreeItem([""] * len(headers))
        self.all_results = all_results
        self.generation_type = generation_type

    def update_data(self, headers, item_name, all_results, generation_type):
        self.headers = headers
        self.item_name = item_name
        self.root_item = TreeItem([""] * len(headers))
        self.all_results = all_results
        self.generation_type = generation_type
        self.populate_data()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        return parent_item.child_count()

    def columnCount(self, parent=QModelIndex()):
        if parent.isValid():
            return parent.internalPointer().column_count()
        else:
            return self.root_item.column_count()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        item = index.internalPointer()
        return item.data(index.column())

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            headers = [
                "Mod",
                "Required Level",
                "Total Mods",
                "Tags",
                "Total Spawn Weight"
            ]
            if 0 <= section < len(headers):
                return headers[section]
        return None

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent()

        if parent_item == self.root_item:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def update_and_populate(self, generation_type):
        # Assuming generation_type, headers, item_name, and all_results are instance variables
        self.generation_type = generation_type
        self.beginResetModel()
        self.update_data(self.headers, self.item_name, self.all_results, self.generation_type)
        self.endResetModel()

    def populate_data(self):
        """Populates the model with data based on the current generation type.

        This is a placeholder method. You'll need to replace it with your actual data population logic.
        """
        mods_data = self.all_results
        filtered_results = [mod for mod in mods_data if mod[4] == self.generation_type]
        mod_groups = {}
        mod_group_items = {}
        for mod in filtered_results:
            mod_group = mod[6]
            if mod_group not in mod_groups:
                mod_groups[mod_group] = []
            mod_groups[mod_group].append(mod)
        for mod_group, mods in mod_groups.items():
            # Extract the stats for the mod group
            mod_group_stats = json.loads(mods[0][7])
            # Get the translation text for each stat without filling the placeholder values
            stat_translations = []
            for stat in mod_group_stats:
                stat_id = stat["id"]
                translation_text = self.db_handler.get_translation_text_by_id(stat_id)
                if translation_text is not None:
                    stat_translations.append(translation_text)
            # Join the translation texts and display them as the mod group text
            translated_mod_group = "\n".join(stat_translations).replace('{0}', '#').replace('{1}', '#')
            # Extract the additional information
            tags = json.loads(mods[0][10])
            total_mods = len(mods)
            highest_required_level = max([mod[2] for mod in mods])
            total_spawn_weight = 0
            for mod in mod_groups[mod_group]:
                weight_dict = json.loads(mod[12])
                if "weight" in weight_dict and str(weight_dict["weight"]).isdigit():
                    total_spawn_weight += int(weight_dict["weight"])
            # Format the data for each column
            item_data = [
                translated_mod_group,
                highest_required_level,
                total_mods,
                ', '.join(tags).replace('_', ' '),
                total_spawn_weight
            ]
            mod_group_item = TreeItem(item_data, self.root_item)
            self.root_item.append_child(mod_group_item)
            mod_group_items[mod_group] = mod_group_item
            sorted_mods = sorted(mods, key=lambda mod: mod[2])
            for mod in sorted_mods:
                # Extract the required data
                name = mod[1]
                required_level = mod[2]
                stats = mod[7]
                stats_list = json.loads(stats)
                translated_stats = []
                for stat in stats_list:
                    stat_id = stat["id"]
                    min_value = stat["min"]
                    max_value = stat["max"]
                    # Query the database for the translation_text
                    translation_text = self.db_handler.get_translation_text_by_id(stat_id)
                    if translation_text is not None:
                        placeholder_count = translation_text.count("{")
                        if placeholder_count == 1:
                            if min_value == max_value:
                                value_range = f"+{min_value}"
                                translated_stat = translation_text.format(value_range)
                            else:
                                value_range = f"+({min_value}-{max_value})"
                                translated_stat = translation_text.format(value_range)
                            translated_stats.append(translated_stat)
                        elif placeholder_count == 2:
                            translated_stat = translation_text.format(min_value, max_value)
                            translated_stats.append(translated_stat)
                implicit_tags = mod[10]
                spawn_weights = mod[12]
                highest_weight = 0
                if spawn_weights:
                    weight_dict = json.loads(spawn_weights)
                    if "weight" in weight_dict and str(weight_dict["weight"]).isdigit():
                        highest_weight = int(weight_dict["weight"])
                # Format the text
                stats_text = "\n".join(translated_stats)
                # Convert implicit_tags JSON string to a list and then to a string without brackets
                implicit_tags_list = json.loads(implicit_tags)
                child_item_data = [
                    name,
                    required_level,
                    stats_text,
                    ', '.join(implicit_tags_list).replace('_', ' '),
                    highest_weight
                ]

                child_item = TreeItem(child_item_data, mod_group_item)
                mod_group_item.append_child(child_item)