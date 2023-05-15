import keyboard
import time

# Define the minimum delay between hotkey triggers
HOTKEY_DELAY = 0.5
last_hotkey_trigger_time = 0


def toggle_visibility(window=None):
    """
    Toggles the visibility of the application window.

    This function checks if the window is currently visible. If it is, it hides the window. If it's not visible,
    it shows the window, raises it to the top, and activates it.

    The function is designed to avoid rapid toggling by incorporating a delay (HOTKEY_DELAY).
    It will only allow toggling if the elapsed time since the last trigger is greater than or equal to the delay.

    :param window: A reference to the window object to be toggled. Default is None.
    """
    global last_hotkey_trigger_time
    current_time = time.time()
    if current_time - last_hotkey_trigger_time >= HOTKEY_DELAY:
        if window.isVisible():
            window.hide()
        else:
            window.showNormal()
            window.raise_()
            window.activateWindow()
        last_hotkey_trigger_time = current_time


def register_hotkey(window):
    """
    Registers a hotkey for the application and window.

    This function uses the keyboard library to register a hotkey. When the hotkey is pressed, it triggers
    the toggle_visibility function.

    :param window: A reference to the window object where the hotkey is to be registered.
    """
    hotkey = "ctrl+D"
    # Register the hotkey using the keyboard library
    keyboard.add_hotkey(hotkey, toggle_visibility, args=(window,))
