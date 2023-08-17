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
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PySide6.QtWidgets import QTreeView, QVBoxLayout


class CustomModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super(CustomModel, self).__init__(parent)
        self.root_items = [
            "Base Modpool",
            "Shaper",
            "Elder",
            "Crusader",
            "Hunter",
            "Warlord",
            "Redeemer",
            "Veiled",
            "Crafted",
            "Essence",
        ]
        self.mod_groups = list(data.keys())
        # self.mods = sum(list(data.values()), [])
        self.mods = []
        for group in self.mod_groups:
            sorted_mods = sorted(data[group], key=lambda mod: mod.level_req)
            self.mods.extend(sorted_mods)
        self.index_map = {}

        for i, group in enumerate(self.mod_groups):
            for mod in data[group]:
                self.index_map[mod.group.group] = i

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():  # If parent exists, then it's a child node
            parent_node = parent.internalPointer()
            return sum(1 for mod in self.mods if mod.group.group == parent_node)
        else:  # If parent does not exist, then it's a root node
            return len(self.mod_groups)  # Number of mod groups

    def columnCount(self, parent=QModelIndex()):
        return (
            1  # Display Name, Level Req, Translation String, Implicit Tags, Tag Weight
        )

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        node = index.internalPointer()

        if role == Qt.DisplayRole:
            if (
                index.parent().isValid()
            ):  # If parent exists, then it's a child node (Mod instance)
                mod_instance = node  # node is a Mod instance here
                return (
                    f"{mod_instance.display_name} (Lvl req. {mod_instance.level_req}) "
                    f"{mod_instance.translation_string}"
                )
            else:  # If parent does not exist, then it's a root node (mod group)
                mod_group = node  # node is a mod group name here
                return mod_group

        return None

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        node = index.internalPointer()

        if isinstance(node, str):  # node is a root node (mod group), has no parent
            return QModelIndex()

        # node is a Mod instance, find its parent (mod group)
        mod_instance = node
        group_index = self.index_map[mod_instance.group.group]
        return self.createIndex(group_index, 0, self.mod_groups[group_index])

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if parent.isValid():  # Parent exists, create index for child node
            parent_node = parent.internalPointer()
            mod_instance = [
                mod
                for mod in self.mods
                if self.index_map[mod.group.group] == self.mod_groups.index(parent_node)
            ][row]
            return self.createIndex(row, column, mod_instance)
        else:  # Parent does not exist, create index for root node
            return self.createIndex(row, column, self.mod_groups[row])


class ModTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.model = None
        self.tree_view = QTreeView(self)
        self.tree_view.header().hide()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tree_view)

    def set_data(self, data):
        self.model = CustomModel(data)
        self.tree_view.setModel(self.model)
