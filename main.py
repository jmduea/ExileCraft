import ctypes
import os
import re
import sys
from ctypes import wintypes

import pyautogui
import pygetwindow as gw
import pywintypes
import win32con
import win32gui
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from game_data import base_items_objects
from mainwindow_ui import Ui_MainWindow

basedir = os.path.dirname(__file__)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowOpacity(0.9)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.populate_item_bases_dropdown()

        self.labels = {
            "PrefixInfo1": self.PrefixInfo1,
            "Prefix1": self.Prefix1,
            "PrefixInfo2": self.PrefixInfo2,
            "Prefix2": self.Prefix2,
            "PrefixInfo3": self.PrefixInfo3,
            "Prefix3": self.Prefix3,
            "SuffixInfo1": self.SuffixInfo1,
            "Suffix1": self.Suffix1,
            "SuffixInfo2": self.SuffixInfo2,
            "Suffix2": self.Suffix2,
            "SuffixInfo3": self.SuffixInfo3,
            "Suffix3": self.Suffix3
        }

    def populate_item_bases_dropdown(self):
        item_bases = [base_item.name for base_item in base_items_objects]
        for item_base in item_bases:
            self.itemBaseBox.addItem(item_base)


        @pyqtSlot()
        def toggle_widget(self):
            if self.CraftingOptionsExtended.isHidden():
                self.CraftingOptionsExtended.show()
            else:
                self.CraftingOptionsExtended.hide()

            self.toggle_widget = toggle_widget

    def update_labels(self, info, labels):
        for key, value in info.items():
            if key.startswith("Prefix") or key.startswith("Suffix"):
                idx = int(key[-1]) - 1
                modifier_info_key = key + "Info"
                if modifier_info_key in labels:
                    labels[modifier_info_key].setText(value["modifier"])
                if key in labels:
                    labels[key].setText(value["text"])
            else:
                if key in labels:
                    labels[key].setText(f"{key}: {value}")

    def update_labels_from_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard_data = clipboard.text()
        info = self.parse_clipboard_data(clipboard_data)
        self.update_labels(info, self.labels)

    def parse_clipboard_data(self, clipboard_data):
        info = {}
        prefix_count = 0
        suffix_count = 0

        for line in clipboard_data.splitlines():
            line = line.strip()

            # Handle the cases where modifier types are present
            if line.startswith("{ Prefix Modifier"):
                modifier_data = re.search(r'\{ Prefix Modifier "(.+)" \(Tier: (\d+)\) — .+}', line)
                if modifier_data:
                    modifier_name = modifier_data.group(1)
                    modifier_tier = modifier_data.group(2)
                    info[f"Prefix{prefix_count}"] = {
                        "modifier": f"{modifier_name} (Tier: {modifier_tier})",
                        "text": ""
                    }
                    prefix_count += 1
            elif line.startswith("{ Suffix Modifier"):
                modifier_data = re.search(r'\{ Suffix Modifier "(.+)" \(Tier: (\d+)\) — .+}', line)
                if modifier_data:
                    modifier_name = modifier_data.group(1)
                    modifier_tier = modifier_data.group(2)
                    info[f"Suffix{suffix_count}"] = {
                        "modifier": f"{modifier_name} (Tier: {modifier_tier})",
                        "text": ""
                    }
                    suffix_count += 1
            else:
                # Extract the actual effect of the modifier and store it in the corresponding key
                if prefix_count > 1:
                    effect = line
                    info[f"Prefix{prefix_count - 1}"]["text"] = effect
                if suffix_count > 1:
                    effect = line
                    info[f"Suffix{suffix_count - 1}"]["text"] = effect

        return info


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
                elif msg.wParam == 2:  # The Ctrl+Alt+C hotkey
                    copy_data_to_clipboard()  # Add a function to handle the new hotkey
                return True, 0
        return False, 0


def copy_data_to_clipboard():
    # Get the active window's title
    active_window_title = gw.getActiveWindowTitle()

    # Use Ctrl+Alt+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')

    # Get the data from the clipboard
    clipboard = QtWidgets.QApplication.clipboard()
    data = clipboard.text()

    # Return the copied data
    return data


# Function for toggling the overlay
def toggle_visibility(window=None):
    if window.isVisible():
        window.hide()
    else:
        copy_data_to_clipboard()
        window.update_labels_from_clipboard()

        window.showNormal()
        window.raise_()
        window.activateWindow()
        print(copy_data_to_clipboard())

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
    print("Main Window Activated")

    # Register the Ctrl+D hotkey
    hotkey_id = 1
    try:
        UnregisterHotKey(None, hotkey_id)
    except pywintypes.error:
        pass  # Ignore the error if the hotkey is not registered
    # Register the hotkey
    win32gui.RegisterHotKey(None, hotkey_id, win32con.MOD_CONTROL, 68)
    print("Ctrl+D Hotkey set")

    # Set event filters
    hotkey_event_filter = HotkeyEventFilter(window)
    app.installNativeEventFilter(hotkey_event_filter)
    print("Hotkey event filter set")

    shortcut = QShortcut(QKeySequence("Ctrl+D"), window)
    shortcut.activated.connect(toggle_visibility)
    print("Shortcut activated")

    try:
        sys.exit(app.exec_())
    except Exception as e:
        import traceback
        print("Error:", e)
        print(traceback.format_exc())
