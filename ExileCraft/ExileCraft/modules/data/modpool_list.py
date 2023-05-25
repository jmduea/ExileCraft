from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QWidget

from modules.data.ui_modpool_list import Ui_modpool_list


class ModPoolList(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_modpool_list()
        self.ui.setupUi(self)

    def update_prefix_tree(self, new_data):
        model = self.ui.prefix_tree.model()
        if model:
            # Assuming that new_data is a list of lists where each sub-list is a row in the tree.
            for row_data in new_data:
                model.appendRow([QStandardItem(str(item)) for item in row_data])
        else:
            print("No model set for the prefix tree.")

# You can now create an instance of ModPoolList and call update_prefix_tree
mod_pool_list = ModPoolList()
mod_pool_list.update_prefix_tree(new_data)
