# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnIARVaT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QButtonGroup, QComboBox, QLabel,
                               QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
                               QWidget)

from ...widgets.py_custom_toggle_button import PyCustomToggleButton


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(438, 662)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_1_widget)

        self.btn_2_widget = QWidget(self.menu_1)
        self.btn_2_widget.setObjectName(u"btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 40))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_2_layout = QVBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName(u"btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_2_widget)

        self.btn_3_widget = QWidget(self.menu_1)
        self.btn_3_widget.setObjectName(u"btn_3_widget")
        self.btn_3_widget.setMinimumSize(QSize(0, 40))
        self.btn_3_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_3_layout = QVBoxLayout(self.btn_3_widget)
        self.btn_3_layout.setSpacing(0)
        self.btn_3_layout.setObjectName(u"btn_3_layout")
        self.btn_3_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_3_widget)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.item_combobox_container = QWidget(self.menu_2)
        self.item_combobox_container.setObjectName(u"item_combobox_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_combobox_container.sizePolicy().hasHeightForWidth())
        self.item_combobox_container.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.item_combobox_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.base_group_label = QLabel(self.item_combobox_container)
        self.base_group_label.setObjectName(u"base_group_label")
        font1 = QFont()
        font1.setBold(True)
        self.base_group_label.setFont(font1)
        self.base_group_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.base_group_label)

        self.base_group_combobox = QComboBox(self.item_combobox_container)
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.addItem("")
        self.base_group_combobox.setObjectName(u"base_group_combobox")
        self.base_group_combobox.setStyleSheet(u"QComboBox {\n"
"                                                        border: 1px solid gray;\n"
"                                                        border-radius: 3px;\n"
"                                                        padding: 1px 18px 1px 3px;\n"
"                                                        min-width: 6em;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::disabled {\n"
"                                                        opacity: .5;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:editable {\n"
"                                                        background: white;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:!editable, QComboBox::drop"
                        "-down:editable {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                                        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"                                                        }\n"
"\n"
"                                                        /* QComboBox gets the \"on\" state when the popup is\n"
"                                                        open */\n"
"                                                        QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                                        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"               "
                        "                                         }\n"
"\n"
"                                                        QComboBox:on { /* shift the text when the popup opens */\n"
"                                                        padding-top: 3px;\n"
"                                                        padding-left: 4px;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::drop-down {\n"
"                                                        subcontrol-origin: padding;\n"
"                                                        subcontrol-position: top right;\n"
"                                                        width: 15px;\n"
"\n"
"                                                        border-left-width: 1px;\n"
"                                                        border-left-color: darkgray;\n"
"                                                        border-left-style: solid; /* just a single line */\n"
"       "
                        "                                                 border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"                                                        border-bottom-right-radius: 3px;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow {\n"
"                                                        image: url(:/images/images/down_arrow.png);\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow:on { /* shift the arrow when popup is open\n"
"                                                        */\n"
"                                                        top: 1px;\n"
"                                                        left: 1px;\n"
"                                                        }\n"
"\n"
"                      "
                        "                                  QComboBox QAbstractItemView {\n"
"                                                        border: 2px solid darkgray;\n"
"                                                        selection-background-color: lightgray;\n"
"                                                        color: black;\n"
"                                                        }\n"
"                                                    ")

        self.verticalLayout_3.addWidget(self.base_group_combobox)

        self.base_label = QLabel(self.item_combobox_container)
        self.base_label.setObjectName(u"base_label")
        self.base_label.setFont(font1)
        self.base_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.base_label)

        self.base_combobox = QComboBox(self.item_combobox_container)
        self.base_combobox.setObjectName(u"base_combobox")
        self.base_combobox.setEnabled(False)
        self.base_combobox.setStyleSheet(u"QComboBox {\n"
"                                                        border: 1px solid gray;\n"
"                                                        border-radius: 3px;\n"
"                                                        padding: 1px 18px 1px 3px;\n"
"                                                        min-width: 6em;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::disabled {\n"
"                                                        opacity: .5;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:editable {\n"
"                                                        background: white;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:!editable, QComboBox::drop"
                        "-down:editable {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                                        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"                                                        }\n"
"\n"
"                                                        /* QComboBox gets the \"on\" state when the popup is\n"
"                                                        open */\n"
"                                                        QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                                        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"               "
                        "                                         }\n"
