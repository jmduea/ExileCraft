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

import pytest

from modules.tray import hotkey_methods
from modules.tray.hotkey_methods import HOTKEY_DELAY, last_hotkey_trigger_time, toggle_visibility


class TestToggleVisibility:
    @pytest.fixture(autouse=True)
    def reset_last_hotkey_trigger_time(self):
        hotkey_methods.last_hotkey_trigger_time = 0
        print(f"reset_last_hotkey_trigger_time: {hotkey_methods.last_hotkey_trigger_time}")

    def test_toggle_visibility_visible_window(self, mocker):
        """
        Tests toggling visibility of a visible window.
        """
        print(last_hotkey_trigger_time)
        window = mocker.Mock()
        window.isVisible.return_value = True

        toggle_visibility(window)
        print(window.method_calls)
        window.hide.assert_called_once()

    def test_toggle_visibility_hidden_window(self, mocker):
        """
        Tests toggling visibility of a hidden window.
        """
        window = mocker.Mock()
        window.isVisible.return_value = False

        toggle_visibility(window)
        print(window.method_calls)
        window.show.assert_called_once()
        window.raise_.assert_called_once()
        window.activateWindow.assert_called_once()

    def test_toggle_visibility_maximized_window(self, mocker):
        """
        Tests toggling visibility of a maximized window.
        """
        window = mocker.Mock()
        window.isVisible.return_value = True
        window.isMaximized.return_value = True

        toggle_visibility(window)
        print(window.method_calls)
        window.hide.assert_called_once()

    def test_toggle_visibility_delay_respected(self, mocker):
        """
        Tests ensuring the delay between toggles is respected.
        """
        window = mocker.Mock()
        window.isVisible.return_value = True

        toggle_visibility(window)
        time.sleep(HOTKEY_DELAY / 2)
        toggle_visibility(window)

        print(window.method_calls)
        window.hide.assert_called_once()

    def test_toggle_visibility_not_in_focus_window(self, mocker):
        """
        Tests toggling visibility of a window that is not in focus.
        """
        window = mocker.Mock()
        window.isVisible.return_value = True
        window.isActiveWindow.return_value = False

        toggle_visibility(window)
        print(window.method_calls)
        window.hide.assert_called_once()
