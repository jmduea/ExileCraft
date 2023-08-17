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
from pathlib import Path

from PySide6.QtWidgets import QApplication

from modules.gui.uis.windows.main_window.main_window import MainWindow
from modules.tray.hotkey_methods import register_hotkey
from modules.tray.tray_setup import setup_tray

# Adjust QT Font DPI for high scale and 4k monitors
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

base_dir = Path(__file__).parent


def main():
    """
    Runs the main application.

    This method initializes and runs the main application window using PySide6. It also sets up the tray icon and
    menus, registers hotkeys, and handles any exceptions that occur.

    Returns
    -------
    None

    Raises
    ------
    Exception
        If an error occurs during the execution of the main application.

    Example
    -------
    >>> main()
    """
    try:
        app = QApplication([])
        app.setStyle("Fusion")
        # app.setQuitOnLastWindowClosed(False)
        main_window = MainWindow()

        # Initialize the splash_screen
        window = main_window
        window.show()

        # Set up tray icon and menus
        tray = setup_tray(app, main_window)
        if tray is None:
            print("Tray setup failed")
            return
        # Register hotkeys
        register_hotkey(main_window)

        app.exec()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
