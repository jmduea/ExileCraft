# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_columnnoFAeX.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QIcon)
from PySide6.QtWidgets import (QButtonGroup, QGridLayout, QHBoxLayout,
                               QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget)

from ...widgets.py_custom_cursor_button import PyCustomCursorButton
from ...assets import assets_rc

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
            if not RightColumn.objectName():
                    RightColumn.setObjectName(u"RightColumn")
            RightColumn.resize(247, 510)
            self.verticalLayout = QVBoxLayout(RightColumn)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalLayout.setContentsMargins(5, 5, 5, 5)
            self.menus = QStackedWidget(RightColumn)
            self.menus.setObjectName(u"menus")
            self.menus.setStyleSheet(u"QToolTip {\n"
                                     "	border: 1px solid black;\n"
                                     "	padding: 2px;\n"
                                     "	background-color: rgb(68, 68, 68);\n"
                                     "	opacity: .8;\n"
                                     "	vertical-align: middle;\n"
                                     "}")
            self.crafting_methods_menu = QWidget()
            self.crafting_methods_menu.setObjectName(u"crafting_methods_menu")
            self.crafting_methods_layout1 = QGridLayout(self.crafting_methods_menu)
            self.crafting_methods_layout1.setObjectName(u"crafting_methods_layout1")
            self.method_transmute_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group = QButtonGroup(RightColumn)
            self.crafting_methods_btn_group.setObjectName(u"crafting_methods_btn_group")
            self.crafting_methods_btn_group.setExclusive(False)
            self.crafting_methods_btn_group.addButton(self.method_transmute_btn)
            self.method_transmute_btn.setObjectName(u"method_transmute_btn")
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.method_transmute_btn.sizePolicy().hasHeightForWidth())
            self.method_transmute_btn.setSizePolicy(sizePolicy)
            self.method_transmute_btn.setMinimumSize(QSize(30, 30))
            self.method_transmute_btn.setMaximumSize(QSize(60, 58))
            self.method_transmute_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_transmute_btn.setMouseTracking(True)
            self.method_transmute_btn.setContextMenuPolicy(Qt.NoContextMenu)
            self.method_transmute_btn.setStyleSheet(u"QPushButton {\n"
                                                    "                border: 1px solid #000;\n"
                                                    "                  border-top-width: 1px;\n"
                                                    "                   border-right-width: 1px;\n"
                                                    "                   border-bottom-width: 1px;\n"
                                                    "                   border-left-width: 1px;\n"
                                                    "                   border-top-style: solid;\n"
                                                    "                 border-right-style: solid;\n"
                                                    "                  border-bottom-style: solid;\n"
                                                    "                   border-left-style: solid;\n"
                                                    "                   border-top-color: rgb(0, 0, 0);\n"
                                                    "                  border-right-color: rgb(0, 0, 0);\n"
                                                    "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                    "                   border-left-color: rgb(0, 0, 0);\n"
                                                    "                  border-image-source: initial;\n"
                                                    "                  border-image-slice: initial;\n"
                                                    "                  border-image-width: initial;\n"
                                                    "                  border-image-outset: initial;\n"
                                                    "                border-image-repeat: initial;\n"
                                                    "                border-radius: 4px;\n"
                                                    "                background-color: qlineargradient(x1: 0, y"
                                                    "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                    "                border-image: none;\n"
                                                    "              color: #FFF;\n"
                                                    "               text-shadow: 1px 1px #000;\n"
                                                    "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                    "                font-family: Open Sans;\n"
                                                    "                font-size: 12px;\n"
                                                    "               font-weight: bold;\n"
                                                    "               height: 36px;\n"
                                                    "                line-height: 36px;\n"
                                                    "                text-align: center;\n"
                                                    "				margin: 0px;\n"
                                                    "           }\n"
                                                    "            QPushButton::hover {\n"
                                                    "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                    "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                    "           }\n"
                                                    "            QPushButton::pressed {\n"
                                                    "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                    "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                    "            }\n"
                                                    "QPushButton::checked {\n"
                                                    "				background-color:"
                                                    " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                    "				color: #332211;\n"
                                                    "text-shadow: 1px 1px #FFF;\n"
                                                    "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                    "font-weight: bold;\n"
                                                    "			}\n"
                                                    "            QPushButton::flat {\n"
                                                    "                border: none;\n"
                                                    "}")
            icon = QIcon()
            icon.addFile(u":/crafting_methods/images/crafting_methods/method_transmute.png", QSize(), QIcon.Normal,
                         QIcon.Off)
            self.method_transmute_btn.setIcon(icon)
            self.method_transmute_btn.setIconSize(QSize(30, 30))
            self.method_transmute_btn.setCheckable(True)
            self.method_transmute_btn.setChecked(False)
            self.method_transmute_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_transmute_btn, 0, 0, 1, 1)

            self.method_alteration_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_alteration_btn)
            self.method_alteration_btn.setObjectName(u"method_alteration_btn")
            sizePolicy.setHeightForWidth(self.method_alteration_btn.sizePolicy().hasHeightForWidth())
            self.method_alteration_btn.setSizePolicy(sizePolicy)
            self.method_alteration_btn.setMinimumSize(QSize(30, 30))
            self.method_alteration_btn.setMaximumSize(QSize(60, 60))
            self.method_alteration_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_alteration_btn.setMouseTracking(True)
            self.method_alteration_btn.setStyleSheet(u"QPushButton {\n"
                                                     "                border: 1px solid #000;\n"
                                                     "                  border-top-width: 1px;\n"
                                                     "                   border-right-width: 1px;\n"
                                                     "                   border-bottom-width: 1px;\n"
                                                     "                   border-left-width: 1px;\n"
                                                     "                   border-top-style: solid;\n"
                                                     "                 border-right-style: solid;\n"
                                                     "                  border-bottom-style: solid;\n"
                                                     "                   border-left-style: solid;\n"
                                                     "                   border-top-color: rgb(0, 0, 0);\n"
                                                     "                  border-right-color: rgb(0, 0, 0);\n"
                                                     "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                     "                   border-left-color: rgb(0, 0, 0);\n"
                                                     "                  border-image-source: initial;\n"
                                                     "                  border-image-slice: initial;\n"
                                                     "                  border-image-width: initial;\n"
                                                     "                  border-image-outset: initial;\n"
                                                     "                border-image-repeat: initial;\n"
                                                     "                border-radius: 4px;\n"
                                                     "                background-color: qlineargradient(x1: 0, y"
                                                     "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                     "                border-image: none;\n"
                                                     "              color: #FFF;\n"
                                                     "               text-shadow: 1px 1px #000;\n"
                                                     "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                     "                font-family: Open Sans;\n"
                                                     "                font-size: 12px;\n"
                                                     "               font-weight: bold;\n"
                                                     "               height: 36px;\n"
                                                     "                line-height: 36px;\n"
                                                     "                text-align: center;\n"
                                                     "				margin: 0px;\n"
                                                     "           }\n"
                                                     "            QPushButton::hover {\n"
                                                     "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                     "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                     "           }\n"
                                                     "            QPushButton::pressed {\n"
                                                     "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                     "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                     "            }\n"
                                                     "QPushButton::checked {\n"
                                                     "				background-color:"
                                                     " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                     "				color: #332211;\n"
                                                     "text-shadow: 1px 1px #FFF;\n"
                                                     "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                     "font-weight: bold;\n"
                                                     "			}\n"
                                                     "            QPushButton::flat {\n"
                                                     "                border: none;\n"
                                                     "}")
            icon1 = QIcon()
            icon1.addFile(u":/crafting_methods/images/crafting_methods/method_alteration.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_alteration_btn.setIcon(icon1)
            self.method_alteration_btn.setIconSize(QSize(30, 30))
            self.method_alteration_btn.setCheckable(True)
            self.method_alteration_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_alteration_btn, 0, 1, 1, 1)

            self.method_augmentation_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_augmentation_btn)
            self.method_augmentation_btn.setObjectName(u"method_augmentation_btn")
            sizePolicy.setHeightForWidth(self.method_augmentation_btn.sizePolicy().hasHeightForWidth())
            self.method_augmentation_btn.setSizePolicy(sizePolicy)
            self.method_augmentation_btn.setMinimumSize(QSize(30, 30))
            self.method_augmentation_btn.setMaximumSize(QSize(60, 60))
            self.method_augmentation_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_augmentation_btn.setMouseTracking(True)
            self.method_augmentation_btn.setStyleSheet(u"QPushButton {\n"
                                                       "                border: 1px solid #000;\n"
                                                       "                  border-top-width: 1px;\n"
                                                       "                   border-right-width: 1px;\n"
                                                       "                   border-bottom-width: 1px;\n"
                                                       "                   border-left-width: 1px;\n"
                                                       "                   border-top-style: solid;\n"
                                                       "                 border-right-style: solid;\n"
                                                       "                  border-bottom-style: solid;\n"
                                                       "                   border-left-style: solid;\n"
                                                       "                   border-top-color: rgb(0, 0, 0);\n"
                                                       "                  border-right-color: rgb(0, 0, 0);\n"
                                                       "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                       "                   border-left-color: rgb(0, 0, 0);\n"
                                                       "                  border-image-source: initial;\n"
                                                       "                  border-image-slice: initial;\n"
                                                       "                  border-image-width: initial;\n"
                                                       "                  border-image-outset: initial;\n"
                                                       "                border-image-repeat: initial;\n"
                                                       "                border-radius: 4px;\n"
                                                       "                background-color: qlineargradient(x1: 0, y"
                                                       "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                       "                border-image: none;\n"
                                                       "              color: #FFF;\n"
                                                       "               text-shadow: 1px 1px #000;\n"
                                                       "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                       "                font-family: Open Sans;\n"
                                                       "                font-size: 12px;\n"
                                                       "               font-weight: bold;\n"
                                                       "               height: 36px;\n"
                                                       "                line-height: 36px;\n"
                                                       "                text-align: center;\n"
                                                       "				margin: 0px;\n"
                                                       "           }\n"
                                                       "            QPushButton::hover {\n"
                                                       "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                       "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                       "           }\n"
                                                       "            QPushButton::pressed {\n"
                                                       "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                       "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                       "            }\n"
                                                       "QPushButton::checked {\n"
                                                       "				background-color:"
                                                       " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                       "				color: #332211;\n"
                                                       "text-shadow: 1px 1px #FFF;\n"
                                                       "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                       "font-weight: bold;\n"
                                                       "			}\n"
                                                       "            QPushButton::flat {\n"
                                                       "                border: none;\n"
                                                       "}")
            icon2 = QIcon()
            icon2.addFile(u":/crafting_methods/images/crafting_methods/method_augmentation.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_augmentation_btn.setIcon(icon2)
            self.method_augmentation_btn.setIconSize(QSize(30, 30))
            self.method_augmentation_btn.setCheckable(True)
            self.method_augmentation_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_augmentation_btn, 0, 2, 1, 1)

            self.method_regal_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_regal_btn)
            self.method_regal_btn.setObjectName(u"method_regal_btn")
            sizePolicy.setHeightForWidth(self.method_regal_btn.sizePolicy().hasHeightForWidth())
            self.method_regal_btn.setSizePolicy(sizePolicy)
            self.method_regal_btn.setMinimumSize(QSize(30, 30))
            self.method_regal_btn.setMaximumSize(QSize(60, 60))
            self.method_regal_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_regal_btn.setMouseTracking(True)
            self.method_regal_btn.setStyleSheet(u"QPushButton {\n"
                                                "                border: 1px solid #000;\n"
                                                "                  border-top-width: 1px;\n"
                                                "                   border-right-width: 1px;\n"
                                                "                   border-bottom-width: 1px;\n"
                                                "                   border-left-width: 1px;\n"
                                                "                   border-top-style: solid;\n"
                                                "                 border-right-style: solid;\n"
                                                "                  border-bottom-style: solid;\n"
                                                "                   border-left-style: solid;\n"
                                                "                   border-top-color: rgb(0, 0, 0);\n"
                                                "                  border-right-color: rgb(0, 0, 0);\n"
                                                "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                "                   border-left-color: rgb(0, 0, 0);\n"
                                                "                  border-image-source: initial;\n"
                                                "                  border-image-slice: initial;\n"
                                                "                  border-image-width: initial;\n"
                                                "                  border-image-outset: initial;\n"
                                                "                border-image-repeat: initial;\n"
                                                "                border-radius: 4px;\n"
                                                "                background-color: qlineargradient(x1: 0, y"
                                                "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                "                border-image: none;\n"
                                                "              color: #FFF;\n"
                                                "               text-shadow: 1px 1px #000;\n"
                                                "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "                font-family: Open Sans;\n"
                                                "                font-size: 12px;\n"
                                                "               font-weight: bold;\n"
                                                "               height: 36px;\n"
                                                "                line-height: 36px;\n"
                                                "                text-align: center;\n"
                                                "				margin: 0px;\n"
                                                "           }\n"
                                                "            QPushButton::hover {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                "           }\n"
                                                "            QPushButton::pressed {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                "            }\n"
                                                "QPushButton::checked {\n"
                                                "				background-color:"
                                                " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                "				color: #332211;\n"
                                                "text-shadow: 1px 1px #FFF;\n"
                                                "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "font-weight: bold;\n"
                                                "			}\n"
                                                "            QPushButton::flat {\n"
                                                "                border: none;\n"
                                                "}")
            icon3 = QIcon()
            icon3.addFile(u":/crafting_methods/images/crafting_methods/method_regal.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_regal_btn.setIcon(icon3)
            self.method_regal_btn.setIconSize(QSize(30, 30))
            self.method_regal_btn.setCheckable(True)
            self.method_regal_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_regal_btn, 1, 0, 1, 1)

            self.method_alchemy_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_alchemy_btn)
            self.method_alchemy_btn.setObjectName(u"method_alchemy_btn")
            sizePolicy.setHeightForWidth(self.method_alchemy_btn.sizePolicy().hasHeightForWidth())
            self.method_alchemy_btn.setSizePolicy(sizePolicy)
            self.method_alchemy_btn.setMinimumSize(QSize(30, 30))
            self.method_alchemy_btn.setMaximumSize(QSize(60, 60))
            self.method_alchemy_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_alchemy_btn.setMouseTracking(True)
            self.method_alchemy_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                  border-top-width: 1px;\n"
                                                  "                   border-right-width: 1px;\n"
                                                  "                   border-bottom-width: 1px;\n"
                                                  "                   border-left-width: 1px;\n"
                                                  "                   border-top-style: solid;\n"
                                                  "                 border-right-style: solid;\n"
                                                  "                  border-bottom-style: solid;\n"
                                                  "                   border-left-style: solid;\n"
                                                  "                   border-top-color: rgb(0, 0, 0);\n"
                                                  "                  border-right-color: rgb(0, 0, 0);\n"
                                                  "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                  "                   border-left-color: rgb(0, 0, 0);\n"
                                                  "                  border-image-source: initial;\n"
                                                  "                  border-image-slice: initial;\n"
                                                  "                  border-image-width: initial;\n"
                                                  "                  border-image-outset: initial;\n"
                                                  "                border-image-repeat: initial;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y"
                                                  "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               text-shadow: 1px 1px #000;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                  "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                  "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                  "            }\n"
                                                  "QPushButton::checked {\n"
                                                  "				background-color:"
                                                  " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon4 = QIcon()
            icon4.addFile(u":/crafting_methods/images/crafting_methods/method_alchemy.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_alchemy_btn.setIcon(icon4)
            self.method_alchemy_btn.setIconSize(QSize(30, 30))
            self.method_alchemy_btn.setCheckable(True)
            self.method_alchemy_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_alchemy_btn, 1, 1, 1, 1)

            self.method_chaos_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_chaos_btn)
            self.method_chaos_btn.setObjectName(u"method_chaos_btn")
            sizePolicy.setHeightForWidth(self.method_chaos_btn.sizePolicy().hasHeightForWidth())
            self.method_chaos_btn.setSizePolicy(sizePolicy)
            self.method_chaos_btn.setMinimumSize(QSize(30, 30))
            self.method_chaos_btn.setMaximumSize(QSize(60, 60))
            self.method_chaos_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_chaos_btn.setMouseTracking(True)
            self.method_chaos_btn.setStyleSheet(u"QPushButton {\n"
                                                "                border: 1px solid #000;\n"
                                                "                  border-top-width: 1px;\n"
                                                "                   border-right-width: 1px;\n"
                                                "                   border-bottom-width: 1px;\n"
                                                "                   border-left-width: 1px;\n"
                                                "                   border-top-style: solid;\n"
                                                "                 border-right-style: solid;\n"
                                                "                  border-bottom-style: solid;\n"
                                                "                   border-left-style: solid;\n"
                                                "                   border-top-color: rgb(0, 0, 0);\n"
                                                "                  border-right-color: rgb(0, 0, 0);\n"
                                                "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                "                   border-left-color: rgb(0, 0, 0);\n"
                                                "                  border-image-source: initial;\n"
                                                "                  border-image-slice: initial;\n"
                                                "                  border-image-width: initial;\n"
                                                "                  border-image-outset: initial;\n"
                                                "                border-image-repeat: initial;\n"
                                                "                border-radius: 4px;\n"
                                                "                background-color: qlineargradient(x1: 0, y"
                                                "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                "                border-image: none;\n"
                                                "              color: #FFF;\n"
                                                "               text-shadow: 1px 1px #000;\n"
                                                "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "                font-family: Open Sans;\n"
                                                "                font-size: 12px;\n"
                                                "               font-weight: bold;\n"
                                                "               height: 36px;\n"
                                                "                line-height: 36px;\n"
                                                "                text-align: center;\n"
                                                "				margin: 0px;\n"
                                                "           }\n"
                                                "            QPushButton::hover {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                "           }\n"
                                                "            QPushButton::pressed {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                "            }\n"
                                                "QPushButton::checked {\n"
                                                "				background-color:"
                                                " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                "				color: #332211;\n"
                                                "text-shadow: 1px 1px #FFF;\n"
                                                "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "font-weight: bold;\n"
                                                "			}\n"
                                                "            QPushButton::flat {\n"
                                                "                border: none;\n"
                                                "}")
            icon5 = QIcon()
            icon5.addFile(u":/crafting_methods/images/crafting_methods/method_chaos.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_chaos_btn.setIcon(icon5)
            self.method_chaos_btn.setIconSize(QSize(30, 30))
            self.method_chaos_btn.setCheckable(True)
            self.method_chaos_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_chaos_btn, 1, 2, 1, 1)

            self.method_exalted_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_exalted_btn)
            self.method_exalted_btn.setObjectName(u"method_exalted_btn")
            sizePolicy.setHeightForWidth(self.method_exalted_btn.sizePolicy().hasHeightForWidth())
            self.method_exalted_btn.setSizePolicy(sizePolicy)
            self.method_exalted_btn.setMinimumSize(QSize(30, 30))
            self.method_exalted_btn.setMaximumSize(QSize(60, 60))
            self.method_exalted_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_exalted_btn.setMouseTracking(True)
            self.method_exalted_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                  border-top-width: 1px;\n"
                                                  "                   border-right-width: 1px;\n"
                                                  "                   border-bottom-width: 1px;\n"
                                                  "                   border-left-width: 1px;\n"
                                                  "                   border-top-style: solid;\n"
                                                  "                 border-right-style: solid;\n"
                                                  "                  border-bottom-style: solid;\n"
                                                  "                   border-left-style: solid;\n"
                                                  "                   border-top-color: rgb(0, 0, 0);\n"
                                                  "                  border-right-color: rgb(0, 0, 0);\n"
                                                  "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                  "                   border-left-color: rgb(0, 0, 0);\n"
                                                  "                  border-image-source: initial;\n"
                                                  "                  border-image-slice: initial;\n"
                                                  "                  border-image-width: initial;\n"
                                                  "                  border-image-outset: initial;\n"
                                                  "                border-image-repeat: initial;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y"
                                                  "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               text-shadow: 1px 1px #000;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                  "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                  "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                  "            }\n"
                                                  "QPushButton::checked {\n"
                                                  "				background-color:"
                                                  " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon6 = QIcon()
            icon6.addFile(u":/crafting_methods/images/crafting_methods/method_exalted.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_exalted_btn.setIcon(icon6)
            self.method_exalted_btn.setIconSize(QSize(30, 30))
            self.method_exalted_btn.setCheckable(True)
            self.method_exalted_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_exalted_btn, 2, 0, 1, 1)

            self.method_scour_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_scour_btn)
            self.method_scour_btn.setObjectName(u"method_scour_btn")
            sizePolicy.setHeightForWidth(self.method_scour_btn.sizePolicy().hasHeightForWidth())
            self.method_scour_btn.setSizePolicy(sizePolicy)
            self.method_scour_btn.setMinimumSize(QSize(30, 30))
            self.method_scour_btn.setMaximumSize(QSize(60, 60))
            self.method_scour_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_scour_btn.setMouseTracking(True)
            self.method_scour_btn.setStyleSheet(u"QPushButton {\n"
                                                "                border: 1px solid #000;\n"
                                                "                  border-top-width: 1px;\n"
                                                "                   border-right-width: 1px;\n"
                                                "                   border-bottom-width: 1px;\n"
                                                "                   border-left-width: 1px;\n"
                                                "                   border-top-style: solid;\n"
                                                "                 border-right-style: solid;\n"
                                                "                  border-bottom-style: solid;\n"
                                                "                   border-left-style: solid;\n"
                                                "                   border-top-color: rgb(0, 0, 0);\n"
                                                "                  border-right-color: rgb(0, 0, 0);\n"
                                                "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                "                   border-left-color: rgb(0, 0, 0);\n"
                                                "                  border-image-source: initial;\n"
                                                "                  border-image-slice: initial;\n"
                                                "                  border-image-width: initial;\n"
                                                "                  border-image-outset: initial;\n"
                                                "                border-image-repeat: initial;\n"
                                                "                border-radius: 4px;\n"
                                                "                background-color: qlineargradient(x1: 0, y"
                                                "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                "                border-image: none;\n"
                                                "              color: #FFF;\n"
                                                "               text-shadow: 1px 1px #000;\n"
                                                "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "                font-family: Open Sans;\n"
                                                "                font-size: 12px;\n"
                                                "               font-weight: bold;\n"
                                                "               height: 36px;\n"
                                                "                line-height: 36px;\n"
                                                "                text-align: center;\n"
                                                "				margin: 0px;\n"
                                                "           }\n"
                                                "            QPushButton::hover {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                "           }\n"
                                                "            QPushButton::pressed {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                "            }\n"
                                                "QPushButton::checked {\n"
                                                "				background-color:"
                                                " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                "				color: #332211;\n"
                                                "text-shadow: 1px 1px #FFF;\n"
                                                "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "font-weight: bold;\n"
                                                "			}\n"
                                                "            QPushButton::flat {\n"
                                                "                border: none;\n"
                                                "}")
            icon7 = QIcon()
            icon7.addFile(u":/crafting_methods/images/crafting_methods/method_scour.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_scour_btn.setIcon(icon7)
            self.method_scour_btn.setIconSize(QSize(30, 30))
            self.method_scour_btn.setCheckable(True)
            self.method_scour_btn.setChecked(False)
            self.method_scour_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_scour_btn, 2, 1, 1, 1)

            self.method_annul_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_annul_btn)
            self.method_annul_btn.setObjectName(u"method_annul_btn")
            sizePolicy.setHeightForWidth(self.method_annul_btn.sizePolicy().hasHeightForWidth())
            self.method_annul_btn.setSizePolicy(sizePolicy)
            self.method_annul_btn.setMinimumSize(QSize(30, 30))
            self.method_annul_btn.setMaximumSize(QSize(60, 60))
            self.method_annul_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_annul_btn.setMouseTracking(True)
            self.method_annul_btn.setStyleSheet(u"QPushButton {\n"
                                                "                border: 1px solid #000;\n"
                                                "                  border-top-width: 1px;\n"
                                                "                   border-right-width: 1px;\n"
                                                "                   border-bottom-width: 1px;\n"
                                                "                   border-left-width: 1px;\n"
                                                "                   border-top-style: solid;\n"
                                                "                 border-right-style: solid;\n"
                                                "                  border-bottom-style: solid;\n"
                                                "                   border-left-style: solid;\n"
                                                "                   border-top-color: rgb(0, 0, 0);\n"
                                                "                  border-right-color: rgb(0, 0, 0);\n"
                                                "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                "                   border-left-color: rgb(0, 0, 0);\n"
                                                "                  border-image-source: initial;\n"
                                                "                  border-image-slice: initial;\n"
                                                "                  border-image-width: initial;\n"
                                                "                  border-image-outset: initial;\n"
                                                "                border-image-repeat: initial;\n"
                                                "                border-radius: 4px;\n"
                                                "                background-color: qlineargradient(x1: 0, y"
                                                "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                "                border-image: none;\n"
                                                "              color: #FFF;\n"
                                                "               text-shadow: 1px 1px #000;\n"
                                                "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "                font-family: Open Sans;\n"
                                                "                font-size: 12px;\n"
                                                "               font-weight: bold;\n"
                                                "               height: 36px;\n"
                                                "                line-height: 36px;\n"
                                                "                text-align: center;\n"
                                                "				margin: 0px;\n"
                                                "           }\n"
                                                "            QPushButton::hover {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                "           }\n"
                                                "            QPushButton::pressed {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                "            }\n"
                                                "QPushButton::checked {\n"
                                                "				background-color:"
                                                " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                "				color: #332211;\n"
                                                "text-shadow: 1px 1px #FFF;\n"
                                                "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "font-weight: bold;\n"
                                                "			}\n"
                                                "            QPushButton::flat {\n"
                                                "                border: none;\n"
                                                "}")
            icon8 = QIcon()
            icon8.addFile(u":/crafting_methods/images/crafting_methods/method_annul.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_annul_btn.setIcon(icon8)
            self.method_annul_btn.setIconSize(QSize(30, 30))
            self.method_annul_btn.setCheckable(True)
            self.method_annul_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_annul_btn, 2, 2, 1, 1)

            self.method_crusader_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_crusader_btn)
            self.method_crusader_btn.setObjectName(u"method_crusader_btn")
            sizePolicy.setHeightForWidth(self.method_crusader_btn.sizePolicy().hasHeightForWidth())
            self.method_crusader_btn.setSizePolicy(sizePolicy)
            self.method_crusader_btn.setMinimumSize(QSize(30, 30))
            self.method_crusader_btn.setMaximumSize(QSize(60, 60))
            self.method_crusader_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_crusader_btn.setMouseTracking(True)
            self.method_crusader_btn.setStyleSheet(u"QPushButton {\n"
                                                   "                border: 1px solid #000;\n"
                                                   "                  border-top-width: 1px;\n"
                                                   "                   border-right-width: 1px;\n"
                                                   "                   border-bottom-width: 1px;\n"
                                                   "                   border-left-width: 1px;\n"
                                                   "                   border-top-style: solid;\n"
                                                   "                 border-right-style: solid;\n"
                                                   "                  border-bottom-style: solid;\n"
                                                   "                   border-left-style: solid;\n"
                                                   "                   border-top-color: rgb(0, 0, 0);\n"
                                                   "                  border-right-color: rgb(0, 0, 0);\n"
                                                   "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                   "                   border-left-color: rgb(0, 0, 0);\n"
                                                   "                  border-image-source: initial;\n"
                                                   "                  border-image-slice: initial;\n"
                                                   "                  border-image-width: initial;\n"
                                                   "                  border-image-outset: initial;\n"
                                                   "                border-image-repeat: initial;\n"
                                                   "                border-radius: 4px;\n"
                                                   "                background-color: qlineargradient(x1: 0, y"
                                                   "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                   "                border-image: none;\n"
                                                   "              color: #FFF;\n"
                                                   "               text-shadow: 1px 1px #000;\n"
                                                   "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "                font-family: Open Sans;\n"
                                                   "                font-size: 12px;\n"
                                                   "               font-weight: bold;\n"
                                                   "               height: 36px;\n"
                                                   "                line-height: 36px;\n"
                                                   "                text-align: center;\n"
                                                   "				margin: 0px;\n"
                                                   "           }\n"
                                                   "            QPushButton::hover {\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                   "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                   "           }\n"
                                                   "            QPushButton::pressed {\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                   "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                   "            }\n"
                                                   "QPushButton::checked {\n"
                                                   "				background-color:"
                                                   " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "				color: #332211;\n"
                                                   "text-shadow: 1px 1px #FFF;\n"
                                                   "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "font-weight: bold;\n"
                                                   "			}\n"
                                                   "            QPushButton::flat {\n"
                                                   "                border: none;\n"
                                                   "}")
            icon9 = QIcon()
            icon9.addFile(u":/crafting_methods/images/crafting_methods/method_crusader.png", QSize(), QIcon.Normal,
                          QIcon.Off)
            self.method_crusader_btn.setIcon(icon9)
            self.method_crusader_btn.setIconSize(QSize(30, 30))
            self.method_crusader_btn.setCheckable(True)
            self.method_crusader_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_crusader_btn, 3, 0, 1, 1)

            self.method_hunter_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_hunter_btn)
            self.method_hunter_btn.setObjectName(u"method_hunter_btn")
            sizePolicy.setHeightForWidth(self.method_hunter_btn.sizePolicy().hasHeightForWidth())
            self.method_hunter_btn.setSizePolicy(sizePolicy)
            self.method_hunter_btn.setMinimumSize(QSize(30, 30))
            self.method_hunter_btn.setMaximumSize(QSize(60, 60))
            self.method_hunter_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_hunter_btn.setMouseTracking(True)
            self.method_hunter_btn.setStyleSheet(u"QPushButton {\n"
                                                 "                border: 1px solid #000;\n"
                                                 "                  border-top-width: 1px;\n"
                                                 "                   border-right-width: 1px;\n"
                                                 "                   border-bottom-width: 1px;\n"
                                                 "                   border-left-width: 1px;\n"
                                                 "                   border-top-style: solid;\n"
                                                 "                 border-right-style: solid;\n"
                                                 "                  border-bottom-style: solid;\n"
                                                 "                   border-left-style: solid;\n"
                                                 "                   border-top-color: rgb(0, 0, 0);\n"
                                                 "                  border-right-color: rgb(0, 0, 0);\n"
                                                 "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                 "                   border-left-color: rgb(0, 0, 0);\n"
                                                 "                  border-image-source: initial;\n"
                                                 "                  border-image-slice: initial;\n"
                                                 "                  border-image-width: initial;\n"
                                                 "                  border-image-outset: initial;\n"
                                                 "                border-image-repeat: initial;\n"
                                                 "                border-radius: 4px;\n"
                                                 "                background-color: qlineargradient(x1: 0, y"
                                                 "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                 "                border-image: none;\n"
                                                 "              color: #FFF;\n"
                                                 "               text-shadow: 1px 1px #000;\n"
                                                 "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "                font-family: Open Sans;\n"
                                                 "                font-size: 12px;\n"
                                                 "               font-weight: bold;\n"
                                                 "               height: 36px;\n"
                                                 "                line-height: 36px;\n"
                                                 "                text-align: center;\n"
                                                 "				margin: 0px;\n"
                                                 "           }\n"
                                                 "            QPushButton::hover {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                 "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                 "           }\n"
                                                 "            QPushButton::pressed {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                 "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                 "            }\n"
                                                 "QPushButton::checked {\n"
                                                 "				background-color:"
                                                 " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                 "				color: #332211;\n"
                                                 "text-shadow: 1px 1px #FFF;\n"
                                                 "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "font-weight: bold;\n"
                                                 "			}\n"
                                                 "            QPushButton::flat {\n"
                                                 "                border: none;\n"
                                                 "}")
            icon10 = QIcon()
            icon10.addFile(u":/crafting_methods/images/crafting_methods/method_hunter.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_hunter_btn.setIcon(icon10)
            self.method_hunter_btn.setIconSize(QSize(30, 30))
            self.method_hunter_btn.setCheckable(True)
            self.method_hunter_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_hunter_btn, 3, 1, 1, 1)

            self.method_redeemer_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_redeemer_btn)
            self.method_redeemer_btn.setObjectName(u"method_redeemer_btn")
            sizePolicy.setHeightForWidth(self.method_redeemer_btn.sizePolicy().hasHeightForWidth())
            self.method_redeemer_btn.setSizePolicy(sizePolicy)
            self.method_redeemer_btn.setMinimumSize(QSize(30, 30))
            self.method_redeemer_btn.setMaximumSize(QSize(60, 60))
            self.method_redeemer_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_redeemer_btn.setMouseTracking(True)
            self.method_redeemer_btn.setStyleSheet(u"QPushButton {\n"
                                                   "                border: 1px solid #000;\n"
                                                   "                  border-top-width: 1px;\n"
                                                   "                   border-right-width: 1px;\n"
                                                   "                   border-bottom-width: 1px;\n"
                                                   "                   border-left-width: 1px;\n"
                                                   "                   border-top-style: solid;\n"
                                                   "                 border-right-style: solid;\n"
                                                   "                  border-bottom-style: solid;\n"
                                                   "                   border-left-style: solid;\n"
                                                   "                   border-top-color: rgb(0, 0, 0);\n"
                                                   "                  border-right-color: rgb(0, 0, 0);\n"
                                                   "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                   "                   border-left-color: rgb(0, 0, 0);\n"
                                                   "                  border-image-source: initial;\n"
                                                   "                  border-image-slice: initial;\n"
                                                   "                  border-image-width: initial;\n"
                                                   "                  border-image-outset: initial;\n"
                                                   "                border-image-repeat: initial;\n"
                                                   "                border-radius: 4px;\n"
                                                   "                background-color: qlineargradient(x1: 0, y"
                                                   "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                   "                border-image: none;\n"
                                                   "              color: #FFF;\n"
                                                   "               text-shadow: 1px 1px #000;\n"
                                                   "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "                font-family: Open Sans;\n"
                                                   "                font-size: 12px;\n"
                                                   "               font-weight: bold;\n"
                                                   "               height: 36px;\n"
                                                   "                line-height: 36px;\n"
                                                   "                text-align: center;\n"
                                                   "				margin: 0px;\n"
                                                   "           }\n"
                                                   "            QPushButton::hover {\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                   "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                   "           }\n"
                                                   "            QPushButton::pressed {\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                   "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                   "            }\n"
                                                   "QPushButton::checked {\n"
                                                   "				background-color:"
                                                   " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "				color: #332211;\n"
                                                   "text-shadow: 1px 1px #FFF;\n"
                                                   "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "font-weight: bold;\n"
                                                   "			}\n"
                                                   "            QPushButton::flat {\n"
                                                   "                border: none;\n"
                                                   "}")
            icon11 = QIcon()
            icon11.addFile(u":/crafting_methods/images/crafting_methods/method_redeemer.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_redeemer_btn.setIcon(icon11)
            self.method_redeemer_btn.setIconSize(QSize(30, 30))
            self.method_redeemer_btn.setCheckable(True)
            self.method_redeemer_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_redeemer_btn, 3, 2, 1, 1)

            self.method_warlord_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_warlord_btn)
            self.method_warlord_btn.setObjectName(u"method_warlord_btn")
            sizePolicy.setHeightForWidth(self.method_warlord_btn.sizePolicy().hasHeightForWidth())
            self.method_warlord_btn.setSizePolicy(sizePolicy)
            self.method_warlord_btn.setMinimumSize(QSize(30, 30))
            self.method_warlord_btn.setMaximumSize(QSize(60, 60))
            self.method_warlord_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_warlord_btn.setMouseTracking(True)
            self.method_warlord_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                  border-top-width: 1px;\n"
                                                  "                   border-right-width: 1px;\n"
                                                  "                   border-bottom-width: 1px;\n"
                                                  "                   border-left-width: 1px;\n"
                                                  "                   border-top-style: solid;\n"
                                                  "                 border-right-style: solid;\n"
                                                  "                  border-bottom-style: solid;\n"
                                                  "                   border-left-style: solid;\n"
                                                  "                   border-top-color: rgb(0, 0, 0);\n"
                                                  "                  border-right-color: rgb(0, 0, 0);\n"
                                                  "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                  "                   border-left-color: rgb(0, 0, 0);\n"
                                                  "                  border-image-source: initial;\n"
                                                  "                  border-image-slice: initial;\n"
                                                  "                  border-image-width: initial;\n"
                                                  "                  border-image-outset: initial;\n"
                                                  "                border-image-repeat: initial;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y"
                                                  "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               text-shadow: 1px 1px #000;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                  "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                  "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                  "            }\n"
                                                  "QPushButton::checked {\n"
                                                  "				background-color:"
                                                  " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon12 = QIcon()
            icon12.addFile(u":/crafting_methods/images/crafting_methods/method_warlord.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_warlord_btn.setIcon(icon12)
            self.method_warlord_btn.setIconSize(QSize(30, 30))
            self.method_warlord_btn.setCheckable(True)
            self.method_warlord_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_warlord_btn, 4, 0, 1, 1)

            self.method_blessed_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_blessed_btn)
            self.method_blessed_btn.setObjectName(u"method_blessed_btn")
            sizePolicy.setHeightForWidth(self.method_blessed_btn.sizePolicy().hasHeightForWidth())
            self.method_blessed_btn.setSizePolicy(sizePolicy)
            self.method_blessed_btn.setMinimumSize(QSize(30, 30))
            self.method_blessed_btn.setMaximumSize(QSize(60, 60))
            self.method_blessed_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_blessed_btn.setMouseTracking(True)
            self.method_blessed_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                  border-top-width: 1px;\n"
                                                  "                   border-right-width: 1px;\n"
                                                  "                   border-bottom-width: 1px;\n"
                                                  "                   border-left-width: 1px;\n"
                                                  "                   border-top-style: solid;\n"
                                                  "                 border-right-style: solid;\n"
                                                  "                  border-bottom-style: solid;\n"
                                                  "                   border-left-style: solid;\n"
                                                  "                   border-top-color: rgb(0, 0, 0);\n"
                                                  "                  border-right-color: rgb(0, 0, 0);\n"
                                                  "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                  "                   border-left-color: rgb(0, 0, 0);\n"
                                                  "                  border-image-source: initial;\n"
                                                  "                  border-image-slice: initial;\n"
                                                  "                  border-image-width: initial;\n"
                                                  "                  border-image-outset: initial;\n"
                                                  "                border-image-repeat: initial;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y"
                                                  "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               text-shadow: 1px 1px #000;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                  "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                  "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                  "            }\n"
                                                  "QPushButton::checked {\n"
                                                  "				background-color:"
                                                  " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon13 = QIcon()
            icon13.addFile(u":/crafting_methods/images/crafting_methods/method_blessed.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_blessed_btn.setIcon(icon13)
            self.method_blessed_btn.setIconSize(QSize(30, 30))
            self.method_blessed_btn.setCheckable(True)
            self.method_blessed_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_blessed_btn, 4, 1, 1, 1)

            self.method_divine_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_divine_btn)
            self.method_divine_btn.setObjectName(u"method_divine_btn")
            sizePolicy.setHeightForWidth(self.method_divine_btn.sizePolicy().hasHeightForWidth())
            self.method_divine_btn.setSizePolicy(sizePolicy)
            self.method_divine_btn.setMinimumSize(QSize(30, 30))
            self.method_divine_btn.setMaximumSize(QSize(60, 60))
            self.method_divine_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_divine_btn.setMouseTracking(True)
            self.method_divine_btn.setStyleSheet(u"QPushButton {\n"
                                                 "                border: 1px solid #000;\n"
                                                 "                  border-top-width: 1px;\n"
                                                 "                   border-right-width: 1px;\n"
                                                 "                   border-bottom-width: 1px;\n"
                                                 "                   border-left-width: 1px;\n"
                                                 "                   border-top-style: solid;\n"
                                                 "                 border-right-style: solid;\n"
                                                 "                  border-bottom-style: solid;\n"
                                                 "                   border-left-style: solid;\n"
                                                 "                   border-top-color: rgb(0, 0, 0);\n"
                                                 "                  border-right-color: rgb(0, 0, 0);\n"
                                                 "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                 "                   border-left-color: rgb(0, 0, 0);\n"
                                                 "                  border-image-source: initial;\n"
                                                 "                  border-image-slice: initial;\n"
                                                 "                  border-image-width: initial;\n"
                                                 "                  border-image-outset: initial;\n"
                                                 "                border-image-repeat: initial;\n"
                                                 "                border-radius: 4px;\n"
                                                 "                background-color: qlineargradient(x1: 0, y"
                                                 "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                 "                border-image: none;\n"
                                                 "              color: #FFF;\n"
                                                 "               text-shadow: 1px 1px #000;\n"
                                                 "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "                font-family: Open Sans;\n"
                                                 "                font-size: 12px;\n"
                                                 "               font-weight: bold;\n"
                                                 "               height: 36px;\n"
                                                 "                line-height: 36px;\n"
                                                 "                text-align: center;\n"
                                                 "				margin: 0px;\n"
                                                 "           }\n"
                                                 "            QPushButton::hover {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                 "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                 "           }\n"
                                                 "            QPushButton::pressed {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                 "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                 "            }\n"
                                                 "QPushButton::checked {\n"
                                                 "				background-color:"
                                                 " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                 "				color: #332211;\n"
                                                 "text-shadow: 1px 1px #FFF;\n"
                                                 "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "font-weight: bold;\n"
                                                 "			}\n"
                                                 "            QPushButton::flat {\n"
                                                 "                border: none;\n"
                                                 "}")
            icon14 = QIcon()
            icon14.addFile(u":/crafting_methods/images/crafting_methods/method_divine.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_divine_btn.setIcon(icon14)
            self.method_divine_btn.setIconSize(QSize(30, 30))
            self.method_divine_btn.setCheckable(True)
            self.method_divine_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_divine_btn, 4, 2, 1, 1)

            self.method_veiled_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_veiled_btn)
            self.method_veiled_btn.setObjectName(u"method_veiled_btn")
            sizePolicy.setHeightForWidth(self.method_veiled_btn.sizePolicy().hasHeightForWidth())
            self.method_veiled_btn.setSizePolicy(sizePolicy)
            self.method_veiled_btn.setMinimumSize(QSize(30, 30))
            self.method_veiled_btn.setMaximumSize(QSize(60, 60))
            self.method_veiled_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_veiled_btn.setMouseTracking(True)
            self.method_veiled_btn.setStyleSheet(u"QPushButton {\n"
                                                 "                border: 1px solid #000;\n"
                                                 "                  border-top-width: 1px;\n"
                                                 "                   border-right-width: 1px;\n"
                                                 "                   border-bottom-width: 1px;\n"
                                                 "                   border-left-width: 1px;\n"
                                                 "                   border-top-style: solid;\n"
                                                 "                 border-right-style: solid;\n"
                                                 "                  border-bottom-style: solid;\n"
                                                 "                   border-left-style: solid;\n"
                                                 "                   border-top-color: rgb(0, 0, 0);\n"
                                                 "                  border-right-color: rgb(0, 0, 0);\n"
                                                 "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                 "                   border-left-color: rgb(0, 0, 0);\n"
                                                 "                  border-image-source: initial;\n"
                                                 "                  border-image-slice: initial;\n"
                                                 "                  border-image-width: initial;\n"
                                                 "                  border-image-outset: initial;\n"
                                                 "                border-image-repeat: initial;\n"
                                                 "                border-radius: 4px;\n"
                                                 "                background-color: qlineargradient(x1: 0, y"
                                                 "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                 "                border-image: none;\n"
                                                 "              color: #FFF;\n"
                                                 "               text-shadow: 1px 1px #000;\n"
                                                 "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "                font-family: Open Sans;\n"
                                                 "                font-size: 12px;\n"
                                                 "               font-weight: bold;\n"
                                                 "               height: 36px;\n"
                                                 "                line-height: 36px;\n"
                                                 "                text-align: center;\n"
                                                 "				margin: 0px;\n"
                                                 "           }\n"
                                                 "            QPushButton::hover {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                 "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                 "           }\n"
                                                 "            QPushButton::pressed {\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                 "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                 "            }\n"
                                                 "QPushButton::checked {\n"
                                                 "				background-color:"
                                                 " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                 "				color: #332211;\n"
                                                 "text-shadow: 1px 1px #FFF;\n"
                                                 "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "font-weight: bold;\n"
                                                 "			}\n"
                                                 "            QPushButton::flat {\n"
                                                 "                border: none;\n"
                                                 "}")
            icon15 = QIcon()
            icon15.addFile(u":/crafting_methods/images/crafting_methods/method_veiled.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_veiled_btn.setIcon(icon15)
            self.method_veiled_btn.setIconSize(QSize(30, 30))
            self.method_veiled_btn.setCheckable(True)
            self.method_veiled_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_veiled_btn, 5, 0, 1, 1)

            self.method_woke_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_woke_btn)
            self.method_woke_btn.setObjectName(u"method_woke_btn")
            sizePolicy.setHeightForWidth(self.method_woke_btn.sizePolicy().hasHeightForWidth())
            self.method_woke_btn.setSizePolicy(sizePolicy)
            self.method_woke_btn.setMinimumSize(QSize(30, 30))
            self.method_woke_btn.setMaximumSize(QSize(60, 60))
            self.method_woke_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_woke_btn.setMouseTracking(True)
            self.method_woke_btn.setStyleSheet(u"QPushButton {\n"
                                               "                border: 1px solid #000;\n"
                                               "                  border-top-width: 1px;\n"
                                               "                   border-right-width: 1px;\n"
                                               "                   border-bottom-width: 1px;\n"
                                               "                   border-left-width: 1px;\n"
                                               "                   border-top-style: solid;\n"
                                               "                 border-right-style: solid;\n"
                                               "                  border-bottom-style: solid;\n"
                                               "                   border-left-style: solid;\n"
                                               "                   border-top-color: rgb(0, 0, 0);\n"
                                               "                  border-right-color: rgb(0, 0, 0);\n"
                                               "                   border-bottom-color: rgb(0, 0, 0);\n"
                                               "                   border-left-color: rgb(0, 0, 0);\n"
                                               "                  border-image-source: initial;\n"
                                               "                  border-image-slice: initial;\n"
                                               "                  border-image-width: initial;\n"
                                               "                  border-image-outset: initial;\n"
                                               "                border-image-repeat: initial;\n"
                                               "                border-radius: 4px;\n"
                                               "                background-color: qlineargradient(x1: 0, y"
                                               "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                               "                border-image: none;\n"
                                               "              color: #FFF;\n"
                                               "               text-shadow: 1px 1px #000;\n"
                                               "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                               "                font-family: Open Sans;\n"
                                               "                font-size: 12px;\n"
                                               "               font-weight: bold;\n"
                                               "               height: 36px;\n"
                                               "                line-height: 36px;\n"
                                               "                text-align: center;\n"
                                               "				margin: 0px;\n"
                                               "           }\n"
                                               "            QPushButton::hover {\n"
                                               "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                               "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                               "           }\n"
                                               "            QPushButton::pressed {\n"
                                               "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                               "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                               "            }\n"
                                               "QPushButton::checked {\n"
                                               "				background-color:"
                                               " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                               "				color: #332211;\n"
                                               "text-shadow: 1px 1px #FFF;\n"
                                               "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                               "font-weight: bold;\n"
                                               "			}\n"
                                               "            QPushButton::flat {\n"
                                               "                border: none;\n"
                                               "}")
            icon16 = QIcon()
            icon16.addFile(u":/crafting_methods/images/crafting_methods/method_woke.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_woke_btn.setIcon(icon16)
            self.method_woke_btn.setIconSize(QSize(30, 30))
            self.method_woke_btn.setCheckable(True)
            self.method_woke_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_woke_btn, 5, 1, 1, 1)

            self.method_maven_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_maven_btn)
            self.method_maven_btn.setObjectName(u"method_maven_btn")
            sizePolicy.setHeightForWidth(self.method_maven_btn.sizePolicy().hasHeightForWidth())
            self.method_maven_btn.setSizePolicy(sizePolicy)
            self.method_maven_btn.setMinimumSize(QSize(30, 30))
            self.method_maven_btn.setMaximumSize(QSize(60, 60))
            self.method_maven_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_maven_btn.setMouseTracking(True)
            self.method_maven_btn.setStyleSheet(u"QPushButton {\n"
                                                "                border: 1px solid #000;\n"
                                                "                  border-top-width: 1px;\n"
                                                "                   border-right-width: 1px;\n"
                                                "                   border-bottom-width: 1px;\n"
                                                "                   border-left-width: 1px;\n"
                                                "                   border-top-style: solid;\n"
                                                "                 border-right-style: solid;\n"
                                                "                  border-bottom-style: solid;\n"
                                                "                   border-left-style: solid;\n"
                                                "                   border-top-color: rgb(0, 0, 0);\n"
                                                "                  border-right-color: rgb(0, 0, 0);\n"
                                                "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                "                   border-left-color: rgb(0, 0, 0);\n"
                                                "                  border-image-source: initial;\n"
                                                "                  border-image-slice: initial;\n"
                                                "                  border-image-width: initial;\n"
                                                "                  border-image-outset: initial;\n"
                                                "                border-image-repeat: initial;\n"
                                                "                border-radius: 4px;\n"
                                                "                background-color: qlineargradient(x1: 0, y"
                                                "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                "                border-image: none;\n"
                                                "              color: #FFF;\n"
                                                "               text-shadow: 1px 1px #000;\n"
                                                "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "                font-family: Open Sans;\n"
                                                "                font-size: 12px;\n"
                                                "               font-weight: bold;\n"
                                                "               height: 36px;\n"
                                                "                line-height: 36px;\n"
                                                "                text-align: center;\n"
                                                "				margin: 0px;\n"
                                                "           }\n"
                                                "            QPushButton::hover {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                "           }\n"
                                                "            QPushButton::pressed {\n"
                                                "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                "            }\n"
                                                "QPushButton::checked {\n"
                                                "				background-color:"
                                                " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                "				color: #332211;\n"
                                                "text-shadow: 1px 1px #FFF;\n"
                                                "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                "font-weight: bold;\n"
                                                "			}\n"
                                                "            QPushButton::flat {\n"
                                                "                border: none;\n"
                                                "}")
            icon17 = QIcon()
            icon17.addFile(u":/crafting_methods/images/crafting_methods/method_maven.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_maven_btn.setIcon(icon17)
            self.method_maven_btn.setIconSize(QSize(30, 30))
            self.method_maven_btn.setCheckable(True)
            self.method_maven_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_maven_btn, 5, 2, 1, 1)

            self.method_fracturing_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_fracturing_btn)
            self.method_fracturing_btn.setObjectName(u"method_fracturing_btn")
            sizePolicy.setHeightForWidth(self.method_fracturing_btn.sizePolicy().hasHeightForWidth())
            self.method_fracturing_btn.setSizePolicy(sizePolicy)
            self.method_fracturing_btn.setMinimumSize(QSize(30, 30))
            self.method_fracturing_btn.setMaximumSize(QSize(60, 60))
            self.method_fracturing_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_fracturing_btn.setMouseTracking(True)
            self.method_fracturing_btn.setStyleSheet(u"QPushButton {\n"
                                                     "                border: 1px solid #000;\n"
                                                     "                  border-top-width: 1px;\n"
                                                     "                   border-right-width: 1px;\n"
                                                     "                   border-bottom-width: 1px;\n"
                                                     "                   border-left-width: 1px;\n"
                                                     "                   border-top-style: solid;\n"
                                                     "                 border-right-style: solid;\n"
                                                     "                  border-bottom-style: solid;\n"
                                                     "                   border-left-style: solid;\n"
                                                     "                   border-top-color: rgb(0, 0, 0);\n"
                                                     "                  border-right-color: rgb(0, 0, 0);\n"
                                                     "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                     "                   border-left-color: rgb(0, 0, 0);\n"
                                                     "                  border-image-source: initial;\n"
                                                     "                  border-image-slice: initial;\n"
                                                     "                  border-image-width: initial;\n"
                                                     "                  border-image-outset: initial;\n"
                                                     "                border-image-repeat: initial;\n"
                                                     "                border-radius: 4px;\n"
                                                     "                background-color: qlineargradient(x1: 0, y"
                                                     "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                     "                border-image: none;\n"
                                                     "              color: #FFF;\n"
                                                     "               text-shadow: 1px 1px #000;\n"
                                                     "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                     "                font-family: Open Sans;\n"
                                                     "                font-size: 12px;\n"
                                                     "               font-weight: bold;\n"
                                                     "               height: 36px;\n"
                                                     "                line-height: 36px;\n"
                                                     "                text-align: center;\n"
                                                     "				margin: 0px;\n"
                                                     "           }\n"
                                                     "            QPushButton::hover {\n"
                                                     "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                     "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                     "           }\n"
                                                     "            QPushButton::pressed {\n"
                                                     "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                     "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                     "            }\n"
                                                     "QPushButton::checked {\n"
                                                     "				background-color:"
                                                     " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                     "				color: #332211;\n"
                                                     "text-shadow: 1px 1px #FFF;\n"
                                                     "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                     "font-weight: bold;\n"
                                                     "			}\n"
                                                     "            QPushButton::flat {\n"
                                                     "                border: none;\n"
                                                     "}")
            icon18 = QIcon()
            icon18.addFile(u":/crafting_methods/images/crafting_methods/method_fracturing.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_fracturing_btn.setIcon(icon18)
            self.method_fracturing_btn.setIconSize(QSize(30, 30))
            self.method_fracturing_btn.setCheckable(True)
            self.method_fracturing_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_fracturing_btn, 6, 0, 1, 1)

            self.method_double_corrupt_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_double_corrupt_btn)
            self.method_double_corrupt_btn.setObjectName(u"method_double_corrupt_btn")
            sizePolicy.setHeightForWidth(self.method_double_corrupt_btn.sizePolicy().hasHeightForWidth())
            self.method_double_corrupt_btn.setSizePolicy(sizePolicy)
            self.method_double_corrupt_btn.setMinimumSize(QSize(30, 30))
            self.method_double_corrupt_btn.setMaximumSize(QSize(60, 60))
            self.method_double_corrupt_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_double_corrupt_btn.setMouseTracking(True)
            self.method_double_corrupt_btn.setStyleSheet(u"QPushButton {\n"
                                                         "                border: 1px solid #000;\n"
                                                         "                  border-top-width: 1px;\n"
                                                         "                   border-right-width: 1px;\n"
                                                         "                   border-bottom-width: 1px;\n"
                                                         "                   border-left-width: 1px;\n"
                                                         "                   border-top-style: solid;\n"
                                                         "                 border-right-style: solid;\n"
                                                         "                  border-bottom-style: solid;\n"
                                                         "                   border-left-style: solid;\n"
                                                         "                   border-top-color: rgb(0, 0, 0);\n"
                                                         "                  border-right-color: rgb(0, 0, 0);\n"
                                                         "                   border-bottom-color: rgb(0, 0, 0);\n"
                                                         "                   border-left-color: rgb(0, 0, 0);\n"
                                                         "                  border-image-source: initial;\n"
                                                         "                  border-image-slice: initial;\n"
                                                         "                  border-image-width: initial;\n"
                                                         "                  border-image-outset: initial;\n"
                                                         "                border-image-repeat: initial;\n"
                                                         "                border-radius: 4px;\n"
                                                         "                background-color: qlineargradient(x1: 0, y"
                                                         "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                         "                border-image: none;\n"
                                                         "              color: #FFF;\n"
                                                         "               text-shadow: 1px 1px #000;\n"
                                                         "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                         "                font-family: Open Sans;\n"
                                                         "                font-size: 12px;\n"
                                                         "               font-weight: bold;\n"
                                                         "               height: 36px;\n"
                                                         "                line-height: 36px;\n"
                                                         "                text-align: center;\n"
                                                         "				margin: 0px;\n"
                                                         "           }\n"
                                                         "            QPushButton::hover {\n"
                                                         "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                                         "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                                         "           }\n"
                                                         "            QPushButton::pressed {\n"
                                                         "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                                         "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                                         "            }\n"
                                                         "QPushButton::checked {\n"
                                                         "				background-color:"
                                                         " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                         "				color: #332211;\n"
                                                         "text-shadow: 1px 1px #FFF;\n"
                                                         "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                         "font-weight: bold;\n"
                                                         "			}\n"
                                                         "            QPushButton::flat {\n"
                                                         "                border: none;\n"
                                                         "}")
            icon19 = QIcon()
            icon19.addFile(u":/crafting_methods/images/crafting_methods/method_double_corrupt.png", QSize(),
                           QIcon.Normal, QIcon.Off)
            self.method_double_corrupt_btn.setIcon(icon19)
            self.method_double_corrupt_btn.setIconSize(QSize(30, 30))
            self.method_double_corrupt_btn.setCheckable(True)
            self.method_double_corrupt_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_double_corrupt_btn, 6, 1, 1, 1)

            self.method_vaal_btn = PyCustomCursorButton(self.crafting_methods_menu)
            self.crafting_methods_btn_group.addButton(self.method_vaal_btn)
            self.method_vaal_btn.setObjectName(u"method_vaal_btn")
            sizePolicy.setHeightForWidth(self.method_vaal_btn.sizePolicy().hasHeightForWidth())
            self.method_vaal_btn.setSizePolicy(sizePolicy)
            self.method_vaal_btn.setMinimumSize(QSize(30, 30))
            self.method_vaal_btn.setMaximumSize(QSize(60, 60))
            self.method_vaal_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_vaal_btn.setMouseTracking(True)
            self.method_vaal_btn.setStyleSheet(u"QPushButton {\n"
                                               "                border: 1px solid #000;\n"
                                               "                  border-top-width: 1px;\n"
                                               "                   border-right-width: 1px;\n"
                                               "                   border-bottom-width: 1px;\n"
                                               "                   border-left-width: 1px;\n"
                                               "                   border-top-style: solid;\n"
                                               "                 border-right-style: solid;\n"
                                               "                  border-bottom-style: solid;\n"
                                               "                   border-left-style: solid;\n"
                                               "                   border-top-color: rgb(0, 0, 0);\n"
                                               "                  border-right-color: rgb(0, 0, 0);\n"
                                               "                   border-bottom-color: rgb(0, 0, 0);\n"
                                               "                   border-left-color: rgb(0, 0, 0);\n"
                                               "                  border-image-source: initial;\n"
                                               "                  border-image-slice: initial;\n"
                                               "                  border-image-width: initial;\n"
                                               "                  border-image-outset: initial;\n"
                                               "                border-image-repeat: initial;\n"
                                               "                border-radius: 4px;\n"
                                               "                background-color: qlineargradient(x1: 0, y"
                                               "1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                               "                border-image: none;\n"
                                               "              color: #FFF;\n"
                                               "               text-shadow: 1px 1px #000;\n"
                                               "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                               "                font-family: Open Sans;\n"
                                               "                font-size: 12px;\n"
                                               "               font-weight: bold;\n"
                                               "               height: 36px;\n"
                                               "                line-height: 36px;\n"
                                               "                text-align: center;\n"
                                               "				margin: 0px;\n"
                                               "           }\n"
                                               "            QPushButton::hover {\n"
                                               "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
                                               "                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
                                               "           }\n"
                                               "            QPushButton::pressed {\n"
                                               "                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                               "                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
                                               "            }\n"
                                               "QPushButton::checked {\n"
                                               "				background-color:"
                                               " qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                               "				color: #332211;\n"
                                               "text-shadow: 1px 1px #FFF;\n"
                                               "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                               "font-weight: bold;\n"
                                               "			}\n"
                                               "            QPushButton::flat {\n"
                                               "                border: none;\n"
                                               "}")
            icon20 = QIcon()
            icon20.addFile(u":/crafting_methods/images/crafting_methods/method_vaal.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_vaal_btn.setIcon(icon20)
            self.method_vaal_btn.setIconSize(QSize(30, 30))
            self.method_vaal_btn.setCheckable(True)
            self.method_vaal_btn.setAutoExclusive(True)

            self.crafting_methods_layout1.addWidget(self.method_vaal_btn, 6, 2, 1, 1)

            self.menus.addWidget(self.crafting_methods_menu)
            self.menu_2 = QWidget()
            self.menu_2.setObjectName(u"menu_2")
            self.verticalLayout_2 = QVBoxLayout(self.menu_2)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.method_fossil_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group = QButtonGroup(RightColumn)
            self.advanced_crafting_method_btn_group.setObjectName(u"advanced_crafting_method_btn_group")
            self.advanced_crafting_method_btn_group.addButton(self.method_fossil_btn)
            self.method_fossil_btn.setObjectName(u"method_fossil_btn")
            sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            sizePolicy1.setHorizontalStretch(0)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.method_fossil_btn.sizePolicy().hasHeightForWidth())
            self.method_fossil_btn.setSizePolicy(sizePolicy1)
            self.method_fossil_btn.setMinimumSize(QSize(0, 0))
            self.method_fossil_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_fossil_btn.setMouseTracking(True)
            self.method_fossil_btn.setStyleSheet(u"QPushButton {\n"
                                                 "                border: 1px solid #000;\n"
                                                 "                border-radius: 4px;\n"
                                                 "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                 "                border-image: none;\n"
                                                 "              color: #FFF;\n"
                                                 "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "                font-family: Open Sans;\n"
                                                 "                font-size: 12px;\n"
                                                 "               font-weight: bold;\n"
                                                 "               height: 36px;\n"
                                                 "                line-height: 36px;\n"
                                                 "                text-align: center;\n"
                                                 "				margin: 0px;\n"
                                                 "				padding: 5px 10px;\n"
                                                 "				cursor: pointer;\n"
                                                 "				text-shadow: 1px 1px #000;\n"
                                                 "				vertical-align: top;\n"
                                                 "           }\n"
                                                 "            QPushButton::hover {         \n"
                                                 "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                 "           }\n"
                                                 "            QPushButton::pressed {\n"
                                                 "                \n"
                                                 "	background-color: qlinear"
                                                 "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                 "            }\n"
                                                 "			QPushButton::checked {\n"
                                                 "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                 "				color: #332211;\n"
                                                 "text-shadow: 1px 1px #FFF;\n"
                                                 "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                 "font-weight: bold;\n"
                                                 "			}\n"
                                                 "            QPushButton::flat {\n"
                                                 "                border: none;\n"
                                                 "}")
            icon21 = QIcon()
            icon21.addFile(u":/crafting_methods/images/crafting_methods/method_fossil.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_fossil_btn.setIcon(icon21)
            self.method_fossil_btn.setIconSize(QSize(30, 30))
            self.method_fossil_btn.setCheckable(True)
            self.method_fossil_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_fossil_btn)

            self.method_harvest_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.method_harvest_btn)
            self.method_harvest_btn.setObjectName(u"method_harvest_btn")
            sizePolicy1.setHeightForWidth(self.method_harvest_btn.sizePolicy().hasHeightForWidth())
            self.method_harvest_btn.setSizePolicy(sizePolicy1)
            self.method_harvest_btn.setMinimumSize(QSize(0, 0))
            self.method_harvest_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_harvest_btn.setMouseTracking(True)
            self.method_harvest_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "				padding: 5px 10px;\n"
                                                  "				cursor: pointer;\n"
                                                  "				text-shadow: 1px 1px #000;\n"
                                                  "				vertical-align: top;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {         \n"
                                                  "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                \n"
                                                  "	background-color: qlinear"
                                                  "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "            }\n"
                                                  "			QPushButton::checked {\n"
                                                  "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon22 = QIcon()
            icon22.addFile(u":/crafting_methods/images/crafting_methods/method_harvest.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_harvest_btn.setIcon(icon22)
            self.method_harvest_btn.setIconSize(QSize(30, 30))
            self.method_harvest_btn.setCheckable(True)
            self.method_harvest_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_harvest_btn)

            self.method_essence_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.method_essence_btn)
            self.method_essence_btn.setObjectName(u"method_essence_btn")
            sizePolicy1.setHeightForWidth(self.method_essence_btn.sizePolicy().hasHeightForWidth())
            self.method_essence_btn.setSizePolicy(sizePolicy1)
            self.method_essence_btn.setMinimumSize(QSize(0, 0))
            self.method_essence_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_essence_btn.setMouseTracking(True)
            self.method_essence_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "				padding: 5px 10px;\n"
                                                  "				cursor: pointer;\n"
                                                  "				text-shadow: 1px 1px #000;\n"
                                                  "				vertical-align: top;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {         \n"
                                                  "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                \n"
                                                  "	background-color: qlinear"
                                                  "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "            }\n"
                                                  "			QPushButton::checked {\n"
                                                  "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon23 = QIcon()
            icon23.addFile(u":/crafting_methods/images/crafting_methods/method_essence.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_essence_btn.setIcon(icon23)
            self.method_essence_btn.setIconSize(QSize(30, 30))
            self.method_essence_btn.setCheckable(True)
            self.method_essence_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_essence_btn)

            self.method_syndicate_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.method_syndicate_btn)
            self.method_syndicate_btn.setObjectName(u"method_syndicate_btn")
            sizePolicy1.setHeightForWidth(self.method_syndicate_btn.sizePolicy().hasHeightForWidth())
            self.method_syndicate_btn.setSizePolicy(sizePolicy1)
            self.method_syndicate_btn.setMinimumSize(QSize(0, 0))
            self.method_syndicate_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_syndicate_btn.setMouseTracking(True)
            self.method_syndicate_btn.setStyleSheet(u"QPushButton {\n"
                                                    "                border: 1px solid #000;\n"
                                                    "                border-radius: 4px;\n"
                                                    "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                    "                border-image: none;\n"
                                                    "              color: #FFF;\n"
                                                    "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                    "                font-family: Open Sans;\n"
                                                    "                font-size: 12px;\n"
                                                    "               font-weight: bold;\n"
                                                    "               height: 36px;\n"
                                                    "                line-height: 36px;\n"
                                                    "                text-align: center;\n"
                                                    "				margin: 0px;\n"
                                                    "				padding: 5px 10px;\n"
                                                    "				cursor: pointer;\n"
                                                    "				text-shadow: 1px 1px #000;\n"
                                                    "				vertical-align: top;\n"
                                                    "           }\n"
                                                    "            QPushButton::hover {         \n"
                                                    "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                    "           }\n"
                                                    "            QPushButton::pressed {\n"
                                                    "                \n"
                                                    "	background-color: qlinear"
                                                    "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                    "            }\n"
                                                    "			QPushButton::checked {\n"
                                                    "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                    "				color: #332211;\n"
                                                    "text-shadow: 1px 1px #FFF;\n"
                                                    "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                    "font-weight: bold;\n"
                                                    "			}\n"
                                                    "            QPushButton::flat {\n"
                                                    "                border: none;\n"
                                                    "}")
            icon24 = QIcon()
            icon24.addFile(u":/crafting_methods/images/crafting_methods/method_syndicate.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_syndicate_btn.setIcon(icon24)
            self.method_syndicate_btn.setIconSize(QSize(30, 30))
            self.method_syndicate_btn.setCheckable(True)
            self.method_syndicate_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_syndicate_btn)

            self.eldritch_method_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.eldritch_method_btn)
            self.eldritch_method_btn.setObjectName(u"eldritch_method_btn")
            sizePolicy1.setHeightForWidth(self.eldritch_method_btn.sizePolicy().hasHeightForWidth())
            self.eldritch_method_btn.setSizePolicy(sizePolicy1)
            self.eldritch_method_btn.setMinimumSize(QSize(0, 0))
            self.eldritch_method_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.eldritch_method_btn.setMouseTracking(True)
            self.eldritch_method_btn.setStyleSheet(u"QPushButton {\n"
                                                   "                border: 1px solid #000;\n"
                                                   "                border-radius: 4px;\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                   "                border-image: none;\n"
                                                   "              color: #FFF;\n"
                                                   "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "                font-family: Open Sans;\n"
                                                   "                font-size: 12px;\n"
                                                   "               font-weight: bold;\n"
                                                   "               height: 36px;\n"
                                                   "                line-height: 36px;\n"
                                                   "                text-align: center;\n"
                                                   "				margin: 0px;\n"
                                                   "				padding: 5px 10px;\n"
                                                   "				cursor: pointer;\n"
                                                   "				text-shadow: 1px 1px #000;\n"
                                                   "				vertical-align: top;\n"
                                                   "           }\n"
                                                   "            QPushButton::hover {         \n"
                                                   "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                   "           }\n"
                                                   "            QPushButton::pressed {\n"
                                                   "                \n"
                                                   "	background-color: qlinear"
                                                   "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "            }\n"
                                                   "			QPushButton::checked {\n"
                                                   "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "				color: #332211;\n"
                                                   "text-shadow: 1px 1px #FFF;\n"
                                                   "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "font-weight: bold;\n"
                                                   "			}\n"
                                                   "            QPushButton::flat {\n"
                                                   "                border: none;\n"
                                                   "}")
            icon25 = QIcon()
            icon25.addFile(u":/crafting_methods/images/crafting_methods/method_eldritch.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.eldritch_method_btn.setIcon(icon25)
            self.eldritch_method_btn.setIconSize(QSize(30, 30))
            self.eldritch_method_btn.setCheckable(True)
            self.eldritch_method_btn.setChecked(False)
            self.eldritch_method_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.eldritch_method_btn)

            self.method_crafting_bench_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.method_crafting_bench_btn)
            self.method_crafting_bench_btn.setObjectName(u"method_crafting_bench_btn")
            sizePolicy1.setHeightForWidth(self.method_crafting_bench_btn.sizePolicy().hasHeightForWidth())
            self.method_crafting_bench_btn.setSizePolicy(sizePolicy1)
            self.method_crafting_bench_btn.setMinimumSize(QSize(0, 0))
            self.method_crafting_bench_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_crafting_bench_btn.setMouseTracking(True)
            self.method_crafting_bench_btn.setStyleSheet(u"QPushButton {\n"
                                                         "                border: 1px solid #000;\n"
                                                         "                border-radius: 4px;\n"
                                                         "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                         "                border-image: none;\n"
                                                         "              color: #FFF;\n"
                                                         "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                         "                font-family: Open Sans;\n"
                                                         "                font-size: 12px;\n"
                                                         "               font-weight: bold;\n"
                                                         "               height: 36px;\n"
                                                         "                line-height: 36px;\n"
                                                         "                text-align: center;\n"
                                                         "				margin: 0px;\n"
                                                         "				padding: 5px 10px;\n"
                                                         "				cursor: pointer;\n"
                                                         "				text-shadow: 1px 1px #000;\n"
                                                         "				vertical-align: top;\n"
                                                         "           }\n"
                                                         "            QPushButton::hover {         \n"
                                                         "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                         "           }\n"
                                                         "            QPushButton::pressed {\n"
                                                         "                \n"
                                                         "	background-color: qlinear"
                                                         "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                         "            }\n"
                                                         "			QPushButton::checked {\n"
                                                         "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                         "				color: #332211;\n"
                                                         "text-shadow: 1px 1px #FFF;\n"
                                                         "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                         "font-weight: bold;\n"
                                                         "			}\n"
                                                         "            QPushButton::flat {\n"
                                                         "                border: none;\n"
                                                         "}")
            icon26 = QIcon()
            icon26.addFile(u":/crafting_methods/images/crafting_methods/method_crafting_bench.png", QSize(),
                           QIcon.Normal, QIcon.Off)
            self.method_crafting_bench_btn.setIcon(icon26)
            self.method_crafting_bench_btn.setIconSize(QSize(30, 30))
            self.method_crafting_bench_btn.setCheckable(True)
            self.method_crafting_bench_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_crafting_bench_btn)

            self.method_imprint_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.method_imprint_btn)
            self.method_imprint_btn.setObjectName(u"method_imprint_btn")
            sizePolicy1.setHeightForWidth(self.method_imprint_btn.sizePolicy().hasHeightForWidth())
            self.method_imprint_btn.setSizePolicy(sizePolicy1)
            self.method_imprint_btn.setMinimumSize(QSize(0, 0))
            self.method_imprint_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.method_imprint_btn.setMouseTracking(True)
            self.method_imprint_btn.setStyleSheet(u"QPushButton {\n"
                                                  "                border: 1px solid #000;\n"
                                                  "                border-radius: 4px;\n"
                                                  "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                  "                border-image: none;\n"
                                                  "              color: #FFF;\n"
                                                  "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "                font-family: Open Sans;\n"
                                                  "                font-size: 12px;\n"
                                                  "               font-weight: bold;\n"
                                                  "               height: 36px;\n"
                                                  "                line-height: 36px;\n"
                                                  "                text-align: center;\n"
                                                  "				margin: 0px;\n"
                                                  "				padding: 5px 10px;\n"
                                                  "				cursor: pointer;\n"
                                                  "				text-shadow: 1px 1px #000;\n"
                                                  "				vertical-align: top;\n"
                                                  "           }\n"
                                                  "            QPushButton::hover {         \n"
                                                  "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                  "           }\n"
                                                  "            QPushButton::pressed {\n"
                                                  "                \n"
                                                  "	background-color: qlinear"
                                                  "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "            }\n"
                                                  "			QPushButton::checked {\n"
                                                  "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                  "				color: #332211;\n"
                                                  "text-shadow: 1px 1px #FFF;\n"
                                                  "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                  "font-weight: bold;\n"
                                                  "			}\n"
                                                  "            QPushButton::flat {\n"
                                                  "                border: none;\n"
                                                  "}")
            icon27 = QIcon()
            icon27.addFile(u":/crafting_methods/images/crafting_methods/method_imprint.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.method_imprint_btn.setIcon(icon27)
            self.method_imprint_btn.setIconSize(QSize(30, 30))
            self.method_imprint_btn.setCheckable(True)
            self.method_imprint_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.method_imprint_btn)

            self.catalyst_method_btn = QPushButton(self.menu_2)
            self.advanced_crafting_method_btn_group.addButton(self.catalyst_method_btn)
            self.catalyst_method_btn.setObjectName(u"catalyst_method_btn")
            sizePolicy1.setHeightForWidth(self.catalyst_method_btn.sizePolicy().hasHeightForWidth())
            self.catalyst_method_btn.setSizePolicy(sizePolicy1)
            self.catalyst_method_btn.setMinimumSize(QSize(0, 0))
            self.catalyst_method_btn.setCursor(QCursor(Qt.PointingHandCursor))
            self.catalyst_method_btn.setMouseTracking(True)
            self.catalyst_method_btn.setStyleSheet(u"QPushButton {\n"
                                                   "                border: 1px solid #000;\n"
                                                   "                border-radius: 4px;\n"
                                                   "                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
                                                   "                border-image: none;\n"
                                                   "              color: #FFF;\n"
                                                   "               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "                font-family: Open Sans;\n"
                                                   "                font-size: 12px;\n"
                                                   "               font-weight: bold;\n"
                                                   "               height: 36px;\n"
                                                   "                line-height: 36px;\n"
                                                   "                text-align: center;\n"
                                                   "				margin: 0px;\n"
                                                   "				padding: 5px 10px;\n"
                                                   "				cursor: pointer;\n"
                                                   "				text-shadow: 1px 1px #000;\n"
                                                   "				vertical-align: top;\n"
                                                   "           }\n"
                                                   "            QPushButton::hover {         \n"
                                                   "	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
                                                   "           }\n"
                                                   "            QPushButton::pressed {\n"
                                                   "                \n"
                                                   "	background-color: qlinear"
                                                   "gradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "            }\n"
                                                   "			QPushButton::checked {\n"
                                                   "				background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
                                                   "				color: #332211;\n"
                                                   "text-shadow: 1px 1px #FFF;\n"
                                                   "box-shadow: inset 0 1px 1px #BBB, 0 1px 2px rgba(0,0,0,0.31);\n"
                                                   "font-weight: bold;\n"
                                                   "			}\n"
                                                   "            QPushButton::flat {\n"
                                                   "                border: none;\n"
                                                   "}")
            icon28 = QIcon()
            icon28.addFile(u":/crafting_methods/images/crafting_methods/method_catalyst.png", QSize(), QIcon.Normal,
                           QIcon.Off)
            self.catalyst_method_btn.setIcon(icon28)
            self.catalyst_method_btn.setIconSize(QSize(30, 30))
            self.catalyst_method_btn.setCheckable(True)
            self.catalyst_method_btn.setAutoExclusive(True)

            self.verticalLayout_2.addWidget(self.catalyst_method_btn)

            self.menus.addWidget(self.menu_2)
            self.menu_3 = QWidget()
            self.menu_3.setObjectName(u"menu_3")
            self.menus.addWidget(self.menu_3)
            self.menu_4 = QWidget()
            self.menu_4.setObjectName(u"menu_4")
            self.menus.addWidget(self.menu_4)

            self.verticalLayout.addWidget(self.menus)

            self.right_column_btns = QWidget(RightColumn)
            self.right_column_btns.setObjectName(u"right_column_btns")
            sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            sizePolicy2.setHorizontalStretch(0)
            sizePolicy2.setVerticalStretch(0)
            sizePolicy2.setHeightForWidth(self.right_column_btns.sizePolicy().hasHeightForWidth())
            self.right_column_btns.setSizePolicy(sizePolicy2)
            self.right_column_btns.setMinimumSize(QSize(0, 50))
            self.horizontalLayout = QHBoxLayout(self.right_column_btns)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.btn_2 = QWidget(self.right_column_btns)
            self.btn_2.setObjectName(u"btn_2")
            sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
            self.btn_2.setSizePolicy(sizePolicy1)
            self.verticalLayout_3 = QVBoxLayout(self.btn_2)
            self.verticalLayout_3.setSpacing(0)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
            self.btn_2_layout = QHBoxLayout()
            self.btn_2_layout.setObjectName(u"btn_2_layout")

            self.verticalLayout_3.addLayout(self.btn_2_layout)

            self.horizontalLayout.addWidget(self.btn_2)

            self.btn_1 = QWidget(self.right_column_btns)
            self.btn_1.setObjectName(u"btn_1")
            sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
            self.btn_1.setSizePolicy(sizePolicy1)
            self.verticalLayout_4 = QVBoxLayout(self.btn_1)
            self.verticalLayout_4.setSpacing(0)
            self.verticalLayout_4.setObjectName(u"verticalLayout_4")
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.btn_1_layout = QHBoxLayout()
            self.btn_1_layout.setObjectName(u"btn_1_layout")

            self.verticalLayout_4.addLayout(self.btn_1_layout)

            self.horizontalLayout.addWidget(self.btn_1)

            self.verticalLayout.addWidget(self.right_column_btns)

            self.retranslateUi(RightColumn)

            self.menus.setCurrentIndex(1)

            QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
            RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
            # if QT_CONFIG(tooltip)
            self.method_transmute_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Upgrades a Normal Item to a Magic Item</span></p></body></html>",
                                                                            None))
            # endif // QT_CONFIG(tooltip)
            self.method_transmute_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_alteration_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Reforges a Magic Item with new random properties</span></p></body></html>",
                                                                             None))
            # endif // QT_CONFIG(tooltip)
            self.method_alteration_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_augmentation_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                               u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Magic Item with a new random property</span></p></body></html>",
                                                                               None))
            # endif // QT_CONFIG(tooltip)
            self.method_augmentation_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_regal_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Upgrades a Magic Item to a Rare Item</span></p></body></html>",
                                                                        None))
            # endif // QT_CONFIG(tooltip)
            self.method_regal_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_alchemy_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Upgrades a Normal Item to a Rare Item</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_alchemy_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_chaos_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Reforges a Rare Item with new random modifiers</span></p></body></html>",
                                                                        None))
            # endif // QT_CONFIG(tooltip)
            self.method_chaos_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_exalted_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Rare Item with a new random property</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_exalted_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_scour_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Removes all properties from an Item</span></p></body></html>",
                                                                        None))
            # endif // QT_CONFIG(tooltip)
            self.method_scour_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_annul_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Removes a random modifier from an Item</span></p></body></html>",
                                                                        None))
            # endif // QT_CONFIG(tooltip)
            self.method_annul_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_crusader_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Rare Item with a new Crusader modifier</span></p></body></html>",
                                                                           None))
            # endif // QT_CONFIG(tooltip)
            self.method_crusader_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_hunter_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Rare Item with a new Hunter modifier</span></p></body></html>",
                                                                         None))
            # endif // QT_CONFIG(tooltip)
            self.method_hunter_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_redeemer_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Rare Item with a new Redeemer modifier</span></p></body></html>",
                                                                           None))
            # endif // QT_CONFIG(tooltip)
            self.method_redeemer_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_warlord_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Enchants a Rare Item with a new Warlord modifier</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_warlord_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_blessed_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Randomises the numeric values of the Implicit properties of an Item</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_blessed_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_divine_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Randomises the numeric values of the random properties on an Item</span></p></body></html>",
                                                                         None))
            # endif // QT_CONFIG(tooltip)
            self.method_divine_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_veiled_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Reforges a Rare Item with new random modifiers, including a Veiled modifier</span></p><p align=\"center\"><span style=\" font-size:14pt;\"><br/></span></p></body></html>",
                                                                         None))
            # endif // QT_CONFIG(tooltip)
            self.method_veiled_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_woke_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                       u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Destroys an Item, applying its' Influence to another of the same Item class. The second Item is reforged as a Rare Item with both Influence types and new modifiers </span></p></body></html>",
                                                                       None))
            # endif // QT_CONFIG(tooltip)
            self.method_woke_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_maven_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Removes one Influenced modifier from an Item with at least two Influenced modifiers and upgrades another Influenced modifier</span></p></body></html>",
                                                                        None))
            # endif // QT_CONFIG(tooltip)
            self.method_maven_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_fracturing_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                             u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Fractures a random modifier on a Rare Item with at least 4 modifiers, locking it in place.</span></p></body></html>",
                                                                             None))
            # endif // QT_CONFIG(tooltip)
            self.method_fracturing_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_double_corrupt_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                                 u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Potently corrupts an Item, modifying it drastically and unpredictably</span></p></body></html>",
                                                                                 None))
            # endif // QT_CONFIG(tooltip)
            self.method_double_corrupt_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_vaal_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                       u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Corrupts an Item, modifying it unpredictably</span></p></body></html>",
                                                                       None))
            # endif // QT_CONFIG(tooltip)
            self.method_vaal_btn.setText("")
            # if QT_CONFIG(tooltip)
            self.method_fossil_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Fossil crafting</span></p></body></html>",
                                                                         None))
            # endif // QT_CONFIG(tooltip)
            self.method_fossil_btn.setText(QCoreApplication.translate("RightColumn", u"Fossil Crafting", None))
            # if QT_CONFIG(tooltip)
            self.method_harvest_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Harvest crafting</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_harvest_btn.setText(QCoreApplication.translate("RightColumn", u"Harvest Crafting", None))
            # if QT_CONFIG(tooltip)
            self.method_essence_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Essences</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_essence_btn.setText(QCoreApplication.translate("RightColumn", u"Essence Crafting", None))
            # if QT_CONFIG(tooltip)
            self.method_syndicate_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Syndicate</span></p></body></html>",
                                                                            None))
            # endif // QT_CONFIG(tooltip)
            self.method_syndicate_btn.setText(QCoreApplication.translate("RightColumn", u"Syndicate Crafts", None))
            # if QT_CONFIG(tooltip)
            self.eldritch_method_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Eldritch crafting</span></p></body></html>",
                                                                           None))
            # endif // QT_CONFIG(tooltip)
            self.eldritch_method_btn.setText(QCoreApplication.translate("RightColumn", u"Eldritch Currency", None))
            # if QT_CONFIG(tooltip)
            self.method_crafting_bench_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                                 u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Vendor recipes</span></p></body></html>",
                                                                                 None))
            # endif // QT_CONFIG(tooltip)
            self.method_crafting_bench_btn.setText(QCoreApplication.translate("RightColumn", u"Crafting Bench", None))
            # if QT_CONFIG(tooltip)
            self.method_imprint_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Beast crafting</span></p></body></html>",
                                                                          None))
            # endif // QT_CONFIG(tooltip)
            self.method_imprint_btn.setText(QCoreApplication.translate("RightColumn", u"Beast Crafting", None))
            # if QT_CONFIG(tooltip)
            self.catalyst_method_btn.setToolTip(QCoreApplication.translate("RightColumn",
                                                                           u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#8787fe;\">Catalysts</span></p></body></html>",
                                                                           None))
            # endif // QT_CONFIG(tooltip)
            self.catalyst_method_btn.setText(QCoreApplication.translate("RightColumn", u"Catalysts", None))
    # retranslateUi

