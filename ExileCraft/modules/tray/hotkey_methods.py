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

import time

import keyboard

# Define the minimum delay between hotkey triggers
HOTKEY_DELAY = 1.0
last_hotkey_trigger_time = 0


def toggle_visibility(window=None):
    """
    Parameters
    ----------
    window : PyQt5.QtWidgets.QMainWindow or None
        The window to toggle visibility. If None, no action will be performed.

    Return
    ------
    None
        This method does not return anything.

    Raises
    ------
    None

    Description
    -----------
    This method toggles the visibility of a PyQt5.QtWidgets.QMainWindow window. If the window is currently visible, it will be hidden. If it is hidden, it will be activated, brought to the front, and shown. The method keeps track of the last time the toggle is triggered to avoid rapid toggling.
    """
    global last_hotkey_trigger_time
    current_time = time.time()
    if current_time - last_hotkey_trigger_time >= HOTKEY_DELAY:
        if window.isVisible():
            window.hide()
        else:
            window.activateWindow()
            window.raise_()
            window.show()
        last_hotkey_trigger_time = current_time


def register_hotkey(window):
    """
    Registers a hotkey for toggling the visibility cooldown on a specified window.

    Parameters
    ----------
    window : modules.gui.uis.windows.main_window.main_window.MainWindow
        The window on which to toggle the visibility cooldown.

    Returns
    -------
    None

    """
    # Register the hotkey using the keyboard library
    keyboard.add_hotkey("ctrl+d", toggle_visibility_cooldown, args=(window,))
    # keyboard.add_hotkey('ctrl+alt+c', window.parse_clipboard_text)


def toggle_visibility_cooldown(window: object = None):
    """
    Parameters
    ----------
    window : object, optional
        The window object on which the visibility will be toggled. If not provided, the default window will be used.

    Returns
    -------
    None
    """
    global last_hotkey_trigger_time
    current_time = time.time()
    if current_time - last_hotkey_trigger_time >= HOTKEY_DELAY:
        toggle_visibility(window)
        last_hotkey_trigger_time = current_time
