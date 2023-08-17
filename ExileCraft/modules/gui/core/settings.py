# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################


import json

from PySide6.QtCore import QSettings

# Define the JSON settings
settings_json = """
{
  "app_name": "ExileCraft",
  "version": "v1.0.0",
  "copyright": "By: Jon Duea",
  "year": 2023,
  "theme_name": "default",
  "custom_title_bar": true,
  "startup_size": [1280, 1080],
  "minimum_size": [1024, 768],
  "lef_menu_size": {"minimum": 50, "maximum": 240},
  "left_menu_content_margins": 3,
  "left_column_size": {"minimum": 0, "maximum": 240},
  "right_column_size": {"minimum": 0, "maximum": 240},
  "time_animation": 250,
  "font": {"family": "fontin-regular", "title_size": 10, "text_size": 9}
}
"""

# Parse the JSON string
settings_dict = json.loads(settings_json)


class ApplicationSettings(QSettings):
    """ """


# Create a QSettings object
settings = QSettings("Jmduea", "ExileCraft")

# Iterate through the dictionary and store the key-value pairs
for key, value in settings_dict.items():
    settings.setValue(key, value)


def _write_window_attribute_settings(self):
    """
    Save window attributes as settings.

    Called when window moved, resized, or closed.
    """
    self.settings.begin_group("mainWindow")
    self.settings.setValue("pos", self.MainWindow.pos())
    self.settings.setValue("maximized", self.MainWindow.isMaximized())
    if not self.MainWindow.isMaximized():
        self.settings.setValue("size", self.MainWindow.size())

    self.settings.endGroup()


def _read_and_apply_window_attribute_settings(self):
    """
    Read window attributes from settings,
    using current attributes as defaults (if settings not exist.)

    Called at QMainWindow initialization, before show().
    """
    self.settings.beginGroup("mainWindow")
    # No need for toPoint, etc. : PySide converts types
    try:
        self.MainWindow.move(self.settings.value("pos"))
        if self.settings.value("maximized") in "true":
            self.MainWindow.showMaximized()
        else:
            self.MainWindow.resize(self.settings.value("size"))
    except:
        pass
    self.settings.endGroup()
