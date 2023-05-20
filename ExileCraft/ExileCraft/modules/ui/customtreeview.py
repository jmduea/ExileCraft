from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QTreeView, QHeaderView


class CustomTreeView(QTreeView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setHeaderHidden(False)
        self.setStyleSheet("""
            QTreeView {
                color: "white";
            }
            QWidget {
                background-color: #282828;
                border: 0px;
            }
            QLabel {
                color: #8888ff;
                border: 0px;
                margin: 0;
                padding: 0;
                font-size: 16px;
            }
        """)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.header().setSizeAdjustPolicy(QHeaderView.AdjustToContents)

    def setEnabled(self, enabled):
        super().setEnabled(enabled)
        if enabled:
            self.isEnabled()
