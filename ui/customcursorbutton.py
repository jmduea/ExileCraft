import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QCursor, QPixmap


class CustomCursorButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.setCheckable(True)
        self.toggled.connect(self._handle_cursor)

    def _handle_cursor(self, checked):
        if checked:
            # Set the custom cursor'
            custom_cursor_button_name = self.objectName()
            print(custom_cursor_button_name)
            custom_cursor_pixmap = QPixmap(f"assets/images/{custom_cursor_button_name}.png")
            print(custom_cursor_pixmap)
            custom_cursor = QCursor(custom_cursor_pixmap)
            QApplication.instance().setOverrideCursor(custom_cursor)
        else:
            # Restore the original cursor
            QApplication.instance().restoreOverrideCursor()