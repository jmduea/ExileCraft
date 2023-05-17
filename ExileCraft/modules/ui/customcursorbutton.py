from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QCursor, QPixmap
from ..parser.path_utils import get_abs_path


class CustomCursorButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.setCheckable(True)
        self.toggled.connect(self._handle_cursor)


    def _handle_cursor(self, checked):
        if checked:
            # Set the custom cursor
            custom_cursor_button_name = self.objectName()
            custom_cursor_path = f"assets/images/{custom_cursor_button_name}.png"
            abs_cursor_path = get_abs_path(custom_cursor_path, __file__)
            custom_cursor_pixmap = QPixmap(abs_cursor_path)
            custom_cursor_pixmap.setDevicePixelRatio(1.25)
            custom_cursor = QCursor(custom_cursor_pixmap)
            QApplication.instance().setOverrideCursor(custom_cursor)
        else:
            # Restore the original cursor
            QApplication.instance().restoreOverrideCursor()
