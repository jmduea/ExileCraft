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

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu


def setup_tray(app, window):
    """
    Sets up the system tray icon and its context menu for a given application and window.

    This function initializes a QSystemTrayIcon object with an application-specific icon and makes it visible.
    It then creates a context menu with several QAction objects, each associated with a different function:
    - "Show Window": shows the application window.
    - "Check for Updates": placeholder function for checking for updates.
    - "Settings": placeholder function for opening settings.
    - "Donate": placeholder function for opening donation page.
    - "Quit": quits the application.

    The context menu is then attached to the system tray icon and displayed.

    :param app: A reference to the QApplication object where the system tray is to be set up.
    :param window: A reference to the QMainWindow object where the system tray is to be set up.
    :return: Returns the initialized QSystemTrayIcon object.
    """
    basedir = os.path.dirname(__file__)
    icon_path = os.path.join(basedir, '../gui/assets/images/icons/vendor.ico')

    icon = QIcon(icon_path)

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    menu.setStyleSheet("""
        QMenu {
            font-size: 14px;
        }
    """)

    show_window = QAction("Show Window")
    show_window.triggered.connect(window.show)
    menu.addAction(show_window)

    check_updates = QAction("Check for Updates")
    check_updates.triggered.connect(lambda: print("Checking for updates..."))  # TODO Replace with actual function
    menu.addAction(check_updates)

    settings = QAction("Settings")
    settings.triggered.connect(lambda: print("Opening settings..."))  # TODO Replace with actual function
    menu.addAction(settings)

    donate = QAction("Donate")
    donate.triggered.connect(lambda: print("Opening donation page..."))  # TODO Replace with actual function
    menu.addAction(donate)

    quit_action = QAction("Quit")
    quit_action.triggered.connect(app.quit)
    menu.addAction(quit_action)

    tray.setContextMenu(menu)
    tray.show()
    return tray
