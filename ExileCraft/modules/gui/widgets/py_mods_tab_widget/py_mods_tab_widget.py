# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import QAbstractListModel, QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QLabel,
    QListView,
    QMainWindow,
    QStyledItemDelegate,
    QToolBox,
    QVBoxLayout,
)
from PySide6.QtWidgets import QWidget

from modules import MOD_LIST_CACHE
from modules.gui.widgets.py_mods_tab_widget.ui_mods_widget import Ui_mods_widget

# Generate the relative path from the source file to the target file
relative_path = Path("modules/data/json/mods.min.json")

print(relative_path)

item_classes = [
    "wands_(minion_type)",
    "quivers",
    "rings_(minion_type)",
    "Unset_Ring",
    "body_armours_(dexterity)",
    "body_armours_(dexterity/intelligence)",
    "body_armours_(intelligence)",
    "body_armours_(strength)",
    "body_armours_(strength/dexterity)",
    "body_armours_(strength/dexterity/intelligence)",
    "body_armours_(strength/intelligence)",
    "boots_(dexterity)",
    "boots_(dexterity/intelligence)",
    "boots_(intelligence)",
    "boots_(strength)",
    "boots_(strength/dexterity)",
    "boots_(strength/dexterity/intelligence)",
    "boots_(strength/intelligence)",
    "gloves_(dexterity)",
    "gloves_(dexterity/intelligence)",
    "gloves_(intelligence)",
    "gloves_(strength)",
    "gloves_(strength/dexterity)",
    "gloves_(strength/dexterity/intelligence)",
    "gloves_(strength/intelligence)",
    "helmets_(dexterity)",
    "helmets_(dexterity/intelligence)",
    "helmets_(intelligence)",
    "helmets_(strength)",
    "helmets_(strength/dexterity)",
    "helmets_(strength/dexterity/intelligence)",
    "helmets_(strength/intelligence)",
    "shields_(dexterity)",
    "shields_(dexterity/intelligence)",
    "shields_(intelligence)",
    "shields_(minion_type)",
    "shields_(strength)",
    "shields_(strength/dexterity)",
    "shields_(strength/intelligence)",
]
ITEM_CLASS_URL_MAP = {
    "Claw": "claws",
    "Dagger": "generic_daggers",
    "One Hand Sword": "generic_one-handed_swords",
    "One Hand Axe": "one-handed_axes",
    "One Hand Mace": "one-handed_maces",
    "Rune Dagger": "rune_daggers",
    "Sceptre": "sceptres",
    "Thrusting One Hand Sword": "thrusting_one-handed_swords",
    "Wand": "wands",
    "Bow": "bows",
    "Staff": "generic_staves",
    "Warstaff": "warstaves",
    "Two Hand Axe": "two-handed_axes",
    "Two Hand Mace": "two-handed_maces",
    "Two Hand Sword": "two-handed_swords",
    "Amulet": "amulets",
    "Belt": "belts",
    "Body Armour (dex)": "body_armours_(dexterity)",
    "Body Armour (dex/int)": "body_armours_(dexterity/intelligence)",
    "Body Armour (int)": "body_armours_(intelligence)",
    "Body Armour (str)": "body_armours_(strength)",
    "Body Armour (str/dex)": "body_armours_(strength/intelligence)",
    "Body Armour (str/dex/int)": "body_armours_(strength/dexterity/intelligence)",
    "Body Armour (str/int)": "body_armours_(strength/intelligence)",
    "Boots (dex)": "boots_(dexterity)",
    "Boots (dex/int)": "boots_(dexterity/intelligence)",
    "Boots (int)": "boots_(intelligence)",
    "Boots (str)": "boots_(strength)",
    "Boots (str/dex)": "boots_(strength/dexterity)",
    "Boots (str/int)": "boots_(strength/intelligence)",
    "Helmet (dex)": "helmets_(dexterity)",
    "Helmet (dex/int)": "helmets_(dexterity/intelligence)",
    "Helmet (int)": "helmets_(intelligence)",
    "Helmet (str)": "helmets_(strength)",
    "Helmet (str/dex)": "helmets_(strength/dexterity)",
    "Helmet (str/int)": "helmets_(strength/intelligence)",
    "Gloves (dex)": "gloves_(dexterity)",
    "Gloves (dex/int)": "gloves_(dexterity/intelligence)",
    "Gloves (int)": "gloves_(intelligence)",
    "Gloves (str)": "gloves_(strength)",
    "Gloves (str/dex)": "gloves_(strength/dexterity)",
    "Gloves (str/int)": "gloves_(strength/intelligence)",
    "Shield (dex)": "shields_(dexterity)",
    "Shield (dex/int)": "shields_(dexterity/intelligence)",
    "Shield (int)": "shields_(intelligence)",
    "Shield (str)": "shields_(strength)",
    "Shield (str/dex)": "shields_(strength/dexterity)",
    "Shield (str/int)": "shields_(strength/intelligence)",
}


