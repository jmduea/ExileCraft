# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mods_widgetdanNev.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QCursor,
    QFont,
)
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QToolBox,
    QUndoView,
    QVBoxLayout,
    QWidget,
)


class Ui_mods_widget(object):
    def setupUi(self, mods_widget):
        if not mods_widget.objectName():
            mods_widget.setObjectName("mods_widget")
        mods_widget.resize(1010, 784)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mods_widget.sizePolicy().hasHeightForWidth())
        mods_widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Segoe UI"])
        font.setPointSize(14)
        mods_widget.setFont(font)
        mods_widget.setMouseTracking(True)
        mods_widget.setAutoFillBackground(False)
        mods_widget.setStyleSheet(
            "QWidget {\n"
            "color: #FFF;\n"
            "background-color: #333333;\n"
            "padding: 0px;\n"
            "margin: 0px;\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QTabWidget {\n"
            "width: 400px;\n"
            "margin: 0px;\n"
            "padding: 0px;\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "position:relative;\n"
            "}\n"
            "\n"
            "QTabBar::tab:first {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(112, 91, 124, 255), stop:1 rgba(112, 91, 124, 255));\n"
            "width: 134px;\n"
            "padding: 5px 10px;\n"
            "border: 1px solid #000;\n"
            "box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0, 0, 0, 0.31);\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QTabBar::tab:first:selected, QTabBar::tab:first:hover {\n"
            "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(134, 69, 172, 255), stop:1 rgba(138, 71, 177, 255));\n"
            "\n"
            "}\n"
            "\n"
            "QTabBar::tab:middle {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 88, 98, 255), stop:1 rgba(84, 105, 116, 255));\n"
            ""
            "width: 134px;\n"
            "padding: 5px 10px;\n"
            "border: 1px solid #000;\n"
            "box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0, 0, 0, 0.31);\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QTabBar::tab:middle:selected, QTabBar::tab:middle:hover {\n"
            "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(60, 119, 152, 255), stop:1 rgba(63, 124, 159, 255));\n"
            "}\n"
            "\n"
            "QTabBar::tab:last {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(95, 69, 69, 255), stop:1 rgba(106, 67, 67, 255));\n"
            "width: 134px;\n"
            "padding: 5px 10px;\n"
            "border: 1px solid #000;\n"
            "box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0, 0, 0, 0.31);\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QTabBar::tab:last:selected, QTabBar::tab:last:hover {\n"
            "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(180, 99, 99, 255), stop:1 rgba(150, 83, 83, 255));\n"
            "}\n"
            "\n"
            "QToolBox {\n"
            "border-image: none;\n"
            "margin: 0px;\n"
            "padding: 0px;\n"
            "}\n"
            ""
            "QToolBox::tab {\n"
            "border: 1px solid #000;\n"
            "padding: 5px 10px;\n"
            "font-weight: bold;\n"
            "box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0, 0, 0, 0.31);\n"
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(30, 30, 30, 1), stop: 1 rgba(60, 60, 60, 1));\n"
            "text-shadow: 1px, 1px, #000;\n"
            "color: #FFF;\n"
            "}\n"
            "\n"
            "QToolBox::tab:selected {\n"
            "color: #f6e5b2;\n"
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(30, 30, 30, 255), stop: 1 rgba(60, 60, 60, 255));\n"
            "}\n"
            "\n"
            "QToolBox::tab:hover {\n"
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(30, 30, 30, 255), stop: 1 rgba(60, 60, 60, 255));\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "background-color: #000;\n"
            "selection-background-color: #000;\n"
            "placeholder-text-color: #666;\n"
            "height: 31px;\n"
            "line-height: 31px;\n"
            "width: 100%;\n"
            "border: 1px solid #444;\n"
            "text-align: left;\n"
            "padding-left: 7px;\n"
            "padding-right: 37px;\n"
            "border-image: none;\n"
            "}\n"
            "\n"
            "QLineEdit:focu"
            "s {\n"
            "border: 1px solid #FFEEBB;\n"
            "}\n"
            "\n"
            "QWidget #prefixes_tab {\n"
            "margin: 0px;\n"
            "padding: 0px;\n"
            "}\n"
            "\n"
            "QWidget #suffixes_tab {\n"
            "margin: 0px;\n"
            "padding: 0px;\n"
            "}\n"
            "\n"
            "QWidget #implicits_tab {\n"
            "margin: 0px;\n"
            "padding: 0px;\n"
            "}\n"
            "\n"
            "QTreeView {\n"
            "alternate-background-color: grey;\n"
            "border-image: none;\n"
            "padding: 0px;\n"
            "margin: 0px;\n"
            "\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    border: 1px solid #BBB;\n"
            "    background: #f1f1f1;\n"
            "    width: 20px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "    background: #AAA;\n"
            "    border: 1px solid #666;\n"
            "    min-height: 20px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QHorizontalBoxLayout {\n"
            "font-size: 14px;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
            "QWidget#implicits_tab>QToolBox::tab {\n"
            ""
            "background-color: #000;\n"
            "border-bottom: 1px solid #000;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "QWidget#suffixes_tab>QToolBox::tab {\n"
            "background-color: #000;\n"
            "border-bottom: 1px solid #000;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "QWidget#prefixes_tab>QToolBox::tab {\n"
            "background-color: #000;\n"
            "border-bottom: 1px solid #000;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "QListView {\n"
            "padding: 0px 0px;\n"
            "font-size: 12px;\n"
            "color: #FFF;\n"
            "show-decoration-selected: 1;\n"
            "}\n"
            "QListView::item {\n"
            "background-color: #222;\n"
            "padding: 5px 10px;\n"
            "}\n"
            "QListView::item:hover {\n"
            "background-color: #EEE;\n"
            "cursor: pointer;\n"
            "color: #333333;\n"
            "}\n"
            "QListView::item:selected:!active {\n"
            "background-color: #EEE;\n"
            "color: #333333;\n"
            "}\n"
            "QListView::item:alternate {\n"
            "background-color: #333;\n"
            "}\n"
            "QListView::item:alternate:hover {\n"
            "background-color:"
            " #EEE;\n"
            "cursor: pointer;\n"
            "color: #333333;\n"
            "}\n"
            "QListView::item:alternate:selected:!active {\n"
            "background-color: #EEE;\n"
            "color: #333333;\n"
            "}"
        )
        self.mods_widget_layout = QHBoxLayout(mods_widget)
        self.mods_widget_layout.setSpacing(0)
        self.mods_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.mods_widget_layout.setObjectName("mods_widget_layout")
        self.mods_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.mods_widget_grid_layout = QGridLayout()
        self.mods_widget_grid_layout.setSpacing(0)
        self.mods_widget_grid_layout.setObjectName("mods_widget_grid_layout")
        self.crafting_log_widget = QToolBox(mods_widget)
        self.crafting_log_widget.setObjectName("crafting_log_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.crafting_log_widget.sizePolicy().hasHeightForWidth()
        )
        self.crafting_log_widget.setSizePolicy(sizePolicy1)
        self.crafting_log_widget.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.crafting_log_widget.setFont(font1)
        self.crafting_log_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.crafting_log_widget.setFrameShape(QFrame.StyledPanel)
        self.crafting_log_widget.setFrameShadow(QFrame.Raised)
        self.history_log_widget = QWidget()
        self.history_log_widget.setObjectName("history_log_widget")
        self.history_log_widget.setGeometry(QRect(0, 0, 334, 678))
        font2 = QFont()
        font2.setPointSize(14)
        self.history_log_widget.setFont(font2)
        self.history_log_widget.setCursor(QCursor(Qt.ArrowCursor))
        self.history_log_widget.setMouseTracking(True)
        self.history_view_layout = QVBoxLayout(self.history_log_widget)
        self.history_view_layout.setSpacing(0)
        self.history_view_layout.setContentsMargins(0, 0, 0, 0)
        self.history_view_layout.setObjectName("history_view_layout")
        self.history_view_layout.setContentsMargins(0, 0, 0, 0)
        self.history_view = QUndoView(self.history_log_widget)
        self.history_view.setObjectName("history_view")
        font3 = QFont()
        self.history_view.setFont(font3)
        self.history_view.setFrameShape(QFrame.StyledPanel)
        self.history_view.setFrameShadow(QFrame.Raised)
        self.history_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.history_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.history_view_layout.addWidget(self.history_view)

        self.crafting_log_widget.addItem(self.history_log_widget, "HISTORY")
        self.spending_log_widget = QWidget()
        self.spending_log_widget.setObjectName("spending_log_widget")
        self.spending_log_widget.setGeometry(QRect(0, 0, 334, 678))
        self.spending_log_widget.setFont(font2)
        self.spending_log_widget.setCursor(QCursor(Qt.ArrowCursor))
        self.spending_log_widget.setMouseTracking(True)
        self.spending_log_layout = QVBoxLayout(self.spending_log_widget)
        self.spending_log_layout.setSpacing(0)
        self.spending_log_layout.setContentsMargins(0, 0, 0, 0)
        self.spending_log_layout.setObjectName("spending_log_layout")
        self.spending_log_layout.setContentsMargins(0, 0, 0, 0)
        self.spending_view = QUndoView(self.spending_log_widget)
        self.spending_view.setObjectName("spending_view")
        self.spending_view.setFont(font3)
        self.spending_view.setFrameShadow(QFrame.Raised)
        self.spending_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.spending_view.setMovement(QListView.Static)
        self.spending_view.setWordWrap(True)
        self.spending_view.setItemAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.spending_log_layout.addWidget(self.spending_view)

        self.crafting_log_widget.addItem(self.spending_log_widget, "SPENDING")
        self.export_widget = QWidget()
        self.export_widget.setObjectName("export_widget")
        self.export_widget.setGeometry(QRect(0, 0, 334, 678))
        self.export_widget.setCursor(QCursor(Qt.ArrowCursor))
        self.export_widget.setMouseTracking(True)
        self.export_widget.setTabletTracking(False)
        self.export_layout = QVBoxLayout(self.export_widget)
        self.export_layout.setSpacing(0)
        self.export_layout.setContentsMargins(0, 0, 0, 0)
        self.export_layout.setObjectName("export_layout")
        self.export_layout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.export_widget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(
            20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.export_layout.addWidget(self.frame)

        self.crafting_log_widget.addItem(self.export_widget, "EXPORT")

        self.mods_widget_grid_layout.addWidget(self.crafting_log_widget, 0, 1, 3, 1)

        self.search_bar = QLineEdit(mods_widget)
        self.search_bar.setObjectName("search_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy2)
        self.search_bar.setMinimumSize(QSize(400, 31))
        self.search_bar.setFont(font2)
        self.search_bar.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_bar.setFocusPolicy(Qt.ClickFocus)
        self.search_bar.setFrame(False)
        self.search_bar.setClearButtonEnabled(True)

        self.mods_widget_grid_layout.addWidget(self.search_bar, 0, 0, 1, 1)

        self.mods_tab_widget = QTabWidget(mods_widget)
        self.mods_tab_widget.setObjectName("mods_tab_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mods_tab_widget.sizePolicy().hasHeightForWidth()
        )
        self.mods_tab_widget.setSizePolicy(sizePolicy3)
        self.mods_tab_widget.setMinimumSize(QSize(463, 0))
        self.mods_tab_widget.setFont(font1)
        self.mods_tab_widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.mods_tab_widget.setMouseTracking(True)
        self.mods_tab_widget.setFocusPolicy(Qt.ClickFocus)
        self.mods_tab_widget.setUsesScrollButtons(False)
        self.mods_tab_widget.setDocumentMode(True)
        self.mods_tab_widget.setProperty("expanding", True)
        self.prefixes_tab = QWidget()
        self.prefixes_tab.setObjectName("prefixes_tab")
        self.prefixes_tab.setFont(font1)
        self.prefixes_tab.setCursor(QCursor(Qt.PointingHandCursor))
        self.prefixes_tab.setMouseTracking(True)
        self.prefixes_layout = QVBoxLayout(self.prefixes_tab)
        self.prefixes_layout.setSpacing(0)
        self.prefixes_layout.setContentsMargins(0, 0, 0, 0)
        self.prefixes_layout.setObjectName("prefixes_layout")
        self.prefixes_layout.setContentsMargins(0, 0, 0, 0)
        self.mods_tab_widget.addTab(self.prefixes_tab, "")
        self.suffixes_tab = QWidget()
        self.suffixes_tab.setObjectName("suffixes_tab")
        self.suffixes_tab.setFont(font2)
        self.suffixes_tab.setCursor(QCursor(Qt.PointingHandCursor))
        self.suffixes_tab.setMouseTracking(True)
        self.suffixes_layout = QVBoxLayout(self.suffixes_tab)
        self.suffixes_layout.setSpacing(0)
        self.suffixes_layout.setContentsMargins(0, 0, 0, 0)
        self.suffixes_layout.setObjectName("suffixes_layout")
        self.suffixes_layout.setContentsMargins(0, 0, 0, 0)
        self.mods_tab_widget.addTab(self.suffixes_tab, "")
        self.implicits_tab = QWidget()
        self.implicits_tab.setObjectName("implicits_tab")
        self.implicits_tab.setFont(font1)
        self.implicits_tab.setMouseTracking(True)
        self.implicits_layout = QVBoxLayout(self.implicits_tab)
        self.implicits_layout.setSpacing(0)
        self.implicits_layout.setContentsMargins(0, 0, 0, 0)
        self.implicits_layout.setObjectName("implicits_layout")
        self.implicits_layout.setContentsMargins(0, 0, 0, 0)
        self.mods_tab_widget.addTab(self.implicits_tab, "")

        self.mods_widget_grid_layout.addWidget(self.mods_tab_widget, 2, 0, 1, 1)

        self.mods_widget_layout.addLayout(self.mods_widget_grid_layout)

        self.retranslateUi(mods_widget)

        self.crafting_log_widget.setCurrentIndex(0)
        self.crafting_log_widget.layout().setSpacing(0)
        self.mods_tab_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(mods_widget)

    # setupUi

    def retranslateUi(self, mods_widget):
        self.crafting_log_widget.setItemText(
            self.crafting_log_widget.indexOf(self.history_log_widget),
            QCoreApplication.translate("mods_widget", "HISTORY", None),
        )
        self.spending_view.setEmptyLabel(
            QCoreApplication.translate("mods_widget", "Total Currency Spent:", None)
        )
        self.crafting_log_widget.setItemText(
            self.crafting_log_widget.indexOf(self.spending_log_widget),
            QCoreApplication.translate("mods_widget", "SPENDING", None),
        )
        self.pushButton.setText(
            QCoreApplication.translate("mods_widget", "Export to Clipboard", None)
        )
        self.crafting_log_widget.setItemText(
            self.crafting_log_widget.indexOf(self.export_widget),
            QCoreApplication.translate("mods_widget", "EXPORT", None),
        )
        self.search_bar.setPlaceholderText(
            QCoreApplication.translate("mods_widget", "Search for an affix", None)
        )
        self.mods_tab_widget.setTabText(
            self.mods_tab_widget.indexOf(self.prefixes_tab),
            QCoreApplication.translate("mods_widget", "PREFIXES", None),
        )
        self.mods_tab_widget.setTabText(
            self.mods_tab_widget.indexOf(self.suffixes_tab),
            QCoreApplication.translate("mods_widget", "SUFFIXES", None),
        )
        self.mods_tab_widget.setTabText(
            self.mods_tab_widget.indexOf(self.implicits_tab),
            QCoreApplication.translate("mods_widget", "IMPLICITS", None),
        )
        pass

    # retranslateUi
