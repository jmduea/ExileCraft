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

import os
import sys

from PySide6 import QtGui

from modules.gui.core.functions import Functions
from modules.gui.core.json_settings import Settings
from modules.gui.uis.windows.main_window.functions_main_window import MainFunctions
from modules.gui.uis.windows.main_window.setup_main_window import SetupMainWindow
from modules.gui.uis.windows.main_window.ui_mainwindow import UI_MainWindow
from modules.tray.hotkey_methods import register_hotkey
from modules.tray.tray_setup import SetupTray

from qt_core import *

# Adjust QT Font DPI for high scale and 4k monitors
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'


basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        # Setup Main Window UI
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.setWindowOpacity(.8)

        # Load Settings
        settings = Settings()
        self.settings = settings.items

        # Hide size grips
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)

        # Show the main window
        self.show()

        self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(self.set_item_header_label)
        self.ui.left_column.menus.base_item_combobox.currentTextChanged.connect(self.set_item_view_box_background)
        self.ui.left_column.menus.base_group_combobox.currentTextChanged.connect(self.clear_item_view_box_background)
        self.ui.left_column.menus.base_combobox.currentTextChanged.connect(self.clear_item_view_box_background)

        self.ui.left_column.menus.item_level_spinbox.valueChanged.connect(self.set_item_level)
        self.ui.left_column.menus.item_quality_spinbox.valueChanged.connect(self.set_item_quality)

    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # Page 2 btn
        if btn.objectName() == "btn_page_2":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # Page 3 btn
        if btn.objectName() == "btn_page_3":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Item Settings",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            btn_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            btn_settings.set_active_tab(False)

            btn_info = MainFunctions.get_left_menu_btn(self, "btn_info")
            btn_info.set_active_tab(False)

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

    # RESIZE EVENT
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def leaveEvent(self, event):
        QApplication.instance().restoreOverrideCursor()

    def set_item_view_box_background(self):
        """
        Sets the background of the item view box to the image of the currently selected item.

        This method fetches the name of the currently selected item from the base item combo box,
        modifies the name to match the naming convention of the item images, constructs the path to
        the image, and then attempts to load and display the image in the item view box.

        If the image fails to load or an error occurs during the process, a message is printed to
        the console. If the image is loaded successfully, it is displayed in the item view box and
        is centered and not scaled.

        Raises:
        Exception: If an error occurs when loading the image.
        """
        base_item_name = self.ui.left_column.menus.base_item_combobox.currentText()
        base_item = base_item_name.replace(' ', '_').lower()
        image_path = os.path.abspath(
            os.path.join('F:', 'modules', 'gui', 'assets', 'images', 'items',
                         base_item + '.png'))
        print(image_path)
        try:
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image at {image_path}")
            else:
                self.ui.load_pages.item_img_label.setPixmap(pixmap)
                self.ui.load_pages.item_img_label.setAlignment(Qt.AlignCenter)
                self.ui.load_pages.item_img_label.setScaledContents(False)
        except Exception as e:
            print(f"Error loading image: {e}")

    def clear_item_view_box_background(self):
        """
        Clears the background image of a label widget assigned to the item_img_label attribute of the load_pages object in the current instance of a class.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        self.ui.load_pages.item_img_label.setPixmap(QPixmap())

    def set_item_header_label(self):
        """
           Update the item header label in the load_pages object by retrieving the currently selected item from the base_item_combobox object in the left_column object.

           Args:
               self: The current instance of the class where the method is called.

           Returns:
               None
           """
        item_name = self.ui.left_column.menus.base_item_combobox.currentText()
        self.update_item_header_label(item_name)

    def update_item_header_label(self, item_name):
        """
        Updates the item header label in the load_pages object with the provided item name.

        Args:
            item_name: The string name of the item to be displayed in the item header label.

        Returns:
            None
        """
        self.ui.load_pages.item_header_label.setText(item_name)

    def set_item_level(self):
        """
            Sets the item level value from the item_level_spinbox object in the left_column object and updates the HTML formatted label to display the item level in the load_pages object.

            Args:
                self: The current instance of the class where the method is called.

            Returns:
                None
            """
        item_level_value = self.ui.left_column.menus.item_level_spinbox.value()
        item_level = str(item_level_value)
        item_html = f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Item Level: </span>' \
                    f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_level}</span></p>'
        self.update_item_level_label(item_html)

    def set_item_quality(self):
        """
            Sets the item quality value from the item_quality_spinbox object in the left_column object and updates the HTML formatted label to display the item quality percentage in the load_pages object.

            Args:
                self: The current instance of the class where the method is called.

            Returns:
                None
            """
        item_quality_value = self.ui.left_column.menus.item_quality_spinbox.value()
        item_quality = str(item_quality_value)
        quality_html = f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Quality: </span>' \
                       f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_quality}%</span></p>'
        self.update_item_quality_label(quality_html)

    def update_item_level_label(self, item_level):
        """
            Updates the item level label in the load_pages object with the provided HTML formatted string.

            Args:
                item_level: The HTML formatted string to be displayed in the item level label.

            Returns:
                None
            """
        self.ui.load_pages.item_level_label.setText(item_level)

    def update_item_quality_label(self, quality_html):
        """
            Updates the item quality label in the load_pages object with the provided HTML formatted string.

            Args:
                quality_html: The HTML formatted string to be displayed in the item quality label.

            Returns:
                None
            """
        self.ui.load_pages.item_quality_label.setText(quality_html)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)

    window = MainWindow()

    # Set up tray icon
    tray = SetupTray(app, window)

    # Registers hotkeys
    register_hotkey(window)

    sys.exit(app.exec())
