# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnfCSkxm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
                               QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
                               QWidget)
from ...assets import assets_rc


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(206, 662)
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
        self.widget = QWidget(self.menu_2)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_3.addWidget(self.comboBox_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_3.addWidget(self.comboBox_3)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.menu_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(100)

        self.verticalLayout_4.addWidget(self.spinBox)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.widget_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(30)

        self.verticalLayout_4.addWidget(self.spinBox_2)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.menu_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.item_influences_label = QLabel(self.widget_3)
        self.item_influences_label.setObjectName(u"item_influences_label")
        sizePolicy.setHeightForWidth(self.item_influences_label.sizePolicy().hasHeightForWidth())
        self.item_influences_label.setSizePolicy(sizePolicy)
        self.item_influences_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.item_influences_label)

        self.crusader_btn = QPushButton(self.widget_3)
        self.crusader_btn.setObjectName(u"crusader_btn")
        self.crusader_btn.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/influences/images/influences/crusader_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crusader_btn.setIcon(icon)

        self.verticalLayout_5.addWidget(self.crusader_btn)

        self.elder_btn = QPushButton(self.widget_3)
        self.elder_btn.setObjectName(u"elder_btn")
        self.elder_btn.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/influences/images/influences/elder_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.elder_btn.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.elder_btn)

        self.hunter_btn = QPushButton(self.widget_3)
        self.hunter_btn.setObjectName(u"hunter_btn")
        self.hunter_btn.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/influences/images/influences/hunter_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hunter_btn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.hunter_btn)

        self.redeemer_btn = QPushButton(self.widget_3)
        self.redeemer_btn.setObjectName(u"redeemer_btn")
        self.redeemer_btn.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/influences/images/influences/redeemer_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemer_btn.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.redeemer_btn)

        self.shaper_btn = QPushButton(self.widget_3)
        self.shaper_btn.setObjectName(u"shaper_btn")
        self.shaper_btn.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/influences/images/influences/shaper_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shaper_btn.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.shaper_btn)

        self.warlord_btn = QPushButton(self.widget_3)
        self.warlord_btn.setObjectName(u"warlord_btn")
        self.warlord_btn.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/influences/images/influences/warlord_influence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.warlord_btn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.warlord_btn)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

        # if QT_CONFIG(shortcut)
        self.label.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.comboBox_2)
        self.label_5.setBuddy(self.comboBox_3)
        self.label_2.setBuddy(self.spinBox)
        self.label_3.setBuddy(self.spinBox_2)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(LeftColumn)

    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Menu 1 - Left Menu", None))
        self.label.setText(QCoreApplication.translate("LeftColumn", u"Base Group", None))
        self.label_4.setText(QCoreApplication.translate("LeftColumn", u"Base", None))
        self.label_5.setText(QCoreApplication.translate("LeftColumn", u"Base Item", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Item Level (0-100)", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"Item Quality (0-30)", None))
        self.item_influences_label.setText(QCoreApplication.translate("LeftColumn", u"Set Item Influences (0-2)", None))
        self.crusader_btn.setText(QCoreApplication.translate("LeftColumn", u"Crusader", None))
        self.elder_btn.setText(QCoreApplication.translate("LeftColumn", u"Elder", None))
        self.hunter_btn.setText(QCoreApplication.translate("LeftColumn", u"Hunter", None))
        self.redeemer_btn.setText(QCoreApplication.translate("LeftColumn", u"Redeemer", None))
        self.shaper_btn.setText(QCoreApplication.translate("LeftColumn", u"Shaper", None))
        self.warlord_btn.setText(QCoreApplication.translate("LeftColumn", u"Warlord", None))
    # retranslateUi
