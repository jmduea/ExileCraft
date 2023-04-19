import ctypes
from ctypes import wintypes
import sys, os
import win32con
import win32gui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from mainwindow_ui import Ui_MainWindow
import resources_rc

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

        self.CraftingOptionsExtended.hide()



        @pyqtSlot()
        def toggle_widget(self):
            if self.CraftingOptionsExtended.isHidden():
                self.CraftingOptionsExtended.show()
            else:
                self.CraftingOptionsExtended.hide()


class HotkeyEventFilter(QAbstractNativeEventFilter):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def nativeEventFilter(self, eventType, message):
        if eventType == "windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(int(message))
            if msg.message == win32con.WM_HOTKEY:
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
    showexilecraft = QAction("Show Crafting Window")
    menu.addAction(showexilecraft)

    # Add a Quit option to the menu
    quitexilecraft = QAction("Quit")
    quitexilecraft.triggered.connect(app.quit)
    menu.addAction(quitexilecraft)

    # Add menu to the tray
    tray.setContextMenu(menu)

    # Load the Fontin-Regular font
    font_database = QFontDatabase()
    font_database.addApplicationFont(os.path.join(basedir, 'assets/fonts/fontin-regular.otf'))
    app.setFont(QFont('Fontin-Regular'))

    window = MainWindow()
    window.show()
    print("Main Window Activated")

    # Register the hotkey
    hotkey_id = 1
    UnregisterHotKey(None, hotkey_id)
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