class ModsWidget(QWidget):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)

        if not parent.objectName():
            parent.setObjectName("MainWindow")
        self.parent = parent
        self.ui = Ui_mods_widget()
        self.ui.setupUi(self)
        self.mod_list_cache = MOD_LIST_CACHE
        self.mod_list = None
        self.item_class = None
        self.prefix_categories = None
        self.suffix_categories = None
        self.implicit_categories = None

    def update_mod_tabs(self, item_class):
        self.clear_toolboxes()
        self.item_class = ITEM_CLASS_URL_MAP.get(item_class, item_class)
        self.create_toolboxes()
        self.mod_list = self.mod_list_cache.get_mod_list(self.item_class)
        for key in self.mod_list.keys():
            mod_category_dict = self.mod_list.get(key)
            mod_category = key
            mod_generation_types = mod_category_dict.keys()
            self.create_toolbox_pages(
                mod_category, mod_category_dict, mod_generation_types
            )
        self.ui.prefixes_layout.addWidget(self.prefix_categories)
        self.ui.suffixes_layout.addWidget(self.suffix_categories)
        self.ui.implicits_layout.addWidget(self.implicit_categories)

    def create_toolboxes(self):
        self.prefix_categories = QToolBox()
        self.prefix_categories.layout().setContentsMargins(0, 0, 0, 0)
        self.prefix_categories.layout().setSpacing(0)
        self.suffix_categories = QToolBox()
        self.suffix_categories.layout().setSpacing(0)
        self.suffix_categories.layout().setContentsMargins(0, 0, 0, 0)
        self.implicit_categories = QToolBox()
        self.implicit_categories.layout().setSpacing(0)
        self.implicit_categories.layout().setContentsMargins(0, 0, 0, 0)

    def create_toolbox_pages(
        self, mod_category, mod_category_dict, mod_generation_types
    ):
        for generation_type in mod_generation_types:
            if generation_type == "Prefixes":
                list_view = self.create_list_view(generation_type, mod_category_dict)
                layout = QVBoxLayout()
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(list_view)
                widget = QWidget()
                widget.setLayout(layout)
                self.prefix_categories.addItem(widget, mod_category)

            elif generation_type == "Suffixes":
                list_view = self.create_list_view(generation_type, mod_category_dict)
                layout = QVBoxLayout()
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(list_view)
                widget = QWidget()
                widget.setLayout(layout)
                self.suffix_categories.addItem(widget, mod_category)

            else:
                list_view = self.create_list_view(generation_type, mod_category_dict)

                layout = QVBoxLayout()
                layout.setSpacing(0)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.addWidget(list_view)
                widget = QWidget()
                widget.setLayout(layout)
                self.implicit_categories.addItem(widget, mod_category)

    def create_list_view(self, generation_type, mod_category_dict):
        generation_type_dict = mod_category_dict.get(generation_type)
        groups = generation_type_dict.keys()
        list_view = ExpandableListView()
        list_view.set_model(generation_type_dict)  # Set the model
        list_view.setItemDelegate(ExpandableDelegate(list_view))
        list_view.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        list_view.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.NoDragDrop)
        list_view.setAlternatingRowColors(True)
        list_view.setStyleSheet("QListView {font-size: 14px;}")
        return list_view

    def clear_toolboxes(self):
        # Remove pages from prefix categories
        if self.prefix_categories:
            for i in range(self.prefix_categories.count() - 1, -1, -1):
                self.prefix_categories.removeItem(i)
        # Remove pages from suffix categories
        if self.suffix_categories:
            for i in range(self.suffix_categories.count() - 1, -1, -1):
                self.suffix_categories.removeItem(i)
        # Remove pages from implicit categories
        if self.implicit_categories:
            for i in range(self.implicit_categories.count() - 1, -1, -1):
                self.implicit_categories.removeItem(i)


