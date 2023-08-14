from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QApplication, QPushButton

from modules.data.parser.path_utils import get_abs_path


class PyCustomCursorButton(QPushButton):
    """
    Constructs a new PyCustomCursorButton object.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_widget = self.parent()
        self.setMouseTracking(True)
        self.setCheckable(True)
        self.setAutoExclusive(False)
        self.clicked.connect(self._handle_click)
        self._was_checked = False

    def _handle_click(self):
        """
        Handles the click event for the button.

        If the button was previously checked, it unchecks it. If it was previously unchecked, it checks it.

        Returns:
            None
        """
        if self._was_checked:
            # If the button was previously checked, uncheck it
            self.setChecked(False)
            self._was_checked = False
            self._handle_cursor(False)
        else:
            # Uncheck all other buttons that are siblings of this button
            if self.parent_widget is not None:
                for sibling_widget in self.parent_widget.children():
                    if isinstance(sibling_widget, PyCustomCursorButton) and sibling_widget.isChecked():
                        sibling_widget.setChecked(False)
                        sibling_widget._was_checked = False
                        sibling_widget._handle_cursor(False)
            # If the button was previously unchecked, check it
            self.setChecked(True)
            self._was_checked = True
            self._handle_cursor(True)

    def _handle_cursor(self, checked):
        """
        Handles the cursor change event for the button.

        If the button is checked, it sets a custom cursor based on the button's object name, otherwise,
         it restores the original cursor.

        Args:
            checked: A boolean value indicating whether the button is checked.

        Returns:
            None
        """
        if checked:
            custom_cursor_button_name = self.objectName()
            custom_cursor_path = f"modules/gui/assets/images/crafting_methods/" \
                                 f"{custom_cursor_button_name.replace('_btn', '')}.png"
            abs_cursor_path = get_abs_path(__file__, custom_cursor_path)
            custom_cursor_pixmap = QPixmap(abs_cursor_path)
            custom_cursor_pixmap.setDevicePixelRatio(1.25)
            custom_cursor = QCursor(custom_cursor_pixmap)
            QApplication.instance().setOverrideCursor(custom_cursor)
        else:
            QApplication.instance().restoreOverrideCursor()