"\n"
"                                                        QComboBox:on { /* shift the text when the popup opens */\n"
"                                                        padding-top: 3px;\n"
"                                                        padding-left: 4px;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::drop-down {\n"
"                                                        subcontrol-origin: padding;\n"
"                                                        subcontrol-position: top right;\n"
"                                                        width: 15px;\n"
"\n"
"                                                        border-left-width: 1px;\n"
"                                                        border-left-color: darkgray;\n"
"                                                        border-left-style: solid; /* just a single line */\n"
"       "
                        "                                                 border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"                                                        border-bottom-right-radius: 3px;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow {\n"
"                                                        image: url(:/images/images/down_arrow.png);\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow:on { /* shift the arrow when popup is open\n"
"                                                        */\n"
"                                                        top: 1px;\n"
"                                                        left: 1px;\n"
"                                                        }\n"
"\n"
"                      "
                        "                                  QComboBox QAbstractItemView {\n"
"                                                        border: 2px solid darkgray;\n"
"                                                        selection-background-color: lightgray;\n"
"                                                        color: black;\n"
"                                                        }\n"
"                                                    ")

        self.verticalLayout_3.addWidget(self.base_combobox)

        self.base_item_label = QLabel(self.item_combobox_container)
        self.base_item_label.setObjectName(u"base_item_label")
        self.base_item_label.setFont(font1)
        self.base_item_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.base_item_label)

        self.base_item_combobox = QComboBox(self.item_combobox_container)
        self.base_item_combobox.setObjectName(u"base_item_combobox")
        self.base_item_combobox.setEnabled(False)
        self.base_item_combobox.setStyleSheet(u"QComboBox {\n"
"                                                        border: 1px solid gray;\n"
"                                                        border-radius: 3px;\n"
"                                                        padding: 1px 18px 1px 3px;\n"
"                                                        min-width: 6em;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::disabled {\n"
"                                                        opacity: .5;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:editable {\n"
"                                                        background: white;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox:!editable, QComboBox::drop"
                        "-down:editable {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                                        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"                                                        }\n"
"\n"
"                                                        /* QComboBox gets the \"on\" state when the popup is\n"
"                                                        open */\n"
"                                                        QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"                                                        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                        stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                                        stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"               "
                        "                                         }\n"
"\n"
"                                                        QComboBox:on { /* shift the text when the popup opens */\n"
"                                                        padding-top: 3px;\n"
"                                                        padding-left: 4px;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::drop-down {\n"
"                                                        subcontrol-origin: padding;\n"
"                                                        subcontrol-position: top right;\n"
"                                                        width: 15px;\n"
"\n"
"                                                        border-left-width: 1px;\n"
"                                                        border-left-color: darkgray;\n"
"                                                        border-left-style: solid; /* just a single line */\n"
"       "
                        "                                                 border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"                                                        border-bottom-right-radius: 3px;\n"
"                                                        color: black;\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow {\n"
"                                                        image: url(:/images/images/down_arrow.png);\n"
"                                                        }\n"
"\n"
"                                                        QComboBox::down-arrow:on { /* shift the arrow when popup is open\n"
"                                                        */\n"
"                                                        top: 1px;\n"
"                                                        left: 1px;\n"
"                                                        }\n"
"\n"
"                      "
                        "                                  QComboBox QAbstractItemView {\n"
