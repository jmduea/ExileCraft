import os
import sys

from PySide6 import QtGui
from PySide6.QtQuick import QQuickView
from PySide6.QtWidgets import QApplication

from modules.tray.hotkey_methods import register_hotkey
from modules.tray.tray_setup import SetupTray
from modules.ui.main_window import MainWindow, SplashScreen

basedir = os.path.dirname(__file__)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    window = SplashScreen()
    window.show()

    # Set up tray icon
    tray = SetupTray(app, window)

    # Registers hotkeys
    register_hotkey(window)

    sys.exit(app.exec())
