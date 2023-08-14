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
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Signal

from modules.gui.core.functions import Functions
from modules.gui.core.json_settings import Settings
from modules.gui.splash_screen import SplashScreen
from modules.gui.uis.windows.main_window.functions_main_window import (
    ButtonFunctions,
    MainFunctions,
)
from modules.gui.uis.windows.main_window.setup_main_window import SetupMainWindow
from modules.gui.uis.windows.main_window.ui_mainwindow import UiMainWindow
from modules.gui.widgets import PyCustomCursorButton
from modules.shared.config.gui_constants import (
    BTN_CLOSE_LEFT_COLUMN,
    BTN_HOME,
    BTN_INFO,
    BTN_PAGE_2,
    BTN_PAGE_3,
    BTN_SETTINGS,
    BTN_TOP_SETTINGS,
)


class MainWindow(QtWidgets.QMainWindow):
    """Main Window Class"""

    window_initialized = Signal()

    def __init__(self, *args, **kwargs):
        # Setup Main Window UI
        super().__init__(*args, **kwargs)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.setWindowOpacity(0.8)

        # Load Settings
        settings = Settings()
        self.settings = settings.items

        # Hide size grips
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)
        SetupMainWindow.setup_left_menu_connections(self)

        # Show the main window
        self.ui.load_pages.item_implicits.hide()
        self.ui.load_pages.item_spacer_3.hide()
        self.splash_screen = SplashScreen(self)
        self.ui.load_pages.item_img_label.mousePressEvent = (
            self.handle_item_img_label_click
        )

    def btn_clicked(self):
        """Handle Button Clicks"""
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != BTN_SETTINGS:
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active
        top_settings = ButtonFunctions.get_title_bar_btn(self, BTN_TOP_SETTINGS)
        top_settings.set_active(False)

        # HOME BTN
        if btn.objectName() == BTN_HOME:
            MainFunctions.select_menu_and_load_page(
                self, btn, self.ui.load_pages.crafting_emu_page
            )

        # Page 2 btn
        if btn.objectName() == BTN_PAGE_2:
            MainFunctions.select_menu_and_load_page(
                self, btn, self.ui.load_pages.modpool_page
            )

        # Page 3 btn
        if btn.objectName() == BTN_PAGE_3:
            MainFunctions.select_menu_and_load_page(
                self, btn, self.ui.load_pages.crafting_calc_page
            )

        # BOTTOM INFORMATION
        if btn.objectName() == BTN_INFO:
            # Checks if left column is visible and if not, show it and select the tab corresponding to the button
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            # If left column is visible, check if the menu for the button is visible and if so, hide the left column
            elif self.ui.left_column.menus.menu_2.isVisible():
                MainFunctions.toggle_left_column(self)
            # If left column is visible, check if the btn clicked is the close btn and if so, hide the left column
            else:
                if btn.objectName() == BTN_CLOSE_LEFT_COLUMN:
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            # If the btn clicked is not the close btn, set the left column menu
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
            # Checks if left column is visible and if not, show it and select the tab corresponding to the button
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Checks if menu 1 is already visible and if so, hide it
            elif self.ui.left_column.menus.menu_1.isVisible():
                MainFunctions.toggle_left_column(self)
            # If menu 1 is visible, check if the button clicked is the close button and if so, hide the left column
            else:
                if btn.objectName() == BTN_CLOSE_LEFT_COLUMN:
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            # If the button clicked is not the close button, set the menu to menu 1
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
            btn_settings = ButtonFunctions.get_left_menu_btn(self, BTN_SETTINGS)
            btn_settings.set_active_tab(False)

            btn_info = ButtonFunctions.get_left_menu_btn(self, BTN_INFO)
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
        """
        Event when mouse leaves the window

        Used to ensure that when the mouse cursor leaves the window, the cursor is reset to the default cursor.
        Args:
            event (QEvent): Event
        """
        QtWidgets.QApplication.instance().restoreOverrideCursor()

    def handle_item_img_label_click(self, event):
        if event.button() == Qt.LeftButton:
            checked_button = None

            for child_widget in self.ui.right_column.crafting_methods_menu.children():
                if (
                    isinstance(child_widget, PyCustomCursorButton)
                    and child_widget.isChecked()
                ):
                    checked_button = child_widget
                    break

        if checked_button:
            print(checked_button.objectName())
            method_name = (
                checked_button.objectName().replace("method_", "").replace("_btn", "")
            )
            print(method_name)
            if hasattr(self, method_name):
                getattr(self, method_name)(self.current_item)
