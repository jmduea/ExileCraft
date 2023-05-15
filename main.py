import os
import sys

from PyQt5 import QtGui, QtWidgets

from ExileCraft.tray.hotkey_methods import register_hotkey
from ExileCraft.tray.tray_setup import SetupTray
from ExileCraft.ui.main_window import MainWindow

basedir = os.path.dirname(__file__)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'assets/images/vendor.png')))
    app.setQuitOnLastWindowClosed(False)

    window = MainWindow()
    window.show()

    # Set up tray icon
    tray = SetupTray(app, window)

    # Registers hotkeys
    register_hotkey(window)

    sys.exit(app.exec_())
