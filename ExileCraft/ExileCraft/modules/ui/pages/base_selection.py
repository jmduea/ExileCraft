from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout

from ...config.constants import BTN_STYLESHEET, LABEL_STYLESHEET, ITEM_CLASS_SUBTYPES, SUBTYPE_DISPLAY_NAMES
from ...db.database_handler import DatabaseHandler


class BaseSelection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db_handler = DatabaseHandler()
        self.item_class_name = ""
        # Create the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Maximum)
        # Create a vertical layout for the Previous, Next buttons and the header label
        self.top_layout = QVBoxLayout()
        self.layout.addLayout(self.top_layout)

        # self.previous_button = QPushButton("Previous")
        # self.previous_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.previous_button.setStyleSheet(BTN_STYLESHEET)
        #
        # self.next_button = QPushButton("Next")
        # self.next_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # self.next_button.setStyleSheet(BTN_STYLESHEET)

        # Add buttons to layout
        # self.top_layout.addWidget(self.previous_button)
        # self.top_layout.addWidget(self.next_button, 1)

        self.header_label = QLabel()
        self.header_label.setStyleSheet(LABEL_STYLESHEET)
        self.header_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.header_label.setSizePolicy(sizePolicy)
        self.header_label.setMaximumHeight(40)

        self.top_layout.addWidget(self.header_label, 2)

        self.items = []
        self.item_class_subtypes = ITEM_CLASS_SUBTYPES
        self.subtype_display_names = SUBTYPE_DISPLAY_NAMES
        self.subtype_original_names = {v: k for k, v in self.subtype_display_names.items()}

    def update_header_label(self, item_class_name):
        self.header_label.setText(
            f'Choose a Base <span style="display: inline-block; '
            f'text-align: center; '
            f'background: #222; '
            f'text-shadow: 1px 1px #000; '
            f'padding: 10px 10px; '
            f'font-size: 12px; '
            f'text-transform: uppercase;">{item_class_name}</span>'
        )

    def clear_buttons(self):
        for i in reversed(range(self.layout.count())):
            if i != 0:
                item = self.layout.itemAt(i).widget()
                if item is not None:
                    item.setParent(None)

    def populate_buttons(self, item_class_name):
        self.current_item_class_name = item_class_name
        subtypes = self.item_class_subtypes.get(item_class_name, set())

        # Remove previous buttons
        self.clear_buttons()

        # Create a new widget for the buttons
        button_widget = QWidget()
        button_layout = QGridLayout()
        button_widget.setLayout(button_layout)

        # Create a button for each subtype and add it to the button layout
        for i, subtype in enumerate(subtypes):
            # Get the display name for the subtype
            display_name = self.subtype_display_names.get(subtype, subtype)
            button = QPushButton(display_name.format(item_class_name))
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            button.setStyleSheet(BTN_STYLESHEET)

            def create_lambda(subtype):
                return lambda: self.on_button_clicked(subtype)

            button.clicked.connect(create_lambda(subtype))
            button_layout.addWidget(button, i // 3, i % 3)  # Arrange buttons in a 3-column grid
        # Add the button widget to the main layout
        self.layout.addWidget(button_widget)

    # def connect_buttons(self, previous_function, next_function):
    #     self.previous_button.clicked.connect(previous_function)
    #     self.next_button.clicked.connect(next_function)

    # def on_button_clicked(self, display_name):
    #     subtype = self.subtype_original_names.get(display_name, display_name)
    #     self.base_selected.emit(self.current_item_class_name, subtype)
