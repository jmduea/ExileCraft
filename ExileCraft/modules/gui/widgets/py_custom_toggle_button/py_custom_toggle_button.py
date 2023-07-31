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
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton


class PyCustomToggleButton(QPushButton):
    button_checked = Signal(str)
    button_unchecked = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_widget = self.parent()
        self.setCheckable(True)
        self.setAutoExclusive(False)
        self.clicked.connect(self.handle_clicked)

    def handle_clicked(self):
        if not hasattr(self.parent_widget, "_checked_buttons"):
            self.parent_widget._checked_buttons = []

        if self.isChecked():
            # Uncheck the button if there are already 2 buttons checked
            checked_buttons = self.parent_widget._checked_buttons
            if len(checked_buttons) >= 2:
                least_recently_checked = checked_buttons.pop(0)
                least_recently_checked.setChecked(False)
                least_recently_checked.button_unchecked.emit('_'+f'{least_recently_checked.objectName().replace("_btn", "")}')

            # Add the button to the list of checked buttons
            checked_buttons.append(self)
            self.button_checked.emit('_'+self.objectName().replace("_btn", ""))
        else:
            # Remove the button from the list of checked buttons
            self.parent_widget._checked_buttons.remove(self)
            self.button_unchecked.emit('_'+self.objectName().replace("_btn", ""))

    @staticmethod
    def get_checked_buttons(parent_widget):
        return getattr(parent_widget, "_checked_buttons", [])