"                                                        border: 2px solid darkgray;\n"
"                                                        selection-background-color: lightgray;\n"
"                                                        color: black;\n"
"                                                        }\n"
"                                                    ")

        self.verticalLayout_3.addWidget(self.base_item_combobox)


        self.verticalLayout_2.addWidget(self.item_combobox_container)

        self.item_level_and_quality_container = QWidget(self.menu_2)
        self.item_level_and_quality_container.setObjectName(u"item_level_and_quality_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_level_and_quality_container.sizePolicy().hasHeightForWidth())
        self.item_level_and_quality_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.item_level_and_quality_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.item_level_label = QLabel(self.item_level_and_quality_container)
        self.item_level_label.setObjectName(u"item_level_label")
        self.item_level_label.setFont(font1)
        self.item_level_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.item_level_label)

        self.item_level_spinbox = QSpinBox(self.item_level_and_quality_container)
        self.item_level_spinbox.setObjectName(u"item_level_spinbox")
        self.item_level_spinbox.setEnabled(False)
        self.item_level_spinbox.setStyleSheet(u"QSpinBox {\n"
"                                                        color: black;\n"
"                                                        }\n"
"                                                    ")
        self.item_level_spinbox.setMaximum(100)

        self.verticalLayout_4.addWidget(self.item_level_spinbox)

        self.item_quality_label = QLabel(self.item_level_and_quality_container)
        self.item_quality_label.setObjectName(u"item_quality_label")
        self.item_quality_label.setFont(font1)
        self.item_quality_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.item_quality_label)

        self.item_quality_spinbox = QSpinBox(self.item_level_and_quality_container)
        self.item_quality_spinbox.setObjectName(u"item_quality_spinbox")
        self.item_quality_spinbox.setEnabled(False)
        self.item_quality_spinbox.setStyleSheet(u"QSpinBox {\n"
"                                                        color: black;\n"
"                                                        }\n"
"                                                    ")
        self.item_quality_spinbox.setMaximum(30)
        self.item_quality_spinbox.setDisplayIntegerBase(10)

        self.verticalLayout_4.addWidget(self.item_quality_spinbox)


        self.verticalLayout_2.addWidget(self.item_level_and_quality_container)

        self.item_influence_btns_container = QWidget(self.menu_2)
        self.item_influence_btns_container.setObjectName(u"item_influence_btns_container")
        sizePolicy.setHeightForWidth(self.item_influence_btns_container.sizePolicy().hasHeightForWidth())
        self.item_influence_btns_container.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.item_influence_btns_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.item_influences_label = QLabel(self.item_influence_btns_container)
        self.item_influences_label.setObjectName(u"item_influences_label")
        sizePolicy.setHeightForWidth(self.item_influences_label.sizePolicy().hasHeightForWidth())
        self.item_influences_label.setSizePolicy(sizePolicy)
        self.item_influences_label.setFont(font1)
        self.item_influences_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.item_influences_label)

        self.crusader_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group = QButtonGroup(LeftColumn)
        self.item_influence_btn_group.setObjectName(u"item_influence_btn_group")
        self.item_influence_btn_group.setExclusive(False)
        self.item_influence_btn_group.addButton(self.crusader_btn)
        self.crusader_btn.setObjectName(u"crusader_btn")
        self.crusader_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.crusader_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon = QIcon()
        icon.addFile(u":/influences/images/influences/crusader_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crusader_btn.setIcon(icon)
        self.crusader_btn.setIconSize(QSize(30, 30))
        self.crusader_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.crusader_btn)

        self.elder_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group.addButton(self.elder_btn)
        self.elder_btn.setObjectName(u"elder_btn")
        self.elder_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.elder_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon1 = QIcon()
        icon1.addFile(u":/influences/images/influences/elder_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.elder_btn.setIcon(icon1)
        self.elder_btn.setIconSize(QSize(30, 30))
        self.elder_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.elder_btn)

        self.hunter_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group.addButton(self.hunter_btn)
        self.hunter_btn.setObjectName(u"hunter_btn")
        self.hunter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.hunter_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon2 = QIcon()
        icon2.addFile(u":/influences/images/influences/hunter_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hunter_btn.setIcon(icon2)
        self.hunter_btn.setIconSize(QSize(30, 30))
        self.hunter_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.hunter_btn)

        self.redeemer_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group.addButton(self.redeemer_btn)
        self.redeemer_btn.setObjectName(u"redeemer_btn")
        self.redeemer_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.redeemer_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon3 = QIcon()
        icon3.addFile(u":/influences/images/influences/redeemer_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemer_btn.setIcon(icon3)
        self.redeemer_btn.setIconSize(QSize(30, 30))
        self.redeemer_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.redeemer_btn)

        self.shaper_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group.addButton(self.shaper_btn)
        self.shaper_btn.setObjectName(u"shaper_btn")
        self.shaper_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.shaper_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon4 = QIcon()
        icon4.addFile(u":/influences/images/influences/shaper_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shaper_btn.setIcon(icon4)
        self.shaper_btn.setIconSize(QSize(30, 30))
        self.shaper_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.shaper_btn)

        self.warlord_btn = PyCustomToggleButton(self.item_influence_btns_container)
        self.item_influence_btn_group.addButton(self.warlord_btn)
        self.warlord_btn.setObjectName(u"warlord_btn")
        self.warlord_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.warlord_btn.setStyleSheet(u"QPushButton {\n"
"                                                        border: 1px solid #000;\n"
"                                                        border-radius: 4px;\n"
"                                                        background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,\n"
"                                                        stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                                                        border-image: none;\n"
"                                                        color: #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-family: Open Sans;\n"
"                                                        font-size: 12px;\n"
"                                                        font-weight: bold;\n"
"                                                        height: 36px;\n"
"                                     "
                        "                   line-height: 36px;\n"
"                                                        text-align: center;\n"
"                                                        margin: 0px;\n"
"                                                        padding: 5px 10px;\n"
"                                                        cursor: pointer;\n"
"                                                        text-shadow: 1px 1px #000;\n"
"                                                        vertical-align: top;\n"
"                                                        }\n"
"                                                        QPushButton::hover {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"                                                        }\n"
"                                                        QPushButto"
                        "n::pressed {\n"
