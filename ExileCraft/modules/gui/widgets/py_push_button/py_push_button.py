# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

style = ('\n'
         'QPushButton {{\n'
         '	border: none;\n'
         '    padding-left: 10px;\n'
         '    padding-right: 5px;\n'
         '    color: {_color};\n'
         '	border-radius: {_radius};	\n'
         '	background-color: {_bg_color};\n'
         '}}\n'
         'QPushButton:hover {{\n'
         '	background-color: {_bg_color_hover};\n'
         '}}\n'
         'QPushButton:pressed {{	\n'
         '	background-color: {_bg_color_pressed};\n'
         '}}\n')


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
        self,
        text,
        radius,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed
        )
        self.setStyleSheet(custom_style)
