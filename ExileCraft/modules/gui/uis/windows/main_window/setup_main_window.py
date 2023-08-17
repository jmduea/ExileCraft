# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from modules.gui.core.functions import Functions
from modules.gui.core.json_settings import Settings
from modules.gui.core.json_themes import Themes
from modules.gui.uis.windows.main_window.functions_main_window import (
    GUIUpdater,
    MainFunctions,
)
from modules.gui.uis.windows.main_window.ui_mainwindow import UiMainWindow
from modules.gui.widgets import PyGrips, PyPushButton
from modules.gui.widgets.py_mods_tab_widget import ModsWidget
from modules.shared.config.gui_constants import (
    ADD_LEFT_MENUS,
    ADD_TITLE_BAR_MENUS,
)


class SetupMainWindow:
    """
    This class sets up the main window of the application, including the left and right columns,
    title bar, buttons, and other GUI elements. It also handles the resizing of the window and
    the updating of comboboxes based on user interaction.

    Attributes:
        add_left_menus (list): A list of dictionaries, each representing a button to be added to the left menu.
        add_title_bar_menus (list): A list of dictionaries, each representing a button to be added to the title bar.
    """

    def __init__(self, parent: QMainWindow, *args, **kwargs):
        """Initializes the SetupMainWindow class, setting up the UI."""
        super().__init__(parent, *args, **kwargs)
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        self.ui = UiMainWindow()
        self.settings = Settings()
        self.ui.setup_ui(parent)

    add_left_menus = ADD_LEFT_MENUS
    add_title_bar_menus = ADD_TITLE_BAR_MENUS

    def setup_btns(self):
        """
        Sets up the buttons for the UI, returning the sender of the button that was clicked.

        Returns:
            QPushButton: The button that was clicked.
        """
        if self.ui.title_bar.sender() is not None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() is not None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() is not None:
            return self.ui.left_column.sender()
        elif self.ui.right_column.sender() is not None:
            return self.ui.right_column.sender()
        elif self.ui.load_pages.sender() is not None:
            return self.ui.load_pages.sender()

    def setup_gui(self):
        """Sets up the GUI for the application, including the title, custom widgets, and animations."""
        self.setWindowTitle(self.settings["app_name"])

        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            # self.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to ExileCraft")

        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        MainFunctions.set_page(self, self.ui.load_pages.crafting_emu_page)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg"),
        )
        MainFunctions.set_right_column_menu(
            self, self.ui.right_column.crafting_methods_menu
        )

        themes = Themes()
        self.themes = themes.items

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Next",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(
            lambda: MainFunctions.set_right_column_menu(
                self, self.ui.right_column.menu_2
            )
        )
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Previous",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(
            lambda: MainFunctions.set_right_column_menu(
                self, self.ui.right_column.crafting_methods_menu
            )
        )
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)
        self.gui_updater = GUIUpdater(self)
        self.mods_widget = ModsWidget(self)
        self.ui.load_pages.mod_widget_layout.addWidget(self.mods_widget)

    def resize_grips(self):
        """Resizes the grips of the window based on the current window size."""
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15
            )

    def setup_left_menu_connections(self):
        """Sets up the comboboxes in the UI, connecting their signals to the appropriate slots for updating the UI."""
        self.ui.left_column.menus.base_group_combobox.setCurrentIndex(-1)
        # Base group combobox connections
        self.ui.left_column.menus.base_group_combobox.currentTextChanged.connect(
            self.gui_updater.clear_item_view_box_background
        )
        self.ui.left_column.menus.base_group_combobox.currentTextChanged.connect(
            self.gui_updater.clear_labels
        )
        self.ui.left_column.menus.base_group_combobox.currentIndexChanged.connect(
            self.gui_updater.update_base_combobox
        )

        # Base combobox connections
        self.ui.left_column.menus.base_combobox.currentTextChanged.connect(
            self.gui_updater.clear_labels
        )
        self.ui.left_column.menus.base_combobox.currentTextChanged.connect(
            self.gui_updater.clear_item_view_box_background
        )
        self.ui.left_column.menus.base_combobox.currentIndexChanged.connect(
            self.gui_updater.update_base_item_combobox
        )

        # Base item combobox connections
        if self.ui.left_column.menus.base_item_combobox.currentText != "":
            self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(
                self.gui_updater.set_current_item
            )
            self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(
                self.gui_updater.set_item_header_label
            )
            self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(
                self.gui_updater.set_item_view_box_background
            )
            self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(
                self.gui_updater.update_labels
            )
        else:
            self.gui_updater.clear_labels()

        # Item level spinbox connections
        self.ui.left_column.menus.item_level_spinbox.valueChanged.connect(
            self.gui_updater.set_item_level
        )

        # Quality Spinbox connections
        self.ui.left_column.menus.item_quality_spinbox.valueChanged.connect(
            self.gui_updater.set_item_quality
        )

        # Item influence pushbutton connections
        self.ui.left_column.menus.crusader_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.crusader_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )

        self.ui.left_column.menus.elder_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.elder_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )

        self.ui.left_column.menus.hunter_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.hunter_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )

        self.ui.left_column.menus.redeemer_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.redeemer_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )

        self.ui.left_column.menus.shaper_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.shaper_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )

        self.ui.left_column.menus.warlord_btn.button_checked.connect(
            self.gui_updater.set_influence
        )
        self.ui.left_column.menus.warlord_btn.button_unchecked.connect(
            self.gui_updater.remove_influence
        )
