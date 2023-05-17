import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction


def SetupTray(app, window):
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
    icon_path = os.path.join(basedir, '../ui/assets/icons/vendor.ico')

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

    showWindow = QAction("Show Window")
    showWindow.triggered.connect(window.show)
    menu.addAction(showWindow)

    checkUpdates = QAction("Check for Updates")
    checkUpdates.triggered.connect(lambda: print("Checking for updates..."))  #TODO Replace with actual function
    menu.addAction(checkUpdates)

    settings = QAction("Settings")
    settings.triggered.connect(lambda: print("Opening settings..."))  #TODO Replace with actual function
    menu.addAction(settings)

    donate = QAction("Donate")
    donate.triggered.connect(lambda: print("Opening donation page..."))  #TODO Replace with actual function
    menu.addAction(donate)

    quitAction = QAction("Quit")
    quitAction = QAction("Quit")
    quitAction.triggered.connect(app.quit)
    menu.addAction(quitAction)

    tray.setContextMenu(menu)
    tray.show()
    return tray
