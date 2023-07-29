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

import os
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from modules.gui.core.functions import Functions
from modules.gui.core.json_settings import Settings
from modules.gui.uis.windows.main_window.functions_main_window import (
    ComboboxUpdater,
    MainFunctions,
)
from modules.gui.uis.windows.main_window.setup_main_window import SetupMainWindow
from modules.gui.uis.windows.main_window.ui_mainwindow import UI_MainWindow
from modules.shared.config.gui_constants import (
    BTN_CLOSE_LEFT_COLUMN,
    BTN_HOME,
    BTN_INFO,
    BTN_PAGE_2,
    BTN_PAGE_3,
    BTN_SETTINGS,
    BTN_TOP_SETTINGS,
)
from modules.tray.hotkey_methods import register_hotkey
from modules.tray.tray_setup import setup_tray

# Adjust QT Font DPI for high scale and 4k monitors
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'


basedir = os.path.dirname(__file__)


class MainWindow(QtWidgets.QMainWindow):
    """Main Window Class"""

    def __init__(self, *args, **kwargs):
        # Setup Main Window UI
        super().__init__(*args, **kwargs)
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.setWindowOpacity(0.8)
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.combobox_updater = ComboboxUpdater(
            self.ui.left_column.menus.base_group_combobox,
            self.ui.left_column.menus.base_combobox,
            self.ui.left_column.menus.base_item_combobox,
            self.ui.left_column.menus.item_level_spinbox,
            self.ui.left_column.menus.item_quality_spinbox,
            self.ui.load_pages.item_img_label,
            self.ui.load_pages.item_properties_label,
            self.ui.load_pages.item_requirements_label,
            self.ui.load_pages.item_level_label,
            self.ui.load_pages.item_quality_label,
            self.ui.load_pages.item_header_label,
            self.ui.load_pages.item_implicits_container,
            self.ui.load_pages.item_implicits_label,
            self.ui.load_pages.item_spacer_3,
            self.ui.load_pages.prefix_1_container,
            self.ui.load_pages.prefix_2_container,
            self.ui.load_pages.prefix_3_container,
            self.ui.load_pages.suffix_1_container,
            self.ui.load_pages.suffix_2_container,
            self.ui.load_pages.suffix_3_container,
        )

        # Load Settings
        settings = Settings()
        self.settings = settings.items

        # Hide size grips
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)
        SetupMainWindow.setup_comboboxes(self)

        # Show the main window
        self.show()
        self.ui.load_pages.item_implicits_container.hide()
        self.ui.load_pages.item_spacer_3.hide()

    def select_menu_and_load_page(self, btn, page):
        """Select Menu And Load Page"""
        self.ui.left_menu.select_only_one(btn.objectName())
        MainFunctions.set_page(self, page)

    @staticmethod
    def set_button_active(button):
        """Set Button Active"""
        button.set_active(True)

    def btn_clicked(self):
        """Handle Button Clicks"""
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != BTN_SETTINGS:
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active
        top_settings = MainFunctions.get_title_bar_btn(self, BTN_TOP_SETTINGS)
        top_settings.set_active(False)

        # HOME BTN
        if btn.objectName() == BTN_HOME:
            self.select_menu_and_load_page(btn, self.ui.load_pages.crafting_emu_page)

        # Page 2 btn
        if btn.objectName() == BTN_PAGE_2:
            self.select_menu_and_load_page(btn, self.ui.load_pages.modpool_page)

        # Page 3 btn
        if btn.objectName() == BTN_PAGE_3:
            self.select_menu_and_load_page(btn, self.ui.load_pages.crafting_calc_page)

        # BOTTOM INFORMATION
        if btn.objectName() == BTN_INFO:
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == BTN_CLOSE_LEFT_COLUMN:
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != BTN_CLOSE_LEFT_COLUMN:
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Item Settings",
                    icon_path=Functions.set_svg_icon("icon_info.svg"),
                )

        # SETTINGS LEFT
        if (
            btn.objectName() == BTN_SETTINGS
            or btn.objectName() == BTN_CLOSE_LEFT_COLUMN
        ):
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == BTN_CLOSE_LEFT_COLUMN:
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != BTN_CLOSE_LEFT_COLUMN:
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg"),
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == BTN_TOP_SETTINGS:
            # Toggle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            btn_settings = MainFunctions.get_left_menu_btn(self, BTN_SETTINGS)
            btn_settings.set_active_tab(False)

            btn_info = MainFunctions.get_left_menu_btn(self, BTN_INFO)
            btn_info.set_active_tab(False)

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check function by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        """Run function when btn is released"""
        # GET BT CLICKED
        self.btn = SetupMainWindow.setup_btns(self)

    # RESIZE EVENT
    def resizeEvent(self, event):
        """Event when window is resized"""
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """Event when mouse is pressed"""
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def leaveEvent(self, event):
        """Event when mouse leaves the window"""
        QtWidgets.QApplication.instance().restoreOverrideCursor()


if __name__ == "__main__":
    app = QApplication()
    # app.setQuitOnLastWindowClosed(False)

    window = MainWindow()

    # Set up tray icon
    tray = setup_tray(app, window)

    # Registers hotkeys
    register_hotkey(window)

    sys.exit(app.exec())
