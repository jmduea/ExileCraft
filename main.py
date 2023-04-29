import ctypes
import os
import sys
from ctypes import wintypes
import pywintypes
import win32con
import win32gui
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_updater
from mainwindow_ui import Ui_MainWindow
from ui_updater import UIUpdater
from craftingsim import CraftingSimulator
from databasehandler import DatabaseHandler

basedir = os.path.dirname(__file__)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowOpacity(0.85)
        self.ui_updater = ui_updater
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.item_subtype_combobox.clear()
        self.item_subtype_combobox.hide()
        self.base_item_combobox.clear()
        self.base_item_combobox.hide()
        self.base_item_influence_combobox.hide()
        self.base_item_level_combobox.hide()
        self.base_item_quality_combobox.hide()
        self.ui_updater = UIUpdater(
            self.item_class_combobox,
            self.item_subtype_combobox,
            self.base_item_combobox,
            self.base_item_level_combobox,
            self.base_item_quality_combobox,
            self.base_item_influence_combobox,
            self.item_header_text_label,
            self.ItemProperties,
            self.ItemRequirements,
            self.ItemImplicits,
            self.ItemSpacer3,
            self.Modifiers,
            self.item_img_box,
            self
        )
        db_handler = DatabaseHandler()
        self.crafting_simulator = CraftingSimulator(db_handler)
        self.import_custom_item = self.import_custom_item
        self.import_custom_item.clicked.connect(lambda: self.crafting_simulator.open_crafting_project_dialog())

        mods_data = self.ui_updater.get_mods_for_item_class()


class HotkeyEventFilter(QAbstractNativeEventFilter):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def nativeEventFilter(self, eventType, message):
        if eventType == "windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(int(message))
            if msg.message == win32con.WM_HOTKEY:
                if msg.wParam == 1:  # The Ctrl+D hotkey
                    toggle_visibility(self.window)
                return True, 0
        return False, 0


# Function for toggling the overlay
def toggle_visibility(window=None):
    if window.isVisible():
        window.hide()
    else:
        window.showNormal()
        window.raise_()
        window.activateWindow()


# Define the UnregisterHotKey function
user32 = ctypes.WinDLL('user32', use_last_error=True)
UnregisterHotKey = user32.UnregisterHotKey
UnregisterHotKey.restype = wintypes.BOOL
UnregisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'assets/images/vendor.png')))
    app.setQuitOnLastWindowClosed(False)

    # Create system tray icon
    icon = QIcon(os.path.join(basedir, 'assets/images/vendor.png'))

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    showExileCraft = QAction("Show Crafting Window")
    menu.addAction(showExileCraft)

    # Add a Quit option to the menu
    quitExileCraft = QAction("Quit")
    quitExileCraft.triggered.connect(app.quit)
    menu.addAction(quitExileCraft)

    # Add menu to the tray
    tray.setContextMenu(menu)

    # Load the Fontin-Regular font
    font_database = QFontDatabase()
    font_database.addApplicationFont(os.path.join(basedir, 'assets/fonts/fontin-regular.otf'))
    app.setFont(QFont('Fontin-Regular'))

    window = MainWindow()
    window.show()

    # Register the Ctrl+D hotkey
    hotkey_id = 1
    try:
        UnregisterHotKey(None, hotkey_id)
    except pywintypes.error:
        pass  # Ignore the error if the hotkey is not registered
    # Register the hotkey
    win32gui.RegisterHotKey(None, hotkey_id, win32con.MOD_CONTROL, 68)

    # Set event filters
    hotkey_event_filter = HotkeyEventFilter(window)
    app.installNativeEventFilter(hotkey_event_filter)

    shortcut = QShortcut(QKeySequence("Ctrl+D"), window)
    shortcut.activated.connect(toggle_visibility)

    try:
        sys.exit(app.exec_())
    except Exception as e:
        import traceback
        print("Error:", e)
        print(traceback.format_exc())