class ModGroupListModel(QAbstractListModel):
    def __init__(self, mod_groups, parent=None):
        super().__init__(parent)
        self.mod_groups = mod_groups
        self.mod_keys_set = set(mod_groups.keys())
        self.mod_keys = list(self.mod_keys_set)
        self.expanded_states = [False] * len(self.mod_groups)

    def rowCount(self, parent=None):
        row_count = len(self.mod_groups)  # One row for each group
        for group_index, is_expanded in enumerate(self.expanded_states):
            modifiers_count = len(
                self.mod_groups[self.mod_keys[group_index]]["modifiers"]
            )
            if is_expanded or modifiers_count == 1:
                # Add extra rows for the table if the group is expanded or has only one modifier
                row_count += modifiers_count
        return row_count

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        group_index, is_table_row, modifier_index = self.get_indexes(row)
        group_key = self.mod_keys[group_index]
        if is_table_row:
            if not self.expanded_states[group_index]:
                return None  # Hide table row if not expanded
            modifier = self.mod_groups[group_key]["modifiers"][modifier_index]
            if role == Qt.DisplayRole:
                return modifier["name"], modifier["req_level"], modifier["stats"]
            elif role == Qt.UserRole:
                return (
                    group_index,
                    modifier_index,
                    is_table_row,
                    self.expanded_states[group_index],
                )
        else:
            if role == Qt.DisplayRole:
                return self.mod_groups[group_key]["modifiers"][modifier_index]
            elif role == Qt.UserRole:
                return (
                    group_index,
                    is_table_row,
                    modifier_index,
                    self.expanded_states[group_index],
                )

    def setData(self, index, value, role=Qt.EditRole):
        row = index.row()
        group_index, is_table_row, _ = self.get_indexes(row)
        if not is_table_row and role == Qt.UserRole:
            self.expanded_states[group_index] = value
            self.dataChanged.emit(index, index, [role])
            self.layoutChanged.emit()  # Notify the view that the layout has changed
            return True
        return False

    def get_indexes(self, row):
        group_index = 0
        for key in self.mod_keys:
            if row == 0:
                return group_index, False, 0
            row -= 1
            modifiers_count = len(self.mod_groups[key]["modifiers"])
            if (
                self.expanded_states[group_index]
                or len(self.mod_groups[key]["modifiers"]) == 1
            ):
                if row < modifiers_count:
                    return group_index, True, row
                row -= modifiers_count
            group_index += 1
        return 0, False, 0  # Fallback values


class ExpandableDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        user_data = index.data(Qt.UserRole)
        if user_data:
            group_index, is_table_row, modifier_index, is_expanded = user_data
            if (
                is_table_row
                and not is_expanded
                and len(
                    self.parent()
                    .model()
                    .mod_groups[self.parent().model().mod_keys[group_index]][
                        "modifiers"
                    ]
                )
                > 1
            ):
                return  # Skip painting for table rows that are not expanded and have more than one modifier
            if is_table_row:
                # Paint table row
                name, req_level, stats = index.data(Qt.DisplayRole)
                table_row_widget = TableRowWidget(name, req_level, stats)
                table_row_widget.resize(option.rect.size())
                table_pixmap = QPixmap(table_row_widget.size())
                table_row_widget.render(table_pixmap)
                painter.drawPixmap(option.rect.topLeft(), table_pixmap)
            else:
                # Paint regular row
                QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        user_data = index.data(Qt.UserRole)
        if user_data is not None:
            group_index, is_table_row, modifier_index, is_expanded = user_data
            if is_table_row:
                name, req_level, stats = index.data(Qt.DisplayRole)
                table_row_widget = TableRowWidget(name, req_level, stats)
                return table_row_widget.calculate_size_hint()
        return QStyledItemDelegate.sizeHint(self, option, index)


class ExpandableListView(QListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.delegate = ExpandableDelegate()
        self.setItemDelegate(self.delegate)
        self.clicked.connect(self.on_item_clicked)
        self.setWordWrap(True)
        self.ResizeMode = QListView.ResizeMode.Adjust

    def set_model(self, mod_groups):
        model = ModGroupListModel(mod_groups)
        self.setModel(model)

    def on_item_clicked(self, index):
        model = self.model()
        user_data = index.data(Qt.UserRole)
        if user_data is None:
            return  # Skip if there is no user data

        group_index, is_table_row, _, is_expanded = user_data
        if not is_table_row:
            # Toggle the expanded state of the clicked mod group row
            model.setData(index, not is_expanded, Qt.UserRole)

        # Trigger a repaint
        self.viewport().update()


class TableRowWidget(QWidget):
    def __init__(self, name, req_level, stats, parent=None):
        super().__init__(parent)
        self.name = name
        self.req_level = req_level
        self.stats = stats
        layout = QHBoxLayout()
        layout.addWidget(QLabel(name))
        layout.addWidget(QLabel(str(req_level)))
        layout.addWidget(QLabel(stats))
        self.setLayout(layout)

    def calculate_size_hint(self):
        name_width = self.fontMetrics().boundingRect(self.name).width()
        req_level_width = self.fontMetrics().boundingRect(str(self.req_level)).width()
        stats_width = self.fontMetrics().boundingRect(self.stats).width()
        total_width = name_width + req_level_width + stats_width + 30  # Some padding
        height = max(
            self.fontMetrics().boundingRect(self.name).height(),
            self.fontMetrics().boundingRect(str(self.req_level)).height(),
            self.fontMetrics().boundingRect(self.stats).height(),
        )
        return QSize(total_width, height + 10)  # Some padding for the height