"\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        }\n"
"                                                        QPushButton::checked {\n"
"                                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0\n"
"                                                        rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"                                                        color: #332211;\n"
"                                                        text-shadow: 1px 1px #FFF;\n"
"                                                        box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
"                                                        font-weight: bold;\n"
"        "
                        "                                                }\n"
"                                                        QPushButton::flat {\n"
"                                                        border: none;\n"
"                                                        }\n"
"                                                    ")
        icon5 = QIcon()
        icon5.addFile(u":/influences/images/influences/warlord_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.warlord_btn.setIcon(icon5)
        self.warlord_btn.setIconSize(QSize(30, 30))
        self.warlord_btn.setCheckable(True)

        self.verticalLayout_5.addWidget(self.warlord_btn)


        self.verticalLayout_2.addWidget(self.item_influence_btns_container)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

#if QT_CONFIG(shortcut)
        self.base_group_label.setBuddy(self.base_group_combobox)
        self.base_label.setBuddy(self.base_combobox)
        self.base_item_label.setBuddy(self.base_item_combobox)
        self.item_level_label.setBuddy(self.item_level_spinbox)
        self.item_quality_label.setBuddy(self.item_quality_spinbox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(LeftColumn)
        self.base_item_combobox.currentTextChanged.connect(self.item_level_spinbox.show)
        self.base_item_combobox.currentTextChanged.connect(self.item_quality_spinbox.show)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Menu 1 - Left Menu", None))
        self.base_group_label.setText(QCoreApplication.translate("LeftColumn", u"Base Group", None))
        self.base_group_combobox.setItemText(0, QCoreApplication.translate("LeftColumn", u"One Hand Weapons", None))
        self.base_group_combobox.setItemText(1, QCoreApplication.translate("LeftColumn", u"Two Hand Weapons", None))
        self.base_group_combobox.setItemText(2, QCoreApplication.translate("LeftColumn", u"Body Armours", None))
        self.base_group_combobox.setItemText(3, QCoreApplication.translate("LeftColumn", u"Helmets", None))
        self.base_group_combobox.setItemText(4, QCoreApplication.translate("LeftColumn", u"Gloves", None))
        self.base_group_combobox.setItemText(5, QCoreApplication.translate("LeftColumn", u"Boots", None))
        self.base_group_combobox.setItemText(6, QCoreApplication.translate("LeftColumn", u"Shields", None))
        self.base_group_combobox.setItemText(7, QCoreApplication.translate("LeftColumn", u"Offhands", None))
        self.base_group_combobox.setItemText(8, QCoreApplication.translate("LeftColumn", u"Flasks", None))
        self.base_group_combobox.setItemText(9, QCoreApplication.translate("LeftColumn", u"Jewellery", None))
        self.base_group_combobox.setItemText(10, QCoreApplication.translate("LeftColumn", u"Jewels", None))

        self.base_group_combobox.setPlaceholderText(QCoreApplication.translate("LeftColumn", u"Select a Base Group", None))
        self.base_label.setText(QCoreApplication.translate("LeftColumn", u"Base", None))
        self.base_combobox.setPlaceholderText(QCoreApplication.translate("LeftColumn", u"Select a Base", None))
        self.base_item_label.setText(QCoreApplication.translate("LeftColumn", u"Base Item", None))
        self.base_item_combobox.setPlaceholderText(QCoreApplication.translate("LeftColumn", u"Select a Base Item", None))
        self.item_level_label.setText(QCoreApplication.translate("LeftColumn", u"Item Level (0-100)", None))
        self.item_quality_label.setText(QCoreApplication.translate("LeftColumn", u"Item Quality (0-30)", None))
        self.item_influences_label.setText(QCoreApplication.translate("LeftColumn", u"Set Item Influences (0-2)", None))
        self.crusader_btn.setText(QCoreApplication.translate("LeftColumn", u"Crusader", None))
        self.elder_btn.setText(QCoreApplication.translate("LeftColumn", u"Elder", None))
        self.hunter_btn.setText(QCoreApplication.translate("LeftColumn", u"Hunter", None))
        self.redeemer_btn.setText(QCoreApplication.translate("LeftColumn", u"Redeemer", None))
        self.shaper_btn.setText(QCoreApplication.translate("LeftColumn", u"Shaper", None))
        self.warlord_btn.setText(QCoreApplication.translate("LeftColumn", u"Warlord", None))
    # retranslateUi

