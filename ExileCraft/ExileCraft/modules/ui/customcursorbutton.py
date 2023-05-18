from PySide6.QtWidgets import QPushButton, QApplication, QButtonGroup
from PySide6.QtGui import QCursor, QPixmap
from ..parser.path_utils import get_abs_path


class CustomCursorButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.setCheckable(True)
        self.setAutoExclusive(False)
        self.toggled.connect(self._handle_cursor)
        self.clicked.connect(self._handle_click)
        self._was_checked = False

    def _handle_click(self):
        if self._was_checked:
            # If the button was previously checked, uncheck it
            self.setChecked(False)
            self._was_checked = False
        else:
            # If the button was previously unchecked, check it
            self.setChecked(True)
            self._was_checked = True

    def _handle_cursor(self, checked):
        if checked:
            # Set the custom cursor
            custom_cursor_button_name = self.objectName()
            custom_cursor_path = f"modules/ui/assets/images/crafting_methods/" \
                                 f"{custom_cursor_button_name.replace('_btn', '')}.png"
            print(custom_cursor_path)
            abs_cursor_path = get_abs_path(__file__, custom_cursor_path)
            custom_cursor_pixmap = QPixmap(abs_cursor_path)
            custom_cursor_pixmap.setDevicePixelRatio(1.25)
            custom_cursor = QCursor(custom_cursor_pixmap)
            QApplication.instance().setOverrideCursor(custom_cursor)
        else:
            # Restore the original cursor
            QApplication.instance().restoreOverrideCursor()
