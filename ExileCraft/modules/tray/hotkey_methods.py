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

import keyboard
import time

# Define the minimum delay between hotkey triggers
HOTKEY_DELAY = 1.0
last_hotkey_trigger_time = 0


def toggle_visibility(window=None):
    """
    Toggles the visibility of a window based on its current state.

    If the window is currently visible, it will be hidden. If the window is hidden,
    it will be shown, activated, and raised to the top.

    Args:
        window: Optional reference to the window object. If not provided, the function will have no effect.
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
    Register hotkeys to the application window instance.
    
    Args:
        window: A reference to the window object.
    """
    # Register the hotkey using the keyboard library
    keyboard.add_hotkey('ctrl+d', toggle_visibility_cooldown, args=(window,))
    # keyboard.add_hotkey('ctrl+alt+c', window.parse_clipboard_text)


def toggle_visibility_cooldown(window: object = None):
    """
    Adds a cooldown period to the toggle_visibility function.
    
    The objective of the toggle_visibility_cooldown function is to add a cooldown period to the toggle_visibility
    function, which toggles the visibility of a window based on its current state. This is achieved by checking the
    time elapsed since the last hotkey trigger and only executing the toggle_visibility function if the elapsed time
    is greater than or equal to the HOTKEY_DELAY.
    
    Args:
        window: A reference to the window object
    """
    global last_hotkey_trigger_time
    current_time = time.time()
    if current_time - last_hotkey_trigger_time >= HOTKEY_DELAY:
        toggle_visibility(window)
        last_hotkey_trigger_time = current_time
