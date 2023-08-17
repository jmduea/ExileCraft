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

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import (
    QWidget,
)

from modules.gui.widgets.py_mods_tab_widget.mods_model_views import (
    ModItemModel,
    ModSortFilterProxyModel,
)
from modules.gui.widgets.py_mods_tab_widget.ui_mods_widget import Ui_mods_widget
from modules.shared.config.constants import (
    SPAWNABLE_ITEM_MOD_DOMAINS,
    SPAWNABLE_ITEM_MOD_GENERATION_TYPES,
)

# Generate the relative path from the source file to the target file
relative_path = Path("modules/data/json/mods.min.json")

print(relative_path)


class ModsWidget(QWidget):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)

        if not parent.objectName():
            parent.setObjectName("MainWindow")
        self.parent = parent
        self.ui = Ui_mods_widget()
        self.ui.setupUi(self)
        self.mod_item_model = ModItemModel(relative_path)
        self.prefix_proxy_model = None
        self.suffix_proxy_model = None
        self.implicit_proxy_model = None
        self.prefix_view = None
        self.suffix_view = None
        self.implicit_view = None
        self.gui_updater = self.parent.gui_updater
        self.current_item = self.gui_updater.current_item
        self.load_data()
        self.gui_updater.item_changed.connect(self.load_data)

    def load_data(self):
        if self.current_item:
            active_tab = self.ui.mods_tab_widget.currentWidget().objectName()

            if active_tab == "prefixes_tab":
                None if self.prefix_view else self.refresh_or_create_prefix_view()
            elif active_tab == "suffixes_tab":
                None if self.suffix_view else self.refresh_or_create_suffix_view()
            else:
                None if self.implicit_view else self.refresh_or_create_implicit_view()
        else:
            self.refresh_or_create_implicit_view()
            self.refresh_or_create_suffix_view()
            self.refresh_or_create_prefix_view()

    def load_filter(self, generation_type):
        return (
            {
                "generation_type": generation_type,
                "domain": self.current_item.domain,
                "tags": self.current_item.tags,
                "required_level": self.current_item.item_level,
                "is_essence_only": False,
            }
            if self.current_item is not None
            else {
                "generation_type": SPAWNABLE_ITEM_MOD_GENERATION_TYPES,
                "domain": SPAWNABLE_ITEM_MOD_DOMAINS,
                "required_level": 100,
            }
        )

    def refresh_or_create_prefix_view(self):
        prefix_filters = self.load_filter("prefix")
        if not self.prefix_proxy_model:
            self.prefix_proxy_model = ModSortFilterProxyModel(filters=prefix_filters)
            self.prefix_proxy_model.setSourceModel(self.mod_item_model)
            self.ui.prefixes_view.setModel(self.prefix_proxy_model)
        else:
            self.prefix_proxy_model.setFilters(prefix_filters)
            self.prefix_proxy_model.refresh()

    def refresh_or_create_suffix_view(self):
        suffix_filters = self.load_filter("suffix")
        if not self.suffix_proxy_model:
            self.suffix_proxy_model = ModSortFilterProxyModel(filters=suffix_filters)
            self.suffix_proxy_model.setSourceModel(self.mod_item_model)
            self.ui.suffixes_view.setModel(self.suffix_proxy_model)
        else:
            self.suffix_proxy_model.setFilters(suffix_filters)
            self.suffix_proxy_model.refresh()

    def refresh_or_create_implicit_view(self):
        implicit_filters = self.load_filter("corrupted")
        if not self.implicit_proxy_model:
            self.implicit_proxy_model = ModSortFilterProxyModel(
                filters=implicit_filters
            )
            self.implicit_proxy_model.setSourceModel(self.mod_item_model)
            self.ui.implicits_view.setModel(self.implicit_proxy_model)
        else:
            self.implicit_proxy_model.setFilters(implicit_filters)
            self.implicit_proxy_model.refresh()
