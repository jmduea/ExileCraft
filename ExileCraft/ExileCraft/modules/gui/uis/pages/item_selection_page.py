import sqlite3

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout

from modules.config.constants import BTN_STYLESHEET, LABEL_STYLESHEET, SUBTYPE_DISPLAY_NAMES
from modules.db.database_handler import DatabaseHandler
from modules.parser import path_utils

rel_path_to_db = "data/exilecraft.db"  # replace this with the correct relative path
db_path = path_utils.get_abs_path(__file__, rel_path_to_db)


class ItemSelectionPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db_handler = DatabaseHandler()
        self.item_clas_name = ""
        self.item_subtype = ""
        # Create the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Maximum)

        # Create a vertical layout for the Previous, Next buttons and the header label
        self.top_layout = QVBoxLayout()
        self.layout.addLayout(self.top_layout)

        self.header_label = QLabel()
        self.header_label.setStyleSheet(LABEL_STYLESHEET)
        self.header_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.header_label.setSizePolicy(sizePolicy)
        self.header_label.setMaximumHeight(40)

        self.top_layout.addWidget(self.header_label, 2)

        self.subtype_display_names = SUBTYPE_DISPLAY_NAMES
        self.subtype_original_names = {v: k for k, v in self.subtype_display_names.items()}

    def update_header_label(self, item_class_name, item_subtype):
        display_name = self.subtype_display_names.get(item_subtype, item_subtype)
        subtype_label = display_name.format(item_class_name)
        self.header_label.setText(
            f'Choose an Item <span style="display: inline-block; '
            f'text-align: center; '
            f'background: #222; '
            f'text-shadow: 1px 1px #000; '
            f'padding: 10px 10px; '
            f'font-size: 12px; '
            f'text-transform: uppercase;">{item_class_name}</span>'
            f'<span style="display: inline-block; '
            f'text-align: center; '
            f'padding: 10px 10px; '
            f'font-size: 12px; '
            f'text-transform: uppercase;">&#8594;</span>'
            f'<span style="display: inline-block; '
            f'text-align: center; '
            f'background: #222; '
            f'text-shadow: 1px 1px #000; '
            f'padding: 10px 10px; '
            f'font-size: 12px; '
            f'text-transform: uppercase;">{subtype_label}</span>'
        )

    def connect_buttons(self, previous_function, next_function):
        self.previous_button.clicked.connect(previous_function)
        self.next_button.clicked.connect(next_function)

    def clear_buttons(self):
        for i in reversed(range(self.layout.count())):
            if i != 0:
                item = self.layout.itemAt(i).widget()
                if item is not None:
                    item.setParent(None)

    def populate_with_subtype(self, item_class_id, item_subtype):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get the item_class_id from the crafting_project table
        cursor.execute('''SELECT item_class_id FROM crafting_project ORDER BY id DESC LIMIT 1''',)
        item_class_id = cursor.fetchone()[0]
        print(f'{item_class_id}, {item_subtype}')
        # Get the base items for the given subtype
        cursor.execute('''SELECT name FROM base_items WHERE item_class_id = ? AND tags LIKE ?
                        ORDER BY drop_level ASC''', (item_class_id, f'%"{item_subtype}"%'))
        base_items = cursor.fetchall()
        conn.close()

        # Clear current buttons, but skip the first two (Previous, Next)
        for i in reversed(range(self.layout.count())):
            if i != 0:
                item = self.layout.itemAt(i).widget()
                if item is not None:
                    item.setParent(None)

        # Create a new widget for the buttons
        button_widget = QWidget()
        button_layout = QGridLayout()
        button_widget.setLayout(button_layout)

        # Create a button for each base item and add it to the layout
        for base_item, (base_item,) in enumerate(base_items):
            button = QPushButton(base_item)
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            button.setStyleSheet(BTN_STYLESHEET)

            def create_lambda(base_item):
                return lambda: self.on_button_clicked(base_item)

            button.clicked.connect(create_lambda(base_item))
            button_layout.addWidget(button, i // 3, i % 3)  # Arrange buttons in a 3-column grid

            self.layout.addWidget(button)

    def on_button_clicked(self, base_item):
        print(f"{base_item}")
        self.item_selected.emit(base_item)
