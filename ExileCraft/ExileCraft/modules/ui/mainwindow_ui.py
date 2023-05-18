# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)

from .pages.base_selection import BaseSelection
from ..ui.customcursorbutton import CustomCursorButton
from ..ui.customtreeview import CustomTreeView
from .pages.item_selection import ItemSelection
from ..ui import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1239, 714)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(2560, 1440))
        font = QFont()
        font.setFamilies([u"fontin-smallcaps"])
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/icons/assets/images/vendor.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setToolTipDuration(0)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-blend-mode: overlay;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"QLineEdit {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"border-image: none;\n"
"}\n"
"QToolBox {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"border-image: none;\n"
"}\n"
"QGroupBox {\n"
"    border:0px ridge #8f8f91;\n"
"    border-radius: 0px;\n"
"	background-blend-mode: overlay;\n"
"	border-image: none;\n"
"}\n"
"QLabel {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"border-im"
                        "age: none;\n"
"}\n"
"QStackedWidget {\n"
"    border: 0px;\n"
"    border-radius: 0px;\n"
"	background-blend-mode: overlay;\n"
"	border-image: none;\n"
"}\n"
"\n"
"QToolTip {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"border-image: none;\n"
"}\n"
"QPushButton {\n"
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
"               "
                        "    border-left-color: rgb(0, 0, 0);\n"
"                  border-image-source: initial;\n"
"                  border-image-slice: initial;\n"
"                  border-image-width: initial;\n"
"                  border-image-outset: initial;\n"
"                border-image-repeat: initial;\n"
"                border-radius: 4px;\n"
"                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
"                border-image: none;\n"
"              color: #FFF;\n"
"               text-shadow: 1px 1px #000;\n"
"               box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);\n"
"               padding: 0px 10px;\n"
"                margin: 7px;\n"
"                font-family: Open Sans;\n"
"                font-size: 16px;\n"
"               font-weight: bold;\n"
"               height: 36px;\n"
"                line-height: 36px;\n"
"                text-align: center;\n"
"           }\n"
"            QPushButton::hover {\n"
"                b"
                        "ackground-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"           }\n"
"            QPushButton::pressed {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.actionStartOver = QAction(MainWindow)
        self.actionStartOver.setObjectName(u"actionStartOver")
        self.actionPOEDB_TW = QAction(MainWindow)
        self.actionPOEDB_TW.setObjectName(u"actionPOEDB_TW")
        self.actionPrice_Checker = QAction(MainWindow)
        self.actionPrice_Checker.setObjectName(u"actionPrice_Checker")
        self.actionPOE_NINJA = QAction(MainWindow)
        self.actionPOE_NINJA.setObjectName(u"actionPOE_NINJA")
        self.actionPATHOFEXILE_COM_TRADE = QAction(MainWindow)
        self.actionPATHOFEXILE_COM_TRADE.setObjectName(u"actionPATHOFEXILE_COM_TRADE")
        self.actionUI = QAction(MainWindow)
        self.actionUI.setObjectName(u"actionUI")
        self.actionTrade = QAction(MainWindow)
        self.actionTrade.setObjectName(u"actionTrade")
        self.actionCrafting = QAction(MainWindow)
        self.actionCrafting.setObjectName(u"actionCrafting")
        self.actionCrafting_Tutorials = QAction(MainWindow)
        self.actionCrafting_Tutorials.setObjectName(u"actionCrafting_Tutorials")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon1 = QIcon()
        icon1.addFile(u"assets/images/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon1)
        self.crafting_simulator_container = QWidget(MainWindow)
        self.crafting_simulator_container.setObjectName(u"crafting_simulator_container")
        self.crafting_simulator_container.setEnabled(True)
        sizePolicy.setHeightForWidth(self.crafting_simulator_container.sizePolicy().hasHeightForWidth())
        self.crafting_simulator_container.setSizePolicy(sizePolicy)
        self.crafting_simulator_container.setMaximumSize(QSize(2560, 1440))
        font1 = QFont()
        font1.setFamilies([u"fontin-smallcaps"])
        self.crafting_simulator_container.setFont(font1)
        self.crafting_simulator_container.setMouseTracking(True)
        self.crafting_simulator_container.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.crafting_simulator_container)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.crafting_simulator = QStackedWidget(self.crafting_simulator_container)
        self.crafting_simulator.setObjectName(u"crafting_simulator")
        sizePolicy.setHeightForWidth(self.crafting_simulator.sizePolicy().hasHeightForWidth())
        self.crafting_simulator.setSizePolicy(sizePolicy)
        self.crafting_simulator.setMinimumSize(QSize(0, 0))
        self.crafting_simulator.setMaximumSize(QSize(2560, 1440))
        self.crafting_simulator.setMouseTracking(True)
        self.crafting_simulator.setAutoFillBackground(False)
        self.landing_page = QWidget()
        self.landing_page.setObjectName(u"landing_page")
        sizePolicy.setHeightForWidth(self.landing_page.sizePolicy().hasHeightForWidth())
        self.landing_page.setSizePolicy(sizePolicy)
        self.landing_page.setStyleSheet(u"QWidget {\n"
"border: 0px;\n"
"border-image: url(:/icons/assets/images/emubg.png);\n"
"}\n"
"QLabel {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"}\n"
"QPushButton {\n"
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
"    "
                        "              border-image-slice: initial;\n"
"                  border-image-width: initial;\n"
"                  border-image-outset: initial;\n"
"                border-image-repeat: initial;\n"
"                border-radius: 4px;\n"
"                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
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
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);"
                        "\n"
"           }\n"
"            QPushButton::pressed {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.landing_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.landing_page_container = QWidget(self.landing_page)
        self.landing_page_container.setObjectName(u"landing_page_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.landing_page_container.sizePolicy().hasHeightForWidth())
        self.landing_page_container.setSizePolicy(sizePolicy1)
        self.landing_page_container.setStyleSheet(u"border-image: none;")
        self.verticalLayout_11 = QVBoxLayout(self.landing_page_container)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.landing_page_container)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QWidget {\n"
"	border-image: none;\n"
"	border: 0px;\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.label, 0, Qt.AlignTop)

        self.startCraftingProject = QPushButton(self.landing_page_container)
        self.startCraftingProject.setObjectName(u"startCraftingProject")
        sizePolicy.setHeightForWidth(self.startCraftingProject.sizePolicy().hasHeightForWidth())
        self.startCraftingProject.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.startCraftingProject, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.loadSavedProject = QPushButton(self.landing_page_container)
        self.loadSavedProject.setObjectName(u"loadSavedProject")

        self.verticalLayout_11.addWidget(self.loadSavedProject, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.importItemFromPOE = QPushButton(self.landing_page_container)
        self.importItemFromPOE.setObjectName(u"importItemFromPOE")
        sizePolicy.setHeightForWidth(self.importItemFromPOE.sizePolicy().hasHeightForWidth())
        self.importItemFromPOE.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.importItemFromPOE, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.landing_page_container, 0, Qt.AlignTop)

        self.crafting_simulator.addWidget(self.landing_page)
        self.base_groups_page = QWidget()
        self.base_groups_page.setObjectName(u"base_groups_page")
        sizePolicy.setHeightForWidth(self.base_groups_page.sizePolicy().hasHeightForWidth())
        self.base_groups_page.setSizePolicy(sizePolicy)
        self.base_groups_page.setMaximumSize(QSize(2560, 1440))
        self.base_groups_page.setStyleSheet(u"QWidget {\n"
"border: 0px;\n"
"border-image: url(:/icons/assets/images/emubg.png);\n"
"}\n"
"\n"
"QLabel {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.base_groups_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.base_groups_container = QWidget(self.base_groups_page)
        self.base_groups_container.setObjectName(u"base_groups_container")
        sizePolicy.setHeightForWidth(self.base_groups_container.sizePolicy().hasHeightForWidth())
        self.base_groups_container.setSizePolicy(sizePolicy)
        self.base_groups_container.setMinimumSize(QSize(0, 0))
        self.base_groups_container.setMaximumSize(QSize(2560, 1440))
        self.base_groups_container.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.base_groups_container)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.base_groups_container)
        self.header.setObjectName(u"header")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy3)
        self.header.setStyleSheet(u"QWidget {\n"
"	border-image:none;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.header)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.base_group_label = QLabel(self.header)
        self.base_group_label.setObjectName(u"base_group_label")
        sizePolicy.setHeightForWidth(self.base_group_label.sizePolicy().hasHeightForWidth())
        self.base_group_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Open Sans"])
        self.base_group_label.setFont(font3)
        self.base_group_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.base_group_label, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.header)

        self.base_group_btns = QWidget(self.base_groups_container)
        self.base_group_btns.setObjectName(u"base_group_btns")
        self.base_group_btns.setStyleSheet(u"QWidget {\n"
"border-image: none;\n"
"}\n"
"QPushButton {\n"
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
"              "
                        "  background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
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
"			Q"
                        "PushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 5px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.base_group_btns)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.one_handed_weapons_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group = QButtonGroup(MainWindow)
        self.base_group_btns_group.setObjectName(u"base_group_btns_group")
        self.base_group_btns_group.addButton(self.one_handed_weapons_btn)
        self.one_handed_weapons_btn.setObjectName(u"one_handed_weapons_btn")

        self.gridLayout_9.addWidget(self.one_handed_weapons_btn, 1, 2, 1, 1)

        self.body_armours_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.body_armours_btn)
        self.body_armours_btn.setObjectName(u"body_armours_btn")

        self.gridLayout_9.addWidget(self.body_armours_btn, 0, 0, 1, 1)

        self.two_handed_weapons_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.two_handed_weapons_btn)
        self.two_handed_weapons_btn.setObjectName(u"two_handed_weapons_btn")

        self.gridLayout_9.addWidget(self.two_handed_weapons_btn, 2, 0, 1, 1)

        self.gloves_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.gloves_btn)
        self.gloves_btn.setObjectName(u"gloves_btn")

        self.gridLayout_9.addWidget(self.gloves_btn, 0, 2, 1, 1)

        self.offhands_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.offhands_btn)
        self.offhands_btn.setObjectName(u"offhands_btn")

        self.gridLayout_9.addWidget(self.offhands_btn, 2, 1, 1, 1)

        self.boots_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.boots_btn)
        self.boots_btn.setObjectName(u"boots_btn")

        self.gridLayout_9.addWidget(self.boots_btn, 0, 1, 1, 1)

        self.jewels_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.jewels_btn)
        self.jewels_btn.setObjectName(u"jewels_btn")

        self.gridLayout_9.addWidget(self.jewels_btn, 2, 2, 1, 1)

        self.cluster_jewels_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.cluster_jewels_btn)
        self.cluster_jewels_btn.setObjectName(u"cluster_jewels_btn")

        self.gridLayout_9.addWidget(self.cluster_jewels_btn, 3, 0, 1, 1)

        self.helmets_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.helmets_btn)
        self.helmets_btn.setObjectName(u"helmets_btn")

        self.gridLayout_9.addWidget(self.helmets_btn, 1, 0, 1, 1)

        self.jewellery_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.jewellery_btn)
        self.jewellery_btn.setObjectName(u"jewellery_btn")

        self.gridLayout_9.addWidget(self.jewellery_btn, 1, 1, 1, 1)

        self.flasks_btn = QPushButton(self.base_group_btns)
        self.base_group_btns_group.addButton(self.flasks_btn)
        self.flasks_btn.setObjectName(u"flasks_btn")

        self.gridLayout_9.addWidget(self.flasks_btn, 3, 2, 1, 1)


        self.verticalLayout_12.addWidget(self.base_group_btns, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.base_groups_container)

        self.crafting_simulator.addWidget(self.base_groups_page)
        self.base_selection_page = BaseSelection()
        self.base_selection_page.setObjectName(u"base_selection_page")
        self.base_selection_page.setStyleSheet(u"QWidget {\n"
"	border-image: url(:/icons/assets/images/emubg.png);\n"
"}")
        self.crafting_simulator.addWidget(self.base_selection_page)
        self.item_selection_page = ItemSelection()
        self.item_selection_page.setObjectName(u"item_selection_page")
        self.item_selection_page.setStyleSheet(u"QWidget {\n"
"	border-image: url(:/icons/assets/images/emubg.png);\n"
"}")
        self.crafting_simulator.addWidget(self.item_selection_page)
        self.item_options_page = QWidget()
        self.item_options_page.setObjectName(u"item_options_page")
        sizePolicy1.setHeightForWidth(self.item_options_page.sizePolicy().hasHeightForWidth())
        self.item_options_page.setSizePolicy(sizePolicy1)
        self.item_options_page.setStyleSheet(u"QWidget {\n"
"border: 0px;\n"
"border-image: url(:/icons/assets/images/emubg.png);\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.item_options_page)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.item_options_label_2 = QLabel(self.item_options_page)
        self.item_options_label_2.setObjectName(u"item_options_label_2")
        sizePolicy.setHeightForWidth(self.item_options_label_2.sizePolicy().hasHeightForWidth())
        self.item_options_label_2.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Open Sans"])
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.item_options_label_2.setFont(font4)
        self.item_options_label_2.setStyleSheet(u"QLabel {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 16px;\n"
"background-color: #444;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"border-image: none;\n"
"}")
        self.item_options_label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_19.addWidget(self.item_options_label_2, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.item_options_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_5)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.item_options_container = QWidget(self.frame_5)
        self.item_options_container.setObjectName(u"item_options_container")
        sizePolicy1.setHeightForWidth(self.item_options_container.sizePolicy().hasHeightForWidth())
        self.item_options_container.setSizePolicy(sizePolicy1)
        self.item_options_container.setMinimumSize(QSize(0, 0))
        self.item_options_container.setMaximumSize(QSize(1677215, 400))
        self.item_options_container.setStyleSheet(u"QWidget {\n"
"border-image: none;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.item_options_container)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.splitter_7 = QSplitter(self.item_options_container)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.influence_options = QWidget(self.splitter_7)
        self.influence_options.setObjectName(u"influence_options")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.influence_options.sizePolicy().hasHeightForWidth())
        self.influence_options.setSizePolicy(sizePolicy4)
        self.influence_options.setMinimumSize(QSize(0, 0))
        self.influence_options.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"fontin-smallcaps"])
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.influence_options.setFont(font5)
        self.influence_options.setStyleSheet(u"QWidget {\n"
"border-image: none;\n"
"border: 0px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.influence_options)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.influence_header_label = QLabel(self.influence_options)
        self.influence_header_label.setObjectName(u"influence_header_label")
        sizePolicy.setHeightForWidth(self.influence_header_label.sizePolicy().hasHeightForWidth())
        self.influence_header_label.setSizePolicy(sizePolicy)
        self.influence_header_label.setMinimumSize(QSize(0, 35))
        self.influence_header_label.setFont(font4)
        self.influence_header_label.setStyleSheet(u"border-radius: 4px;")
        self.influence_header_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.influence_header_label)

        self.influence_buttons = QWidget(self.influence_options)
        self.influence_buttons.setObjectName(u"influence_buttons")
        sizePolicy.setHeightForWidth(self.influence_buttons.sizePolicy().hasHeightForWidth())
        self.influence_buttons.setSizePolicy(sizePolicy)
        self.influence_buttons.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.influence_buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.crusader_btn = QPushButton(self.influence_buttons)
        self.crusader_btn.setObjectName(u"crusader_btn")
        sizePolicy1.setHeightForWidth(self.crusader_btn.sizePolicy().hasHeightForWidth())
        self.crusader_btn.setSizePolicy(sizePolicy1)
        self.crusader_btn.setFont(font2)
        self.crusader_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/images/smlinf_4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crusader_btn.setIcon(icon2)
        self.crusader_btn.setIconSize(QSize(30, 30))
        self.crusader_btn.setCheckable(True)
        self.crusader_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.crusader_btn)

        self.elder_btn = QPushButton(self.influence_buttons)
        self.elder_btn.setObjectName(u"elder_btn")
        sizePolicy1.setHeightForWidth(self.elder_btn.sizePolicy().hasHeightForWidth())
        self.elder_btn.setSizePolicy(sizePolicy1)
        self.elder_btn.setFont(font2)
        self.elder_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/images/smlinf_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.elder_btn.setIcon(icon3)
        self.elder_btn.setIconSize(QSize(30, 30))
        self.elder_btn.setCheckable(True)
        self.elder_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.elder_btn)

        self.hunter_btn = QPushButton(self.influence_buttons)
        self.hunter_btn.setObjectName(u"hunter_btn")
        sizePolicy1.setHeightForWidth(self.hunter_btn.sizePolicy().hasHeightForWidth())
        self.hunter_btn.setSizePolicy(sizePolicy1)
        self.hunter_btn.setFont(font2)
        self.hunter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/images/smlinf_5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hunter_btn.setIcon(icon4)
        self.hunter_btn.setIconSize(QSize(30, 30))
        self.hunter_btn.setCheckable(True)
        self.hunter_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.hunter_btn)

        self.redeemer_btn = QPushButton(self.influence_buttons)
        self.redeemer_btn.setObjectName(u"redeemer_btn")
        sizePolicy1.setHeightForWidth(self.redeemer_btn.sizePolicy().hasHeightForWidth())
        self.redeemer_btn.setSizePolicy(sizePolicy1)
        self.redeemer_btn.setFont(font2)
        self.redeemer_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/images/smlinf_7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemer_btn.setIcon(icon5)
        self.redeemer_btn.setIconSize(QSize(30, 30))
        self.redeemer_btn.setCheckable(True)
        self.redeemer_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.redeemer_btn)

        self.shaper_btn = QPushButton(self.influence_buttons)
        self.shaper_btn.setObjectName(u"shaper_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.shaper_btn.sizePolicy().hasHeightForWidth())
        self.shaper_btn.setSizePolicy(sizePolicy5)
        self.shaper_btn.setFont(font2)
        self.shaper_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/images/smlinf_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shaper_btn.setIcon(icon6)
        self.shaper_btn.setIconSize(QSize(30, 30))
        self.shaper_btn.setCheckable(True)
        self.shaper_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.shaper_btn)

        self.warlord_btn = QPushButton(self.influence_buttons)
        self.warlord_btn.setObjectName(u"warlord_btn")
        sizePolicy1.setHeightForWidth(self.warlord_btn.sizePolicy().hasHeightForWidth())
        self.warlord_btn.setSizePolicy(sizePolicy1)
        self.warlord_btn.setFont(font2)
        self.warlord_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/images/smlinf_6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.warlord_btn.setIcon(icon7)
        self.warlord_btn.setIconSize(QSize(30, 30))
        self.warlord_btn.setCheckable(True)
        self.warlord_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.warlord_btn)


        self.verticalLayout_18.addWidget(self.influence_buttons)

        self.splitter_7.addWidget(self.influence_options)
        self.ilvl_options = QWidget(self.splitter_7)
        self.ilvl_options.setObjectName(u"ilvl_options")
        sizePolicy3.setHeightForWidth(self.ilvl_options.sizePolicy().hasHeightForWidth())
        self.ilvl_options.setSizePolicy(sizePolicy3)
        self.ilvl_options.setStyleSheet(u"QWidget {\n"
"	border: none;\n"
"	border-image: none;\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.ilvl_options)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ilvl_header_label = QLabel(self.ilvl_options)
        self.ilvl_header_label.setObjectName(u"ilvl_header_label")
        sizePolicy.setHeightForWidth(self.ilvl_header_label.sizePolicy().hasHeightForWidth())
        self.ilvl_header_label.setSizePolicy(sizePolicy)
        self.ilvl_header_label.setMinimumSize(QSize(0, 35))
        self.ilvl_header_label.setFont(font4)
        self.ilvl_header_label.setStyleSheet(u"border-radius: 4px;")
        self.ilvl_header_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.ilvl_header_label)

        self.ilvl_buttons = QWidget(self.ilvl_options)
        self.ilvl_buttons.setObjectName(u"ilvl_buttons")
        sizePolicy.setHeightForWidth(self.ilvl_buttons.sizePolicy().hasHeightForWidth())
        self.ilvl_buttons.setSizePolicy(sizePolicy)
        self.ilvl_buttons.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamilies([u"fontin-smallcaps"])
        font6.setPointSize(8)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.ilvl_buttons.setFont(font6)
        self.ilvl_buttons.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.ilvl_buttons)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ilvl_87 = QPushButton(self.ilvl_buttons)
        self.ilvl_87.setObjectName(u"ilvl_87")
        sizePolicy.setHeightForWidth(self.ilvl_87.sizePolicy().hasHeightForWidth())
        self.ilvl_87.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setFamilies([u"Open Sans"])
        font7.setBold(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        self.ilvl_87.setFont(font7)
        self.ilvl_87.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_87.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_87, 3, 11, 1, 1)

        self.ilvl_73 = QPushButton(self.ilvl_buttons)
        self.ilvl_73.setObjectName(u"ilvl_73")
        sizePolicy.setHeightForWidth(self.ilvl_73.sizePolicy().hasHeightForWidth())
        self.ilvl_73.setSizePolicy(sizePolicy)
        self.ilvl_73.setFont(font7)
        self.ilvl_73.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_73.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_73, 2, 22, 1, 1)

        self.ilvl_78 = QPushButton(self.ilvl_buttons)
        self.ilvl_78.setObjectName(u"ilvl_78")
        sizePolicy.setHeightForWidth(self.ilvl_78.sizePolicy().hasHeightForWidth())
        self.ilvl_78.setSizePolicy(sizePolicy)
        self.ilvl_78.setFont(font7)
        self.ilvl_78.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_78.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_78, 3, 2, 1, 1)

        self.ilvl_63 = QPushButton(self.ilvl_buttons)
        self.ilvl_63.setObjectName(u"ilvl_63")
        sizePolicy.setHeightForWidth(self.ilvl_63.sizePolicy().hasHeightForWidth())
        self.ilvl_63.setSizePolicy(sizePolicy)
        self.ilvl_63.setFont(font7)
        self.ilvl_63.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_63.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_63, 2, 12, 1, 1)

        self.ilvl_96 = QPushButton(self.ilvl_buttons)
        self.ilvl_96.setObjectName(u"ilvl_96")
        sizePolicy.setHeightForWidth(self.ilvl_96.sizePolicy().hasHeightForWidth())
        self.ilvl_96.setSizePolicy(sizePolicy)
        self.ilvl_96.setFont(font7)
        self.ilvl_96.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_96.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_96, 3, 20, 1, 1)

        self.ilvl_71 = QPushButton(self.ilvl_buttons)
        self.ilvl_71.setObjectName(u"ilvl_71")
        sizePolicy.setHeightForWidth(self.ilvl_71.sizePolicy().hasHeightForWidth())
        self.ilvl_71.setSizePolicy(sizePolicy)
        self.ilvl_71.setFont(font7)
        self.ilvl_71.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_71.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_71, 2, 20, 1, 1)

        self.ilvl_8 = QPushButton(self.ilvl_buttons)
        self.ilvl_8.setObjectName(u"ilvl_8")
        sizePolicy.setHeightForWidth(self.ilvl_8.sizePolicy().hasHeightForWidth())
        self.ilvl_8.setSizePolicy(sizePolicy)
        self.ilvl_8.setFont(font7)
        self.ilvl_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_8.setIconSize(QSize(30, 30))
        self.ilvl_8.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_8, 0, 7, 1, 1)

        self.ilvl_75 = QPushButton(self.ilvl_buttons)
        self.ilvl_75.setObjectName(u"ilvl_75")
        sizePolicy.setHeightForWidth(self.ilvl_75.sizePolicy().hasHeightForWidth())
        self.ilvl_75.setSizePolicy(sizePolicy)
        self.ilvl_75.setFont(font7)
        self.ilvl_75.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_75.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_75, 2, 24, 1, 1)

        self.ilvl_89 = QPushButton(self.ilvl_buttons)
        self.ilvl_89.setObjectName(u"ilvl_89")
        sizePolicy.setHeightForWidth(self.ilvl_89.sizePolicy().hasHeightForWidth())
        self.ilvl_89.setSizePolicy(sizePolicy)
        self.ilvl_89.setFont(font7)
        self.ilvl_89.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_89.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_89, 3, 13, 1, 1)

        self.ilvl_62 = QPushButton(self.ilvl_buttons)
        self.ilvl_62.setObjectName(u"ilvl_62")
        sizePolicy.setHeightForWidth(self.ilvl_62.sizePolicy().hasHeightForWidth())
        self.ilvl_62.setSizePolicy(sizePolicy)
        self.ilvl_62.setFont(font7)
        self.ilvl_62.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_62.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_62, 2, 11, 1, 1)

        self.ilvl_82 = QPushButton(self.ilvl_buttons)
        self.ilvl_82.setObjectName(u"ilvl_82")
        sizePolicy.setHeightForWidth(self.ilvl_82.sizePolicy().hasHeightForWidth())
        self.ilvl_82.setSizePolicy(sizePolicy)
        self.ilvl_82.setFont(font7)
        self.ilvl_82.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_82.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_82, 3, 6, 1, 1)

        self.ilvl_45 = QPushButton(self.ilvl_buttons)
        self.ilvl_45.setObjectName(u"ilvl_45")
        sizePolicy.setHeightForWidth(self.ilvl_45.sizePolicy().hasHeightForWidth())
        self.ilvl_45.setSizePolicy(sizePolicy)
        self.ilvl_45.setFont(font7)
        self.ilvl_45.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_45.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_45, 1, 19, 1, 1)

        self.ilvl_97 = QPushButton(self.ilvl_buttons)
        self.ilvl_97.setObjectName(u"ilvl_97")
        sizePolicy.setHeightForWidth(self.ilvl_97.sizePolicy().hasHeightForWidth())
        self.ilvl_97.setSizePolicy(sizePolicy)
        self.ilvl_97.setFont(font7)
        self.ilvl_97.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_97.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_97, 3, 21, 1, 1)

        self.ilvl_38 = QPushButton(self.ilvl_buttons)
        self.ilvl_38.setObjectName(u"ilvl_38")
        sizePolicy.setHeightForWidth(self.ilvl_38.sizePolicy().hasHeightForWidth())
        self.ilvl_38.setSizePolicy(sizePolicy)
        self.ilvl_38.setFont(font7)
        self.ilvl_38.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_38.setIconSize(QSize(30, 30))
        self.ilvl_38.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_38, 1, 12, 1, 1)

        self.ilvl_40 = QPushButton(self.ilvl_buttons)
        self.ilvl_40.setObjectName(u"ilvl_40")
        sizePolicy.setHeightForWidth(self.ilvl_40.sizePolicy().hasHeightForWidth())
        self.ilvl_40.setSizePolicy(sizePolicy)
        self.ilvl_40.setFont(font7)
        self.ilvl_40.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_40.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_40, 1, 14, 1, 1)

        self.ilvl_72 = QPushButton(self.ilvl_buttons)
        self.ilvl_72.setObjectName(u"ilvl_72")
        sizePolicy.setHeightForWidth(self.ilvl_72.sizePolicy().hasHeightForWidth())
        self.ilvl_72.setSizePolicy(sizePolicy)
        self.ilvl_72.setFont(font7)
        self.ilvl_72.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_72.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_72, 2, 21, 1, 1)

        self.ilvl_93 = QPushButton(self.ilvl_buttons)
        self.ilvl_93.setObjectName(u"ilvl_93")
        sizePolicy.setHeightForWidth(self.ilvl_93.sizePolicy().hasHeightForWidth())
        self.ilvl_93.setSizePolicy(sizePolicy)
        self.ilvl_93.setFont(font7)
        self.ilvl_93.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_93.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_93, 3, 17, 1, 1)

        self.ilvl_43 = QPushButton(self.ilvl_buttons)
        self.ilvl_43.setObjectName(u"ilvl_43")
        sizePolicy.setHeightForWidth(self.ilvl_43.sizePolicy().hasHeightForWidth())
        self.ilvl_43.setSizePolicy(sizePolicy)
        self.ilvl_43.setFont(font7)
        self.ilvl_43.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_43.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_43, 1, 17, 1, 1)

        self.ilvl_28 = QPushButton(self.ilvl_buttons)
        self.ilvl_28.setObjectName(u"ilvl_28")
        sizePolicy.setHeightForWidth(self.ilvl_28.sizePolicy().hasHeightForWidth())
        self.ilvl_28.setSizePolicy(sizePolicy)
        self.ilvl_28.setFont(font7)
        self.ilvl_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_28.setIconSize(QSize(30, 30))
        self.ilvl_28.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_28, 1, 2, 1, 1)

        self.ilvl_64 = QPushButton(self.ilvl_buttons)
        self.ilvl_64.setObjectName(u"ilvl_64")
        sizePolicy.setHeightForWidth(self.ilvl_64.sizePolicy().hasHeightForWidth())
        self.ilvl_64.setSizePolicy(sizePolicy)
        self.ilvl_64.setFont(font7)
        self.ilvl_64.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_64.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_64, 2, 13, 1, 1)

        self.ilvl_66 = QPushButton(self.ilvl_buttons)
        self.ilvl_66.setObjectName(u"ilvl_66")
        sizePolicy.setHeightForWidth(self.ilvl_66.sizePolicy().hasHeightForWidth())
        self.ilvl_66.setSizePolicy(sizePolicy)
        self.ilvl_66.setFont(font7)
        self.ilvl_66.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_66.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_66, 2, 15, 1, 1)

        self.ilvl_79 = QPushButton(self.ilvl_buttons)
        self.ilvl_79.setObjectName(u"ilvl_79")
        sizePolicy.setHeightForWidth(self.ilvl_79.sizePolicy().hasHeightForWidth())
        self.ilvl_79.setSizePolicy(sizePolicy)
        self.ilvl_79.setFont(font7)
        self.ilvl_79.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_79.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_79, 3, 3, 1, 1)

        self.ilvl_83 = QPushButton(self.ilvl_buttons)
        self.ilvl_83.setObjectName(u"ilvl_83")
        sizePolicy.setHeightForWidth(self.ilvl_83.sizePolicy().hasHeightForWidth())
        self.ilvl_83.setSizePolicy(sizePolicy)
        self.ilvl_83.setFont(font7)
        self.ilvl_83.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_83.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_83, 3, 7, 1, 1)

        self.ilvl_100 = QPushButton(self.ilvl_buttons)
        self.ilvl_100.setObjectName(u"ilvl_100")
        sizePolicy.setHeightForWidth(self.ilvl_100.sizePolicy().hasHeightForWidth())
        self.ilvl_100.setSizePolicy(sizePolicy)
        self.ilvl_100.setFont(font7)
        self.ilvl_100.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_100.setCheckable(True)
        self.ilvl_100.setChecked(False)

        self.gridLayout_10.addWidget(self.ilvl_100, 3, 24, 1, 1)

        self.ilvl_13 = QPushButton(self.ilvl_buttons)
        self.ilvl_13.setObjectName(u"ilvl_13")
        sizePolicy.setHeightForWidth(self.ilvl_13.sizePolicy().hasHeightForWidth())
        self.ilvl_13.setSizePolicy(sizePolicy)
        self.ilvl_13.setFont(font7)
        self.ilvl_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_13.setIconSize(QSize(30, 30))
        self.ilvl_13.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_13, 0, 12, 1, 1)

        self.ilvl_23 = QPushButton(self.ilvl_buttons)
        self.ilvl_23.setObjectName(u"ilvl_23")
        sizePolicy.setHeightForWidth(self.ilvl_23.sizePolicy().hasHeightForWidth())
        self.ilvl_23.setSizePolicy(sizePolicy)
        self.ilvl_23.setFont(font7)
        self.ilvl_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_23.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_23, 0, 22, 1, 1)

        self.ilvl_98 = QPushButton(self.ilvl_buttons)
        self.ilvl_98.setObjectName(u"ilvl_98")
        sizePolicy.setHeightForWidth(self.ilvl_98.sizePolicy().hasHeightForWidth())
        self.ilvl_98.setSizePolicy(sizePolicy)
        self.ilvl_98.setFont(font7)
        self.ilvl_98.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_98.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_98, 3, 22, 1, 1)

        self.ilvl_52 = QPushButton(self.ilvl_buttons)
        self.ilvl_52.setObjectName(u"ilvl_52")
        sizePolicy.setHeightForWidth(self.ilvl_52.sizePolicy().hasHeightForWidth())
        self.ilvl_52.setSizePolicy(sizePolicy)
        self.ilvl_52.setFont(font7)
        self.ilvl_52.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_52.setIconSize(QSize(30, 30))
        self.ilvl_52.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_52, 2, 1, 1, 1)

        self.ilvl_3 = QPushButton(self.ilvl_buttons)
        self.ilvl_3.setObjectName(u"ilvl_3")
        sizePolicy.setHeightForWidth(self.ilvl_3.sizePolicy().hasHeightForWidth())
        self.ilvl_3.setSizePolicy(sizePolicy)
        self.ilvl_3.setFont(font7)
        self.ilvl_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_3.setIconSize(QSize(30, 30))
        self.ilvl_3.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_3, 0, 2, 1, 1)

        self.ilvl_90 = QPushButton(self.ilvl_buttons)
        self.ilvl_90.setObjectName(u"ilvl_90")
        sizePolicy.setHeightForWidth(self.ilvl_90.sizePolicy().hasHeightForWidth())
        self.ilvl_90.setSizePolicy(sizePolicy)
        self.ilvl_90.setFont(font7)
        self.ilvl_90.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_90.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_90, 3, 14, 1, 1)

        self.ilvl_51 = QPushButton(self.ilvl_buttons)
        self.ilvl_51.setObjectName(u"ilvl_51")
        sizePolicy.setHeightForWidth(self.ilvl_51.sizePolicy().hasHeightForWidth())
        self.ilvl_51.setSizePolicy(sizePolicy)
        self.ilvl_51.setFont(font7)
        self.ilvl_51.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_51.setIconSize(QSize(30, 30))
        self.ilvl_51.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_51, 2, 0, 1, 1)

        self.ilvl_74 = QPushButton(self.ilvl_buttons)
        self.ilvl_74.setObjectName(u"ilvl_74")
        sizePolicy.setHeightForWidth(self.ilvl_74.sizePolicy().hasHeightForWidth())
        self.ilvl_74.setSizePolicy(sizePolicy)
        self.ilvl_74.setFont(font7)
        self.ilvl_74.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_74.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_74, 2, 23, 1, 1)

        self.ilvl_16 = QPushButton(self.ilvl_buttons)
        self.ilvl_16.setObjectName(u"ilvl_16")
        sizePolicy.setHeightForWidth(self.ilvl_16.sizePolicy().hasHeightForWidth())
        self.ilvl_16.setSizePolicy(sizePolicy)
        self.ilvl_16.setFont(font7)
        self.ilvl_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_16.setIconSize(QSize(30, 30))
        self.ilvl_16.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_16, 0, 15, 1, 1)

        self.ilvl_57 = QPushButton(self.ilvl_buttons)
        self.ilvl_57.setObjectName(u"ilvl_57")
        sizePolicy.setHeightForWidth(self.ilvl_57.sizePolicy().hasHeightForWidth())
        self.ilvl_57.setSizePolicy(sizePolicy)
        self.ilvl_57.setFont(font7)
        self.ilvl_57.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_57.setIconSize(QSize(30, 30))
        self.ilvl_57.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_57, 2, 6, 1, 1)

        self.ilvl_86 = QPushButton(self.ilvl_buttons)
        self.ilvl_86.setObjectName(u"ilvl_86")
        sizePolicy.setHeightForWidth(self.ilvl_86.sizePolicy().hasHeightForWidth())
        self.ilvl_86.setSizePolicy(sizePolicy)
        self.ilvl_86.setFont(font7)
        self.ilvl_86.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_86.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_86, 3, 10, 1, 1)

        self.ilvl_77 = QPushButton(self.ilvl_buttons)
        self.ilvl_77.setObjectName(u"ilvl_77")
        sizePolicy.setHeightForWidth(self.ilvl_77.sizePolicy().hasHeightForWidth())
        self.ilvl_77.setSizePolicy(sizePolicy)
        self.ilvl_77.setFont(font7)
        self.ilvl_77.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_77.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_77, 3, 1, 1, 1)

        self.ilvl_1 = QPushButton(self.ilvl_buttons)
        self.ilvl_1.setObjectName(u"ilvl_1")
        sizePolicy.setHeightForWidth(self.ilvl_1.sizePolicy().hasHeightForWidth())
        self.ilvl_1.setSizePolicy(sizePolicy)
        self.ilvl_1.setFont(font7)
        self.ilvl_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_1.setIconSize(QSize(30, 30))
        self.ilvl_1.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_1, 0, 0, 1, 1)

        self.ilvl_20 = QPushButton(self.ilvl_buttons)
        self.ilvl_20.setObjectName(u"ilvl_20")
        sizePolicy.setHeightForWidth(self.ilvl_20.sizePolicy().hasHeightForWidth())
        self.ilvl_20.setSizePolicy(sizePolicy)
        self.ilvl_20.setFont(font7)
        self.ilvl_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_20.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_20, 0, 19, 1, 1)

        self.ilvl_44 = QPushButton(self.ilvl_buttons)
        self.ilvl_44.setObjectName(u"ilvl_44")
        sizePolicy.setHeightForWidth(self.ilvl_44.sizePolicy().hasHeightForWidth())
        self.ilvl_44.setSizePolicy(sizePolicy)
        self.ilvl_44.setFont(font7)
        self.ilvl_44.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_44.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_44, 1, 18, 1, 1)

        self.ilvl_5 = QPushButton(self.ilvl_buttons)
        self.ilvl_5.setObjectName(u"ilvl_5")
        sizePolicy.setHeightForWidth(self.ilvl_5.sizePolicy().hasHeightForWidth())
        self.ilvl_5.setSizePolicy(sizePolicy)
        self.ilvl_5.setFont(font7)
        self.ilvl_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_5.setIconSize(QSize(30, 30))
        self.ilvl_5.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_5, 0, 4, 1, 1)

        self.ilvl_17 = QPushButton(self.ilvl_buttons)
        self.ilvl_17.setObjectName(u"ilvl_17")
        sizePolicy.setHeightForWidth(self.ilvl_17.sizePolicy().hasHeightForWidth())
        self.ilvl_17.setSizePolicy(sizePolicy)
        self.ilvl_17.setFont(font7)
        self.ilvl_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_17.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_17, 0, 16, 1, 1)

        self.ilvl_91 = QPushButton(self.ilvl_buttons)
        self.ilvl_91.setObjectName(u"ilvl_91")
        sizePolicy.setHeightForWidth(self.ilvl_91.sizePolicy().hasHeightForWidth())
        self.ilvl_91.setSizePolicy(sizePolicy)
        self.ilvl_91.setFont(font7)
        self.ilvl_91.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_91.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_91, 3, 15, 1, 1)

        self.ilvl_81 = QPushButton(self.ilvl_buttons)
        self.ilvl_81.setObjectName(u"ilvl_81")
        sizePolicy.setHeightForWidth(self.ilvl_81.sizePolicy().hasHeightForWidth())
        self.ilvl_81.setSizePolicy(sizePolicy)
        self.ilvl_81.setFont(font7)
        self.ilvl_81.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_81.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_81, 3, 5, 1, 1)

        self.ilvl_58 = QPushButton(self.ilvl_buttons)
        self.ilvl_58.setObjectName(u"ilvl_58")
        sizePolicy.setHeightForWidth(self.ilvl_58.sizePolicy().hasHeightForWidth())
        self.ilvl_58.setSizePolicy(sizePolicy)
        self.ilvl_58.setFont(font7)
        self.ilvl_58.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_58.setIconSize(QSize(30, 30))
        self.ilvl_58.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_58, 2, 7, 1, 1)

        self.ilvl_80 = QPushButton(self.ilvl_buttons)
        self.ilvl_80.setObjectName(u"ilvl_80")
        sizePolicy.setHeightForWidth(self.ilvl_80.sizePolicy().hasHeightForWidth())
        self.ilvl_80.setSizePolicy(sizePolicy)
        self.ilvl_80.setFont(font7)
        self.ilvl_80.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_80.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_80, 3, 4, 1, 1)

        self.ilvl_60 = QPushButton(self.ilvl_buttons)
        self.ilvl_60.setObjectName(u"ilvl_60")
        sizePolicy.setHeightForWidth(self.ilvl_60.sizePolicy().hasHeightForWidth())
        self.ilvl_60.setSizePolicy(sizePolicy)
        self.ilvl_60.setFont(font7)
        self.ilvl_60.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_60.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_60, 2, 9, 1, 1)

        self.ilvl_69 = QPushButton(self.ilvl_buttons)
        self.ilvl_69.setObjectName(u"ilvl_69")
        sizePolicy.setHeightForWidth(self.ilvl_69.sizePolicy().hasHeightForWidth())
        self.ilvl_69.setSizePolicy(sizePolicy)
        self.ilvl_69.setFont(font7)
        self.ilvl_69.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_69.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_69, 2, 18, 1, 1)

        self.ilvl_42 = QPushButton(self.ilvl_buttons)
        self.ilvl_42.setObjectName(u"ilvl_42")
        sizePolicy.setHeightForWidth(self.ilvl_42.sizePolicy().hasHeightForWidth())
        self.ilvl_42.setSizePolicy(sizePolicy)
        self.ilvl_42.setFont(font7)
        self.ilvl_42.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_42.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_42, 1, 16, 1, 1)

        self.ilvl_12 = QPushButton(self.ilvl_buttons)
        self.ilvl_12.setObjectName(u"ilvl_12")
        sizePolicy.setHeightForWidth(self.ilvl_12.sizePolicy().hasHeightForWidth())
        self.ilvl_12.setSizePolicy(sizePolicy)
        self.ilvl_12.setFont(font7)
        self.ilvl_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_12.setIconSize(QSize(30, 30))
        self.ilvl_12.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_12, 0, 11, 1, 1)

        self.ilvl_50 = QPushButton(self.ilvl_buttons)
        self.ilvl_50.setObjectName(u"ilvl_50")
        sizePolicy.setHeightForWidth(self.ilvl_50.sizePolicy().hasHeightForWidth())
        self.ilvl_50.setSizePolicy(sizePolicy)
        self.ilvl_50.setFont(font7)
        self.ilvl_50.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_50.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_50, 1, 24, 1, 1)

        self.ilvl_54 = QPushButton(self.ilvl_buttons)
        self.ilvl_54.setObjectName(u"ilvl_54")
        sizePolicy.setHeightForWidth(self.ilvl_54.sizePolicy().hasHeightForWidth())
        self.ilvl_54.setSizePolicy(sizePolicy)
        self.ilvl_54.setFont(font7)
        self.ilvl_54.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_54.setIconSize(QSize(30, 30))
        self.ilvl_54.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_54, 2, 3, 1, 1)

        self.ilvl_6 = QPushButton(self.ilvl_buttons)
        self.ilvl_6.setObjectName(u"ilvl_6")
        sizePolicy.setHeightForWidth(self.ilvl_6.sizePolicy().hasHeightForWidth())
        self.ilvl_6.setSizePolicy(sizePolicy)
        self.ilvl_6.setFont(font7)
        self.ilvl_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_6.setIconSize(QSize(30, 30))
        self.ilvl_6.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_6, 0, 5, 1, 1)

        self.ilvl_10 = QPushButton(self.ilvl_buttons)
        self.ilvl_10.setObjectName(u"ilvl_10")
        sizePolicy.setHeightForWidth(self.ilvl_10.sizePolicy().hasHeightForWidth())
        self.ilvl_10.setSizePolicy(sizePolicy)
        self.ilvl_10.setFont(font7)
        self.ilvl_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_10.setIconSize(QSize(30, 30))
        self.ilvl_10.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_10, 0, 9, 1, 1)

        self.ilvl_18 = QPushButton(self.ilvl_buttons)
        self.ilvl_18.setObjectName(u"ilvl_18")
        sizePolicy.setHeightForWidth(self.ilvl_18.sizePolicy().hasHeightForWidth())
        self.ilvl_18.setSizePolicy(sizePolicy)
        self.ilvl_18.setFont(font7)
        self.ilvl_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_18.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_18, 0, 17, 1, 1)

        self.ilvl_36 = QPushButton(self.ilvl_buttons)
        self.ilvl_36.setObjectName(u"ilvl_36")
        sizePolicy.setHeightForWidth(self.ilvl_36.sizePolicy().hasHeightForWidth())
        self.ilvl_36.setSizePolicy(sizePolicy)
        self.ilvl_36.setFont(font7)
        self.ilvl_36.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_36.setIconSize(QSize(30, 30))
        self.ilvl_36.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_36, 1, 10, 1, 1)

        self.ilvl_39 = QPushButton(self.ilvl_buttons)
        self.ilvl_39.setObjectName(u"ilvl_39")
        sizePolicy.setHeightForWidth(self.ilvl_39.sizePolicy().hasHeightForWidth())
        self.ilvl_39.setSizePolicy(sizePolicy)
        self.ilvl_39.setFont(font7)
        self.ilvl_39.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_39.setIconSize(QSize(30, 30))
        self.ilvl_39.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_39, 1, 13, 1, 1)

        self.ilvl_61 = QPushButton(self.ilvl_buttons)
        self.ilvl_61.setObjectName(u"ilvl_61")
        sizePolicy.setHeightForWidth(self.ilvl_61.sizePolicy().hasHeightForWidth())
        self.ilvl_61.setSizePolicy(sizePolicy)
        self.ilvl_61.setFont(font7)
        self.ilvl_61.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_61.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_61, 2, 10, 1, 1)

        self.ilvl_59 = QPushButton(self.ilvl_buttons)
        self.ilvl_59.setObjectName(u"ilvl_59")
        sizePolicy.setHeightForWidth(self.ilvl_59.sizePolicy().hasHeightForWidth())
        self.ilvl_59.setSizePolicy(sizePolicy)
        self.ilvl_59.setFont(font7)
        self.ilvl_59.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_59.setIconSize(QSize(30, 30))
        self.ilvl_59.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_59, 2, 8, 1, 1)

        self.ilvl_2 = QPushButton(self.ilvl_buttons)
        self.ilvl_2.setObjectName(u"ilvl_2")
        sizePolicy.setHeightForWidth(self.ilvl_2.sizePolicy().hasHeightForWidth())
        self.ilvl_2.setSizePolicy(sizePolicy)
        self.ilvl_2.setFont(font7)
        self.ilvl_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_2.setIconSize(QSize(30, 30))
        self.ilvl_2.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_2, 0, 1, 1, 1)

        self.ilvl_34 = QPushButton(self.ilvl_buttons)
        self.ilvl_34.setObjectName(u"ilvl_34")
        sizePolicy.setHeightForWidth(self.ilvl_34.sizePolicy().hasHeightForWidth())
        self.ilvl_34.setSizePolicy(sizePolicy)
        self.ilvl_34.setFont(font7)
        self.ilvl_34.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_34.setIconSize(QSize(30, 30))
        self.ilvl_34.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_34, 1, 8, 1, 1)

        self.ilvl_26 = QPushButton(self.ilvl_buttons)
        self.ilvl_26.setObjectName(u"ilvl_26")
        sizePolicy.setHeightForWidth(self.ilvl_26.sizePolicy().hasHeightForWidth())
        self.ilvl_26.setSizePolicy(sizePolicy)
        self.ilvl_26.setFont(font7)
        self.ilvl_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_26.setIconSize(QSize(30, 30))
        self.ilvl_26.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_26, 1, 0, 1, 1)

        self.ilvl_67 = QPushButton(self.ilvl_buttons)
        self.ilvl_67.setObjectName(u"ilvl_67")
        sizePolicy.setHeightForWidth(self.ilvl_67.sizePolicy().hasHeightForWidth())
        self.ilvl_67.setSizePolicy(sizePolicy)
        self.ilvl_67.setFont(font7)
        self.ilvl_67.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_67.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_67, 2, 16, 1, 1)

        self.ilvl_15 = QPushButton(self.ilvl_buttons)
        self.ilvl_15.setObjectName(u"ilvl_15")
        sizePolicy.setHeightForWidth(self.ilvl_15.sizePolicy().hasHeightForWidth())
        self.ilvl_15.setSizePolicy(sizePolicy)
        self.ilvl_15.setFont(font7)
        self.ilvl_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_15.setIconSize(QSize(30, 30))
        self.ilvl_15.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_15, 0, 14, 1, 1)

        self.ilvl_9 = QPushButton(self.ilvl_buttons)
        self.ilvl_9.setObjectName(u"ilvl_9")
        sizePolicy.setHeightForWidth(self.ilvl_9.sizePolicy().hasHeightForWidth())
        self.ilvl_9.setSizePolicy(sizePolicy)
        self.ilvl_9.setFont(font7)
        self.ilvl_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_9.setIconSize(QSize(30, 30))
        self.ilvl_9.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_9, 0, 8, 1, 1)

        self.ilvl_99 = QPushButton(self.ilvl_buttons)
        self.ilvl_99.setObjectName(u"ilvl_99")
        sizePolicy.setHeightForWidth(self.ilvl_99.sizePolicy().hasHeightForWidth())
        self.ilvl_99.setSizePolicy(sizePolicy)
        self.ilvl_99.setFont(font7)
        self.ilvl_99.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_99.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_99, 3, 23, 1, 1)

        self.ilvl_65 = QPushButton(self.ilvl_buttons)
        self.ilvl_65.setObjectName(u"ilvl_65")
        sizePolicy.setHeightForWidth(self.ilvl_65.sizePolicy().hasHeightForWidth())
        self.ilvl_65.setSizePolicy(sizePolicy)
        self.ilvl_65.setFont(font7)
        self.ilvl_65.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_65.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_65, 2, 14, 1, 1)

        self.ilvl_49 = QPushButton(self.ilvl_buttons)
        self.ilvl_49.setObjectName(u"ilvl_49")
        sizePolicy.setHeightForWidth(self.ilvl_49.sizePolicy().hasHeightForWidth())
        self.ilvl_49.setSizePolicy(sizePolicy)
        self.ilvl_49.setFont(font7)
        self.ilvl_49.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_49.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_49, 1, 23, 1, 1)

        self.ilvl_7 = QPushButton(self.ilvl_buttons)
        self.ilvl_7.setObjectName(u"ilvl_7")
        sizePolicy.setHeightForWidth(self.ilvl_7.sizePolicy().hasHeightForWidth())
        self.ilvl_7.setSizePolicy(sizePolicy)
        self.ilvl_7.setFont(font7)
        self.ilvl_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_7.setIconSize(QSize(30, 30))
        self.ilvl_7.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_7, 0, 6, 1, 1)

        self.ilvl_94 = QPushButton(self.ilvl_buttons)
        self.ilvl_94.setObjectName(u"ilvl_94")
        sizePolicy.setHeightForWidth(self.ilvl_94.sizePolicy().hasHeightForWidth())
        self.ilvl_94.setSizePolicy(sizePolicy)
        self.ilvl_94.setFont(font7)
        self.ilvl_94.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_94.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_94, 3, 18, 1, 1)

        self.ilvl_31 = QPushButton(self.ilvl_buttons)
        self.ilvl_31.setObjectName(u"ilvl_31")
        sizePolicy.setHeightForWidth(self.ilvl_31.sizePolicy().hasHeightForWidth())
        self.ilvl_31.setSizePolicy(sizePolicy)
        self.ilvl_31.setFont(font7)
        self.ilvl_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_31.setIconSize(QSize(30, 30))
        self.ilvl_31.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_31, 1, 5, 1, 1)

        self.ilvl_29 = QPushButton(self.ilvl_buttons)
        self.ilvl_29.setObjectName(u"ilvl_29")
        sizePolicy.setHeightForWidth(self.ilvl_29.sizePolicy().hasHeightForWidth())
        self.ilvl_29.setSizePolicy(sizePolicy)
        self.ilvl_29.setFont(font7)
        self.ilvl_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_29.setIconSize(QSize(30, 30))
        self.ilvl_29.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_29, 1, 3, 1, 1)

        self.ilvl_95 = QPushButton(self.ilvl_buttons)
        self.ilvl_95.setObjectName(u"ilvl_95")
        sizePolicy.setHeightForWidth(self.ilvl_95.sizePolicy().hasHeightForWidth())
        self.ilvl_95.setSizePolicy(sizePolicy)
        self.ilvl_95.setFont(font7)
        self.ilvl_95.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_95.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_95, 3, 19, 1, 1)

        self.ilvl_19 = QPushButton(self.ilvl_buttons)
        self.ilvl_19.setObjectName(u"ilvl_19")
        sizePolicy.setHeightForWidth(self.ilvl_19.sizePolicy().hasHeightForWidth())
        self.ilvl_19.setSizePolicy(sizePolicy)
        self.ilvl_19.setFont(font7)
        self.ilvl_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_19.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_19, 0, 18, 1, 1)

        self.ilvl_32 = QPushButton(self.ilvl_buttons)
        self.ilvl_32.setObjectName(u"ilvl_32")
        sizePolicy.setHeightForWidth(self.ilvl_32.sizePolicy().hasHeightForWidth())
        self.ilvl_32.setSizePolicy(sizePolicy)
        self.ilvl_32.setFont(font7)
        self.ilvl_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_32.setIconSize(QSize(30, 30))
        self.ilvl_32.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_32, 1, 6, 1, 1)

        self.ilvl_30 = QPushButton(self.ilvl_buttons)
        self.ilvl_30.setObjectName(u"ilvl_30")
        sizePolicy.setHeightForWidth(self.ilvl_30.sizePolicy().hasHeightForWidth())
        self.ilvl_30.setSizePolicy(sizePolicy)
        self.ilvl_30.setFont(font7)
        self.ilvl_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_30.setIconSize(QSize(30, 30))
        self.ilvl_30.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_30, 1, 4, 1, 1)

        self.ilvl_47 = QPushButton(self.ilvl_buttons)
        self.ilvl_47.setObjectName(u"ilvl_47")
        sizePolicy.setHeightForWidth(self.ilvl_47.sizePolicy().hasHeightForWidth())
        self.ilvl_47.setSizePolicy(sizePolicy)
        self.ilvl_47.setFont(font7)
        self.ilvl_47.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_47.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_47, 1, 21, 1, 1)

        self.ilvl_84 = QPushButton(self.ilvl_buttons)
        self.ilvl_84.setObjectName(u"ilvl_84")
        sizePolicy.setHeightForWidth(self.ilvl_84.sizePolicy().hasHeightForWidth())
        self.ilvl_84.setSizePolicy(sizePolicy)
        self.ilvl_84.setFont(font7)
        self.ilvl_84.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_84.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_84, 3, 8, 1, 1)

        self.ilvl_76 = QPushButton(self.ilvl_buttons)
        self.ilvl_76.setObjectName(u"ilvl_76")
        sizePolicy.setHeightForWidth(self.ilvl_76.sizePolicy().hasHeightForWidth())
        self.ilvl_76.setSizePolicy(sizePolicy)
        self.ilvl_76.setFont(font7)
        self.ilvl_76.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_76.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_76, 3, 0, 1, 1)

        self.ilvl_56 = QPushButton(self.ilvl_buttons)
        self.ilvl_56.setObjectName(u"ilvl_56")
        sizePolicy.setHeightForWidth(self.ilvl_56.sizePolicy().hasHeightForWidth())
        self.ilvl_56.setSizePolicy(sizePolicy)
        self.ilvl_56.setFont(font7)
        self.ilvl_56.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_56.setIconSize(QSize(30, 30))
        self.ilvl_56.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_56, 2, 5, 1, 1)

        self.ilvl_33 = QPushButton(self.ilvl_buttons)
        self.ilvl_33.setObjectName(u"ilvl_33")
        sizePolicy.setHeightForWidth(self.ilvl_33.sizePolicy().hasHeightForWidth())
        self.ilvl_33.setSizePolicy(sizePolicy)
        self.ilvl_33.setFont(font7)
        self.ilvl_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_33.setIconSize(QSize(30, 30))
        self.ilvl_33.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_33, 1, 7, 1, 1)

        self.ilvl_35 = QPushButton(self.ilvl_buttons)
        self.ilvl_35.setObjectName(u"ilvl_35")
        sizePolicy.setHeightForWidth(self.ilvl_35.sizePolicy().hasHeightForWidth())
        self.ilvl_35.setSizePolicy(sizePolicy)
        self.ilvl_35.setFont(font7)
        self.ilvl_35.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_35.setIconSize(QSize(30, 30))
        self.ilvl_35.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_35, 1, 9, 1, 1)

        self.ilvl_37 = QPushButton(self.ilvl_buttons)
        self.ilvl_37.setObjectName(u"ilvl_37")
        sizePolicy.setHeightForWidth(self.ilvl_37.sizePolicy().hasHeightForWidth())
        self.ilvl_37.setSizePolicy(sizePolicy)
        self.ilvl_37.setFont(font7)
        self.ilvl_37.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_37.setIconSize(QSize(30, 30))
        self.ilvl_37.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_37, 1, 11, 1, 1)

        self.ilvl_92 = QPushButton(self.ilvl_buttons)
        self.ilvl_92.setObjectName(u"ilvl_92")
        sizePolicy.setHeightForWidth(self.ilvl_92.sizePolicy().hasHeightForWidth())
        self.ilvl_92.setSizePolicy(sizePolicy)
        self.ilvl_92.setFont(font7)
        self.ilvl_92.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_92.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_92, 3, 16, 1, 1)

        self.ilvl_25 = QPushButton(self.ilvl_buttons)
        self.ilvl_25.setObjectName(u"ilvl_25")
        sizePolicy.setHeightForWidth(self.ilvl_25.sizePolicy().hasHeightForWidth())
        self.ilvl_25.setSizePolicy(sizePolicy)
        self.ilvl_25.setFont(font7)
        self.ilvl_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_25.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_25, 0, 24, 1, 1)

        self.ilvl_27 = QPushButton(self.ilvl_buttons)
        self.ilvl_27.setObjectName(u"ilvl_27")
        sizePolicy.setHeightForWidth(self.ilvl_27.sizePolicy().hasHeightForWidth())
        self.ilvl_27.setSizePolicy(sizePolicy)
        self.ilvl_27.setFont(font7)
        self.ilvl_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_27.setIconSize(QSize(30, 30))
        self.ilvl_27.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_27, 1, 1, 1, 1)

        self.ilvl_22 = QPushButton(self.ilvl_buttons)
        self.ilvl_22.setObjectName(u"ilvl_22")
        sizePolicy.setHeightForWidth(self.ilvl_22.sizePolicy().hasHeightForWidth())
        self.ilvl_22.setSizePolicy(sizePolicy)
        self.ilvl_22.setFont(font7)
        self.ilvl_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_22.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_22, 0, 21, 1, 1)

        self.ilvl_4 = QPushButton(self.ilvl_buttons)
        self.ilvl_4.setObjectName(u"ilvl_4")
        sizePolicy.setHeightForWidth(self.ilvl_4.sizePolicy().hasHeightForWidth())
        self.ilvl_4.setSizePolicy(sizePolicy)
        self.ilvl_4.setFont(font7)
        self.ilvl_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_4.setIconSize(QSize(30, 30))
        self.ilvl_4.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_4, 0, 3, 1, 1)

        self.ilvl_48 = QPushButton(self.ilvl_buttons)
        self.ilvl_48.setObjectName(u"ilvl_48")
        sizePolicy.setHeightForWidth(self.ilvl_48.sizePolicy().hasHeightForWidth())
        self.ilvl_48.setSizePolicy(sizePolicy)
        self.ilvl_48.setFont(font7)
        self.ilvl_48.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_48.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_48, 1, 22, 1, 1)

        self.ilvl_46 = QPushButton(self.ilvl_buttons)
        self.ilvl_46.setObjectName(u"ilvl_46")
        sizePolicy.setHeightForWidth(self.ilvl_46.sizePolicy().hasHeightForWidth())
        self.ilvl_46.setSizePolicy(sizePolicy)
        self.ilvl_46.setFont(font7)
        self.ilvl_46.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_46.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_46, 1, 20, 1, 1)

        self.ilvl_85 = QPushButton(self.ilvl_buttons)
        self.ilvl_85.setObjectName(u"ilvl_85")
        sizePolicy.setHeightForWidth(self.ilvl_85.sizePolicy().hasHeightForWidth())
        self.ilvl_85.setSizePolicy(sizePolicy)
        self.ilvl_85.setFont(font7)
        self.ilvl_85.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_85.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_85, 3, 9, 1, 1)

        self.ilvl_88 = QPushButton(self.ilvl_buttons)
        self.ilvl_88.setObjectName(u"ilvl_88")
        sizePolicy.setHeightForWidth(self.ilvl_88.sizePolicy().hasHeightForWidth())
        self.ilvl_88.setSizePolicy(sizePolicy)
        self.ilvl_88.setFont(font7)
        self.ilvl_88.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_88.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_88, 3, 12, 1, 1)

        self.ilvl_41 = QPushButton(self.ilvl_buttons)
        self.ilvl_41.setObjectName(u"ilvl_41")
        sizePolicy.setHeightForWidth(self.ilvl_41.sizePolicy().hasHeightForWidth())
        self.ilvl_41.setSizePolicy(sizePolicy)
        self.ilvl_41.setFont(font7)
        self.ilvl_41.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_41.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_41, 1, 15, 1, 1)

        self.ilvl_24 = QPushButton(self.ilvl_buttons)
        self.ilvl_24.setObjectName(u"ilvl_24")
        sizePolicy.setHeightForWidth(self.ilvl_24.sizePolicy().hasHeightForWidth())
        self.ilvl_24.setSizePolicy(sizePolicy)
        self.ilvl_24.setFont(font7)
        self.ilvl_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_24.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_24, 0, 23, 1, 1)

        self.ilvl_55 = QPushButton(self.ilvl_buttons)
        self.ilvl_55.setObjectName(u"ilvl_55")
        sizePolicy.setHeightForWidth(self.ilvl_55.sizePolicy().hasHeightForWidth())
        self.ilvl_55.setSizePolicy(sizePolicy)
        self.ilvl_55.setFont(font7)
        self.ilvl_55.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_55.setIconSize(QSize(30, 30))
        self.ilvl_55.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_55, 2, 4, 1, 1)

        self.ilvl_11 = QPushButton(self.ilvl_buttons)
        self.ilvl_11.setObjectName(u"ilvl_11")
        sizePolicy.setHeightForWidth(self.ilvl_11.sizePolicy().hasHeightForWidth())
        self.ilvl_11.setSizePolicy(sizePolicy)
        self.ilvl_11.setFont(font7)
        self.ilvl_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_11.setIconSize(QSize(30, 30))
        self.ilvl_11.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_11, 0, 10, 1, 1)

        self.ilvl_14 = QPushButton(self.ilvl_buttons)
        self.ilvl_14.setObjectName(u"ilvl_14")
        sizePolicy.setHeightForWidth(self.ilvl_14.sizePolicy().hasHeightForWidth())
        self.ilvl_14.setSizePolicy(sizePolicy)
        self.ilvl_14.setFont(font7)
        self.ilvl_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_14.setIconSize(QSize(30, 30))
        self.ilvl_14.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_14, 0, 13, 1, 1)

        self.ilvl_53 = QPushButton(self.ilvl_buttons)
        self.ilvl_53.setObjectName(u"ilvl_53")
        sizePolicy.setHeightForWidth(self.ilvl_53.sizePolicy().hasHeightForWidth())
        self.ilvl_53.setSizePolicy(sizePolicy)
        self.ilvl_53.setFont(font7)
        self.ilvl_53.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_53.setIconSize(QSize(30, 30))
        self.ilvl_53.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_53, 2, 2, 1, 1)

        self.ilvl_68 = QPushButton(self.ilvl_buttons)
        self.ilvl_68.setObjectName(u"ilvl_68")
        sizePolicy.setHeightForWidth(self.ilvl_68.sizePolicy().hasHeightForWidth())
        self.ilvl_68.setSizePolicy(sizePolicy)
        self.ilvl_68.setFont(font7)
        self.ilvl_68.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_68.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_68, 2, 17, 1, 1)

        self.ilvl_70 = QPushButton(self.ilvl_buttons)
        self.ilvl_70.setObjectName(u"ilvl_70")
        sizePolicy.setHeightForWidth(self.ilvl_70.sizePolicy().hasHeightForWidth())
        self.ilvl_70.setSizePolicy(sizePolicy)
        self.ilvl_70.setFont(font7)
        self.ilvl_70.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_70.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_70, 2, 19, 1, 1)

        self.ilvl_21 = QPushButton(self.ilvl_buttons)
        self.ilvl_21.setObjectName(u"ilvl_21")
        sizePolicy.setHeightForWidth(self.ilvl_21.sizePolicy().hasHeightForWidth())
        self.ilvl_21.setSizePolicy(sizePolicy)
        self.ilvl_21.setFont(font7)
        self.ilvl_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.ilvl_21.setCheckable(True)

        self.gridLayout_10.addWidget(self.ilvl_21, 0, 20, 1, 1)


        self.verticalLayout_26.addWidget(self.ilvl_buttons)

        self.splitter_7.addWidget(self.ilvl_options)
        self.quality_options = QWidget(self.splitter_7)
        self.quality_options.setObjectName(u"quality_options")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.quality_options.sizePolicy().hasHeightForWidth())
        self.quality_options.setSizePolicy(sizePolicy6)
        self.quality_options.setStyleSheet(u"QWidget {\n"
"	border: none;\n"
"	border-image: none;\n"
"}\n"
"\n"
"QPushButton {\n"
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
"                border-radius"
                        ": 4px;\n"
"                background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);\n"
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
"            QPushButton:hover {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"           }\n"
"            QPushButton:pressed {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
""
                        "            }\n"
"			QPushButton:checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 5px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton:flat {\n"
"                border: none;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.quality_options)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.quality_header_label = QLabel(self.quality_options)
        self.quality_header_label.setObjectName(u"quality_header_label")
        sizePolicy.setHeightForWidth(self.quality_header_label.sizePolicy().hasHeightForWidth())
        self.quality_header_label.setSizePolicy(sizePolicy)
        self.quality_header_label.setMinimumSize(QSize(0, 35))
        self.quality_header_label.setFont(font4)
        self.quality_header_label.setStyleSheet(u"border-radius: 4px;")
        self.quality_header_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.quality_header_label)

        self.quality_buttons = QWidget(self.quality_options)
        self.quality_buttons.setObjectName(u"quality_buttons")
        sizePolicy1.setHeightForWidth(self.quality_buttons.sizePolicy().hasHeightForWidth())
        self.quality_buttons.setSizePolicy(sizePolicy1)
        self.quality_buttons.setMinimumSize(QSize(0, 0))
        self.quality_buttons.setMaximumSize(QSize(16777215, 16777215))
        self.quality_buttons.setFont(font6)
        self.quality_buttons.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.quality_buttons)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.quality_28 = QPushButton(self.quality_buttons)
        self.quality_28.setObjectName(u"quality_28")
        sizePolicy1.setHeightForWidth(self.quality_28.sizePolicy().hasHeightForWidth())
        self.quality_28.setSizePolicy(sizePolicy1)
        self.quality_28.setMinimumSize(QSize(0, 0))
        self.quality_28.setMaximumSize(QSize(167775, 167775))
        self.quality_28.setFont(font7)
        self.quality_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_28.setIconSize(QSize(30, 30))
        self.quality_28.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_28, 1, 12, 1, 1)

        self.quality_5 = QPushButton(self.quality_buttons)
        self.quality_5.setObjectName(u"quality_5")
        sizePolicy1.setHeightForWidth(self.quality_5.sizePolicy().hasHeightForWidth())
        self.quality_5.setSizePolicy(sizePolicy1)
        self.quality_5.setMinimumSize(QSize(0, 0))
        self.quality_5.setMaximumSize(QSize(167775, 167775))
        self.quality_5.setFont(font7)
        self.quality_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_5.setIconSize(QSize(30, 30))
        self.quality_5.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_5, 0, 4, 1, 1)

        self.quality_13 = QPushButton(self.quality_buttons)
        self.quality_13.setObjectName(u"quality_13")
        sizePolicy1.setHeightForWidth(self.quality_13.sizePolicy().hasHeightForWidth())
        self.quality_13.setSizePolicy(sizePolicy1)
        self.quality_13.setMinimumSize(QSize(0, 0))
        self.quality_13.setMaximumSize(QSize(167775, 167775))
        self.quality_13.setFont(font7)
        self.quality_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_13.setIconSize(QSize(30, 30))
        self.quality_13.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_13, 0, 12, 1, 1)

        self.quality_20 = QPushButton(self.quality_buttons)
        self.quality_20.setObjectName(u"quality_20")
        sizePolicy1.setHeightForWidth(self.quality_20.sizePolicy().hasHeightForWidth())
        self.quality_20.setSizePolicy(sizePolicy1)
        self.quality_20.setMinimumSize(QSize(0, 0))
        self.quality_20.setMaximumSize(QSize(167775, 167775))
        self.quality_20.setFont(font7)
        self.quality_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_20.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_20, 1, 4, 1, 1)

        self.quality_27 = QPushButton(self.quality_buttons)
        self.quality_27.setObjectName(u"quality_27")
        sizePolicy1.setHeightForWidth(self.quality_27.sizePolicy().hasHeightForWidth())
        self.quality_27.setSizePolicy(sizePolicy1)
        self.quality_27.setMinimumSize(QSize(0, 0))
        self.quality_27.setMaximumSize(QSize(167775, 167775))
        self.quality_27.setFont(font7)
        self.quality_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_27.setIconSize(QSize(30, 30))
        self.quality_27.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_27, 1, 11, 1, 1)

        self.quality_3 = QPushButton(self.quality_buttons)
        self.quality_3.setObjectName(u"quality_3")
        sizePolicy1.setHeightForWidth(self.quality_3.sizePolicy().hasHeightForWidth())
        self.quality_3.setSizePolicy(sizePolicy1)
        self.quality_3.setMinimumSize(QSize(0, 0))
        self.quality_3.setMaximumSize(QSize(167775, 167775))
        self.quality_3.setFont(font7)
        self.quality_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_3.setIconSize(QSize(30, 30))
        self.quality_3.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_3, 0, 2, 1, 1)

        self.quality_30 = QPushButton(self.quality_buttons)
        self.quality_30.setObjectName(u"quality_30")
        sizePolicy1.setHeightForWidth(self.quality_30.sizePolicy().hasHeightForWidth())
        self.quality_30.setSizePolicy(sizePolicy1)
        self.quality_30.setMinimumSize(QSize(0, 0))
        self.quality_30.setMaximumSize(QSize(167775, 167775))
        self.quality_30.setFont(font7)
        self.quality_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_30.setIconSize(QSize(30, 30))
        self.quality_30.setCheckable(True)
        self.quality_30.setFlat(False)

        self.gridLayout_11.addWidget(self.quality_30, 1, 14, 1, 1)

        self.quality_26 = QPushButton(self.quality_buttons)
        self.quality_26.setObjectName(u"quality_26")
        sizePolicy1.setHeightForWidth(self.quality_26.sizePolicy().hasHeightForWidth())
        self.quality_26.setSizePolicy(sizePolicy1)
        self.quality_26.setMinimumSize(QSize(0, 0))
        self.quality_26.setMaximumSize(QSize(167775, 167775))
        self.quality_26.setFont(font7)
        self.quality_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_26.setIconSize(QSize(30, 30))
        self.quality_26.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_26, 1, 10, 1, 1)

        self.quality_22 = QPushButton(self.quality_buttons)
        self.quality_22.setObjectName(u"quality_22")
        sizePolicy1.setHeightForWidth(self.quality_22.sizePolicy().hasHeightForWidth())
        self.quality_22.setSizePolicy(sizePolicy1)
        self.quality_22.setMinimumSize(QSize(0, 0))
        self.quality_22.setMaximumSize(QSize(167775, 167775))
        self.quality_22.setFont(font7)
        self.quality_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_22.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_22, 1, 6, 1, 1)

        self.quality_25 = QPushButton(self.quality_buttons)
        self.quality_25.setObjectName(u"quality_25")
        sizePolicy1.setHeightForWidth(self.quality_25.sizePolicy().hasHeightForWidth())
        self.quality_25.setSizePolicy(sizePolicy1)
        self.quality_25.setMinimumSize(QSize(0, 0))
        self.quality_25.setMaximumSize(QSize(167775, 167775))
        self.quality_25.setFont(font7)
        self.quality_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_25.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_25, 1, 9, 1, 1)

        self.quality_9 = QPushButton(self.quality_buttons)
        self.quality_9.setObjectName(u"quality_9")
        sizePolicy1.setHeightForWidth(self.quality_9.sizePolicy().hasHeightForWidth())
        self.quality_9.setSizePolicy(sizePolicy1)
        self.quality_9.setMinimumSize(QSize(0, 0))
        self.quality_9.setMaximumSize(QSize(167775, 167775))
        self.quality_9.setFont(font7)
        self.quality_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_9.setIconSize(QSize(30, 30))
        self.quality_9.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_9, 0, 8, 1, 1)

        self.quality_4 = QPushButton(self.quality_buttons)
        self.quality_4.setObjectName(u"quality_4")
        sizePolicy1.setHeightForWidth(self.quality_4.sizePolicy().hasHeightForWidth())
        self.quality_4.setSizePolicy(sizePolicy1)
        self.quality_4.setMinimumSize(QSize(0, 0))
        self.quality_4.setMaximumSize(QSize(167775, 167775))
        self.quality_4.setFont(font7)
        self.quality_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_4.setIconSize(QSize(30, 30))
        self.quality_4.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_4, 0, 3, 1, 1)

        self.quality_16 = QPushButton(self.quality_buttons)
        self.quality_16.setObjectName(u"quality_16")
        sizePolicy1.setHeightForWidth(self.quality_16.sizePolicy().hasHeightForWidth())
        self.quality_16.setSizePolicy(sizePolicy1)
        self.quality_16.setMinimumSize(QSize(0, 0))
        self.quality_16.setMaximumSize(QSize(167775, 167775))
        self.quality_16.setFont(font7)
        self.quality_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_16.setIconSize(QSize(30, 30))
        self.quality_16.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_16, 1, 0, 1, 1)

        self.quality_24 = QPushButton(self.quality_buttons)
        self.quality_24.setObjectName(u"quality_24")
        sizePolicy1.setHeightForWidth(self.quality_24.sizePolicy().hasHeightForWidth())
        self.quality_24.setSizePolicy(sizePolicy1)
        self.quality_24.setMinimumSize(QSize(0, 0))
        self.quality_24.setMaximumSize(QSize(167775, 167775))
        self.quality_24.setFont(font7)
        self.quality_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_24.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_24, 1, 8, 1, 1)

        self.quality_6 = QPushButton(self.quality_buttons)
        self.quality_6.setObjectName(u"quality_6")
        sizePolicy1.setHeightForWidth(self.quality_6.sizePolicy().hasHeightForWidth())
        self.quality_6.setSizePolicy(sizePolicy1)
        self.quality_6.setMinimumSize(QSize(0, 0))
        self.quality_6.setMaximumSize(QSize(167775, 167775))
        self.quality_6.setFont(font7)
        self.quality_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_6.setIconSize(QSize(30, 30))
        self.quality_6.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_6, 0, 5, 1, 1)

        self.quality_21 = QPushButton(self.quality_buttons)
        self.quality_21.setObjectName(u"quality_21")
        sizePolicy1.setHeightForWidth(self.quality_21.sizePolicy().hasHeightForWidth())
        self.quality_21.setSizePolicy(sizePolicy1)
        self.quality_21.setMinimumSize(QSize(0, 0))
        self.quality_21.setMaximumSize(QSize(167775, 167775))
        self.quality_21.setFont(font7)
        self.quality_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_21.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_21, 1, 5, 1, 1)

        self.quality_11 = QPushButton(self.quality_buttons)
        self.quality_11.setObjectName(u"quality_11")
        sizePolicy1.setHeightForWidth(self.quality_11.sizePolicy().hasHeightForWidth())
        self.quality_11.setSizePolicy(sizePolicy1)
        self.quality_11.setMinimumSize(QSize(0, 0))
        self.quality_11.setMaximumSize(QSize(167775, 167775))
        self.quality_11.setFont(font7)
        self.quality_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_11.setIconSize(QSize(30, 30))
        self.quality_11.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_11, 0, 10, 1, 1)

        self.quality_12 = QPushButton(self.quality_buttons)
        self.quality_12.setObjectName(u"quality_12")
        sizePolicy1.setHeightForWidth(self.quality_12.sizePolicy().hasHeightForWidth())
        self.quality_12.setSizePolicy(sizePolicy1)
        self.quality_12.setMinimumSize(QSize(0, 0))
        self.quality_12.setMaximumSize(QSize(167775, 167775))
        self.quality_12.setFont(font7)
        self.quality_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_12.setIconSize(QSize(30, 30))
        self.quality_12.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_12, 0, 11, 1, 1)

        self.quality_29 = QPushButton(self.quality_buttons)
        self.quality_29.setObjectName(u"quality_29")
        sizePolicy1.setHeightForWidth(self.quality_29.sizePolicy().hasHeightForWidth())
        self.quality_29.setSizePolicy(sizePolicy1)
        self.quality_29.setMinimumSize(QSize(0, 0))
        self.quality_29.setMaximumSize(QSize(167775, 167775))
        self.quality_29.setFont(font7)
        self.quality_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_29.setIconSize(QSize(30, 30))
        self.quality_29.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_29, 1, 13, 1, 1)

        self.quality_15 = QPushButton(self.quality_buttons)
        self.quality_15.setObjectName(u"quality_15")
        sizePolicy1.setHeightForWidth(self.quality_15.sizePolicy().hasHeightForWidth())
        self.quality_15.setSizePolicy(sizePolicy1)
        self.quality_15.setMinimumSize(QSize(0, 0))
        self.quality_15.setMaximumSize(QSize(167775, 167775))
        self.quality_15.setFont(font7)
        self.quality_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_15.setIconSize(QSize(30, 30))
        self.quality_15.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_15, 0, 14, 1, 1)

        self.quality_19 = QPushButton(self.quality_buttons)
        self.quality_19.setObjectName(u"quality_19")
        sizePolicy1.setHeightForWidth(self.quality_19.sizePolicy().hasHeightForWidth())
        self.quality_19.setSizePolicy(sizePolicy1)
        self.quality_19.setMinimumSize(QSize(0, 0))
        self.quality_19.setMaximumSize(QSize(167775, 167775))
        self.quality_19.setFont(font7)
        self.quality_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_19.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_19, 1, 3, 1, 1)

        self.quality_14 = QPushButton(self.quality_buttons)
        self.quality_14.setObjectName(u"quality_14")
        sizePolicy1.setHeightForWidth(self.quality_14.sizePolicy().hasHeightForWidth())
        self.quality_14.setSizePolicy(sizePolicy1)
        self.quality_14.setMinimumSize(QSize(0, 0))
        self.quality_14.setMaximumSize(QSize(167775, 167775))
        self.quality_14.setFont(font7)
        self.quality_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_14.setIconSize(QSize(30, 30))
        self.quality_14.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_14, 0, 13, 1, 1)

        self.quality_2 = QPushButton(self.quality_buttons)
        self.quality_2.setObjectName(u"quality_2")
        sizePolicy1.setHeightForWidth(self.quality_2.sizePolicy().hasHeightForWidth())
        self.quality_2.setSizePolicy(sizePolicy1)
        self.quality_2.setMinimumSize(QSize(0, 0))
        self.quality_2.setMaximumSize(QSize(167775, 167775))
        self.quality_2.setFont(font7)
        self.quality_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_2.setIconSize(QSize(30, 30))
        self.quality_2.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_2, 0, 1, 1, 1)

        self.quality_7 = QPushButton(self.quality_buttons)
        self.quality_7.setObjectName(u"quality_7")
        sizePolicy1.setHeightForWidth(self.quality_7.sizePolicy().hasHeightForWidth())
        self.quality_7.setSizePolicy(sizePolicy1)
        self.quality_7.setMinimumSize(QSize(0, 0))
        self.quality_7.setMaximumSize(QSize(167775, 167775))
        self.quality_7.setFont(font7)
        self.quality_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_7.setIconSize(QSize(30, 30))
        self.quality_7.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_7, 0, 6, 1, 1)

        self.quality_1 = QPushButton(self.quality_buttons)
        self.quality_1.setObjectName(u"quality_1")
        sizePolicy1.setHeightForWidth(self.quality_1.sizePolicy().hasHeightForWidth())
        self.quality_1.setSizePolicy(sizePolicy1)
        self.quality_1.setMinimumSize(QSize(0, 0))
        self.quality_1.setMaximumSize(QSize(167775, 167775))
        self.quality_1.setFont(font7)
        self.quality_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_1.setIconSize(QSize(30, 30))
        self.quality_1.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_1, 0, 0, 1, 1)

        self.quality_18 = QPushButton(self.quality_buttons)
        self.quality_18.setObjectName(u"quality_18")
        sizePolicy1.setHeightForWidth(self.quality_18.sizePolicy().hasHeightForWidth())
        self.quality_18.setSizePolicy(sizePolicy1)
        self.quality_18.setMinimumSize(QSize(0, 0))
        self.quality_18.setMaximumSize(QSize(167775, 167775))
        self.quality_18.setFont(font7)
        self.quality_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_18.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_18, 1, 2, 1, 1)

        self.quality_23 = QPushButton(self.quality_buttons)
        self.quality_23.setObjectName(u"quality_23")
        sizePolicy1.setHeightForWidth(self.quality_23.sizePolicy().hasHeightForWidth())
        self.quality_23.setSizePolicy(sizePolicy1)
        self.quality_23.setMinimumSize(QSize(0, 0))
        self.quality_23.setMaximumSize(QSize(167775, 167775))
        self.quality_23.setFont(font7)
        self.quality_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_23.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_23, 1, 7, 1, 1)

        self.quality_10 = QPushButton(self.quality_buttons)
        self.quality_10.setObjectName(u"quality_10")
        sizePolicy1.setHeightForWidth(self.quality_10.sizePolicy().hasHeightForWidth())
        self.quality_10.setSizePolicy(sizePolicy1)
        self.quality_10.setMinimumSize(QSize(0, 0))
        self.quality_10.setMaximumSize(QSize(167775, 167775))
        self.quality_10.setFont(font7)
        self.quality_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_10.setIconSize(QSize(30, 30))
        self.quality_10.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_10, 0, 9, 1, 1)

        self.quality_17 = QPushButton(self.quality_buttons)
        self.quality_17.setObjectName(u"quality_17")
        sizePolicy1.setHeightForWidth(self.quality_17.sizePolicy().hasHeightForWidth())
        self.quality_17.setSizePolicy(sizePolicy1)
        self.quality_17.setMinimumSize(QSize(0, 0))
        self.quality_17.setMaximumSize(QSize(167775, 167775))
        self.quality_17.setFont(font7)
        self.quality_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_17.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_17, 1, 1, 1, 1)

        self.quality_8 = QPushButton(self.quality_buttons)
        self.quality_8.setObjectName(u"quality_8")
        sizePolicy1.setHeightForWidth(self.quality_8.sizePolicy().hasHeightForWidth())
        self.quality_8.setSizePolicy(sizePolicy1)
        self.quality_8.setMinimumSize(QSize(0, 0))
        self.quality_8.setMaximumSize(QSize(167775, 167775))
        self.quality_8.setFont(font7)
        self.quality_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.quality_8.setIconSize(QSize(30, 30))
        self.quality_8.setCheckable(True)

        self.gridLayout_11.addWidget(self.quality_8, 0, 7, 1, 1)


        self.verticalLayout_16.addWidget(self.quality_buttons)

        self.splitter_7.addWidget(self.quality_options)

        self.verticalLayout_15.addWidget(self.splitter_7)


        self.verticalLayout_38.addWidget(self.item_options_container)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.proceed_btn = QPushButton(self.item_options_page)
        self.proceed_btn.setObjectName(u"proceed_btn")
        sizePolicy3.setHeightForWidth(self.proceed_btn.sizePolicy().hasHeightForWidth())
        self.proceed_btn.setSizePolicy(sizePolicy3)
        self.proceed_btn.setFont(font7)
        self.proceed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.proceed_btn.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 5px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")

        self.verticalLayout_19.addWidget(self.proceed_btn)

        self.crafting_simulator.addWidget(self.item_options_page)
        self.crafting_page = QWidget()
        self.crafting_page.setObjectName(u"crafting_page")
        sizePolicy.setHeightForWidth(self.crafting_page.sizePolicy().hasHeightForWidth())
        self.crafting_page.setSizePolicy(sizePolicy)
        self.crafting_page.setStyleSheet(u"border-image: url(:/icons/assets/images/emubg.png);")
        self.verticalLayout_17 = QVBoxLayout(self.crafting_page)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.crafting_methods = QWidget(self.crafting_page)
        self.crafting_methods.setObjectName(u"crafting_methods")
        sizePolicy1.setHeightForWidth(self.crafting_methods.sizePolicy().hasHeightForWidth())
        self.crafting_methods.setSizePolicy(sizePolicy1)
        self.crafting_methods.setMouseTracking(True)
        self.crafting_methods.setStyleSheet(u"border-image: none;")
        self.verticalLayout_7 = QVBoxLayout(self.crafting_methods)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.common_crafting_methods = QWidget(self.crafting_methods)
        self.common_crafting_methods.setObjectName(u"common_crafting_methods")
        sizePolicy1.setHeightForWidth(self.common_crafting_methods.sizePolicy().hasHeightForWidth())
        self.common_crafting_methods.setSizePolicy(sizePolicy1)
        self.common_crafting_methods.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"fontin-smallcaps"])
        font8.setPointSize(9)
        self.common_crafting_methods.setFont(font8)
        self.common_crafting_methods.setCursor(QCursor(Qt.PointingHandCursor))
        self.common_crafting_methods.setMouseTracking(True)
        self.common_crafting_methods.setFocusPolicy(Qt.ClickFocus)
        self.common_crafting_methods.setToolTipDuration(-3)
        self.common_crafting_methods.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.common_crafting_methods)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.method_transmute_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_transmute_btn.setObjectName(u"method_transmute_btn")
        sizePolicy1.setHeightForWidth(self.method_transmute_btn.sizePolicy().hasHeightForWidth())
        self.method_transmute_btn.setSizePolicy(sizePolicy1)
        self.method_transmute_btn.setMinimumSize(QSize(0, 0))
        self.method_transmute_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_transmute_btn.setMouseTracking(True)
        self.method_transmute_btn.setContextMenuPolicy(Qt.NoContextMenu)
        icon8 = QIcon()
        icon8.addFile(u":/crafting_methods/assets/images/crafting_methods/method_transmute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_transmute_btn.setIcon(icon8)
        self.method_transmute_btn.setIconSize(QSize(30, 30))
        self.method_transmute_btn.setCheckable(True)
        self.method_transmute_btn.setChecked(False)

        self.horizontalLayout_8.addWidget(self.method_transmute_btn)

        self.method_alteration_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_alteration_btn.setObjectName(u"method_alteration_btn")
        sizePolicy1.setHeightForWidth(self.method_alteration_btn.sizePolicy().hasHeightForWidth())
        self.method_alteration_btn.setSizePolicy(sizePolicy1)
        self.method_alteration_btn.setMinimumSize(QSize(0, 0))
        self.method_alteration_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_alteration_btn.setMouseTracking(True)
        icon9 = QIcon()
        icon9.addFile(u":/crafting_methods/assets/images/crafting_methods/method_alteration.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_alteration_btn.setIcon(icon9)
        self.method_alteration_btn.setIconSize(QSize(30, 30))
        self.method_alteration_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_alteration_btn)

        self.method_augmentation_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_augmentation_btn.setObjectName(u"method_augmentation_btn")
        sizePolicy1.setHeightForWidth(self.method_augmentation_btn.sizePolicy().hasHeightForWidth())
        self.method_augmentation_btn.setSizePolicy(sizePolicy1)
        self.method_augmentation_btn.setMinimumSize(QSize(0, 0))
        self.method_augmentation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_augmentation_btn.setMouseTracking(True)
        icon10 = QIcon()
        icon10.addFile(u":/crafting_methods/assets/images/crafting_methods/method_augmentation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_augmentation_btn.setIcon(icon10)
        self.method_augmentation_btn.setIconSize(QSize(30, 30))
        self.method_augmentation_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_augmentation_btn)

        self.method_regal_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_regal_btn.setObjectName(u"method_regal_btn")
        sizePolicy1.setHeightForWidth(self.method_regal_btn.sizePolicy().hasHeightForWidth())
        self.method_regal_btn.setSizePolicy(sizePolicy1)
        self.method_regal_btn.setMinimumSize(QSize(0, 0))
        self.method_regal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_regal_btn.setMouseTracking(True)
        icon11 = QIcon()
        icon11.addFile(u":/crafting_methods/assets/images/crafting_methods/method_regal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_regal_btn.setIcon(icon11)
        self.method_regal_btn.setIconSize(QSize(30, 30))
        self.method_regal_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_regal_btn)

        self.method_alchemy_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_alchemy_btn.setObjectName(u"method_alchemy_btn")
        sizePolicy1.setHeightForWidth(self.method_alchemy_btn.sizePolicy().hasHeightForWidth())
        self.method_alchemy_btn.setSizePolicy(sizePolicy1)
        self.method_alchemy_btn.setMinimumSize(QSize(0, 0))
        self.method_alchemy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_alchemy_btn.setMouseTracking(True)
        icon12 = QIcon()
        icon12.addFile(u":/crafting_methods/assets/images/crafting_methods/method_alchemy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_alchemy_btn.setIcon(icon12)
        self.method_alchemy_btn.setIconSize(QSize(30, 30))
        self.method_alchemy_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_alchemy_btn)

        self.method_chaos_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_chaos_btn.setObjectName(u"method_chaos_btn")
        sizePolicy1.setHeightForWidth(self.method_chaos_btn.sizePolicy().hasHeightForWidth())
        self.method_chaos_btn.setSizePolicy(sizePolicy1)
        self.method_chaos_btn.setMinimumSize(QSize(0, 0))
        self.method_chaos_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_chaos_btn.setMouseTracking(True)
        icon13 = QIcon()
        icon13.addFile(u":/crafting_methods/assets/images/crafting_methods/method_chaos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_chaos_btn.setIcon(icon13)
        self.method_chaos_btn.setIconSize(QSize(30, 30))
        self.method_chaos_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_chaos_btn)

        self.method_exalted_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_exalted_btn.setObjectName(u"method_exalted_btn")
        sizePolicy1.setHeightForWidth(self.method_exalted_btn.sizePolicy().hasHeightForWidth())
        self.method_exalted_btn.setSizePolicy(sizePolicy1)
        self.method_exalted_btn.setMinimumSize(QSize(0, 0))
        self.method_exalted_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_exalted_btn.setMouseTracking(True)
        icon14 = QIcon()
        icon14.addFile(u":/crafting_methods/assets/images/crafting_methods/method_exalted.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_exalted_btn.setIcon(icon14)
        self.method_exalted_btn.setIconSize(QSize(30, 30))
        self.method_exalted_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_exalted_btn)

        self.method_scour_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_scour_btn.setObjectName(u"method_scour_btn")
        sizePolicy1.setHeightForWidth(self.method_scour_btn.sizePolicy().hasHeightForWidth())
        self.method_scour_btn.setSizePolicy(sizePolicy1)
        self.method_scour_btn.setMinimumSize(QSize(0, 0))
        self.method_scour_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_scour_btn.setMouseTracking(True)
        icon15 = QIcon()
        icon15.addFile(u":/crafting_methods/assets/images/crafting_methods/method_scour.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_scour_btn.setIcon(icon15)
        self.method_scour_btn.setIconSize(QSize(30, 30))
        self.method_scour_btn.setCheckable(True)
        self.method_scour_btn.setChecked(False)

        self.horizontalLayout_8.addWidget(self.method_scour_btn)

        self.method_annul_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_annul_btn.setObjectName(u"method_annul_btn")
        sizePolicy1.setHeightForWidth(self.method_annul_btn.sizePolicy().hasHeightForWidth())
        self.method_annul_btn.setSizePolicy(sizePolicy1)
        self.method_annul_btn.setMinimumSize(QSize(0, 0))
        self.method_annul_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_annul_btn.setMouseTracking(True)
        icon16 = QIcon()
        icon16.addFile(u":/crafting_methods/assets/images/crafting_methods/method_annul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_annul_btn.setIcon(icon16)
        self.method_annul_btn.setIconSize(QSize(30, 30))
        self.method_annul_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_annul_btn)

        self.method_crusader_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_crusader_btn.setObjectName(u"method_crusader_btn")
        sizePolicy1.setHeightForWidth(self.method_crusader_btn.sizePolicy().hasHeightForWidth())
        self.method_crusader_btn.setSizePolicy(sizePolicy1)
        self.method_crusader_btn.setMinimumSize(QSize(0, 0))
        self.method_crusader_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_crusader_btn.setMouseTracking(True)
        icon17 = QIcon()
        icon17.addFile(u":/crafting_methods/assets/images/crafting_methods/method_crusader.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_crusader_btn.setIcon(icon17)
        self.method_crusader_btn.setIconSize(QSize(30, 30))
        self.method_crusader_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_crusader_btn)

        self.method_hunter_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_hunter_btn.setObjectName(u"method_hunter_btn")
        sizePolicy1.setHeightForWidth(self.method_hunter_btn.sizePolicy().hasHeightForWidth())
        self.method_hunter_btn.setSizePolicy(sizePolicy1)
        self.method_hunter_btn.setMinimumSize(QSize(0, 0))
        self.method_hunter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_hunter_btn.setMouseTracking(True)
        icon18 = QIcon()
        icon18.addFile(u":/crafting_methods/assets/images/crafting_methods/method_hunter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_hunter_btn.setIcon(icon18)
        self.method_hunter_btn.setIconSize(QSize(30, 30))
        self.method_hunter_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_hunter_btn)

        self.method_redeemer_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_redeemer_btn.setObjectName(u"method_redeemer_btn")
        sizePolicy1.setHeightForWidth(self.method_redeemer_btn.sizePolicy().hasHeightForWidth())
        self.method_redeemer_btn.setSizePolicy(sizePolicy1)
        self.method_redeemer_btn.setMinimumSize(QSize(0, 0))
        self.method_redeemer_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_redeemer_btn.setMouseTracking(True)
        icon19 = QIcon()
        icon19.addFile(u":/crafting_methods/assets/images/crafting_methods/method_redeemer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_redeemer_btn.setIcon(icon19)
        self.method_redeemer_btn.setIconSize(QSize(30, 30))
        self.method_redeemer_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_redeemer_btn)

        self.method_warlord_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_warlord_btn.setObjectName(u"method_warlord_btn")
        sizePolicy1.setHeightForWidth(self.method_warlord_btn.sizePolicy().hasHeightForWidth())
        self.method_warlord_btn.setSizePolicy(sizePolicy1)
        self.method_warlord_btn.setMinimumSize(QSize(0, 0))
        self.method_warlord_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_warlord_btn.setMouseTracking(True)
        icon20 = QIcon()
        icon20.addFile(u":/crafting_methods/assets/images/crafting_methods/method_warlord.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_warlord_btn.setIcon(icon20)
        self.method_warlord_btn.setIconSize(QSize(30, 30))
        self.method_warlord_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_warlord_btn)

        self.method_blessed_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_blessed_btn.setObjectName(u"method_blessed_btn")
        sizePolicy1.setHeightForWidth(self.method_blessed_btn.sizePolicy().hasHeightForWidth())
        self.method_blessed_btn.setSizePolicy(sizePolicy1)
        self.method_blessed_btn.setMinimumSize(QSize(0, 0))
        self.method_blessed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_blessed_btn.setMouseTracking(True)
        icon21 = QIcon()
        icon21.addFile(u":/crafting_methods/assets/images/crafting_methods/method_blessed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_blessed_btn.setIcon(icon21)
        self.method_blessed_btn.setIconSize(QSize(30, 30))
        self.method_blessed_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_blessed_btn)

        self.method_divine_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_divine_btn.setObjectName(u"method_divine_btn")
        sizePolicy1.setHeightForWidth(self.method_divine_btn.sizePolicy().hasHeightForWidth())
        self.method_divine_btn.setSizePolicy(sizePolicy1)
        self.method_divine_btn.setMinimumSize(QSize(0, 0))
        self.method_divine_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_divine_btn.setMouseTracking(True)
        icon22 = QIcon()
        icon22.addFile(u":/crafting_methods/assets/images/crafting_methods/method_divine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_divine_btn.setIcon(icon22)
        self.method_divine_btn.setIconSize(QSize(30, 30))
        self.method_divine_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_divine_btn)

        self.method_veiled_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_veiled_btn.setObjectName(u"method_veiled_btn")
        sizePolicy1.setHeightForWidth(self.method_veiled_btn.sizePolicy().hasHeightForWidth())
        self.method_veiled_btn.setSizePolicy(sizePolicy1)
        self.method_veiled_btn.setMinimumSize(QSize(0, 0))
        self.method_veiled_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_veiled_btn.setMouseTracking(True)
        icon23 = QIcon()
        icon23.addFile(u":/crafting_methods/assets/images/crafting_methods/method_veiled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_veiled_btn.setIcon(icon23)
        self.method_veiled_btn.setIconSize(QSize(30, 30))
        self.method_veiled_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_veiled_btn)

        self.method_woke_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_woke_btn.setObjectName(u"method_woke_btn")
        sizePolicy1.setHeightForWidth(self.method_woke_btn.sizePolicy().hasHeightForWidth())
        self.method_woke_btn.setSizePolicy(sizePolicy1)
        self.method_woke_btn.setMinimumSize(QSize(0, 0))
        self.method_woke_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_woke_btn.setMouseTracking(True)
        icon24 = QIcon()
        icon24.addFile(u":/crafting_methods/assets/images/crafting_methods/method_woke.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_woke_btn.setIcon(icon24)
        self.method_woke_btn.setIconSize(QSize(30, 30))
        self.method_woke_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_woke_btn)

        self.method_maven_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_maven_btn.setObjectName(u"method_maven_btn")
        sizePolicy1.setHeightForWidth(self.method_maven_btn.sizePolicy().hasHeightForWidth())
        self.method_maven_btn.setSizePolicy(sizePolicy1)
        self.method_maven_btn.setMinimumSize(QSize(0, 0))
        self.method_maven_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_maven_btn.setMouseTracking(True)
        icon25 = QIcon()
        icon25.addFile(u":/crafting_methods/assets/images/crafting_methods/method_maven.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_maven_btn.setIcon(icon25)
        self.method_maven_btn.setIconSize(QSize(30, 30))
        self.method_maven_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_maven_btn)

        self.method_fracturing_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_fracturing_btn.setObjectName(u"method_fracturing_btn")
        sizePolicy1.setHeightForWidth(self.method_fracturing_btn.sizePolicy().hasHeightForWidth())
        self.method_fracturing_btn.setSizePolicy(sizePolicy1)
        self.method_fracturing_btn.setMinimumSize(QSize(0, 0))
        self.method_fracturing_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_fracturing_btn.setMouseTracking(True)
        icon26 = QIcon()
        icon26.addFile(u":/crafting_methods/assets/images/crafting_methods/method_fracturing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_fracturing_btn.setIcon(icon26)
        self.method_fracturing_btn.setIconSize(QSize(30, 30))
        self.method_fracturing_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_fracturing_btn)

        self.locus_btn = CustomCursorButton(self.common_crafting_methods)
        self.locus_btn.setObjectName(u"locus_btn")
        sizePolicy1.setHeightForWidth(self.locus_btn.sizePolicy().hasHeightForWidth())
        self.locus_btn.setSizePolicy(sizePolicy1)
        self.locus_btn.setMinimumSize(QSize(0, 0))
        self.locus_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.locus_btn.setMouseTracking(True)
        icon27 = QIcon()
        icon27.addFile(u":/images/assets/images/locus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locus_btn.setIcon(icon27)
        self.locus_btn.setIconSize(QSize(30, 30))
        self.locus_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.locus_btn)

        self.method_vaal_btn = CustomCursorButton(self.common_crafting_methods)
        self.method_vaal_btn.setObjectName(u"method_vaal_btn")
        sizePolicy1.setHeightForWidth(self.method_vaal_btn.sizePolicy().hasHeightForWidth())
        self.method_vaal_btn.setSizePolicy(sizePolicy1)
        self.method_vaal_btn.setMinimumSize(QSize(0, 0))
        self.method_vaal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_vaal_btn.setMouseTracking(True)
        icon28 = QIcon()
        icon28.addFile(u":/crafting_methods/assets/images/crafting_methods/method_vaal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_vaal_btn.setIcon(icon28)
        self.method_vaal_btn.setIconSize(QSize(30, 30))
        self.method_vaal_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_vaal_btn)


        self.verticalLayout_7.addWidget(self.common_crafting_methods)

        self.crafting_method_group_btns = QWidget(self.crafting_methods)
        self.crafting_method_group_btns.setObjectName(u"crafting_method_group_btns")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.crafting_method_group_btns.sizePolicy().hasHeightForWidth())
        self.crafting_method_group_btns.setSizePolicy(sizePolicy7)
        self.crafting_method_group_btns.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;")
        self.horizontalLayout_9 = QHBoxLayout(self.crafting_method_group_btns)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.method_fossil_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group = QButtonGroup(MainWindow)
        self.crafting_method_group_btns_group.setObjectName(u"crafting_method_group_btns_group")
        self.crafting_method_group_btns_group.addButton(self.method_fossil_btn)
        self.method_fossil_btn.setObjectName(u"method_fossil_btn")
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
        icon29 = QIcon()
        icon29.addFile(u":/crafting_methods/assets/images/crafting_methods/method_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_fossil_btn.setIcon(icon29)
        self.method_fossil_btn.setIconSize(QSize(30, 30))
        self.method_fossil_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_fossil_btn)

        self.method_harvest_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.method_harvest_btn)
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
        icon30 = QIcon()
        icon30.addFile(u":/crafting_methods/assets/images/crafting_methods/method_harvest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_harvest_btn.setIcon(icon30)
        self.method_harvest_btn.setIconSize(QSize(30, 30))
        self.method_harvest_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_harvest_btn)

        self.method_essence_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.method_essence_btn)
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
        icon31 = QIcon()
        icon31.addFile(u":/crafting_methods/assets/images/crafting_methods/method_essence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_essence_btn.setIcon(icon31)
        self.method_essence_btn.setIconSize(QSize(30, 30))
        self.method_essence_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_essence_btn)

        self.catalyst_method_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.catalyst_method_btn)
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
        icon32 = QIcon()
        icon32.addFile(u":/crafting_methods/assets/images/crafting_methods/method_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catalyst_method_btn.setIcon(icon32)
        self.catalyst_method_btn.setIconSize(QSize(30, 30))
        self.catalyst_method_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.catalyst_method_btn)

        self.method_imprint_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.method_imprint_btn)
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
        icon33 = QIcon()
        icon33.addFile(u":/crafting_methods/assets/images/crafting_methods/method_imprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_imprint_btn.setIcon(icon33)
        self.method_imprint_btn.setIconSize(QSize(30, 30))
        self.method_imprint_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_imprint_btn)

        self.eldritch_method_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.eldritch_method_btn)
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
        icon34 = QIcon()
        icon34.addFile(u":/crafting_methods/assets/images/crafting_methods/method_eldritch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_method_btn.setIcon(icon34)
        self.eldritch_method_btn.setIconSize(QSize(30, 30))
        self.eldritch_method_btn.setCheckable(True)
        self.eldritch_method_btn.setChecked(False)

        self.horizontalLayout_9.addWidget(self.eldritch_method_btn)

        self.method_syndicate_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.method_syndicate_btn)
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
        icon35 = QIcon()
        icon35.addFile(u":/crafting_methods/assets/images/crafting_methods/method_syndicate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_syndicate_btn.setIcon(icon35)
        self.method_syndicate_btn.setIconSize(QSize(30, 30))
        self.method_syndicate_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_syndicate_btn)

        self.method_crafting_bench_btn = QPushButton(self.crafting_method_group_btns)
        self.crafting_method_group_btns_group.addButton(self.method_crafting_bench_btn)
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
        icon36 = QIcon()
        icon36.addFile(u":/crafting_methods/assets/images/crafting_methods/method_crafting_bench.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_crafting_bench_btn.setIcon(icon36)
        self.method_crafting_bench_btn.setIconSize(QSize(30, 30))
        self.method_crafting_bench_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_crafting_bench_btn)


        self.verticalLayout_7.addWidget(self.crafting_method_group_btns, 0, Qt.AlignTop)

        self.crafting_method_pages = QStackedWidget(self.crafting_methods)
        self.crafting_method_pages.setObjectName(u"crafting_method_pages")
        self.crafting_method_pages.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.crafting_method_pages.sizePolicy().hasHeightForWidth())
        self.crafting_method_pages.setSizePolicy(sizePolicy7)
        self.crafting_method_pages.setStyleSheet(u"\n"
"QWidget {\n"
"border-image: none;\n"
"}\n"
"QStackedWidget {\n"
"border-image: none;\n"
"}\n"
"QFrame {\n"
"border-image: none;\n"
"}\n"
"QLabel {\n"
"text-align: center;\n"
"padding: 5px 10px;\n"
"font-size: 12px;\n"
"background-color: #000;\n"
"width: 100%;\n"
"box-sizing: border-box;\n"
"color: #FFF;\n"
"font-family: Open Sans;\n"
"}\n"
"\n"
"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px"
                        " #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"           }\n"
"            QPushButton::pressed {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                                  stop: 0 #4b4b4b, stop: 1 #2d2d2d);\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.fossil_crafts = QWidget()
        self.fossil_crafts.setObjectName(u"fossil_crafts")
        self.fossil_crafts.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.fossil_crafts.sizePolicy().hasHeightForWidth())
        self.fossil_crafts.setSizePolicy(sizePolicy7)
        self.verticalLayout_23 = QVBoxLayout(self.fossil_crafts)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.fossil_btns_container = QWidget(self.fossil_crafts)
        self.fossil_btns_container.setObjectName(u"fossil_btns_container")
        self.fossil_btns_container.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.fossil_btns_container.sizePolicy().hasHeightForWidth())
        self.fossil_btns_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_24 = QVBoxLayout(self.fossil_btns_container)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.fossil_btn_row1 = QWidget(self.fossil_btns_container)
        self.fossil_btn_row1.setObjectName(u"fossil_btn_row1")
        self.fossil_btn_row1.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.fossil_btn_row1.sizePolicy().hasHeightForWidth())
        self.fossil_btn_row1.setSizePolicy(sizePolicy6)
        self.fossil_row1 = QHBoxLayout(self.fossil_btn_row1)
        self.fossil_row1.setSpacing(0)
        self.fossil_row1.setContentsMargins(0, 0, 0, 0)
        self.fossil_row1.setObjectName(u"fossil_row1")
        self.fossil_row1.setContentsMargins(0, 0, 0, 0)
        self.fossil_hide_button = QPushButton(self.fossil_btn_row1)
        self.fossil_hide_button.setObjectName(u"fossil_hide_button")
        self.fossil_hide_button.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.fossil_hide_button.sizePolicy().hasHeightForWidth())
        self.fossil_hide_button.setSizePolicy(sizePolicy8)
        self.fossil_hide_button.setFont(font2)
        self.fossil_hide_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.fossil_hide_button.setContextMenuPolicy(Qt.NoContextMenu)
        self.fossil_hide_button.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.fossil_hide_button.setCheckable(True)

        self.fossil_row1.addWidget(self.fossil_hide_button)

        self.fossil_label = QLabel(self.fossil_btn_row1)
        self.fossil_label.setObjectName(u"fossil_label")
        self.fossil_label.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.fossil_label.sizePolicy().hasHeightForWidth())
        self.fossil_label.setSizePolicy(sizePolicy8)

        self.fossil_row1.addWidget(self.fossil_label)

        self.abberant_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup = QButtonGroup(MainWindow)
        self.fossil_btns_broup.setObjectName(u"fossil_btns_broup")
        self.fossil_btns_broup.setExclusive(False)
        self.fossil_btns_broup.addButton(self.abberant_fossil)
        self.abberant_fossil.setObjectName(u"abberant_fossil")
        self.abberant_fossil.setEnabled(True)
        sizePolicy.setHeightForWidth(self.abberant_fossil.sizePolicy().hasHeightForWidth())
        self.abberant_fossil.setSizePolicy(sizePolicy)
        self.abberant_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.abberant_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon37 = QIcon()
        icon37.addFile(u":/fossils/assets/images/fossils/aberrant_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abberant_fossil.setIcon(icon37)
        self.abberant_fossil.setIconSize(QSize(30, 30))
        self.abberant_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.abberant_fossil)

        self.aetheric_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.aetheric_fossil)
        self.aetheric_fossil.setObjectName(u"aetheric_fossil")
        self.aetheric_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.aetheric_fossil.sizePolicy().hasHeightForWidth())
        self.aetheric_fossil.setSizePolicy(sizePolicy1)
        self.aetheric_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.aetheric_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon38 = QIcon()
        icon38.addFile(u":/fossils/assets/images/fossils/aetheric_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aetheric_fossil.setIcon(icon38)
        self.aetheric_fossil.setIconSize(QSize(30, 30))
        self.aetheric_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.aetheric_fossil)

        self.bound_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.bound_fossil)
        self.bound_fossil.setObjectName(u"bound_fossil")
        self.bound_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bound_fossil.sizePolicy().hasHeightForWidth())
        self.bound_fossil.setSizePolicy(sizePolicy1)
        self.bound_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.bound_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon39 = QIcon()
        icon39.addFile(u":/fossils/assets/images/fossils/bound_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bound_fossil.setIcon(icon39)
        self.bound_fossil.setIconSize(QSize(30, 30))
        self.bound_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.bound_fossil)

        self.corroded_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.corroded_fossil)
        self.corroded_fossil.setObjectName(u"corroded_fossil")
        self.corroded_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.corroded_fossil.sizePolicy().hasHeightForWidth())
        self.corroded_fossil.setSizePolicy(sizePolicy1)
        self.corroded_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.corroded_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon40 = QIcon()
        icon40.addFile(u":/fossils/assets/images/fossils/corroded_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.corroded_fossil.setIcon(icon40)
        self.corroded_fossil.setIconSize(QSize(30, 30))
        self.corroded_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.corroded_fossil)

        self.dense_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.dense_fossil)
        self.dense_fossil.setObjectName(u"dense_fossil")
        self.dense_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.dense_fossil.sizePolicy().hasHeightForWidth())
        self.dense_fossil.setSizePolicy(sizePolicy1)
        self.dense_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.dense_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon41 = QIcon()
        icon41.addFile(u":/fossils/assets/images/fossils/dense_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dense_fossil.setIcon(icon41)
        self.dense_fossil.setIconSize(QSize(30, 30))

        self.fossil_row1.addWidget(self.dense_fossil)

        self.faceted_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.faceted_fossil)
        self.faceted_fossil.setObjectName(u"faceted_fossil")
        self.faceted_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.faceted_fossil.sizePolicy().hasHeightForWidth())
        self.faceted_fossil.setSizePolicy(sizePolicy1)
        self.faceted_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.faceted_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon42 = QIcon()
        icon42.addFile(u":/fossils/assets/images/fossils/faceted_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.faceted_fossil.setIcon(icon42)
        self.faceted_fossil.setIconSize(QSize(30, 30))
        self.faceted_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.faceted_fossil)

        self.frigid_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.frigid_fossil)
        self.frigid_fossil.setObjectName(u"frigid_fossil")
        self.frigid_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frigid_fossil.sizePolicy().hasHeightForWidth())
        self.frigid_fossil.setSizePolicy(sizePolicy1)
        self.frigid_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.frigid_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon43 = QIcon()
        icon43.addFile(u":/fossils/assets/images/fossils/frigid_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frigid_fossil.setIcon(icon43)
        self.frigid_fossil.setIconSize(QSize(30, 30))
        self.frigid_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.frigid_fossil)

        self.jagged_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.jagged_fossil)
        self.jagged_fossil.setObjectName(u"jagged_fossil")
        self.jagged_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.jagged_fossil.sizePolicy().hasHeightForWidth())
        self.jagged_fossil.setSizePolicy(sizePolicy1)
        self.jagged_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.jagged_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon44 = QIcon()
        icon44.addFile(u":/fossils/assets/images/fossils/jagged_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jagged_fossil.setIcon(icon44)
        self.jagged_fossil.setIconSize(QSize(30, 30))
        self.jagged_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.jagged_fossil)

        self.lucent_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.lucent_fossil)
        self.lucent_fossil.setObjectName(u"lucent_fossil")
        self.lucent_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lucent_fossil.sizePolicy().hasHeightForWidth())
        self.lucent_fossil.setSizePolicy(sizePolicy1)
        self.lucent_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.lucent_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon45 = QIcon()
        icon45.addFile(u":/fossils/assets/images/fossils/lucent_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lucent_fossil.setIcon(icon45)
        self.lucent_fossil.setIconSize(QSize(30, 30))
        self.lucent_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.lucent_fossil)

        self.metallic_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.metallic_fossil)
        self.metallic_fossil.setObjectName(u"metallic_fossil")
        self.metallic_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.metallic_fossil.sizePolicy().hasHeightForWidth())
        self.metallic_fossil.setSizePolicy(sizePolicy1)
        self.metallic_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        icon46 = QIcon()
        icon46.addFile(u":/fossils/assets/images/fossils/metallic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.metallic_fossil.setIcon(icon46)
        self.metallic_fossil.setIconSize(QSize(30, 30))
        self.metallic_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.metallic_fossil)

        self.prismatic_fossil = CustomCursorButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.prismatic_fossil)
        self.prismatic_fossil.setObjectName(u"prismatic_fossil")
        self.prismatic_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.prismatic_fossil.sizePolicy().hasHeightForWidth())
        self.prismatic_fossil.setSizePolicy(sizePolicy1)
        self.prismatic_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.prismatic_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon47 = QIcon()
        icon47.addFile(u":/fossils/assets/images/fossils/prismatic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prismatic_fossil.setIcon(icon47)
        self.prismatic_fossil.setIconSize(QSize(30, 30))
        self.prismatic_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.prismatic_fossil)


        self.verticalLayout_24.addWidget(self.fossil_btn_row1)

        self.fossil_btn_row2 = QWidget(self.fossil_btns_container)
        self.fossil_btn_row2.setObjectName(u"fossil_btn_row2")
        self.fossil_btn_row2.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.fossil_btn_row2.sizePolicy().hasHeightForWidth())
        self.fossil_btn_row2.setSizePolicy(sizePolicy6)
        self.fossil_row2 = QHBoxLayout(self.fossil_btn_row2)
        self.fossil_row2.setSpacing(0)
        self.fossil_row2.setContentsMargins(0, 0, 0, 0)
        self.fossil_row2.setObjectName(u"fossil_row2")
        self.fossil_row2.setContentsMargins(0, 0, 0, 0)
        self.pristine_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.pristine_fossil)
        self.pristine_fossil.setObjectName(u"pristine_fossil")
        self.pristine_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pristine_fossil.sizePolicy().hasHeightForWidth())
        self.pristine_fossil.setSizePolicy(sizePolicy1)
        self.pristine_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.pristine_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon48 = QIcon()
        icon48.addFile(u":/fossils/assets/images/fossils/pristine_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pristine_fossil.setIcon(icon48)
        self.pristine_fossil.setIconSize(QSize(30, 30))
        self.pristine_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.pristine_fossil)

        self.scorched_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.scorched_fossil)
        self.scorched_fossil.setObjectName(u"scorched_fossil")
        self.scorched_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.scorched_fossil.sizePolicy().hasHeightForWidth())
        self.scorched_fossil.setSizePolicy(sizePolicy1)
        self.scorched_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.scorched_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon49 = QIcon()
        icon49.addFile(u":/fossils/assets/images/fossils/scorched_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scorched_fossil.setIcon(icon49)
        self.scorched_fossil.setIconSize(QSize(30, 30))
        self.scorched_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.scorched_fossil)

        self.serrated_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.serrated_fossil)
        self.serrated_fossil.setObjectName(u"serrated_fossil")
        self.serrated_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.serrated_fossil.sizePolicy().hasHeightForWidth())
        self.serrated_fossil.setSizePolicy(sizePolicy1)
        self.serrated_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.serrated_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon50 = QIcon()
        icon50.addFile(u":/fossils/assets/images/fossils/serrated_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.serrated_fossil.setIcon(icon50)
        self.serrated_fossil.setIconSize(QSize(30, 30))
        self.serrated_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.serrated_fossil)

        self.shuddering_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.shuddering_fossil)
        self.shuddering_fossil.setObjectName(u"shuddering_fossil")
        self.shuddering_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.shuddering_fossil.sizePolicy().hasHeightForWidth())
        self.shuddering_fossil.setSizePolicy(sizePolicy1)
        self.shuddering_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.shuddering_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon51 = QIcon()
        icon51.addFile(u":/fossils/assets/images/fossils/shuddering_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shuddering_fossil.setIcon(icon51)
        self.shuddering_fossil.setIconSize(QSize(30, 30))
        self.shuddering_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.shuddering_fossil)

        self.hollow_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.hollow_fossil)
        self.hollow_fossil.setObjectName(u"hollow_fossil")
        self.hollow_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.hollow_fossil.sizePolicy().hasHeightForWidth())
        self.hollow_fossil.setSizePolicy(sizePolicy1)
        self.hollow_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.hollow_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon52 = QIcon()
        icon52.addFile(u":/fossils/assets/images/fossils/hollow_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hollow_fossil.setIcon(icon52)
        self.hollow_fossil.setIconSize(QSize(30, 30))
        self.hollow_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.hollow_fossil)

        self.sanctified_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.sanctified_fossil)
        self.sanctified_fossil.setObjectName(u"sanctified_fossil")
        self.sanctified_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sanctified_fossil.sizePolicy().hasHeightForWidth())
        self.sanctified_fossil.setSizePolicy(sizePolicy1)
        self.sanctified_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.sanctified_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon53 = QIcon()
        icon53.addFile(u":/fossils/assets/images/fossils/sanctified_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sanctified_fossil.setIcon(icon53)
        self.sanctified_fossil.setIconSize(QSize(30, 30))
        self.sanctified_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.sanctified_fossil)

        self.glyphic_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.glyphic_fossil)
        self.glyphic_fossil.setObjectName(u"glyphic_fossil")
        self.glyphic_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.glyphic_fossil.sizePolicy().hasHeightForWidth())
        self.glyphic_fossil.setSizePolicy(sizePolicy1)
        self.glyphic_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.glyphic_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon54 = QIcon()
        icon54.addFile(u":/fossils/assets/images/fossils/glyphic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.glyphic_fossil.setIcon(icon54)
        self.glyphic_fossil.setIconSize(QSize(30, 30))
        self.glyphic_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.glyphic_fossil)

        self.fundamental_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.fundamental_fossil)
        self.fundamental_fossil.setObjectName(u"fundamental_fossil")
        self.fundamental_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.fundamental_fossil.sizePolicy().hasHeightForWidth())
        self.fundamental_fossil.setSizePolicy(sizePolicy1)
        self.fundamental_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.fundamental_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon55 = QIcon()
        icon55.addFile(u":/fossils/assets/images/fossils/fundamental_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fundamental_fossil.setIcon(icon55)
        self.fundamental_fossil.setIconSize(QSize(30, 30))
        self.fundamental_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.fundamental_fossil)

        self.deft_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.deft_fossil)
        self.deft_fossil.setObjectName(u"deft_fossil")
        self.deft_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.deft_fossil.sizePolicy().hasHeightForWidth())
        self.deft_fossil.setSizePolicy(sizePolicy1)
        self.deft_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.deft_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon56 = QIcon()
        icon56.addFile(u":/fossils/assets/images/fossils/deft_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deft_fossil.setIcon(icon56)
        self.deft_fossil.setIconSize(QSize(30, 30))
        self.deft_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.deft_fossil)

        self.gilded_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.gilded_fossil)
        self.gilded_fossil.setObjectName(u"gilded_fossil")
        self.gilded_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.gilded_fossil.sizePolicy().hasHeightForWidth())
        self.gilded_fossil.setSizePolicy(sizePolicy1)
        self.gilded_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.gilded_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon57 = QIcon()
        icon57.addFile(u":/fossils/assets/images/fossils/gilded_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gilded_fossil.setIcon(icon57)
        self.gilded_fossil.setIconSize(QSize(30, 30))
        self.gilded_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.gilded_fossil)

        self.perfect_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.perfect_fossil)
        self.perfect_fossil.setObjectName(u"perfect_fossil")
        self.perfect_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.perfect_fossil.sizePolicy().hasHeightForWidth())
        self.perfect_fossil.setSizePolicy(sizePolicy1)
        self.perfect_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.perfect_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon58 = QIcon()
        icon58.addFile(u":/fossils/assets/images/fossils/perfect_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfect_fossil.setIcon(icon58)
        self.perfect_fossil.setIconSize(QSize(30, 30))
        self.perfect_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.perfect_fossil)

        self.tangled_fossil = CustomCursorButton(self.fossil_btn_row2)
        self.fossil_btns_broup.addButton(self.tangled_fossil)
        self.tangled_fossil.setObjectName(u"tangled_fossil")
        self.tangled_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.tangled_fossil.sizePolicy().hasHeightForWidth())
        self.tangled_fossil.setSizePolicy(sizePolicy1)
        self.tangled_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        self.tangled_fossil.setStyleSheet(u"QPushButton {\n"
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
        icon59 = QIcon()
        icon59.addFile(u":/fossils/assets/images/fossils/tangled_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tangled_fossil.setIcon(icon59)
        self.tangled_fossil.setIconSize(QSize(30, 30))
        self.tangled_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.tangled_fossil)


        self.verticalLayout_24.addWidget(self.fossil_btn_row2)


        self.verticalLayout_23.addWidget(self.fossil_btns_container, 0, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.fossil_crafts)
        self.harvest_crafts = QWidget()
        self.harvest_crafts.setObjectName(u"harvest_crafts")
        sizePolicy7.setHeightForWidth(self.harvest_crafts.sizePolicy().hasHeightForWidth())
        self.harvest_crafts.setSizePolicy(sizePolicy7)
        self.horizontalLayout_7 = QHBoxLayout(self.harvest_crafts)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.harvest_btns_container = QWidget(self.harvest_crafts)
        self.harvest_btns_container.setObjectName(u"harvest_btns_container")
        self.harvest_btns_container.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_btns_container.sizePolicy().hasHeightForWidth())
        self.harvest_btns_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_45 = QVBoxLayout(self.harvest_btns_container)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.harvest_btn_row1 = QWidget(self.harvest_btns_container)
        self.harvest_btn_row1.setObjectName(u"harvest_btn_row1")
        self.harvest_btn_row1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.harvest_btn_row1.sizePolicy().hasHeightForWidth())
        self.harvest_btn_row1.setSizePolicy(sizePolicy4)
        self.harvest_btn_row1.setStyleSheet(u"QPushButton {\n"
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
        self.fossil_row1_2 = QHBoxLayout(self.harvest_btn_row1)
        self.fossil_row1_2.setSpacing(0)
        self.fossil_row1_2.setContentsMargins(0, 0, 0, 0)
        self.fossil_row1_2.setObjectName(u"fossil_row1_2")
        self.fossil_row1_2.setContentsMargins(0, 0, 0, 0)
        self.harvest_hide_btn = QPushButton(self.harvest_btn_row1)
        self.harvest_hide_btn.setObjectName(u"harvest_hide_btn")
        self.harvest_hide_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_hide_btn.sizePolicy().hasHeightForWidth())
        self.harvest_hide_btn.setSizePolicy(sizePolicy1)
        self.harvest_hide_btn.setFont(font2)
        self.harvest_hide_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.harvest_hide_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")

        self.fossil_row1_2.addWidget(self.harvest_hide_btn, 0, Qt.AlignLeft)

        self.harvest_method_label = QLabel(self.harvest_btn_row1)
        self.harvest_method_label.setObjectName(u"harvest_method_label")
        self.harvest_method_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_method_label.sizePolicy().hasHeightForWidth())
        self.harvest_method_label.setSizePolicy(sizePolicy1)
        self.harvest_method_label.setFont(font2)

        self.fossil_row1_2.addWidget(self.harvest_method_label, 0, Qt.AlignLeft)

        self.harvest_add_remove_btn = CustomCursorButton(self.harvest_btn_row1)
        self.harvest_group_btns_group = QButtonGroup(MainWindow)
        self.harvest_group_btns_group.setObjectName(u"harvest_group_btns_group")
        self.harvest_group_btns_group.addButton(self.harvest_add_remove_btn)
        self.harvest_add_remove_btn.setObjectName(u"harvest_add_remove_btn")
        self.harvest_add_remove_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_add_remove_btn.sizePolicy().hasHeightForWidth())
        self.harvest_add_remove_btn.setSizePolicy(sizePolicy1)
        self.harvest_add_remove_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_add_remove_btn.setStyleSheet(u"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {         \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
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
        icon60 = QIcon()
        icon60.addFile(u":/harvest/assets/images/harvest/harvest_augment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harvest_add_remove_btn.setIcon(icon60)
        self.harvest_add_remove_btn.setIconSize(QSize(30, 30))
        self.harvest_add_remove_btn.setCheckable(True)
        self.harvest_add_remove_btn.setChecked(False)

        self.fossil_row1_2.addWidget(self.harvest_add_remove_btn)

        self.harvest_reroll_btn = CustomCursorButton(self.harvest_btn_row1)
        self.harvest_group_btns_group.addButton(self.harvest_reroll_btn)
        self.harvest_reroll_btn.setObjectName(u"harvest_reroll_btn")
        self.harvest_reroll_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_reroll_btn.sizePolicy().hasHeightForWidth())
        self.harvest_reroll_btn.setSizePolicy(sizePolicy1)
        self.harvest_reroll_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_reroll_btn.setStyleSheet(u"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {         \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
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
        icon61 = QIcon()
        icon61.addFile(u":/harvest/assets/images/harvest/harvest_reroll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harvest_reroll_btn.setIcon(icon61)
        self.harvest_reroll_btn.setIconSize(QSize(30, 30))
        self.harvest_reroll_btn.setCheckable(True)

        self.fossil_row1_2.addWidget(self.harvest_reroll_btn)

        self.harvest_resists_btn = CustomCursorButton(self.harvest_btn_row1)
        self.harvest_group_btns_group.addButton(self.harvest_resists_btn)
        self.harvest_resists_btn.setObjectName(u"harvest_resists_btn")
        self.harvest_resists_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_resists_btn.sizePolicy().hasHeightForWidth())
        self.harvest_resists_btn.setSizePolicy(sizePolicy1)
        self.harvest_resists_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_resists_btn.setStyleSheet(u"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {         \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
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
        self.harvest_resists_btn.setIcon(icon30)
        self.harvest_resists_btn.setIconSize(QSize(30, 30))
        self.harvest_resists_btn.setCheckable(True)

        self.fossil_row1_2.addWidget(self.harvest_resists_btn)

        self.harvest_high_tier_btn = CustomCursorButton(self.harvest_btn_row1)
        self.harvest_group_btns_group.addButton(self.harvest_high_tier_btn)
        self.harvest_high_tier_btn.setObjectName(u"harvest_high_tier_btn")
        self.harvest_high_tier_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_high_tier_btn.sizePolicy().hasHeightForWidth())
        self.harvest_high_tier_btn.setSizePolicy(sizePolicy1)
        self.harvest_high_tier_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_high_tier_btn.setStyleSheet(u"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {         \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
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
        self.harvest_high_tier_btn.setIcon(icon30)
        self.harvest_high_tier_btn.setIconSize(QSize(30, 30))
        self.harvest_high_tier_btn.setCheckable(True)

        self.fossil_row1_2.addWidget(self.harvest_high_tier_btn)

        self.harvest_other_btn = CustomCursorButton(self.harvest_btn_row1)
        self.harvest_group_btns_group.addButton(self.harvest_other_btn)
        self.harvest_other_btn.setObjectName(u"harvest_other_btn")
        self.harvest_other_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_other_btn.sizePolicy().hasHeightForWidth())
        self.harvest_other_btn.setSizePolicy(sizePolicy1)
        self.harvest_other_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_other_btn.setStyleSheet(u"QPushButton {\n"
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
"				cursor: pointer;\n"
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover {         \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 1), stop:1 rgba(75, 75, 75, 1));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, "
                        "y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
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
        self.harvest_other_btn.setIcon(icon30)
        self.harvest_other_btn.setIconSize(QSize(30, 30))
        self.harvest_other_btn.setCheckable(True)

        self.fossil_row1_2.addWidget(self.harvest_other_btn)


        self.verticalLayout_45.addWidget(self.harvest_btn_row1, 0, Qt.AlignTop)

        self.harvest_methods_container = QFrame(self.harvest_btns_container)
        self.harvest_methods_container.setObjectName(u"harvest_methods_container")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.harvest_methods_container.sizePolicy().hasHeightForWidth())
        self.harvest_methods_container.setSizePolicy(sizePolicy9)
        self.harvest_methods_container.setFrameShape(QFrame.StyledPanel)
        self.harvest_methods_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.harvest_methods_container)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.harvest_method_stack = QStackedWidget(self.harvest_methods_container)
        self.harvest_method_stack.setObjectName(u"harvest_method_stack")
        sizePolicy9.setHeightForWidth(self.harvest_method_stack.sizePolicy().hasHeightForWidth())
        self.harvest_method_stack.setSizePolicy(sizePolicy9)
        self.harvest_add_remove_reforge_methods = QWidget()
        self.harvest_add_remove_reforge_methods.setObjectName(u"harvest_add_remove_reforge_methods")
        sizePolicy9.setHeightForWidth(self.harvest_add_remove_reforge_methods.sizePolicy().hasHeightForWidth())
        self.harvest_add_remove_reforge_methods.setSizePolicy(sizePolicy9)
        self.verticalLayout_41 = QVBoxLayout(self.harvest_add_remove_reforge_methods)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.harvest_add_remove_reforge_btn_container = QWidget(self.harvest_add_remove_reforge_methods)
        self.harvest_add_remove_reforge_btn_container.setObjectName(u"harvest_add_remove_reforge_btn_container")
        self.harvest_add_remove_reforge_btn_container.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.harvest_add_remove_reforge_btn_container.sizePolicy().hasHeightForWidth())
        self.harvest_add_remove_reforge_btn_container.setSizePolicy(sizePolicy6)
        self.horizontalLayout_6 = QHBoxLayout(self.harvest_add_remove_reforge_btn_container)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.harvest_type_label = QLabel(self.harvest_add_remove_reforge_btn_container)
        self.harvest_type_label.setObjectName(u"harvest_type_label")
        sizePolicy1.setHeightForWidth(self.harvest_type_label.sizePolicy().hasHeightForWidth())
        self.harvest_type_label.setSizePolicy(sizePolicy1)
        self.harvest_type_label.setFont(font2)

        self.horizontalLayout_6.addWidget(self.harvest_type_label)

        self.attack_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.attack_btn.setObjectName(u"attack_btn")
        self.attack_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.attack_btn.sizePolicy().hasHeightForWidth())
        self.attack_btn.setSizePolicy(sizePolicy1)
        self.attack_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.attack_btn.setStyleSheet(u"QPushButton {\n"
"	color: #ff9000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #ff9000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.attack_btn.setCheckable(True)
        self.attack_btn.setChecked(False)

        self.horizontalLayout_6.addWidget(self.attack_btn)

        self.caster_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.caster_btn.setObjectName(u"caster_btn")
        self.caster_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.caster_btn.sizePolicy().hasHeightForWidth())
        self.caster_btn.setSizePolicy(sizePolicy1)
        self.caster_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.caster_btn.setStyleSheet(u"QPushButton {\n"
"	color: #d800ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #d800ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.caster_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.caster_btn)

        self.chaos_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.chaos_btn.setObjectName(u"chaos_btn")
        self.chaos_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.chaos_btn.sizePolicy().hasHeightForWidth())
        self.chaos_btn.setSizePolicy(sizePolicy1)
        self.chaos_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chaos_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a944ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a944ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.chaos_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.chaos_btn)

        self.cold_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.cold_btn.setObjectName(u"cold_btn")
        self.cold_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cold_btn.sizePolicy().hasHeightForWidth())
        self.cold_btn.setSizePolicy(sizePolicy1)
        self.cold_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cold_btn.setStyleSheet(u"QPushButton {\n"
"	color: #5599FF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #5599FF;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.cold_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.cold_btn)

        self.critical_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.critical_btn.setObjectName(u"critical_btn")
        self.critical_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.critical_btn.sizePolicy().hasHeightForWidth())
        self.critical_btn.setSizePolicy(sizePolicy1)
        self.critical_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.critical_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a8ff00;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a8ff00;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.critical_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.critical_btn)

        self.defences_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.defences_btn.setObjectName(u"defences_btn")
        self.defences_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.defences_btn.sizePolicy().hasHeightForWidth())
        self.defences_btn.setSizePolicy(sizePolicy1)
        self.defences_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.defences_btn.setStyleSheet(u"QPushButton {\n"
"	color: #DDD;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #DDD;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.defences_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.defences_btn)

        self.fire_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.fire_btn.setObjectName(u"fire_btn")
        self.fire_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.fire_btn.sizePolicy().hasHeightForWidth())
        self.fire_btn.setSizePolicy(sizePolicy1)
        self.fire_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fire_btn.setStyleSheet(u"QPushButton {\n"
"	color: #FF0000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #FF0000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.fire_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.fire_btn)

        self.life_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.life_btn.setObjectName(u"life_btn")
        self.life_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.life_btn.sizePolicy().hasHeightForWidth())
        self.life_btn.setSizePolicy(sizePolicy1)
        self.life_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.life_btn.setStyleSheet(u"QPushButton {\n"
"	color: #ff00cc;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #ff00cc;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.life_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.life_btn)

        self.lightning_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.lightning_btn.setObjectName(u"lightning_btn")
        self.lightning_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lightning_btn.sizePolicy().hasHeightForWidth())
        self.lightning_btn.setSizePolicy(sizePolicy1)
        self.lightning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lightning_btn.setStyleSheet(u"QPushButton {\n"
"	color: #FFF000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #FFF000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.lightning_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.lightning_btn)

        self.physical_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.physical_btn.setObjectName(u"physical_btn")
        self.physical_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.physical_btn.sizePolicy().hasHeightForWidth())
        self.physical_btn.setSizePolicy(sizePolicy1)
        self.physical_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.physical_btn.setStyleSheet(u"QPushButton {\n"
"	color: #e1b900;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #e1b900;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.physical_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.physical_btn)

        self.speed_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.speed_btn.setObjectName(u"speed_btn")
        self.speed_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.speed_btn.sizePolicy().hasHeightForWidth())
        self.speed_btn.setSizePolicy(sizePolicy1)
        self.speed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_btn.setStyleSheet(u"QPushButton {\n"
"	color: #00ffc0;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #00ffc0;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.speed_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.speed_btn)

        self.influence_btn = QPushButton(self.harvest_add_remove_reforge_btn_container)
        self.influence_btn.setObjectName(u"influence_btn")
        self.influence_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.influence_btn.sizePolicy().hasHeightForWidth())
        self.influence_btn.setSizePolicy(sizePolicy1)
        self.influence_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.influence_btn.setStyleSheet(u"QPushButton {\n"
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
"				border: 0px;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.influence_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.influence_btn)


        self.verticalLayout_41.addWidget(self.harvest_add_remove_reforge_btn_container)

        self.harvest_method_stack.addWidget(self.harvest_add_remove_reforge_methods)
        self.harvest_resists_methods = QWidget()
        self.harvest_resists_methods.setObjectName(u"harvest_resists_methods")
        sizePolicy9.setHeightForWidth(self.harvest_resists_methods.sizePolicy().hasHeightForWidth())
        self.harvest_resists_methods.setSizePolicy(sizePolicy9)
        self.verticalLayout_42 = QVBoxLayout(self.harvest_resists_methods)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.harvest_resists_btns = QWidget(self.harvest_resists_methods)
        self.harvest_resists_btns.setObjectName(u"harvest_resists_btns")
        sizePolicy1.setHeightForWidth(self.harvest_resists_btns.sizePolicy().hasHeightForWidth())
        self.harvest_resists_btns.setSizePolicy(sizePolicy1)
        self.horizontalLayout_20 = QHBoxLayout(self.harvest_resists_btns)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.harvest_resists_label = QLabel(self.harvest_resists_btns)
        self.harvest_resists_label.setObjectName(u"harvest_resists_label")
        self.harvest_resists_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_resists_label.sizePolicy().hasHeightForWidth())
        self.harvest_resists_label.setSizePolicy(sizePolicy1)
        self.harvest_resists_label.setFont(font2)

        self.horizontalLayout_20.addWidget(self.harvest_resists_label)

        self.harvest_fire_to_cold_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_fire_to_cold_btn.setObjectName(u"harvest_fire_to_cold_btn")
        self.harvest_fire_to_cold_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_fire_to_cold_btn.sizePolicy().hasHeightForWidth())
        self.harvest_fire_to_cold_btn.setSizePolicy(sizePolicy1)
        self.harvest_fire_to_cold_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_fire_to_cold_btn.setStyleSheet(u"QPushButton {\n"
"	color: #ff9000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #ff9000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_fire_to_cold_btn.setCheckable(True)
        self.harvest_fire_to_cold_btn.setChecked(False)

        self.horizontalLayout_20.addWidget(self.harvest_fire_to_cold_btn)

        self.harvest_fire_to_lightning_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_fire_to_lightning_btn.setObjectName(u"harvest_fire_to_lightning_btn")
        self.harvest_fire_to_lightning_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_fire_to_lightning_btn.sizePolicy().hasHeightForWidth())
        self.harvest_fire_to_lightning_btn.setSizePolicy(sizePolicy1)
        self.harvest_fire_to_lightning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_fire_to_lightning_btn.setStyleSheet(u"QPushButton {\n"
"	color: #d800ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #d800ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_fire_to_lightning_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.harvest_fire_to_lightning_btn)

        self.harvest_cold_to_fire_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_cold_to_fire_btn.setObjectName(u"harvest_cold_to_fire_btn")
        self.harvest_cold_to_fire_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_cold_to_fire_btn.sizePolicy().hasHeightForWidth())
        self.harvest_cold_to_fire_btn.setSizePolicy(sizePolicy1)
        self.harvest_cold_to_fire_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_cold_to_fire_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a944ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a944ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_cold_to_fire_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.harvest_cold_to_fire_btn)

        self.harvest_cold_to_lightning_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_cold_to_lightning_btn.setObjectName(u"harvest_cold_to_lightning_btn")
        self.harvest_cold_to_lightning_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_cold_to_lightning_btn.sizePolicy().hasHeightForWidth())
        self.harvest_cold_to_lightning_btn.setSizePolicy(sizePolicy1)
        self.harvest_cold_to_lightning_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_cold_to_lightning_btn.setStyleSheet(u"QPushButton {\n"
"	color: #5599FF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #5599FF;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_cold_to_lightning_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.harvest_cold_to_lightning_btn)

        self.harvest_lightning_to_fire_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_lightning_to_fire_btn.setObjectName(u"harvest_lightning_to_fire_btn")
        self.harvest_lightning_to_fire_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_lightning_to_fire_btn.sizePolicy().hasHeightForWidth())
        self.harvest_lightning_to_fire_btn.setSizePolicy(sizePolicy1)
        self.harvest_lightning_to_fire_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_lightning_to_fire_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a8ff00;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a8ff00;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_lightning_to_fire_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.harvest_lightning_to_fire_btn)

        self.harvest_lightning_to_cold_btn = QPushButton(self.harvest_resists_btns)
        self.harvest_lightning_to_cold_btn.setObjectName(u"harvest_lightning_to_cold_btn")
        self.harvest_lightning_to_cold_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_lightning_to_cold_btn.sizePolicy().hasHeightForWidth())
        self.harvest_lightning_to_cold_btn.setSizePolicy(sizePolicy1)
        self.harvest_lightning_to_cold_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_lightning_to_cold_btn.setStyleSheet(u"QPushButton {\n"
"	color: #DDD;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #DDD;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_lightning_to_cold_btn.setCheckable(True)

        self.horizontalLayout_20.addWidget(self.harvest_lightning_to_cold_btn)


        self.verticalLayout_42.addWidget(self.harvest_resists_btns)

        self.harvest_method_stack.addWidget(self.harvest_resists_methods)
        self.harvest_high_tier_methods = QWidget()
        self.harvest_high_tier_methods.setObjectName(u"harvest_high_tier_methods")
        self.verticalLayout_43 = QVBoxLayout(self.harvest_high_tier_methods)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.harvest_high_tier_btn_container = QWidget(self.harvest_high_tier_methods)
        self.harvest_high_tier_btn_container.setObjectName(u"harvest_high_tier_btn_container")
        sizePolicy1.setHeightForWidth(self.harvest_high_tier_btn_container.sizePolicy().hasHeightForWidth())
        self.harvest_high_tier_btn_container.setSizePolicy(sizePolicy1)
        self.horizontalLayout_21 = QHBoxLayout(self.harvest_high_tier_btn_container)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.harvest_high_tier_label = QLabel(self.harvest_high_tier_btn_container)
        self.harvest_high_tier_label.setObjectName(u"harvest_high_tier_label")
        self.harvest_high_tier_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_high_tier_label.sizePolicy().hasHeightForWidth())
        self.harvest_high_tier_label.setSizePolicy(sizePolicy1)
        self.harvest_high_tier_label.setFont(font2)

        self.horizontalLayout_21.addWidget(self.harvest_high_tier_label)

        self.harvest_normal_to_magic_one_btn = QPushButton(self.harvest_high_tier_btn_container)
        self.harvest_normal_to_magic_one_btn.setObjectName(u"harvest_normal_to_magic_one_btn")
        self.harvest_normal_to_magic_one_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_normal_to_magic_one_btn.sizePolicy().hasHeightForWidth())
        self.harvest_normal_to_magic_one_btn.setSizePolicy(sizePolicy1)
        self.harvest_normal_to_magic_one_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_normal_to_magic_one_btn.setStyleSheet(u"QPushButton {\n"
"	color: #ff9000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #ff9000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_normal_to_magic_one_btn.setCheckable(True)
        self.harvest_normal_to_magic_one_btn.setChecked(False)

        self.horizontalLayout_21.addWidget(self.harvest_normal_to_magic_one_btn)

        self.harvest_normal_to_magic_two_btn = QPushButton(self.harvest_high_tier_btn_container)
        self.harvest_normal_to_magic_two_btn.setObjectName(u"harvest_normal_to_magic_two_btn")
        self.harvest_normal_to_magic_two_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_normal_to_magic_two_btn.sizePolicy().hasHeightForWidth())
        self.harvest_normal_to_magic_two_btn.setSizePolicy(sizePolicy1)
        self.harvest_normal_to_magic_two_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_normal_to_magic_two_btn.setStyleSheet(u"QPushButton {\n"
"	color: #d800ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #d800ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_normal_to_magic_two_btn.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.harvest_normal_to_magic_two_btn)

        self.harvest_magic_to_rare_two_btn = QPushButton(self.harvest_high_tier_btn_container)
        self.harvest_magic_to_rare_two_btn.setObjectName(u"harvest_magic_to_rare_two_btn")
        self.harvest_magic_to_rare_two_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_magic_to_rare_two_btn.sizePolicy().hasHeightForWidth())
        self.harvest_magic_to_rare_two_btn.setSizePolicy(sizePolicy1)
        self.harvest_magic_to_rare_two_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_magic_to_rare_two_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a944ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a944ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_magic_to_rare_two_btn.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.harvest_magic_to_rare_two_btn)

        self.harvest_magic_to_rare_three_btn = QPushButton(self.harvest_high_tier_btn_container)
        self.harvest_magic_to_rare_three_btn.setObjectName(u"harvest_magic_to_rare_three_btn")
        self.harvest_magic_to_rare_three_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_magic_to_rare_three_btn.sizePolicy().hasHeightForWidth())
        self.harvest_magic_to_rare_three_btn.setSizePolicy(sizePolicy1)
        self.harvest_magic_to_rare_three_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_magic_to_rare_three_btn.setStyleSheet(u"QPushButton {\n"
"	color: #5599FF;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #5599FF;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_magic_to_rare_three_btn.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.harvest_magic_to_rare_three_btn)

        self.harvest_magic_to_rare_four_btn = QPushButton(self.harvest_high_tier_btn_container)
        self.harvest_magic_to_rare_four_btn.setObjectName(u"harvest_magic_to_rare_four_btn")
        self.harvest_magic_to_rare_four_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_magic_to_rare_four_btn.sizePolicy().hasHeightForWidth())
        self.harvest_magic_to_rare_four_btn.setSizePolicy(sizePolicy1)
        self.harvest_magic_to_rare_four_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_magic_to_rare_four_btn.setStyleSheet(u"QPushButton {\n"
"	color: #a8ff00;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #a8ff00;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_magic_to_rare_four_btn.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.harvest_magic_to_rare_four_btn)


        self.verticalLayout_43.addWidget(self.harvest_high_tier_btn_container)

        self.harvest_method_stack.addWidget(self.harvest_high_tier_methods)
        self.harvest_other_methods = QWidget()
        self.harvest_other_methods.setObjectName(u"harvest_other_methods")
        self.verticalLayout_44 = QVBoxLayout(self.harvest_other_methods)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.harvest_resists_btns_3 = QWidget(self.harvest_other_methods)
        self.harvest_resists_btns_3.setObjectName(u"harvest_resists_btns_3")
        sizePolicy1.setHeightForWidth(self.harvest_resists_btns_3.sizePolicy().hasHeightForWidth())
        self.harvest_resists_btns_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_22 = QHBoxLayout(self.harvest_resists_btns_3)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.harvest_other_label = QLabel(self.harvest_resists_btns_3)
        self.harvest_other_label.setObjectName(u"harvest_other_label")
        self.harvest_other_label.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_other_label.sizePolicy().hasHeightForWidth())
        self.harvest_other_label.setSizePolicy(sizePolicy1)
        self.harvest_other_label.setFont(font2)

        self.horizontalLayout_22.addWidget(self.harvest_other_label, 0, Qt.AlignLeft)

        self.harvest_reforge_more_likely_btn = QPushButton(self.harvest_resists_btns_3)
        self.harvest_reforge_more_likely_btn.setObjectName(u"harvest_reforge_more_likely_btn")
        self.harvest_reforge_more_likely_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_reforge_more_likely_btn.sizePolicy().hasHeightForWidth())
        self.harvest_reforge_more_likely_btn.setSizePolicy(sizePolicy1)
        self.harvest_reforge_more_likely_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_reforge_more_likely_btn.setStyleSheet(u"QPushButton {\n"
"	color: #ff9000;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #ff9000;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_reforge_more_likely_btn.setCheckable(True)
        self.harvest_reforge_more_likely_btn.setChecked(False)

        self.horizontalLayout_22.addWidget(self.harvest_reforge_more_likely_btn)

        self.harvest_reforge_less_likely_btn = QPushButton(self.harvest_resists_btns_3)
        self.harvest_reforge_less_likely_btn.setObjectName(u"harvest_reforge_less_likely_btn")
        self.harvest_reforge_less_likely_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.harvest_reforge_less_likely_btn.sizePolicy().hasHeightForWidth())
        self.harvest_reforge_less_likely_btn.setSizePolicy(sizePolicy1)
        self.harvest_reforge_less_likely_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.harvest_reforge_less_likely_btn.setStyleSheet(u"QPushButton {\n"
"	color: #d800ff;\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"				background-color: #d800ff;\n"
"				color: #000;\n"
"				text-shadow: none;\n"
"				box-shadow: none;\n"
"				border: 0px;\n"
"			}")
        self.harvest_reforge_less_likely_btn.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.harvest_reforge_less_likely_btn)


        self.verticalLayout_44.addWidget(self.harvest_resists_btns_3)

        self.harvest_method_stack.addWidget(self.harvest_other_methods)

        self.verticalLayout_40.addWidget(self.harvest_method_stack)


        self.verticalLayout_45.addWidget(self.harvest_methods_container, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.harvest_btns_container, 0, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.harvest_crafts)
        self.essence_crafts = QWidget()
        self.essence_crafts.setObjectName(u"essence_crafts")
        sizePolicy7.setHeightForWidth(self.essence_crafts.sizePolicy().hasHeightForWidth())
        self.essence_crafts.setSizePolicy(sizePolicy7)
        self.essence_crafts.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.essence_crafts)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.essence_tier_row = QWidget(self.essence_crafts)
        self.essence_tier_row.setObjectName(u"essence_tier_row")
        sizePolicy1.setHeightForWidth(self.essence_tier_row.sizePolicy().hasHeightForWidth())
        self.essence_tier_row.setSizePolicy(sizePolicy1)
        self.essence_tier_row.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.essence_tier_row)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.essence_tier_label = QLabel(self.essence_tier_row)
        self.essence_tier_label.setObjectName(u"essence_tier_label")
        sizePolicy1.setHeightForWidth(self.essence_tier_label.sizePolicy().hasHeightForWidth())
        self.essence_tier_label.setSizePolicy(sizePolicy1)
        self.essence_tier_label.setMinimumSize(QSize(28, 0))

        self.horizontalLayout_12.addWidget(self.essence_tier_label, 0, Qt.AlignLeft)

        self.t6_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group = QButtonGroup(MainWindow)
        self.essence_tier_btns_group.setObjectName(u"essence_tier_btns_group")
        self.essence_tier_btns_group.addButton(self.t6_btn)
        self.t6_btn.setObjectName(u"t6_btn")
        sizePolicy4.setHeightForWidth(self.t6_btn.sizePolicy().hasHeightForWidth())
        self.t6_btn.setSizePolicy(sizePolicy4)
        self.t6_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t6_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t6_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t6_btn)

        self.t5_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group.addButton(self.t5_btn)
        self.t5_btn.setObjectName(u"t5_btn")
        self.t5_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t5_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t5_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t5_btn)

        self.t4_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group.addButton(self.t4_btn)
        self.t4_btn.setObjectName(u"t4_btn")
        self.t4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t4_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t4_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t4_btn)

        self.t3_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group.addButton(self.t3_btn)
        self.t3_btn.setObjectName(u"t3_btn")
        self.t3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t3_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t3_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t3_btn)

        self.t2_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group.addButton(self.t2_btn)
        self.t2_btn.setObjectName(u"t2_btn")
        self.t2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t2_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t2_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t2_btn)

        self.t1_btn = QPushButton(self.essence_tier_row)
        self.essence_tier_btns_group.addButton(self.t1_btn)
        self.t1_btn.setObjectName(u"t1_btn")
        self.t1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.t1_btn.setStyleSheet(u"QPushButton {\n"
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
        self.t1_btn.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.t1_btn)


        self.gridLayout.addWidget(self.essence_tier_row, 2, 3, 1, 1, Qt.AlignHCenter)

        self.essences_row1 = QWidget(self.essence_crafts)
        self.essences_row1.setObjectName(u"essences_row1")
        sizePolicy6.setHeightForWidth(self.essences_row1.sizePolicy().hasHeightForWidth())
        self.essences_row1.setSizePolicy(sizePolicy6)
        self.essences_row1.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;")
        self.horizontalLayout_10 = QHBoxLayout(self.essences_row1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.essences_hide_btn = QPushButton(self.essences_row1)
        self.essences_hide_btn.setObjectName(u"essences_hide_btn")
        self.essences_hide_btn.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.essences_hide_btn.sizePolicy().hasHeightForWidth())
        self.essences_hide_btn.setSizePolicy(sizePolicy10)
        self.essences_hide_btn.setFont(font2)
        self.essences_hide_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essences_hide_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.essences_hide_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")

        self.horizontalLayout_10.addWidget(self.essences_hide_btn)

        self.essences_label = QLabel(self.essences_row1)
        self.essences_label.setObjectName(u"essences_label")
        sizePolicy7.setHeightForWidth(self.essences_label.sizePolicy().hasHeightForWidth())
        self.essences_label.setSizePolicy(sizePolicy7)
        self.essences_label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.essences_label)

        self.essence_anger_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group = QButtonGroup(MainWindow)
        self.essence_btns_group.setObjectName(u"essence_btns_group")
        self.essence_btns_group.addButton(self.essence_anger_btn)
        self.essence_anger_btn.setObjectName(u"essence_anger_btn")
        self.essence_anger_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_anger_btn.setStyleSheet(u"QPushButton {\n"
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
        icon62 = QIcon()
        icon62.addFile(u":/essences/assets/images/essences/essence_Anger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_anger_btn.setIcon(icon62)
        self.essence_anger_btn.setIconSize(QSize(30, 30))
        self.essence_anger_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_anger_btn)

        self.essence_anguish_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_anguish_btn)
        self.essence_anguish_btn.setObjectName(u"essence_anguish_btn")
        self.essence_anguish_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_anguish_btn.setStyleSheet(u"QPushButton {\n"
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
        icon63 = QIcon()
        icon63.addFile(u":/essences/assets/images/essences/essence_Anguish.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_anguish_btn.setIcon(icon63)
        self.essence_anguish_btn.setIconSize(QSize(30, 30))
        self.essence_anguish_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_anguish_btn)

        self.essence_contempt_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_contempt_btn)
        self.essence_contempt_btn.setObjectName(u"essence_contempt_btn")
        self.essence_contempt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_contempt_btn.setStyleSheet(u"QPushButton {\n"
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
        icon64 = QIcon()
        icon64.addFile(u":/essences/assets/images/essences/essence_Contempt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_contempt_btn.setIcon(icon64)
        self.essence_contempt_btn.setIconSize(QSize(30, 30))
        self.essence_contempt_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_contempt_btn)

        self.essence_delirium_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_delirium_btn)
        self.essence_delirium_btn.setObjectName(u"essence_delirium_btn")
        self.essence_delirium_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_delirium_btn.setStyleSheet(u"QPushButton {\n"
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
        icon65 = QIcon()
        icon65.addFile(u":/essences/assets/images/essences/essence_Delirium.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_delirium_btn.setIcon(icon65)
        self.essence_delirium_btn.setIconSize(QSize(30, 30))
        self.essence_delirium_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_delirium_btn)

        self.essence_doubt_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_doubt_btn)
        self.essence_doubt_btn.setObjectName(u"essence_doubt_btn")
        self.essence_doubt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_doubt_btn.setStyleSheet(u"QPushButton {\n"
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
        icon66 = QIcon()
        icon66.addFile(u":/essences/assets/images/essences/essence_Doubt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_doubt_btn.setIcon(icon66)
        self.essence_doubt_btn.setIconSize(QSize(30, 30))
        self.essence_doubt_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_doubt_btn)

        self.essence_dread_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_dread_btn)
        self.essence_dread_btn.setObjectName(u"essence_dread_btn")
        self.essence_dread_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_dread_btn.setStyleSheet(u"QPushButton {\n"
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
        icon67 = QIcon()
        icon67.addFile(u":/essences/assets/images/essences/essence_Dread.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_dread_btn.setIcon(icon67)
        self.essence_dread_btn.setIconSize(QSize(30, 30))
        self.essence_dread_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_dread_btn)

        self.essence_envy_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_envy_btn)
        self.essence_envy_btn.setObjectName(u"essence_envy_btn")
        self.essence_envy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_envy_btn.setStyleSheet(u"QPushButton {\n"
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
        icon68 = QIcon()
        icon68.addFile(u":/essences/assets/images/essences/essence_Envy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_envy_btn.setIcon(icon68)
        self.essence_envy_btn.setIconSize(QSize(30, 30))
        self.essence_envy_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_envy_btn)

        self.essenc_fear_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essenc_fear_btn)
        self.essenc_fear_btn.setObjectName(u"essenc_fear_btn")
        self.essenc_fear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essenc_fear_btn.setStyleSheet(u"QPushButton {\n"
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
        icon69 = QIcon()
        icon69.addFile(u":/essences/assets/images/essences/essence_Fear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essenc_fear_btn.setIcon(icon69)
        self.essenc_fear_btn.setIconSize(QSize(30, 30))
        self.essenc_fear_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essenc_fear_btn)

        self.essence_greed = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_greed)
        self.essence_greed.setObjectName(u"essence_greed")
        self.essence_greed.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_greed.setStyleSheet(u"QPushButton {\n"
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
        icon70 = QIcon()
        icon70.addFile(u":/essences/assets/images/essences/essence_Greed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_greed.setIcon(icon70)
        self.essence_greed.setIconSize(QSize(30, 30))
        self.essence_greed.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_greed)

        self.essence_hatred = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_hatred)
        self.essence_hatred.setObjectName(u"essence_hatred")
        self.essence_hatred.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_hatred.setStyleSheet(u"QPushButton {\n"
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
        icon71 = QIcon()
        icon71.addFile(u":/essences/assets/images/essences/essence_Hatred.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_hatred.setIcon(icon71)
        self.essence_hatred.setIconSize(QSize(30, 30))
        self.essence_hatred.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_hatred)

        self.essence_horror_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_horror_btn)
        self.essence_horror_btn.setObjectName(u"essence_horror_btn")
        self.essence_horror_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_horror_btn.setStyleSheet(u"QPushButton {\n"
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
        icon72 = QIcon()
        icon72.addFile(u":/essences/assets/images/essences/essence_Horror.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_horror_btn.setIcon(icon72)
        self.essence_horror_btn.setIconSize(QSize(30, 30))
        self.essence_horror_btn.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.essence_horror_btn)

        self.essence_hysteria_btn = CustomCursorButton(self.essences_row1)
        self.essence_btns_group.addButton(self.essence_hysteria_btn)
        self.essence_hysteria_btn.setObjectName(u"essence_hysteria_btn")
        self.essence_hysteria_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_hysteria_btn.setStyleSheet(u"QPushButton {\n"
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
        icon73 = QIcon()
        icon73.addFile(u":/essences/assets/images/essences/essence_Hysteria.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_hysteria_btn.setIcon(icon73)
        self.essence_hysteria_btn.setIconSize(QSize(30, 30))
        self.essence_hysteria_btn.setCheckable(True)
        self.essence_hysteria_btn.setChecked(False)

        self.horizontalLayout_10.addWidget(self.essence_hysteria_btn)


        self.gridLayout.addWidget(self.essences_row1, 0, 3, 1, 1, Qt.AlignTop)

        self.essences_row2 = QWidget(self.essence_crafts)
        self.essences_row2.setObjectName(u"essences_row2")
        sizePolicy1.setHeightForWidth(self.essences_row2.sizePolicy().hasHeightForWidth())
        self.essences_row2.setSizePolicy(sizePolicy1)
        self.essences_row2.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;")
        self.horizontalLayout_11 = QHBoxLayout(self.essences_row2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.essence_insanity_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_insanity_btn)
        self.essence_insanity_btn.setObjectName(u"essence_insanity_btn")
        self.essence_insanity_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_insanity_btn.setStyleSheet(u"QPushButton {\n"
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
        icon74 = QIcon()
        icon74.addFile(u":/essences/assets/images/essences/essence_Insanity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_insanity_btn.setIcon(icon74)
        self.essence_insanity_btn.setIconSize(QSize(30, 30))
        self.essence_insanity_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_insanity_btn)

        self.essence_loathing_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_loathing_btn)
        self.essence_loathing_btn.setObjectName(u"essence_loathing_btn")
        self.essence_loathing_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_loathing_btn.setStyleSheet(u"QPushButton {\n"
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
        icon75 = QIcon()
        icon75.addFile(u":/essences/assets/images/essences/essence_Loathing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_loathing_btn.setIcon(icon75)
        self.essence_loathing_btn.setIconSize(QSize(30, 30))
        self.essence_loathing_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_loathing_btn)

        self.essence_misery_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_misery_btn)
        self.essence_misery_btn.setObjectName(u"essence_misery_btn")
        self.essence_misery_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_misery_btn.setStyleSheet(u"QPushButton {\n"
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
        icon76 = QIcon()
        icon76.addFile(u":/essences/assets/images/essences/essence_Misery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_misery_btn.setIcon(icon76)
        self.essence_misery_btn.setIconSize(QSize(30, 30))
        self.essence_misery_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_misery_btn)

        self.essence_rage_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_rage_btn)
        self.essence_rage_btn.setObjectName(u"essence_rage_btn")
        self.essence_rage_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_rage_btn.setStyleSheet(u"QPushButton {\n"
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
        icon77 = QIcon()
        icon77.addFile(u":/essences/assets/images/essences/essence_Rage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_rage_btn.setIcon(icon77)
        self.essence_rage_btn.setIconSize(QSize(30, 30))
        self.essence_rage_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_rage_btn)

        self.essence_scorn_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_scorn_btn)
        self.essence_scorn_btn.setObjectName(u"essence_scorn_btn")
        self.essence_scorn_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_scorn_btn.setStyleSheet(u"QPushButton {\n"
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
        icon78 = QIcon()
        icon78.addFile(u":/essences/assets/images/essences/essence_Scorn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_scorn_btn.setIcon(icon78)
        self.essence_scorn_btn.setIconSize(QSize(30, 30))
        self.essence_scorn_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_scorn_btn)

        self.essence_sorrow_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_sorrow_btn)
        self.essence_sorrow_btn.setObjectName(u"essence_sorrow_btn")
        self.essence_sorrow_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_sorrow_btn.setStyleSheet(u"QPushButton {\n"
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
        icon79 = QIcon()
        icon79.addFile(u":/essences/assets/images/essences/essence_Sorrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_sorrow_btn.setIcon(icon79)
        self.essence_sorrow_btn.setIconSize(QSize(30, 30))
        self.essence_sorrow_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_sorrow_btn)

        self.essence_spite_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_spite_btn)
        self.essence_spite_btn.setObjectName(u"essence_spite_btn")
        self.essence_spite_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_spite_btn.setStyleSheet(u"QPushButton {\n"
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
        icon80 = QIcon()
        icon80.addFile(u":/essences/assets/images/essences/essence_Spite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_spite_btn.setIcon(icon80)
        self.essence_spite_btn.setIconSize(QSize(30, 30))
        self.essence_spite_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_spite_btn)

        self.essence_suffering_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_suffering_btn)
        self.essence_suffering_btn.setObjectName(u"essence_suffering_btn")
        self.essence_suffering_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_suffering_btn.setStyleSheet(u"QPushButton {\n"
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
        icon81 = QIcon()
        icon81.addFile(u":/essences/assets/images/essences/essence_Suffering.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_suffering_btn.setIcon(icon81)
        self.essence_suffering_btn.setIconSize(QSize(30, 30))
        self.essence_suffering_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_suffering_btn)

        self.essence_torment_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_torment_btn)
        self.essence_torment_btn.setObjectName(u"essence_torment_btn")
        self.essence_torment_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_torment_btn.setStyleSheet(u"QPushButton {\n"
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
        icon82 = QIcon()
        icon82.addFile(u":/essences/assets/images/essences/essence_Torment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_torment_btn.setIcon(icon82)
        self.essence_torment_btn.setIconSize(QSize(30, 30))
        self.essence_torment_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_torment_btn)

        self.essence_woe_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_woe_btn)
        self.essence_woe_btn.setObjectName(u"essence_woe_btn")
        self.essence_woe_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_woe_btn.setStyleSheet(u"QPushButton {\n"
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
        icon83 = QIcon()
        icon83.addFile(u":/essences/assets/images/essences/essence_Woe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_woe_btn.setIcon(icon83)
        self.essence_woe_btn.setIconSize(QSize(30, 30))
        self.essence_woe_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_woe_btn)

        self.essence_wrath_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_wrath_btn)
        self.essence_wrath_btn.setObjectName(u"essence_wrath_btn")
        self.essence_wrath_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_wrath_btn.setStyleSheet(u"QPushButton {\n"
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
        icon84 = QIcon()
        icon84.addFile(u":/essences/assets/images/essences/essence_Wrath.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_wrath_btn.setIcon(icon84)
        self.essence_wrath_btn.setIconSize(QSize(30, 30))
        self.essence_wrath_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_wrath_btn)

        self.essence_zeal_btn = CustomCursorButton(self.essences_row2)
        self.essence_btns_group.addButton(self.essence_zeal_btn)
        self.essence_zeal_btn.setObjectName(u"essence_zeal_btn")
        self.essence_zeal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_zeal_btn.setStyleSheet(u"QPushButton {\n"
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
        icon85 = QIcon()
        icon85.addFile(u":/essences/assets/images/essences/essence_Zeal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_zeal_btn.setIcon(icon85)
        self.essence_zeal_btn.setIconSize(QSize(30, 30))
        self.essence_zeal_btn.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.essence_zeal_btn)


        self.gridLayout.addWidget(self.essences_row2, 1, 3, 1, 1, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.essence_crafts)
        self.catalysts = QWidget()
        self.catalysts.setObjectName(u"catalysts")
        sizePolicy7.setHeightForWidth(self.catalysts.sizePolicy().hasHeightForWidth())
        self.catalysts.setSizePolicy(sizePolicy7)
        self.catalysts.setStyleSheet(u"\n"
"border-image: none;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.verticalLayout_22 = QVBoxLayout(self.catalysts)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.catalyst_btn_row = QWidget(self.catalysts)
        self.catalyst_btn_row.setObjectName(u"catalyst_btn_row")
        sizePolicy6.setHeightForWidth(self.catalyst_btn_row.sizePolicy().hasHeightForWidth())
        self.catalyst_btn_row.setSizePolicy(sizePolicy6)
        self.catalyst_btn_row.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;")
        self.horizontalLayout_13 = QHBoxLayout(self.catalyst_btn_row)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.catalysts_hide_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_hide_btn.setObjectName(u"catalysts_hide_btn")
        self.catalysts_hide_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.catalysts_hide_btn.sizePolicy().hasHeightForWidth())
        self.catalysts_hide_btn.setSizePolicy(sizePolicy10)
        self.catalysts_hide_btn.setFont(font2)
        self.catalysts_hide_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.catalysts_hide_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")

        self.horizontalLayout_13.addWidget(self.catalysts_hide_btn)

        self.catalyst_row_label = QLabel(self.catalyst_btn_row)
        self.catalyst_row_label.setObjectName(u"catalyst_row_label")
        sizePolicy.setHeightForWidth(self.catalyst_row_label.sizePolicy().hasHeightForWidth())
        self.catalyst_row_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.catalyst_row_label)

        self.intrinsic_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group = QButtonGroup(MainWindow)
        self.catalysts_btns_group.setObjectName(u"catalysts_btns_group")
        self.catalysts_btns_group.addButton(self.intrinsic_catalyst_btn)
        self.intrinsic_catalyst_btn.setObjectName(u"intrinsic_catalyst_btn")
        sizePolicy.setHeightForWidth(self.intrinsic_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.intrinsic_catalyst_btn.setSizePolicy(sizePolicy)
        self.intrinsic_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.intrinsic_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon86 = QIcon()
        icon86.addFile(u":/catalysts/assets/images/catalysts/intrinsic_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.intrinsic_catalyst_btn.setIcon(icon86)
        self.intrinsic_catalyst_btn.setIconSize(QSize(30, 30))
        self.intrinsic_catalyst_btn.setCheckable(True)
        self.intrinsic_catalyst_btn.setChecked(True)

        self.horizontalLayout_13.addWidget(self.intrinsic_catalyst_btn)

        self.abrasive_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.abrasive_catalyst_btn)
        self.abrasive_catalyst_btn.setObjectName(u"abrasive_catalyst_btn")
        sizePolicy.setHeightForWidth(self.abrasive_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.abrasive_catalyst_btn.setSizePolicy(sizePolicy)
        self.abrasive_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.abrasive_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon87 = QIcon()
        icon87.addFile(u":/catalysts/assets/images/catalysts/abrasive_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abrasive_catalyst_btn.setIcon(icon87)
        self.abrasive_catalyst_btn.setIconSize(QSize(30, 30))
        self.abrasive_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.abrasive_catalyst_btn)

        self.prismatic_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.prismatic_catalyst_btn)
        self.prismatic_catalyst_btn.setObjectName(u"prismatic_catalyst_btn")
        sizePolicy.setHeightForWidth(self.prismatic_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.prismatic_catalyst_btn.setSizePolicy(sizePolicy)
        self.prismatic_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.prismatic_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon88 = QIcon()
        icon88.addFile(u":/catalysts/assets/images/catalysts/prismatic_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prismatic_catalyst_btn.setIcon(icon88)
        self.prismatic_catalyst_btn.setIconSize(QSize(30, 30))
        self.prismatic_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.prismatic_catalyst_btn)

        self.fertile_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.fertile_catalyst_btn)
        self.fertile_catalyst_btn.setObjectName(u"fertile_catalyst_btn")
        sizePolicy.setHeightForWidth(self.fertile_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.fertile_catalyst_btn.setSizePolicy(sizePolicy)
        self.fertile_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fertile_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon89 = QIcon()
        icon89.addFile(u":/catalysts/assets/images/catalysts/fertile_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fertile_catalyst_btn.setIcon(icon89)
        self.fertile_catalyst_btn.setIconSize(QSize(30, 30))
        self.fertile_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.fertile_catalyst_btn)

        self.imbued_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.imbued_catalyst_btn)
        self.imbued_catalyst_btn.setObjectName(u"imbued_catalyst_btn")
        sizePolicy.setHeightForWidth(self.imbued_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.imbued_catalyst_btn.setSizePolicy(sizePolicy)
        self.imbued_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.imbued_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon90 = QIcon()
        icon90.addFile(u":/catalysts/assets/images/catalysts/imbued_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imbued_catalyst_btn.setIcon(icon90)
        self.imbued_catalyst_btn.setIconSize(QSize(30, 30))
        self.imbued_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.imbued_catalyst_btn)

        self.tempering_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.tempering_catalyst_btn)
        self.tempering_catalyst_btn.setObjectName(u"tempering_catalyst_btn")
        sizePolicy.setHeightForWidth(self.tempering_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.tempering_catalyst_btn.setSizePolicy(sizePolicy)
        self.tempering_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tempering_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon91 = QIcon()
        icon91.addFile(u":/catalysts/assets/images/catalysts/tempering_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tempering_catalyst_btn.setIcon(icon91)
        self.tempering_catalyst_btn.setIconSize(QSize(30, 30))
        self.tempering_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.tempering_catalyst_btn)

        self.turbulent_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.turbulent_catalyst_btn)
        self.turbulent_catalyst_btn.setObjectName(u"turbulent_catalyst_btn")
        sizePolicy.setHeightForWidth(self.turbulent_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.turbulent_catalyst_btn.setSizePolicy(sizePolicy)
        self.turbulent_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.turbulent_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon92 = QIcon()
        icon92.addFile(u":/catalysts/assets/images/catalysts/turbulent_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turbulent_catalyst_btn.setIcon(icon92)
        self.turbulent_catalyst_btn.setIconSize(QSize(30, 30))
        self.turbulent_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.turbulent_catalyst_btn)

        self.accelerating_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.accelerating_catalyst_btn)
        self.accelerating_catalyst_btn.setObjectName(u"accelerating_catalyst_btn")
        sizePolicy.setHeightForWidth(self.accelerating_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.accelerating_catalyst_btn.setSizePolicy(sizePolicy)
        self.accelerating_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.accelerating_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon93 = QIcon()
        icon93.addFile(u":/catalysts/assets/images/catalysts/accelerating_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accelerating_catalyst_btn.setIcon(icon93)
        self.accelerating_catalyst_btn.setIconSize(QSize(30, 30))
        self.accelerating_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.accelerating_catalyst_btn)

        self.unstable_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.unstable_catalyst_btn)
        self.unstable_catalyst_btn.setObjectName(u"unstable_catalyst_btn")
        sizePolicy.setHeightForWidth(self.unstable_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.unstable_catalyst_btn.setSizePolicy(sizePolicy)
        self.unstable_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.unstable_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon94 = QIcon()
        icon94.addFile(u":/catalysts/assets/images/catalysts/unstable_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.unstable_catalyst_btn.setIcon(icon94)
        self.unstable_catalyst_btn.setIconSize(QSize(30, 30))
        self.unstable_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.unstable_catalyst_btn)

        self.noxious_catalyst_btn = QPushButton(self.catalyst_btn_row)
        self.catalysts_btns_group.addButton(self.noxious_catalyst_btn)
        self.noxious_catalyst_btn.setObjectName(u"noxious_catalyst_btn")
        sizePolicy.setHeightForWidth(self.noxious_catalyst_btn.sizePolicy().hasHeightForWidth())
        self.noxious_catalyst_btn.setSizePolicy(sizePolicy)
        self.noxious_catalyst_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.noxious_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        icon95 = QIcon()
        icon95.addFile(u":/catalysts/assets/images/catalysts/noxious_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noxious_catalyst_btn.setIcon(icon95)
        self.noxious_catalyst_btn.setIconSize(QSize(30, 30))
        self.noxious_catalyst_btn.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.noxious_catalyst_btn)


        self.verticalLayout_22.addWidget(self.catalyst_btn_row)

        self.catalyst_mode_row = QWidget(self.catalysts)
        self.catalyst_mode_row.setObjectName(u"catalyst_mode_row")
        sizePolicy.setHeightForWidth(self.catalyst_mode_row.sizePolicy().hasHeightForWidth())
        self.catalyst_mode_row.setSizePolicy(sizePolicy)
        self.horizontalLayout_14 = QHBoxLayout(self.catalyst_mode_row)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.catalyst_mode_label = QLabel(self.catalyst_mode_row)
        self.catalyst_mode_label.setObjectName(u"catalyst_mode_label")

        self.horizontalLayout_14.addWidget(self.catalyst_mode_label)

        self.max_catalyst_btn = QPushButton(self.catalyst_mode_row)
        self.catalysts_mode_btns_group = QButtonGroup(MainWindow)
        self.catalysts_mode_btns_group.setObjectName(u"catalysts_mode_btns_group")
        self.catalysts_mode_btns_group.addButton(self.max_catalyst_btn)
        self.max_catalyst_btn.setObjectName(u"max_catalyst_btn")
        self.max_catalyst_btn.setStyleSheet(u"QPushButton {\n"
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
        self.max_catalyst_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.max_catalyst_btn)

        self.single_catalys_btn = QPushButton(self.catalyst_mode_row)
        self.catalysts_mode_btns_group.addButton(self.single_catalys_btn)
        self.single_catalys_btn.setObjectName(u"single_catalys_btn")
        self.single_catalys_btn.setStyleSheet(u"QPushButton {\n"
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
        self.single_catalys_btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.single_catalys_btn)


        self.verticalLayout_22.addWidget(self.catalyst_mode_row, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.catalysts)
        self.beast_crafts = QWidget()
        self.beast_crafts.setObjectName(u"beast_crafts")
        sizePolicy7.setHeightForWidth(self.beast_crafts.sizePolicy().hasHeightForWidth())
        self.beast_crafts.setSizePolicy(sizePolicy7)
        self.beast_crafts.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.beast_crafts)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.beast_crafting_methods_btns = QWidget(self.beast_crafts)
        self.beast_crafting_methods_btns.setObjectName(u"beast_crafting_methods_btns")
        self.beast_crafting_methods_btns.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;\n"
"border-image: none;\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.beast_crafting_methods_btns)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.beast_crafting_hide_btn = QPushButton(self.beast_crafting_methods_btns)
        self.beast_crafting_hide_btn.setObjectName(u"beast_crafting_hide_btn")
        self.beast_crafting_hide_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.beast_crafting_hide_btn.sizePolicy().hasHeightForWidth())
        self.beast_crafting_hide_btn.setSizePolicy(sizePolicy10)
        self.beast_crafting_hide_btn.setFont(font2)
        self.beast_crafting_hide_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.beast_crafting_hide_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.beast_crafting_hide_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")

        self.horizontalLayout_15.addWidget(self.beast_crafting_hide_btn)

        self.beast_crafting_methods_label = QLabel(self.beast_crafting_methods_btns)
        self.beast_crafting_methods_label.setObjectName(u"beast_crafting_methods_label")
        sizePolicy.setHeightForWidth(self.beast_crafting_methods_label.sizePolicy().hasHeightForWidth())
        self.beast_crafting_methods_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.beast_crafting_methods_label)

        self.bprefix__to_suffix_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group = QButtonGroup(MainWindow)
        self.beast_crafting_btns_group.setObjectName(u"beast_crafting_btns_group")
        self.beast_crafting_btns_group.addButton(self.bprefix__to_suffix_btn)
        self.bprefix__to_suffix_btn.setObjectName(u"bprefix__to_suffix_btn")
        self.bprefix__to_suffix_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bprefix__to_suffix_btn.setStyleSheet(u"QPushButton {\n"
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
        icon96 = QIcon()
        icon96.addFile(u":/beasts/assets/images/beasts/bpretsuf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bprefix__to_suffix_btn.setIcon(icon96)
        self.bprefix__to_suffix_btn.setIconSize(QSize(30, 30))
        self.bprefix__to_suffix_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bprefix__to_suffix_btn)

        self.bsuffix_to_prefix_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bsuffix_to_prefix_btn)
        self.bsuffix_to_prefix_btn.setObjectName(u"bsuffix_to_prefix_btn")
        self.bsuffix_to_prefix_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bsuffix_to_prefix_btn.setStyleSheet(u"QPushButton {\n"
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
        icon97 = QIcon()
        icon97.addFile(u":/beasts/assets/images/beasts/bsuftpre.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bsuffix_to_prefix_btn.setIcon(icon97)
        self.bsuffix_to_prefix_btn.setIconSize(QSize(30, 30))
        self.bsuffix_to_prefix_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bsuffix_to_prefix_btn)

        self.bimprint_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bimprint_btn)
        self.bimprint_btn.setObjectName(u"bimprint_btn")
        self.bimprint_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bimprint_btn.setStyleSheet(u"QPushButton {\n"
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
        icon98 = QIcon()
        icon98.addFile(u":/beasts/assets/images/beasts/bimprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bimprint_btn.setIcon(icon98)
        self.bimprint_btn.setIconSize(QSize(30, 30))
        self.bimprint_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bimprint_btn)

        self.breroll_values_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.breroll_values_btn)
        self.breroll_values_btn.setObjectName(u"breroll_values_btn")
        self.breroll_values_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.breroll_values_btn.setStyleSheet(u"QPushButton {\n"
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
        icon99 = QIcon()
        icon99.addFile(u":/beasts/assets/images/beasts/breroll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.breroll_values_btn.setIcon(icon99)
        self.breroll_values_btn.setIconSize(QSize(30, 30))
        self.breroll_values_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.breroll_values_btn)

        self.bcat_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bcat_btn)
        self.bcat_btn.setObjectName(u"bcat_btn")
        self.bcat_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bcat_btn.setStyleSheet(u"QPushButton {\n"
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
        icon100 = QIcon()
        icon100.addFile(u":/beasts/assets/images/beasts/bcat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bcat_btn.setIcon(icon100)
        self.bcat_btn.setIconSize(QSize(30, 30))
        self.bcat_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bcat_btn)

        self.bavian_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bavian_btn)
        self.bavian_btn.setObjectName(u"bavian_btn")
        self.bavian_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bavian_btn.setStyleSheet(u"QPushButton {\n"
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
        icon101 = QIcon()
        icon101.addFile(u":/beasts/assets/images/beasts/bavian.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bavian_btn.setIcon(icon101)
        self.bavian_btn.setIconSize(QSize(30, 30))
        self.bavian_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bavian_btn)

        self.bspider_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bspider_btn)
        self.bspider_btn.setObjectName(u"bspider_btn")
        self.bspider_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bspider_btn.setStyleSheet(u"QPushButton {\n"
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
        icon102 = QIcon()
        icon102.addFile(u":/beasts/assets/images/beasts/bspider.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bspider_btn.setIcon(icon102)
        self.bspider_btn.setIconSize(QSize(30, 30))
        self.bspider_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bspider_btn)

        self.bcrab_btn = CustomCursorButton(self.beast_crafting_methods_btns)
        self.beast_crafting_btns_group.addButton(self.bcrab_btn)
        self.bcrab_btn.setObjectName(u"bcrab_btn")
        self.bcrab_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.bcrab_btn.setStyleSheet(u"QPushButton {\n"
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
        icon103 = QIcon()
        icon103.addFile(u":/beasts/assets/images/beasts/bcrab.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bcrab_btn.setIcon(icon103)
        self.bcrab_btn.setIconSize(QSize(30, 30))
        self.bcrab_btn.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.bcrab_btn)


        self.verticalLayout_29.addWidget(self.beast_crafting_methods_btns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer)

        self.crafting_method_pages.addWidget(self.beast_crafts)
        self.eldritch_crafts = QWidget()
        self.eldritch_crafts.setObjectName(u"eldritch_crafts")
        sizePolicy7.setHeightForWidth(self.eldritch_crafts.sizePolicy().hasHeightForWidth())
        self.eldritch_crafts.setSizePolicy(sizePolicy7)
        self.horizontalLayout_18 = QHBoxLayout(self.eldritch_crafts)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.eldritch_btns_container = QWidget(self.eldritch_crafts)
        self.eldritch_btns_container.setObjectName(u"eldritch_btns_container")
        self.eldritch_btns_container.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.eldritch_btns_container.sizePolicy().hasHeightForWidth())
        self.eldritch_btns_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_36 = QVBoxLayout(self.eldritch_btns_container)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.eldritch_btn_row1 = QWidget(self.eldritch_btns_container)
        self.eldritch_btn_row1.setObjectName(u"eldritch_btn_row1")
        self.eldritch_btn_row1.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.eldritch_btn_row1.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row1.setSizePolicy(sizePolicy7)
        self.fossil_row1_3 = QHBoxLayout(self.eldritch_btn_row1)
        self.fossil_row1_3.setSpacing(0)
        self.fossil_row1_3.setContentsMargins(0, 0, 0, 0)
        self.fossil_row1_3.setObjectName(u"fossil_row1_3")
        self.fossil_row1_3.setContentsMargins(0, 0, 0, 0)
        self.eldritch_hide_btn = QPushButton(self.eldritch_btn_row1)
        self.eldritch_hide_btn.setObjectName(u"eldritch_hide_btn")
        self.eldritch_hide_btn.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.eldritch_hide_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_hide_btn.setSizePolicy(sizePolicy8)
        self.eldritch_hide_btn.setFont(font2)
        self.eldritch_hide_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eldritch_hide_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.eldritch_hide_btn.setStyleSheet(u"QPushButton {\n"
"border: 1px solid #90701b;\n"
"border-radius: 0px;\n"
"border-image: none;\n"
"box-shadow: inset 0 1px 1px #e6b15f,0 1px 2px rgba(0,0,0,0.61);\n"
"font-family: Open Sans;\n"
"font-size: 12px;\n"
"font-weight: bold;\n"
"color: #333;\n"
"text-shadow: 1px 1px #FFF;\n"
"line-height: 29px;\n"
"height: 29px;\n"
"margin: 0px;\n"
"padding: 0px 6px 0px 4px;\n"
"cursor: pointer;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
"}\n"
"            QPushButton::hover {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(237, 231, 182, 255), stop:1 rgba(249, 206, 144, 255));\n"
"           }\n"
"            QPushButton::pressed {\n"
"                \n"
"	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(221, 204, 153, 1), stop:1 rgba(255, 238, 187, 255));\n"
"            }\n"
"			QPushButton::checked {\n"
"				background-color: qlineargradient(x1: 0, y1: 0,"
                        " x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 1px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.eldritch_hide_btn.setCheckable(True)

        self.fossil_row1_3.addWidget(self.eldritch_hide_btn)

        self.eldritch_method_label = QLabel(self.eldritch_btn_row1)
        self.eldritch_method_label.setObjectName(u"eldritch_method_label")
        self.eldritch_method_label.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.eldritch_method_label.sizePolicy().hasHeightForWidth())
        self.eldritch_method_label.setSizePolicy(sizePolicy8)

        self.fossil_row1_3.addWidget(self.eldritch_method_label)

        self.eldritch_chaos_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.eldritch_crafting_btns_group = QButtonGroup(MainWindow)
        self.eldritch_crafting_btns_group.setObjectName(u"eldritch_crafting_btns_group")
        self.eldritch_crafting_btns_group.addButton(self.eldritch_chaos_btn)
        self.eldritch_chaos_btn.setObjectName(u"eldritch_chaos_btn")
        self.eldritch_chaos_btn.setEnabled(True)
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.eldritch_chaos_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_chaos_btn.setSizePolicy(sizePolicy11)
        self.eldritch_chaos_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eldritch_chaos_btn.setStyleSheet(u"QPushButton {\n"
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
        icon104 = QIcon()
        icon104.addFile(u":/eldritch/assets/images/eldritch/eldritch_chaos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_chaos_btn.setIcon(icon104)
        self.eldritch_chaos_btn.setIconSize(QSize(30, 30))
        self.eldritch_chaos_btn.setCheckable(True)

        self.fossil_row1_3.addWidget(self.eldritch_chaos_btn)

        self.eldritch_exalted_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.eldritch_crafting_btns_group.addButton(self.eldritch_exalted_btn)
        self.eldritch_exalted_btn.setObjectName(u"eldritch_exalted_btn")
        self.eldritch_exalted_btn.setEnabled(True)
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.eldritch_exalted_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_exalted_btn.setSizePolicy(sizePolicy12)
        self.eldritch_exalted_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eldritch_exalted_btn.setStyleSheet(u"QPushButton {\n"
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
        icon105 = QIcon()
        icon105.addFile(u":/eldritch/assets/images/eldritch/eldritch_exalted.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_exalted_btn.setIcon(icon105)
        self.eldritch_exalted_btn.setIconSize(QSize(30, 30))
        self.eldritch_exalted_btn.setCheckable(True)

        self.fossil_row1_3.addWidget(self.eldritch_exalted_btn)

        self.eldritch_annul_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.eldritch_crafting_btns_group.addButton(self.eldritch_annul_btn)
        self.eldritch_annul_btn.setObjectName(u"eldritch_annul_btn")
        self.eldritch_annul_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.eldritch_annul_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_annul_btn.setSizePolicy(sizePolicy12)
        self.eldritch_annul_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.eldritch_annul_btn.setStyleSheet(u"QPushButton {\n"
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
        icon106 = QIcon()
        icon106.addFile(u":/eldritch/assets/images/eldritch/eldritch_annul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_annul_btn.setIcon(icon106)
        self.eldritch_annul_btn.setIconSize(QSize(30, 30))
        self.eldritch_annul_btn.setCheckable(True)

        self.fossil_row1_3.addWidget(self.eldritch_annul_btn)

        self.orb_of_conflict_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.eldritch_crafting_btns_group.addButton(self.orb_of_conflict_btn)
        self.orb_of_conflict_btn.setObjectName(u"orb_of_conflict_btn")
        self.orb_of_conflict_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.orb_of_conflict_btn.sizePolicy().hasHeightForWidth())
        self.orb_of_conflict_btn.setSizePolicy(sizePolicy12)
        self.orb_of_conflict_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.orb_of_conflict_btn.setStyleSheet(u"QPushButton {\n"
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
        icon107 = QIcon()
        icon107.addFile(u":/eldritch/assets/images/eldritch/orb_of_conflict.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orb_of_conflict_btn.setIcon(icon107)
        self.orb_of_conflict_btn.setIconSize(QSize(30, 30))
        self.orb_of_conflict_btn.setCheckable(True)

        self.fossil_row1_3.addWidget(self.orb_of_conflict_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row1)

        self.eldritch_btn_row2 = QWidget(self.eldritch_btns_container)
        self.eldritch_btn_row2.setObjectName(u"eldritch_btn_row2")
        self.eldritch_btn_row2.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.eldritch_btn_row2.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row2.setSizePolicy(sizePolicy7)
        self.horizontalLayout_17 = QHBoxLayout(self.eldritch_btn_row2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lesser_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.eldritch_crafting_btns_group.addButton(self.lesser_ember_btn)
        self.lesser_ember_btn.setObjectName(u"lesser_ember_btn")
        self.lesser_ember_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.lesser_ember_btn.sizePolicy().hasHeightForWidth())
        self.lesser_ember_btn.setSizePolicy(sizePolicy12)
        self.lesser_ember_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lesser_ember_btn.setStyleSheet(u"QPushButton {\n"
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
        icon108 = QIcon()
        icon108.addFile(u":/eldritch/assets/images/eldritch/lesser_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lesser_ember_btn.setIcon(icon108)
        self.lesser_ember_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.lesser_ember_btn, 0, Qt.AlignHCenter)

        self.greater_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.eldritch_crafting_btns_group.addButton(self.greater_ember_btn)
        self.greater_ember_btn.setObjectName(u"greater_ember_btn")
        self.greater_ember_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.greater_ember_btn.sizePolicy().hasHeightForWidth())
        self.greater_ember_btn.setSizePolicy(sizePolicy12)
        self.greater_ember_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.greater_ember_btn.setStyleSheet(u"QPushButton {\n"
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
        icon109 = QIcon()
        icon109.addFile(u":/eldritch/assets/images/eldritch/greater_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.greater_ember_btn.setIcon(icon109)
        self.greater_ember_btn.setIconSize(QSize(30, 30))
        self.greater_ember_btn.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.greater_ember_btn)

        self.grand_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.eldritch_crafting_btns_group.addButton(self.grand_ember_btn)
        self.grand_ember_btn.setObjectName(u"grand_ember_btn")
        self.grand_ember_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.grand_ember_btn.sizePolicy().hasHeightForWidth())
        self.grand_ember_btn.setSizePolicy(sizePolicy12)
        self.grand_ember_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.grand_ember_btn.setStyleSheet(u"QPushButton {\n"
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
        icon110 = QIcon()
        icon110.addFile(u":/eldritch/assets/images/eldritch/grand_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grand_ember_btn.setIcon(icon110)
        self.grand_ember_btn.setIconSize(QSize(30, 30))
        self.grand_ember_btn.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.grand_ember_btn)

        self.exceptional_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.eldritch_crafting_btns_group.addButton(self.exceptional_ember_btn)
        self.exceptional_ember_btn.setObjectName(u"exceptional_ember_btn")
        self.exceptional_ember_btn.setEnabled(True)
        sizePolicy12.setHeightForWidth(self.exceptional_ember_btn.sizePolicy().hasHeightForWidth())
        self.exceptional_ember_btn.setSizePolicy(sizePolicy12)
        self.exceptional_ember_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exceptional_ember_btn.setStyleSheet(u"QPushButton {\n"
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
        icon111 = QIcon()
        icon111.addFile(u":/eldritch/assets/images/eldritch/exceptional_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exceptional_ember_btn.setIcon(icon111)
        self.exceptional_ember_btn.setIconSize(QSize(30, 30))
        self.exceptional_ember_btn.setCheckable(True)

        self.horizontalLayout_17.addWidget(self.exceptional_ember_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row2, 0, Qt.AlignHCenter)

        self.eldritch_btn_row3 = QWidget(self.eldritch_btns_container)
        self.eldritch_btn_row3.setObjectName(u"eldritch_btn_row3")
        sizePolicy7.setHeightForWidth(self.eldritch_btn_row3.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row3.setSizePolicy(sizePolicy7)
        self.horizontalLayout_16 = QHBoxLayout(self.eldritch_btn_row3)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lesser_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.eldritch_crafting_btns_group.addButton(self.lesser_ichor_btn)
        self.lesser_ichor_btn.setObjectName(u"lesser_ichor_btn")
        self.lesser_ichor_btn.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.lesser_ichor_btn.sizePolicy().hasHeightForWidth())
        self.lesser_ichor_btn.setSizePolicy(sizePolicy4)
        self.lesser_ichor_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.lesser_ichor_btn.setStyleSheet(u"QPushButton {\n"
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
        icon112 = QIcon()
        icon112.addFile(u":/eldritch/assets/images/eldritch/lesser_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lesser_ichor_btn.setIcon(icon112)
        self.lesser_ichor_btn.setIconSize(QSize(30, 30))
        self.lesser_ichor_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.lesser_ichor_btn)

        self.greater_icho_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.eldritch_crafting_btns_group.addButton(self.greater_icho_btn)
        self.greater_icho_btn.setObjectName(u"greater_icho_btn")
        self.greater_icho_btn.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.greater_icho_btn.sizePolicy().hasHeightForWidth())
        self.greater_icho_btn.setSizePolicy(sizePolicy4)
        self.greater_icho_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.greater_icho_btn.setStyleSheet(u"QPushButton {\n"
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
        icon113 = QIcon()
        icon113.addFile(u":/eldritch/assets/images/eldritch/greater_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.greater_icho_btn.setIcon(icon113)
        self.greater_icho_btn.setIconSize(QSize(30, 30))
        self.greater_icho_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.greater_icho_btn)

        self.grand_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.eldritch_crafting_btns_group.addButton(self.grand_ichor_btn)
        self.grand_ichor_btn.setObjectName(u"grand_ichor_btn")
        self.grand_ichor_btn.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.grand_ichor_btn.sizePolicy().hasHeightForWidth())
        self.grand_ichor_btn.setSizePolicy(sizePolicy4)
        self.grand_ichor_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.grand_ichor_btn.setStyleSheet(u"QPushButton {\n"
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
        icon114 = QIcon()
        icon114.addFile(u":/eldritch/assets/images/eldritch/grand_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grand_ichor_btn.setIcon(icon114)
        self.grand_ichor_btn.setIconSize(QSize(30, 30))
        self.grand_ichor_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.grand_ichor_btn)

        self.exceptional_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.eldritch_crafting_btns_group.addButton(self.exceptional_ichor_btn)
        self.exceptional_ichor_btn.setObjectName(u"exceptional_ichor_btn")
        self.exceptional_ichor_btn.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.exceptional_ichor_btn.sizePolicy().hasHeightForWidth())
        self.exceptional_ichor_btn.setSizePolicy(sizePolicy4)
        self.exceptional_ichor_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exceptional_ichor_btn.setStyleSheet(u"QPushButton {\n"
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
        icon115 = QIcon()
        icon115.addFile(u":/eldritch/assets/images/eldritch/exceptional_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exceptional_ichor_btn.setIcon(icon115)
        self.exceptional_ichor_btn.setIconSize(QSize(30, 30))
        self.exceptional_ichor_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.exceptional_ichor_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_18.addWidget(self.eldritch_btns_container)

        self.crafting_method_pages.addWidget(self.eldritch_crafts)
        self.syndicate_crafts = QWidget()
        self.syndicate_crafts.setObjectName(u"syndicate_crafts")
        sizePolicy7.setHeightForWidth(self.syndicate_crafts.sizePolicy().hasHeightForWidth())
        self.syndicate_crafts.setSizePolicy(sizePolicy7)
        self.crafting_method_pages.addWidget(self.syndicate_crafts)

        self.verticalLayout_7.addWidget(self.crafting_method_pages, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.crafting_methods, 0, Qt.AlignTop)

        self.item_info_container = QWidget(self.crafting_page)
        self.item_info_container.setObjectName(u"item_info_container")
        sizePolicy1.setHeightForWidth(self.item_info_container.sizePolicy().hasHeightForWidth())
        self.item_info_container.setSizePolicy(sizePolicy1)
        self.item_info_container.setStyleSheet(u"QWidget {\n"
"border-image: none;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.item_info_container)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(20, 0, 20, 20)
        self.item_info_display = QWidget(self.item_info_container)
        self.item_info_display.setObjectName(u"item_info_display")
        sizePolicy1.setHeightForWidth(self.item_info_display.sizePolicy().hasHeightForWidth())
        self.item_info_display.setSizePolicy(sizePolicy1)
        self.item_info_display.setAutoFillBackground(False)
        self.item_info_display.setStyleSheet(u"QFrame {\n"
"border-image: none;\n"
"}\n"
"QWidget {\n"
"border-image: none;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.item_info_display)
        self.horizontalLayout_4.setSpacing(60)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.available_mods_container = QWidget(self.item_info_display)
        self.available_mods_container.setObjectName(u"available_mods_container")
        self.available_mods_container.setMaximumSize(QSize(500, 400))
        self.verticalLayout_8 = QVBoxLayout(self.available_mods_container)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.search_bar_container = QFrame(self.available_mods_container)
        self.search_bar_container.setObjectName(u"search_bar_container")
        sizePolicy13 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.search_bar_container.sizePolicy().hasHeightForWidth())
        self.search_bar_container.setSizePolicy(sizePolicy13)
        self.horizontalLayout_3 = QHBoxLayout(self.search_bar_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.affix_search_bar = QLineEdit(self.search_bar_container)
        self.affix_search_bar.setObjectName(u"affix_search_bar")
        sizePolicy13.setHeightForWidth(self.affix_search_bar.sizePolicy().hasHeightForWidth())
        self.affix_search_bar.setSizePolicy(sizePolicy13)
        self.affix_search_bar.setMinimumSize(QSize(130, 30))
        self.affix_search_bar.setMaximumSize(QSize(1675555, 30))
        font9 = QFont()
        font9.setFamilies([u"Open Sans"])
        font9.setBold(False)
        font9.setItalic(False)
        self.affix_search_bar.setFont(font9)
        self.affix_search_bar.setFrame(True)
        self.affix_search_bar.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.affix_search_bar)


        self.verticalLayout_8.addWidget(self.search_bar_container)

        self.modpool_history_widget = QWidget(self.available_mods_container)
        self.modpool_history_widget.setObjectName(u"modpool_history_widget")
        self.modpool_history_widget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.modpool_history_widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.crafting_toolbox = QWidget(self.modpool_history_widget)
        self.crafting_toolbox.setObjectName(u"crafting_toolbox")
        sizePolicy1.setHeightForWidth(self.crafting_toolbox.sizePolicy().hasHeightForWidth())
        self.crafting_toolbox.setSizePolicy(sizePolicy1)
        self.crafting_toolbox.setMinimumSize(QSize(120, 0))
        self.crafting_toolbox.setMaximumSize(QSize(200, 360))
        self.crafting_toolbox.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.crafting_toolbox)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.crafting_history_container = QWidget(self.crafting_toolbox)
        self.crafting_history_container.setObjectName(u"crafting_history_container")
        self.crafting_history_container.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.crafting_history_container)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.crafting_history = QToolBox(self.crafting_history_container)
        self.crafting_history.setObjectName(u"crafting_history")
        self.crafting_history.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.crafting_history.sizePolicy().hasHeightForWidth())
        self.crafting_history.setSizePolicy(sizePolicy1)
        self.crafting_history.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamilies([u"Open Sans"])
        font10.setBold(True)
        font10.setItalic(False)
        self.crafting_history.setFont(font10)
        self.crafting_history.setStyleSheet(u"QWidget {\n"
"	vertical-align: top;\n"
"	padding: 5px 10px;\n"
"	text-shadow: 1px 1px #000;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));\n"
"\n"
"	border: 0px solid #000;\n"
"	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);\n"
"	box-sizing: border-box;\n"
"	text-transform: uppercase;\n"
"	font-weight: bold;\n"
"	color: #f6e5b2;\n"
"	font-family: Open Sans;\n"
"	font-size: 14px;\n"
"	margin: 0px;\n"
"}")
        self.crafting_history.setFrameShape(QFrame.NoFrame)
        self.crafting_history.setFrameShadow(QFrame.Plain)
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.history_tab.setGeometry(QRect(0, 0, 124, 168))
        self.history_tab.setFont(font2)
        self.history_tab.setAutoFillBackground(False)
        self.history_tab.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.history_tab)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.crafting_history.addItem(self.history_tab, u"History")
        self.spending_tab = QWidget()
        self.spending_tab.setObjectName(u"spending_tab")
        self.spending_tab.setGeometry(QRect(0, 0, 124, 168))
        self.spending_tab.setFont(font2)
        self.spending_tab.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.spending_tab)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.crafting_history.addItem(self.spending_tab, u"Spending")
        self.export_tab = QWidget()
        self.export_tab.setObjectName(u"export_tab")
        self.export_tab.setGeometry(QRect(0, 0, 124, 168))
        self.export_tab.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.export_tab)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.crafting_history.addItem(self.export_tab, u"Export")

        self.verticalLayout_20.addWidget(self.crafting_history)

        self.status_buttons = QWidget(self.crafting_history_container)
        self.status_buttons.setObjectName(u"status_buttons")
        sizePolicy1.setHeightForWidth(self.status_buttons.sizePolicy().hasHeightForWidth())
        self.status_buttons.setSizePolicy(sizePolicy1)
        self.status_buttons.setMinimumSize(QSize(120, 90))
        self.status_buttons.setMaximumSize(QSize(400, 90))
        self.status_buttons.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_buttons.setStyleSheet(u"QPushButton {\n"
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
"			QPushButton::checked {\n"
"				background-col"
                        "or: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,\n"
"                                                 stop: 0 #2d2d2d, stop: 1 #4b4b4b);\n"
"				border: 5px inset #FFF;\n"
"				box-shadow: none;\n"
"			}\n"
"            QPushButton::flat {\n"
"                border: none;\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.status_buttons)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.clear_item_options = QPushButton(self.status_buttons)
        self.clear_item_options.setObjectName(u"clear_item_options")
        sizePolicy.setHeightForWidth(self.clear_item_options.sizePolicy().hasHeightForWidth())
        self.clear_item_options.setSizePolicy(sizePolicy)
        self.clear_item_options.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_item_options.setCheckable(False)
        self.clear_item_options.setAutoDefault(False)
        self.clear_item_options.setFlat(False)

        self.verticalLayout_31.addWidget(self.clear_item_options)

        self.import_custom_item = QPushButton(self.status_buttons)
        self.import_custom_item.setObjectName(u"import_custom_item")
        sizePolicy.setHeightForWidth(self.import_custom_item.sizePolicy().hasHeightForWidth())
        self.import_custom_item.setSizePolicy(sizePolicy)
        self.import_custom_item.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_custom_item.setCheckable(False)
        self.import_custom_item.setFlat(False)

        self.verticalLayout_31.addWidget(self.import_custom_item)

        self.simulate_crafting = QPushButton(self.status_buttons)
        self.simulate_crafting.setObjectName(u"simulate_crafting")
        sizePolicy.setHeightForWidth(self.simulate_crafting.sizePolicy().hasHeightForWidth())
        self.simulate_crafting.setSizePolicy(sizePolicy)
        self.simulate_crafting.setMinimumSize(QSize(0, 0))
        self.simulate_crafting.setCursor(QCursor(Qt.PointingHandCursor))
        self.simulate_crafting.setCheckable(False)
        self.simulate_crafting.setChecked(False)
        self.simulate_crafting.setFlat(False)

        self.verticalLayout_31.addWidget(self.simulate_crafting)


        self.verticalLayout_20.addWidget(self.status_buttons)


        self.verticalLayout_37.addWidget(self.crafting_history_container)


        self.horizontalLayout_5.addWidget(self.crafting_toolbox)

        self.mods_container = QWidget(self.modpool_history_widget)
        self.mods_container.setObjectName(u"mods_container")
        sizePolicy1.setHeightForWidth(self.mods_container.sizePolicy().hasHeightForWidth())
        self.mods_container.setSizePolicy(sizePolicy1)
        self.verticalLayout_39 = QVBoxLayout(self.mods_container)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.modpool_tabs = QWidget(self.mods_container)
        self.modpool_tabs.setObjectName(u"modpool_tabs")
        sizePolicy1.setHeightForWidth(self.modpool_tabs.sizePolicy().hasHeightForWidth())
        self.modpool_tabs.setSizePolicy(sizePolicy1)
        self.modpool_tabs.setMinimumSize(QSize(0, 0))
        self.modpool_tabs.setMaximumSize(QSize(500, 500))
        self.verticalLayout_32 = QVBoxLayout(self.modpool_tabs)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.modpool_btns_layout = QFrame(self.modpool_tabs)
        self.modpool_btns_layout.setObjectName(u"modpool_btns_layout")
        sizePolicy13.setHeightForWidth(self.modpool_btns_layout.sizePolicy().hasHeightForWidth())
        self.modpool_btns_layout.setSizePolicy(sizePolicy13)
        self.modpool_btns_layout.setStyleSheet(u"QFrame {\n"
"padding: 0px;\n"
"margin: 0px;\n"
"}\n"
"QWidget {\n"
"margin: 0px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60, 60, 1), stop:1 rgba(136, 75, 75, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: #FFF;\n"
"text-shadow: 1px 1px #000;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.modpool_btns_layout)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.prefix_btn = QPushButton(self.modpool_btns_layout)
        self.modpool_btns_group = QButtonGroup(MainWindow)
        self.modpool_btns_group.setObjectName(u"modpool_btns_group")
        self.modpool_btns_group.addButton(self.prefix_btn)
        self.prefix_btn.setObjectName(u"prefix_btn")
        sizePolicy1.setHeightForWidth(self.prefix_btn.sizePolicy().hasHeightForWidth())
        self.prefix_btn.setSizePolicy(sizePolicy1)
        self.prefix_btn.setStyleSheet(u"QPushButton::flat {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60, 60, 1), stop:1 rgba(136, 75, 75, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: #FFF;\n"
"text-shadow: 1px 1px #000;\n"
"}")
        self.prefix_btn.setCheckable(True)
        self.prefix_btn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.prefix_btn)

        self.suffix_btn = QPushButton(self.modpool_btns_layout)
        self.modpool_btns_group.addButton(self.suffix_btn)
        self.suffix_btn.setObjectName(u"suffix_btn")
        sizePolicy1.setHeightForWidth(self.suffix_btn.sizePolicy().hasHeightForWidth())
        self.suffix_btn.setSizePolicy(sizePolicy1)
        self.suffix_btn.setMinimumSize(QSize(0, 0))
        self.suffix_btn.setMaximumSize(QSize(16777215, 1677215))
        self.suffix_btn.setStyleSheet(u"QPushButton::flat {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60, 60, 1), stop:1 rgba(136, 75, 75, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: #FFF;\n"
"text-shadow: 1px 1px #000;\n"
"}")
        self.suffix_btn.setCheckable(True)
        self.suffix_btn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.suffix_btn)

        self.implicit_btn = QPushButton(self.modpool_btns_layout)
        self.modpool_btns_group.addButton(self.implicit_btn)
        self.implicit_btn.setObjectName(u"implicit_btn")
        sizePolicy1.setHeightForWidth(self.implicit_btn.sizePolicy().hasHeightForWidth())
        self.implicit_btn.setSizePolicy(sizePolicy1)
        self.implicit_btn.setStyleSheet(u"QPushButton::flat {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60, 60, 1), stop:1 rgba(136, 75, 75, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: #FFF;\n"
"text-shadow: 1px 1px #000;\n"
"}")
        self.implicit_btn.setCheckable(True)
        self.implicit_btn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.implicit_btn)


        self.verticalLayout_32.addWidget(self.modpool_btns_layout)

        self.modpool_container = QStackedWidget(self.modpool_tabs)
        self.modpool_container.setObjectName(u"modpool_container")
        sizePolicy1.setHeightForWidth(self.modpool_container.sizePolicy().hasHeightForWidth())
        self.modpool_container.setSizePolicy(sizePolicy1)
        self.modpool_container.setAutoFillBackground(False)
        self.modpool_container.setFrameShape(QFrame.NoFrame)
        self.modpool_container.setFrameShadow(QFrame.Plain)
        self.prefixes = QWidget()
        self.prefixes.setObjectName(u"prefixes")
        sizePolicy1.setHeightForWidth(self.prefixes.sizePolicy().hasHeightForWidth())
        self.prefixes.setSizePolicy(sizePolicy1)
        self.prefixes.setStyleSheet(u"QWidget {\n"
"	vertical-align: top;\n"
"	padding: 5px 10px;\n"
"	text-shadow: 1px 1px #000;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));\n"
"\n"
"	border: 0px solid #000;\n"
"	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);\n"
"	box-sizing: border-box;\n"
"	text-transform: uppercase;\n"
"	font-weight: bold;\n"
"	color: #f6e5b2;\n"
"	font-family: Open Sans;\n"
"	font-size: 14px;\n"
"	margin: 0px;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.prefixes)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.prefix_tree_view = CustomTreeView(self.prefixes)
        self.prefix_tree_view.setObjectName(u"prefix_tree_view")
        sizePolicy1.setHeightForWidth(self.prefix_tree_view.sizePolicy().hasHeightForWidth())
        self.prefix_tree_view.setSizePolicy(sizePolicy1)
        self.prefix_tree_view.setFocusPolicy(Qt.TabFocus)
        self.prefix_tree_view.setFrameShape(QFrame.NoFrame)
        self.prefix_tree_view.setFrameShadow(QFrame.Plain)
        self.prefix_tree_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prefix_tree_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.prefix_tree_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.prefix_tree_view.setAlternatingRowColors(False)
        self.prefix_tree_view.setTextElideMode(Qt.ElideRight)
        self.prefix_tree_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.prefix_tree_view.setIndentation(10)
        self.prefix_tree_view.setUniformRowHeights(True)
        self.prefix_tree_view.header().setCascadingSectionResizes(False)
        self.prefix_tree_view.header().setMinimumSectionSize(80)
        self.prefix_tree_view.header().setStretchLastSection(False)

        self.verticalLayout_33.addWidget(self.prefix_tree_view)

        self.modpool_container.addWidget(self.prefixes)
        self.suffixes = QWidget()
        self.suffixes.setObjectName(u"suffixes")
        sizePolicy1.setHeightForWidth(self.suffixes.sizePolicy().hasHeightForWidth())
        self.suffixes.setSizePolicy(sizePolicy1)
        self.suffixes.setStyleSheet(u"QWidget {\n"
"	vertical-align: top;\n"
"	padding: 5px 10px;\n"
"	text-shadow: 1px 1px #000;\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));\n"
"\n"
"	border: 0px solid #000;\n"
"	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);\n"
"	box-sizing: border-box;\n"
"	text-transform: uppercase;\n"
"	font-weight: bold;\n"
"	color: #f6e5b2;\n"
"	font-family: Open Sans;\n"
"	font-size: 14px;\n"
"	margin: 0px;\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.suffixes)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.suffix_tree_view = CustomTreeView(self.suffixes)
        self.suffix_tree_view.setObjectName(u"suffix_tree_view")
        sizePolicy1.setHeightForWidth(self.suffix_tree_view.sizePolicy().hasHeightForWidth())
        self.suffix_tree_view.setSizePolicy(sizePolicy1)
        self.suffix_tree_view.setFrameShape(QFrame.NoFrame)
        self.suffix_tree_view.setFrameShadow(QFrame.Plain)
        self.suffix_tree_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suffix_tree_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suffix_tree_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.suffix_tree_view.setAlternatingRowColors(False)
        self.suffix_tree_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.suffix_tree_view.setIndentation(10)
        self.suffix_tree_view.setUniformRowHeights(True)
        self.suffix_tree_view.header().setCascadingSectionResizes(False)
        self.suffix_tree_view.header().setMinimumSectionSize(80)
        self.suffix_tree_view.header().setStretchLastSection(False)

        self.verticalLayout_34.addWidget(self.suffix_tree_view)

        self.modpool_container.addWidget(self.suffixes)
        self.implicits = QWidget()
        self.implicits.setObjectName(u"implicits")
        sizePolicy1.setHeightForWidth(self.implicits.sizePolicy().hasHeightForWidth())
        self.implicits.setSizePolicy(sizePolicy1)
        self.implicits.setStyleSheet(u"QWidget {\n"
"	vertical-align: top;\n"
"	padding: 5px 10px;\n"
"	text-shadow: 1px 1px #000;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));\n"
"	border: 0px solid #000;\n"
"	box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0,.31);\n"
"	box-sizing: border-box;\n"
"	text-transform: uppercase;\n"
"	font-weight: bold;\n"
"	color: #f6e5b2;\n"
"	font-family: Open Sans;\n"
"	font-size: 14px;\n"
"	margin: 0px;\n"
"}")
        self.verticalLayout_35 = QVBoxLayout(self.implicits)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.implicit_tree_view = CustomTreeView(self.implicits)
        self.implicit_tree_view.setObjectName(u"implicit_tree_view")
        sizePolicy1.setHeightForWidth(self.implicit_tree_view.sizePolicy().hasHeightForWidth())
        self.implicit_tree_view.setSizePolicy(sizePolicy1)
        self.implicit_tree_view.setFrameShape(QFrame.NoFrame)
        self.implicit_tree_view.setFrameShadow(QFrame.Plain)
        self.implicit_tree_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.implicit_tree_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.implicit_tree_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.implicit_tree_view.setAlternatingRowColors(False)
        self.implicit_tree_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.implicit_tree_view.setIndentation(10)
        self.implicit_tree_view.setUniformRowHeights(True)
        self.implicit_tree_view.header().setCascadingSectionResizes(False)
        self.implicit_tree_view.header().setMinimumSectionSize(80)
        self.implicit_tree_view.header().setStretchLastSection(False)

        self.verticalLayout_35.addWidget(self.implicit_tree_view)

        self.modpool_container.addWidget(self.implicits)

        self.verticalLayout_32.addWidget(self.modpool_container)


        self.verticalLayout_39.addWidget(self.modpool_tabs)


        self.horizontalLayout_5.addWidget(self.mods_container)


        self.verticalLayout_8.addWidget(self.modpool_history_widget)


        self.horizontalLayout_4.addWidget(self.available_mods_container)

        self.item_view = QFrame(self.item_info_display)
        self.item_view.setObjectName(u"item_view")
        sizePolicy1.setHeightForWidth(self.item_view.sizePolicy().hasHeightForWidth())
        self.item_view.setSizePolicy(sizePolicy1)
        self.item_view.setMinimumSize(QSize(128, 298))
        self.item_view.setMaximumSize(QSize(145, 418))
        self.item_view.setStyleSheet(u"QWidget{\n"
"border: 0px;\n"
"background-color: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.item_view)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.item_img_box = QLabel(self.item_view)
        self.item_img_box.setObjectName(u"item_img_box")
        sizePolicy1.setHeightForWidth(self.item_img_box.sizePolicy().hasHeightForWidth())
        self.item_img_box.setSizePolicy(sizePolicy1)
        self.item_img_box.setMinimumSize(QSize(128, 228))
        self.item_img_box.setMaximumSize(QSize(128, 228))
        self.item_img_box.setStyleSheet(u"QLabel{\n"
"	background-image: url(:/images/assets/images/item_box.png);\n"
"opacity: 0.8;\n"
"}\n"
"QLabel::hover{\n"
"background-color:#ffffff;\n"
"opacity: 1;\n"
"}")
        self.item_img_box.setScaledContents(True)
        self.item_img_box.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.item_img_box, 0, Qt.AlignVCenter)

        self.crafting_button = QLabel(self.item_view)
        self.crafting_button.setObjectName(u"crafting_button")
        sizePolicy1.setHeightForWidth(self.crafting_button.sizePolicy().hasHeightForWidth())
        self.crafting_button.setSizePolicy(sizePolicy1)
        self.crafting_button.setMinimumSize(QSize(0, 39))
        self.crafting_button.setMaximumSize(QSize(128, 39))
        self.crafting_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.crafting_button.setFocusPolicy(Qt.StrongFocus)
        self.crafting_button.setStyleSheet(u"QLabel{\n"
"	background-image: url(:/images/assets/images/craftbtn.png);\n"
"}\n"
"QLabel::hover{\n"
"	background-image: url(:/images/assets/images/craftbtnov.png);\n"
"}")
        self.crafting_button.setScaledContents(True)
        self.crafting_button.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.crafting_button)

        self.item_dps_container = QWidget(self.item_view)
        self.item_dps_container.setObjectName(u"item_dps_container")
        sizePolicy1.setHeightForWidth(self.item_dps_container.sizePolicy().hasHeightForWidth())
        self.item_dps_container.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.item_dps_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.item_dps_box = QLabel(self.item_dps_container)
        self.item_dps_box.setObjectName(u"item_dps_box")
        sizePolicy1.setHeightForWidth(self.item_dps_box.sizePolicy().hasHeightForWidth())
        self.item_dps_box.setSizePolicy(sizePolicy1)
        self.item_dps_box.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: hsla(100, 100%, 100%, 0.1);\n"
"}")
        self.item_dps_box.setFrameShape(QFrame.NoFrame)
        self.item_dps_box.setFrameShadow(QFrame.Plain)
        self.item_dps_box.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.item_dps_box.setMargin(0)

        self.verticalLayout.addWidget(self.item_dps_box)


        self.verticalLayout_2.addWidget(self.item_dps_container)


        self.horizontalLayout_4.addWidget(self.item_view, 0, Qt.AlignHCenter)

        self.item_description = QWidget(self.item_info_display)
        self.item_description.setObjectName(u"item_description")
        sizePolicy14 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.item_description.sizePolicy().hasHeightForWidth())
        self.item_description.setSizePolicy(sizePolicy14)
        self.item_description.setMinimumSize(QSize(400, 400))
        self.item_description.setMaximumSize(QSize(400, 500))
        self.item_description.setBaseSize(QSize(400, 319))
        self.item_description.setTabletTracking(False)
        self.item_description.setContextMenuPolicy(Qt.NoContextMenu)
        self.item_description.setLayoutDirection(Qt.LeftToRight)
        self.item_description.setStyleSheet(u"QWidget {\n"
"border: 0px;\n"
"border-radius: 0px;\n"
"font: fontin;\n"
"background-color: black;\n"
"background-color: hsla(0, 0%, 0%, .8);\n"
"border-image: none;\n"
"background-image: none;\n"
"}\n"
"\n"
"QLabel {\n"
"background-color: black;\n"
"background-color: hsla(0, 0%, 0%, .8);\n"
"\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.item_description)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.item_description_layout = QFrame(self.item_description)
        self.item_description_layout.setObjectName(u"item_description_layout")
        sizePolicy14.setHeightForWidth(self.item_description_layout.sizePolicy().hasHeightForWidth())
        self.item_description_layout.setSizePolicy(sizePolicy14)
        self.item_description_layout.setMinimumSize(QSize(400, 318))
        self.item_description_layout.setMaximumSize(QSize(400, 800))
        self.item_description_layout.setMouseTracking(False)
        self.item_description_layout.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.item_description_layout)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.item_header = QWidget(self.item_description_layout)
        self.item_header.setObjectName(u"item_header")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.item_header.sizePolicy().hasHeightForWidth())
        self.item_header.setSizePolicy(sizePolicy15)
        self.item_header.setMinimumSize(QSize(400, 54))
        self.item_header.setMaximumSize(QSize(400, 54))
        self.item_header.setBaseSize(QSize(400, 44))
        self.item_header.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout_10 = QVBoxLayout(self.item_header)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.item_header_text_label = QLabel(self.item_header)
        self.item_header_text_label.setObjectName(u"item_header_text_label")
        self.item_header_text_label.setEnabled(True)
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.item_header_text_label.sizePolicy().hasHeightForWidth())
        self.item_header_text_label.setSizePolicy(sizePolicy16)
        self.item_header_text_label.setMinimumSize(QSize(400, 54))
        self.item_header_text_label.setMaximumSize(QSize(400, 54))
        font11 = QFont()
        font11.setFamilies([u"Open Sans"])
        font11.setBold(False)
        font11.setItalic(False)
        font11.setKerning(True)
        self.item_header_text_label.setFont(font11)
        self.item_header_text_label.setStyleSheet(u"background-image: url(:/images/assets/images/item-header-normal.png);")
        self.item_header_text_label.setTextFormat(Qt.RichText)
        self.item_header_text_label.setScaledContents(True)
        self.item_header_text_label.setAlignment(Qt.AlignCenter)
        self.item_header_text_label.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.item_header_text_label)


        self.verticalLayout_4.addWidget(self.item_header)

        self.item_info_box = QWidget(self.item_description_layout)
        self.item_info_box.setObjectName(u"item_info_box")
        sizePolicy.setHeightForWidth(self.item_info_box.sizePolicy().hasHeightForWidth())
        self.item_info_box.setSizePolicy(sizePolicy)
        self.item_info_box.setMinimumSize(QSize(400, 0))
        self.item_info_box.setMaximumSize(QSize(400, 500))
        self.verticalLayout_5 = QVBoxLayout(self.item_info_box)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.affixes = QWidget(self.item_info_box)
        self.affixes.setObjectName(u"affixes")
        sizePolicy16.setHeightForWidth(self.affixes.sizePolicy().hasHeightForWidth())
        self.affixes.setSizePolicy(sizePolicy16)
        self.affixes.setMinimumSize(QSize(400, 0))
        self.affixes.setMaximumSize(QSize(400, 150))
        self.affixes.setStyleSheet(u"color: #827a6c;\n"
"padding: 2px 10px;\n"
"    font-size: 14px;\n"
"	font-style: fontin;\n"
"    line-height: 14px;\n"
"	font-align: center;")
        self.verticalLayout_3 = QVBoxLayout(self.affixes)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.item_properties = QLabel(self.affixes)
        self.item_properties.setObjectName(u"item_properties")
        sizePolicy.setHeightForWidth(self.item_properties.sizePolicy().hasHeightForWidth())
        self.item_properties.setSizePolicy(sizePolicy)
        self.item_properties.setMinimumSize(QSize(0, 0))
        self.item_properties.setMaximumSize(QSize(16777215, 100))
        self.item_properties.setStyleSheet(u"QLabel{\n"
"color: #827a6c;\n"
"padding: 2px 10px;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0;\n"
"}")
        self.item_properties.setTextFormat(Qt.RichText)
        self.item_properties.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_properties)

        self.item_spacer_1 = QLabel(self.affixes)
        self.item_spacer_1.setObjectName(u"item_spacer_1")
        sizePolicy17 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.item_spacer_1.sizePolicy().hasHeightForWidth())
        self.item_spacer_1.setSizePolicy(sizePolicy17)
        self.item_spacer_1.setMaximumSize(QSize(400, 2))
        self.item_spacer_1.setBaseSize(QSize(0, 0))
        self.item_spacer_1.setTextFormat(Qt.RichText)
        self.item_spacer_1.setPixmap(QPixmap(u"C:/Users/spark/source/repos/ExileCraft/ExileCraft/assets/images/item-sep.png"))
        self.item_spacer_1.setScaledContents(False)
        self.item_spacer_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_spacer_1)

        self.item_requirements = QLabel(self.affixes)
        self.item_requirements.setObjectName(u"item_requirements")
        sizePolicy.setHeightForWidth(self.item_requirements.sizePolicy().hasHeightForWidth())
        self.item_requirements.setSizePolicy(sizePolicy)
        self.item_requirements.setMaximumSize(QSize(16777215, 100))
        self.item_requirements.setStyleSheet(u"QLabel{\n"
"color: #827a6c;\n"
"padding: 2px 10px;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0;\n"
"}")
        self.item_requirements.setTextFormat(Qt.RichText)
        self.item_requirements.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_requirements)

        self.item_spacer_2 = QLabel(self.affixes)
        self.item_spacer_2.setObjectName(u"item_spacer_2")
        sizePolicy17.setHeightForWidth(self.item_spacer_2.sizePolicy().hasHeightForWidth())
        self.item_spacer_2.setSizePolicy(sizePolicy17)
        self.item_spacer_2.setMaximumSize(QSize(400, 2))
        self.item_spacer_2.setBaseSize(QSize(0, 0))
        self.item_spacer_2.setTextFormat(Qt.RichText)
        self.item_spacer_2.setPixmap(QPixmap(u"C:/Users/spark/source/repos/ExileCraft/ExileCraft/assets/images/item-sep.png"))
        self.item_spacer_2.setScaledContents(False)
        self.item_spacer_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_spacer_2)

        self.item_implicits = QLabel(self.affixes)
        self.item_implicits.setObjectName(u"item_implicits")
        self.item_implicits.setEnabled(False)
        sizePolicy.setHeightForWidth(self.item_implicits.sizePolicy().hasHeightForWidth())
        self.item_implicits.setSizePolicy(sizePolicy)
        self.item_implicits.setMaximumSize(QSize(16777215, 100))
        self.item_implicits.setStyleSheet(u"QLabel{\n"
"color: #8787fe;\n"
"padding: 2px 10px;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0;\n"
"}")
        self.item_implicits.setTextFormat(Qt.RichText)
        self.item_implicits.setAlignment(Qt.AlignCenter)
        self.item_implicits.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.item_implicits)

        self.item_spacer_3 = QLabel(self.affixes)
        self.item_spacer_3.setObjectName(u"item_spacer_3")
        self.item_spacer_3.setEnabled(False)
        sizePolicy17.setHeightForWidth(self.item_spacer_3.sizePolicy().hasHeightForWidth())
        self.item_spacer_3.setSizePolicy(sizePolicy17)
        self.item_spacer_3.setMaximumSize(QSize(400, 2))
        self.item_spacer_3.setBaseSize(QSize(0, 0))
        self.item_spacer_3.setTextFormat(Qt.RichText)
        self.item_spacer_3.setPixmap(QPixmap(u"C:/Users/spark/source/repos/ExileCraft/ExileCraft/assets/images/item-sep.png"))
        self.item_spacer_3.setScaledContents(False)
        self.item_spacer_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_spacer_3)


        self.verticalLayout_5.addWidget(self.affixes)

        self.modifiers = QWidget(self.item_info_box)
        self.modifiers.setObjectName(u"modifiers")
        self.modifiers.setEnabled(False)
        sizePolicy14.setHeightForWidth(self.modifiers.sizePolicy().hasHeightForWidth())
        self.modifiers.setSizePolicy(sizePolicy14)
        self.modifiers.setMinimumSize(QSize(400, 0))
        self.modifiers.setMaximumSize(QSize(400, 16777215))
        self.modifiers.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.modifiers)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.prefix_info_1 = QLabel(self.modifiers)
        self.prefix_info_1.setObjectName(u"prefix_info_1")
        self.prefix_info_1.setEnabled(False)
        self.prefix_info_1.setMinimumSize(QSize(0, 0))
        self.prefix_info_1.setFont(font9)
        self.prefix_info_1.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_info_1.setTextFormat(Qt.RichText)
        self.prefix_info_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_info_1, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.prefix_1 = QLabel(self.modifiers)
        self.prefix_1.setObjectName(u"prefix_1")
        self.prefix_1.setEnabled(False)
        self.prefix_1.setMinimumSize(QSize(0, 0))
        self.prefix_1.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_1.setTextFormat(Qt.RichText)
        self.prefix_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.prefix_info_2 = QLabel(self.modifiers)
        self.prefix_info_2.setObjectName(u"prefix_info_2")
        self.prefix_info_2.setEnabled(False)
        self.prefix_info_2.setMinimumSize(QSize(0, 0))
        self.prefix_info_2.setFont(font9)
        self.prefix_info_2.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_info_2.setTextFormat(Qt.RichText)
        self.prefix_info_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_info_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.prefix_2 = QLabel(self.modifiers)
        self.prefix_2.setObjectName(u"prefix_2")
        self.prefix_2.setEnabled(False)
        self.prefix_2.setMinimumSize(QSize(0, 0))
        self.prefix_2.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_2.setTextFormat(Qt.RichText)
        self.prefix_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.prefix_info_3 = QLabel(self.modifiers)
        self.prefix_info_3.setObjectName(u"prefix_info_3")
        self.prefix_info_3.setEnabled(False)
        self.prefix_info_3.setMinimumSize(QSize(0, 0))
        self.prefix_info_3.setFont(font9)
        self.prefix_info_3.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_info_3.setTextFormat(Qt.RichText)
        self.prefix_info_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_info_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.prefix_3 = QLabel(self.modifiers)
        self.prefix_3.setObjectName(u"prefix_3")
        self.prefix_3.setEnabled(False)
        self.prefix_3.setMinimumSize(QSize(0, 0))
        self.prefix_3.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.prefix_3.setTextFormat(Qt.RichText)
        self.prefix_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.prefix_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.suffix_info_1 = QLabel(self.modifiers)
        self.suffix_info_1.setObjectName(u"suffix_info_1")
        self.suffix_info_1.setEnabled(False)
        self.suffix_info_1.setMinimumSize(QSize(0, 0))
        self.suffix_info_1.setFont(font9)
        self.suffix_info_1.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_info_1.setTextFormat(Qt.RichText)
        self.suffix_info_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_info_1)

        self.suffix_1 = QLabel(self.modifiers)
        self.suffix_1.setObjectName(u"suffix_1")
        self.suffix_1.setEnabled(False)
        self.suffix_1.setMinimumSize(QSize(0, 0))
        self.suffix_1.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_1.setTextFormat(Qt.RichText)
        self.suffix_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.suffix_info_2 = QLabel(self.modifiers)
        self.suffix_info_2.setObjectName(u"suffix_info_2")
        self.suffix_info_2.setEnabled(False)
        self.suffix_info_2.setMinimumSize(QSize(0, 0))
        self.suffix_info_2.setFont(font9)
        self.suffix_info_2.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_info_2.setTextFormat(Qt.RichText)
        self.suffix_info_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_info_2)

        self.suffix_2 = QLabel(self.modifiers)
        self.suffix_2.setObjectName(u"suffix_2")
        self.suffix_2.setEnabled(False)
        self.suffix_2.setMinimumSize(QSize(0, 0))
        self.suffix_2.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_2.setTextFormat(Qt.RichText)
        self.suffix_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.suffix_info_3 = QLabel(self.modifiers)
        self.suffix_info_3.setObjectName(u"suffix_info_3")
        self.suffix_info_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.suffix_info_3.sizePolicy().hasHeightForWidth())
        self.suffix_info_3.setSizePolicy(sizePolicy)
        self.suffix_info_3.setMinimumSize(QSize(0, 0))
        self.suffix_info_3.setMaximumSize(QSize(16777215, 16))
        self.suffix_info_3.setFont(font9)
        self.suffix_info_3.setStyleSheet(u"QLabel {\n"
"color: #7f7f7f;\n"
"text-transform: none;\n"
"font-size: 12px;\n"
"padding-bottom: 0px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_info_3.setLineWidth(1)
        self.suffix_info_3.setTextFormat(Qt.RichText)
        self.suffix_info_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_info_3)

        self.suffix_3 = QLabel(self.modifiers)
        self.suffix_3.setObjectName(u"suffix_3")
        self.suffix_3.setEnabled(False)
        self.suffix_3.setMinimumSize(QSize(0, 0))
        self.suffix_3.setStyleSheet(u"QLabel {\n"
"color: #8787fe;\n"
"font-size: 14px;\n"
"padding-bottom: 2px;\n"
"padding-top: 2px;\n"
"padding-right: 10px;\n"
"padding-left: 10px;\n"
"line-height: 14px;\n"
"text-align: center;\n"
"margin: 0px;\n"
"}")
        self.suffix_3.setTextFormat(Qt.RichText)
        self.suffix_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.suffix_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.modifiers, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.item_info_box)


        self.verticalLayout_28.addWidget(self.item_description_layout)


        self.horizontalLayout_4.addWidget(self.item_description)


        self.verticalLayout_27.addWidget(self.item_info_display)


        self.verticalLayout_17.addWidget(self.item_info_container)

        self.crafting_simulator.addWidget(self.crafting_page)

        self.gridLayout_2.addWidget(self.crafting_simulator, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.crafting_simulator_container)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1239, 26))
        self.menuBar.setStyleSheet(u"")
        self.menuCrafting = QMenu(self.menuBar)
        self.menuCrafting.setObjectName(u"menuCrafting")
        self.menuTrade_Info = QMenu(self.menuBar)
        self.menuTrade_Info.setObjectName(u"menuTrade_Info")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuCrafting.menuAction())
        self.menuBar.addAction(self.menuTrade_Info.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuCrafting.addAction(self.actionStartOver)
        self.menuCrafting.addSeparator()
        self.menuCrafting.addAction(self.actionCrafting_Tutorials)
        self.menuCrafting.addSeparator()
        self.menuCrafting.addAction(self.actionPOEDB_TW)
        self.menuTrade_Info.addAction(self.actionPrice_Checker)
        self.menuTrade_Info.addSeparator()
        self.menuTrade_Info.addAction(self.actionPOE_NINJA)
        self.menuTrade_Info.addSeparator()
        self.menuTrade_Info.addAction(self.actionPATHOFEXILE_COM_TRADE)
        self.menuSettings.addAction(self.actionUI)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionTrade)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionCrafting)

        self.retranslateUi(MainWindow)
        self.startCraftingProject.clicked.connect(MainWindow.changePage)
        self.actionStartOver.triggered.connect(MainWindow.resetOptions)

        self.crafting_simulator.setCurrentIndex(0)
        self.crafting_method_pages.setCurrentIndex(0)
        self.harvest_method_stack.setCurrentIndex(1)
        self.crafting_history.setCurrentIndex(2)
        self.crafting_history.layout().setSpacing(0)
        self.clear_item_options.setDefault(False)
        self.import_custom_item.setDefault(False)
        self.implicit_btn.setDefault(False)
        self.modpool_container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExileCraft", None))
        self.actionStartOver.setText(QCoreApplication.translate("MainWindow", u"Start Over", None))
        self.actionPOEDB_TW.setText(QCoreApplication.translate("MainWindow", u"POEDB.TW", None))
        self.actionPrice_Checker.setText(QCoreApplication.translate("MainWindow", u"Price Checker", None))
        self.actionPOE_NINJA.setText(QCoreApplication.translate("MainWindow", u"POE.NINJA", None))
        self.actionPATHOFEXILE_COM_TRADE.setText(QCoreApplication.translate("MainWindow", u"PATHOFEXILE.COM/TRADE", None))
        self.actionUI.setText(QCoreApplication.translate("MainWindow", u"UI", None))
        self.actionTrade.setText(QCoreApplication.translate("MainWindow", u"Trade", None))
        self.actionCrafting.setText(QCoreApplication.translate("MainWindow", u"Crafting", None))
        self.actionCrafting_Tutorials.setText(QCoreApplication.translate("MainWindow", u"Crafting Tutorials", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"Search for an affix", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome To ExileCraft", None))
        self.startCraftingProject.setText(QCoreApplication.translate("MainWindow", u"Start Crafting Project", None))
        self.loadSavedProject.setText(QCoreApplication.translate("MainWindow", u"Load Saved Project", None))
        self.importItemFromPOE.setText(QCoreApplication.translate("MainWindow", u"Import Item Info From Path Of Exile", None))
        self.base_group_label.setText(QCoreApplication.translate("MainWindow", u"Choose a Base Group", None))
        self.one_handed_weapons_btn.setText(QCoreApplication.translate("MainWindow", u"One Handed Weapons", None))
        self.body_armours_btn.setText(QCoreApplication.translate("MainWindow", u"Body Armours", None))
        self.two_handed_weapons_btn.setText(QCoreApplication.translate("MainWindow", u"Two Handed Weapons", None))
        self.gloves_btn.setText(QCoreApplication.translate("MainWindow", u"Gloves", None))
        self.offhands_btn.setText(QCoreApplication.translate("MainWindow", u"Offhands", None))
        self.boots_btn.setText(QCoreApplication.translate("MainWindow", u"Boots", None))
        self.jewels_btn.setText(QCoreApplication.translate("MainWindow", u"Jewels", None))
        self.cluster_jewels_btn.setText(QCoreApplication.translate("MainWindow", u"Cluster Jewels", None))
        self.helmets_btn.setText(QCoreApplication.translate("MainWindow", u"Helmets", None))
        self.jewellery_btn.setText(QCoreApplication.translate("MainWindow", u"Jewellery", None))
        self.flasks_btn.setText(QCoreApplication.translate("MainWindow", u"Flasks", None))
        self.item_options_label_2.setText(QCoreApplication.translate("MainWindow", u"Choose Options", None))
        self.influence_header_label.setText(QCoreApplication.translate("MainWindow", u"Choose zero to two influence(s)", None))
        self.crusader_btn.setText(QCoreApplication.translate("MainWindow", u"Crusader", None))
        self.elder_btn.setText(QCoreApplication.translate("MainWindow", u"Elder", None))
        self.hunter_btn.setText(QCoreApplication.translate("MainWindow", u"Hunter", None))
        self.redeemer_btn.setText(QCoreApplication.translate("MainWindow", u"Redeemer", None))
        self.shaper_btn.setText(QCoreApplication.translate("MainWindow", u"Shaper", None))
        self.warlord_btn.setText(QCoreApplication.translate("MainWindow", u"Warlord", None))
        self.ilvl_header_label.setText(QCoreApplication.translate("MainWindow", u"Select Item Level", None))
        self.ilvl_87.setText(QCoreApplication.translate("MainWindow", u"87", None))
        self.ilvl_73.setText(QCoreApplication.translate("MainWindow", u"73", None))
        self.ilvl_78.setText(QCoreApplication.translate("MainWindow", u"78", None))
        self.ilvl_63.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.ilvl_96.setText(QCoreApplication.translate("MainWindow", u"96", None))
        self.ilvl_71.setText(QCoreApplication.translate("MainWindow", u"71", None))
        self.ilvl_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.ilvl_75.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.ilvl_89.setText(QCoreApplication.translate("MainWindow", u"89", None))
        self.ilvl_62.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.ilvl_82.setText(QCoreApplication.translate("MainWindow", u"82", None))
        self.ilvl_45.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.ilvl_97.setText(QCoreApplication.translate("MainWindow", u"97", None))
        self.ilvl_38.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.ilvl_40.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.ilvl_72.setText(QCoreApplication.translate("MainWindow", u"72", None))
        self.ilvl_93.setText(QCoreApplication.translate("MainWindow", u"93", None))
        self.ilvl_43.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.ilvl_28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.ilvl_64.setText(QCoreApplication.translate("MainWindow", u"64", None))
        self.ilvl_66.setText(QCoreApplication.translate("MainWindow", u"66", None))
        self.ilvl_79.setText(QCoreApplication.translate("MainWindow", u"79", None))
        self.ilvl_83.setText(QCoreApplication.translate("MainWindow", u"83", None))
        self.ilvl_100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.ilvl_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.ilvl_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.ilvl_98.setText(QCoreApplication.translate("MainWindow", u"98", None))
        self.ilvl_52.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.ilvl_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.ilvl_90.setText(QCoreApplication.translate("MainWindow", u"90", None))
        self.ilvl_51.setText(QCoreApplication.translate("MainWindow", u"51", None))
        self.ilvl_74.setText(QCoreApplication.translate("MainWindow", u"74", None))
        self.ilvl_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.ilvl_57.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.ilvl_86.setText(QCoreApplication.translate("MainWindow", u"86", None))
        self.ilvl_77.setText(QCoreApplication.translate("MainWindow", u"77", None))
        self.ilvl_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ilvl_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.ilvl_44.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.ilvl_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.ilvl_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.ilvl_91.setText(QCoreApplication.translate("MainWindow", u"91", None))
        self.ilvl_81.setText(QCoreApplication.translate("MainWindow", u"81", None))
        self.ilvl_58.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.ilvl_80.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.ilvl_60.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.ilvl_69.setText(QCoreApplication.translate("MainWindow", u"69", None))
        self.ilvl_42.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.ilvl_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.ilvl_50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.ilvl_54.setText(QCoreApplication.translate("MainWindow", u"54", None))
        self.ilvl_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.ilvl_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.ilvl_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.ilvl_36.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.ilvl_39.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.ilvl_61.setText(QCoreApplication.translate("MainWindow", u"61", None))
        self.ilvl_59.setText(QCoreApplication.translate("MainWindow", u"59", None))
        self.ilvl_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.ilvl_34.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.ilvl_26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.ilvl_67.setText(QCoreApplication.translate("MainWindow", u"67", None))
        self.ilvl_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.ilvl_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.ilvl_99.setText(QCoreApplication.translate("MainWindow", u"99", None))
        self.ilvl_65.setText(QCoreApplication.translate("MainWindow", u"65", None))
        self.ilvl_49.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.ilvl_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.ilvl_94.setText(QCoreApplication.translate("MainWindow", u"94", None))
        self.ilvl_31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.ilvl_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.ilvl_95.setText(QCoreApplication.translate("MainWindow", u"95", None))
        self.ilvl_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.ilvl_32.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.ilvl_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.ilvl_47.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.ilvl_84.setText(QCoreApplication.translate("MainWindow", u"84", None))
        self.ilvl_76.setText(QCoreApplication.translate("MainWindow", u"76", None))
        self.ilvl_56.setText(QCoreApplication.translate("MainWindow", u"56", None))
        self.ilvl_33.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.ilvl_35.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.ilvl_37.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.ilvl_92.setText(QCoreApplication.translate("MainWindow", u"92", None))
        self.ilvl_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.ilvl_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.ilvl_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.ilvl_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.ilvl_48.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.ilvl_46.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.ilvl_85.setText(QCoreApplication.translate("MainWindow", u"85", None))
        self.ilvl_88.setText(QCoreApplication.translate("MainWindow", u"88", None))
        self.ilvl_41.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.ilvl_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.ilvl_55.setText(QCoreApplication.translate("MainWindow", u"55", None))
        self.ilvl_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.ilvl_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.ilvl_53.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.ilvl_68.setText(QCoreApplication.translate("MainWindow", u"68", None))
        self.ilvl_70.setText(QCoreApplication.translate("MainWindow", u"70", None))
        self.ilvl_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.quality_header_label.setText(QCoreApplication.translate("MainWindow", u"Set Item Quality", None))
        self.quality_28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.quality_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.quality_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.quality_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.quality_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.quality_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.quality_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.quality_26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.quality_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.quality_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.quality_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.quality_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.quality_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.quality_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.quality_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.quality_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.quality_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.quality_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.quality_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.quality_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.quality_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.quality_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.quality_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.quality_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.quality_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.quality_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.quality_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.quality_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.quality_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.quality_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.proceed_btn.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
#if QT_CONFIG(tooltip)
        self.method_transmute_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Upgrades a Normal Item to a Magic Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_transmute_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_alteration_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Reforges a Magic Item with new random properties", None))
#endif // QT_CONFIG(tooltip)
        self.method_alteration_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_augmentation_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Magic Item with a new random property", None))
#endif // QT_CONFIG(tooltip)
        self.method_augmentation_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_regal_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Upgrades a Magic Item to a Rare Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_regal_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_alchemy_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Upgrades a Normal Item to a Rare Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_alchemy_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_chaos_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Reforges a Rare Item with new random modifiers", None))
#endif // QT_CONFIG(tooltip)
        self.method_chaos_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_exalted_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Rare Item with a new random property", None))
#endif // QT_CONFIG(tooltip)
        self.method_exalted_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_scour_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Removes all properties from an Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_scour_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_annul_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Removes a random modifier from an Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_annul_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_crusader_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Rare Item with a new Crusader modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_crusader_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_hunter_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Rare Item with a new Hunter modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_hunter_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_redeemer_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Rare Item with a new Redeemer modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_redeemer_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_warlord_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Enchants a Rare Item with a new Warlord modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_warlord_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_blessed_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Randomises the numeric values of the Implicit properties of an Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_blessed_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_divine_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Randomises the numeric values of the random properties on an Item", None))
#endif // QT_CONFIG(tooltip)
        self.method_divine_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_veiled_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Reforges a Rare Item with new random modifiers, including a Veiled modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_veiled_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_woke_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Destroys an Item, applying its' Influence to another of the same Item class. The second Item is reforged as a Rare Item with both Influence types and new modifiers", None))
#endif // QT_CONFIG(tooltip)
        self.method_woke_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_maven_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Removes one Influenced modifier from an Item with at least two Influenced modifiers and upgrades another Influenced modifier", None))
#endif // QT_CONFIG(tooltip)
        self.method_maven_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_fracturing_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Fractures a random modifier on a Rare Item with at least 4 modifiers, locking it in place.", None))
#endif // QT_CONFIG(tooltip)
        self.method_fracturing_btn.setText("")
#if QT_CONFIG(tooltip)
        self.locus_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Potently corrupts an Item, modifying it drastically and unpredictably", None))
#endif // QT_CONFIG(tooltip)
        self.locus_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_vaal_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Corrupts an Item, modifying it unpredictably", None))
#endif // QT_CONFIG(tooltip)
        self.method_vaal_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_fossil_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Fossil crafting", None))
#endif // QT_CONFIG(tooltip)
        self.method_fossil_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_harvest_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Harvest crafting", None))
#endif // QT_CONFIG(tooltip)
        self.method_harvest_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_essence_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Essences", None))
#endif // QT_CONFIG(tooltip)
        self.method_essence_btn.setText("")
#if QT_CONFIG(tooltip)
        self.catalyst_method_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Catalysts", None))
#endif // QT_CONFIG(tooltip)
        self.catalyst_method_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_imprint_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Beast crafting", None))
#endif // QT_CONFIG(tooltip)
        self.method_imprint_btn.setText("")
#if QT_CONFIG(tooltip)
        self.eldritch_method_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Eldritch crafting", None))
#endif // QT_CONFIG(tooltip)
        self.eldritch_method_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_syndicate_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Syndicate", None))
#endif // QT_CONFIG(tooltip)
        self.method_syndicate_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_crafting_bench_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Vendor recipes", None))
#endif // QT_CONFIG(tooltip)
        self.method_crafting_bench_btn.setText("")
        self.fossil_hide_button.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.fossil_label.setText(QCoreApplication.translate("MainWindow", u"FOSSILS", None))
        self.abberant_fossil.setText(QCoreApplication.translate("MainWindow", u"Aberrant", None))
        self.aetheric_fossil.setText(QCoreApplication.translate("MainWindow", u"Aetheric", None))
        self.bound_fossil.setText(QCoreApplication.translate("MainWindow", u"Bound", None))
        self.corroded_fossil.setText(QCoreApplication.translate("MainWindow", u"Corroded", None))
        self.dense_fossil.setText(QCoreApplication.translate("MainWindow", u"Dense", None))
        self.faceted_fossil.setText(QCoreApplication.translate("MainWindow", u"Faceted", None))
        self.frigid_fossil.setText(QCoreApplication.translate("MainWindow", u"Frigid", None))
        self.jagged_fossil.setText(QCoreApplication.translate("MainWindow", u"Jagged", None))
        self.lucent_fossil.setText(QCoreApplication.translate("MainWindow", u"Lucent", None))
        self.metallic_fossil.setText(QCoreApplication.translate("MainWindow", u"Metallic", None))
        self.prismatic_fossil.setText(QCoreApplication.translate("MainWindow", u"Prismatic", None))
        self.pristine_fossil.setText(QCoreApplication.translate("MainWindow", u"Pristine", None))
        self.scorched_fossil.setText(QCoreApplication.translate("MainWindow", u"Scorched", None))
        self.serrated_fossil.setText(QCoreApplication.translate("MainWindow", u"Serrated", None))
        self.shuddering_fossil.setText(QCoreApplication.translate("MainWindow", u"Shuddering", None))
        self.hollow_fossil.setText(QCoreApplication.translate("MainWindow", u"Hollow", None))
        self.sanctified_fossil.setText(QCoreApplication.translate("MainWindow", u"Sanctified", None))
        self.glyphic_fossil.setText(QCoreApplication.translate("MainWindow", u"Glyphic", None))
        self.fundamental_fossil.setText(QCoreApplication.translate("MainWindow", u"Fundamental", None))
        self.deft_fossil.setText(QCoreApplication.translate("MainWindow", u"Deft", None))
        self.gilded_fossil.setText(QCoreApplication.translate("MainWindow", u"Gilded", None))
        self.perfect_fossil.setText(QCoreApplication.translate("MainWindow", u"Perfect", None))
        self.tangled_fossil.setText(QCoreApplication.translate("MainWindow", u"Tangled", None))
        self.harvest_hide_btn.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.harvest_method_label.setText(QCoreApplication.translate("MainWindow", u"METHOD", None))
        self.harvest_add_remove_btn.setText(QCoreApplication.translate("MainWindow", u"Add/Remove", None))
        self.harvest_reroll_btn.setText(QCoreApplication.translate("MainWindow", u"Reforge", None))
        self.harvest_resists_btn.setText(QCoreApplication.translate("MainWindow", u"Resists", None))
        self.harvest_high_tier_btn.setText(QCoreApplication.translate("MainWindow", u"High-Tier", None))
        self.harvest_other_btn.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.harvest_type_label.setText(QCoreApplication.translate("MainWindow", u"TYPE", None))
        self.attack_btn.setText(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.caster_btn.setText(QCoreApplication.translate("MainWindow", u"Caster", None))
        self.chaos_btn.setText(QCoreApplication.translate("MainWindow", u"Chaos", None))
        self.cold_btn.setText(QCoreApplication.translate("MainWindow", u"Cold", None))
        self.critical_btn.setText(QCoreApplication.translate("MainWindow", u"Critical", None))
        self.defences_btn.setText(QCoreApplication.translate("MainWindow", u"Defences", None))
        self.fire_btn.setText(QCoreApplication.translate("MainWindow", u"Fire", None))
        self.life_btn.setText(QCoreApplication.translate("MainWindow", u"Life", None))
        self.lightning_btn.setText(QCoreApplication.translate("MainWindow", u"Lightning", None))
        self.physical_btn.setText(QCoreApplication.translate("MainWindow", u"Physical", None))
        self.speed_btn.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.influence_btn.setText(QCoreApplication.translate("MainWindow", u"Influence", None))
        self.harvest_resists_label.setText(QCoreApplication.translate("MainWindow", u"FROM>TO", None))
        self.harvest_fire_to_cold_btn.setText(QCoreApplication.translate("MainWindow", u"Fire to Cold", None))
        self.harvest_fire_to_lightning_btn.setText(QCoreApplication.translate("MainWindow", u"Fire to Lightning", None))
        self.harvest_cold_to_fire_btn.setText(QCoreApplication.translate("MainWindow", u"Cold to Fire", None))
        self.harvest_cold_to_lightning_btn.setText(QCoreApplication.translate("MainWindow", u"Cold to Lightning", None))
        self.harvest_lightning_to_fire_btn.setText(QCoreApplication.translate("MainWindow", u"Lightning to Fire", None))
        self.harvest_lightning_to_cold_btn.setText(QCoreApplication.translate("MainWindow", u"Lightning to Cold", None))
        self.harvest_high_tier_label.setText(QCoreApplication.translate("MainWindow", u"OPTION", None))
        self.harvest_normal_to_magic_one_btn.setText(QCoreApplication.translate("MainWindow", u"Normal to Magic > one mod", None))
        self.harvest_normal_to_magic_two_btn.setText(QCoreApplication.translate("MainWindow", u"Normal to Magic > two mod", None))
        self.harvest_magic_to_rare_two_btn.setText(QCoreApplication.translate("MainWindow", u"Magic to Rare > two mod", None))
        self.harvest_magic_to_rare_three_btn.setText(QCoreApplication.translate("MainWindow", u"Magic to Rare > three mod", None))
        self.harvest_magic_to_rare_four_btn.setText(QCoreApplication.translate("MainWindow", u"Magic to rare > four mod", None))
        self.harvest_other_label.setText(QCoreApplication.translate("MainWindow", u"OPTION", None))
        self.harvest_reforge_more_likely_btn.setText(QCoreApplication.translate("MainWindow", u"Reforge more likely", None))
        self.harvest_reforge_less_likely_btn.setText(QCoreApplication.translate("MainWindow", u"Reforge less likely", None))
        self.essence_tier_label.setText(QCoreApplication.translate("MainWindow", u"TIER", None))
        self.t6_btn.setText(QCoreApplication.translate("MainWindow", u"T6", None))
        self.t5_btn.setText(QCoreApplication.translate("MainWindow", u"T5", None))
        self.t4_btn.setText(QCoreApplication.translate("MainWindow", u"T4", None))
        self.t3_btn.setText(QCoreApplication.translate("MainWindow", u"T3", None))
        self.t2_btn.setText(QCoreApplication.translate("MainWindow", u"T2", None))
        self.t1_btn.setText(QCoreApplication.translate("MainWindow", u"T1", None))
        self.essences_hide_btn.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.essences_label.setText(QCoreApplication.translate("MainWindow", u"ESSENCES", None))
        self.essence_anger_btn.setText(QCoreApplication.translate("MainWindow", u"Anger", None))
        self.essence_anguish_btn.setText(QCoreApplication.translate("MainWindow", u"Anguish", None))
        self.essence_contempt_btn.setText(QCoreApplication.translate("MainWindow", u"Contempt", None))
        self.essence_delirium_btn.setText(QCoreApplication.translate("MainWindow", u"Delirium", None))
        self.essence_doubt_btn.setText(QCoreApplication.translate("MainWindow", u"Doubt", None))
        self.essence_dread_btn.setText(QCoreApplication.translate("MainWindow", u"Dread", None))
        self.essence_envy_btn.setText(QCoreApplication.translate("MainWindow", u"Envy", None))
        self.essenc_fear_btn.setText(QCoreApplication.translate("MainWindow", u"Fear", None))
        self.essence_greed.setText(QCoreApplication.translate("MainWindow", u"Greed", None))
        self.essence_hatred.setText(QCoreApplication.translate("MainWindow", u"Hatred", None))
        self.essence_horror_btn.setText(QCoreApplication.translate("MainWindow", u"Horror", None))
        self.essence_hysteria_btn.setText(QCoreApplication.translate("MainWindow", u"Hysteria", None))
        self.essence_insanity_btn.setText(QCoreApplication.translate("MainWindow", u"Insanity", None))
        self.essence_loathing_btn.setText(QCoreApplication.translate("MainWindow", u"Loathing", None))
        self.essence_misery_btn.setText(QCoreApplication.translate("MainWindow", u"Misery", None))
        self.essence_rage_btn.setText(QCoreApplication.translate("MainWindow", u"Rage", None))
        self.essence_scorn_btn.setText(QCoreApplication.translate("MainWindow", u"Scorn", None))
        self.essence_sorrow_btn.setText(QCoreApplication.translate("MainWindow", u"Sorrow", None))
        self.essence_spite_btn.setText(QCoreApplication.translate("MainWindow", u"Spite", None))
        self.essence_suffering_btn.setText(QCoreApplication.translate("MainWindow", u"Suffering", None))
        self.essence_torment_btn.setText(QCoreApplication.translate("MainWindow", u"Torment", None))
        self.essence_woe_btn.setText(QCoreApplication.translate("MainWindow", u"Woe", None))
        self.essence_wrath_btn.setText(QCoreApplication.translate("MainWindow", u"Wrath", None))
        self.essence_zeal_btn.setText(QCoreApplication.translate("MainWindow", u"Zeal", None))
        self.catalysts_hide_btn.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.catalyst_row_label.setText(QCoreApplication.translate("MainWindow", u"CATALYSTS", None))
        self.intrinsic_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Intrinsic", None))
        self.abrasive_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Abrasive", None))
        self.prismatic_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Prismatic", None))
        self.fertile_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Fertile", None))
        self.imbued_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Imbued", None))
        self.tempering_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Tempering", None))
        self.turbulent_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Turbulent", None))
        self.accelerating_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Accelerating", None))
        self.unstable_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Unstable", None))
        self.noxious_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Noxious", None))
        self.catalyst_mode_label.setText(QCoreApplication.translate("MainWindow", u"MODE", None))
        self.max_catalyst_btn.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.single_catalys_btn.setText(QCoreApplication.translate("MainWindow", u"Single", None))
        self.beast_crafting_hide_btn.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.beast_crafting_methods_label.setText(QCoreApplication.translate("MainWindow", u"METHOD", None))
        self.bprefix__to_suffix_btn.setText(QCoreApplication.translate("MainWindow", u"Prefix > Suffix", None))
        self.bsuffix_to_prefix_btn.setText(QCoreApplication.translate("MainWindow", u"Suffix>Prefix", None))
        self.bimprint_btn.setText(QCoreApplication.translate("MainWindow", u"Imprint", None))
        self.breroll_values_btn.setText(QCoreApplication.translate("MainWindow", u"Reroll Values", None))
        self.bcat_btn.setText(QCoreApplication.translate("MainWindow", u"Cat", None))
        self.bavian_btn.setText(QCoreApplication.translate("MainWindow", u"Avian", None))
        self.bspider_btn.setText(QCoreApplication.translate("MainWindow", u"Spider", None))
        self.bcrab_btn.setText(QCoreApplication.translate("MainWindow", u"Crab", None))
        self.eldritch_hide_btn.setText(QCoreApplication.translate("MainWindow", u"Close\n"
" \u27a5", None))
        self.eldritch_method_label.setText(QCoreApplication.translate("MainWindow", u"METHOD", None))
        self.eldritch_chaos_btn.setText(QCoreApplication.translate("MainWindow", u"Chaos", None))
        self.eldritch_exalted_btn.setText(QCoreApplication.translate("MainWindow", u"Exalted", None))
        self.eldritch_annul_btn.setText(QCoreApplication.translate("MainWindow", u"Annul", None))
        self.orb_of_conflict_btn.setText(QCoreApplication.translate("MainWindow", u"Orb of Conflict", None))
        self.lesser_ember_btn.setText(QCoreApplication.translate("MainWindow", u"Lesser Ember", None))
        self.greater_ember_btn.setText(QCoreApplication.translate("MainWindow", u"Greater Ember", None))
        self.grand_ember_btn.setText(QCoreApplication.translate("MainWindow", u"Grand Ember", None))
        self.exceptional_ember_btn.setText(QCoreApplication.translate("MainWindow", u"Exceptional Ember", None))
        self.lesser_ichor_btn.setText(QCoreApplication.translate("MainWindow", u"Lesser Ichor", None))
        self.greater_icho_btn.setText(QCoreApplication.translate("MainWindow", u"Greater Ichor", None))
        self.grand_ichor_btn.setText(QCoreApplication.translate("MainWindow", u"Grand Ichor", None))
        self.exceptional_ichor_btn.setText(QCoreApplication.translate("MainWindow", u"Exceptional Ichor", None))
        self.affix_search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for an affix", None))
        self.crafting_history.setItemText(self.crafting_history.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"History", None))
        self.crafting_history.setItemText(self.crafting_history.indexOf(self.spending_tab), QCoreApplication.translate("MainWindow", u"Spending", None))
        self.crafting_history.setItemText(self.crafting_history.indexOf(self.export_tab), QCoreApplication.translate("MainWindow", u"Export", None))
#if QT_CONFIG(tooltip)
        self.clear_item_options.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the selected item and reset the interface", None))
#endif // QT_CONFIG(tooltip)
        self.clear_item_options.setText(QCoreApplication.translate("MainWindow", u"Clear Item Options", None))
        self.import_custom_item.setText(QCoreApplication.translate("MainWindow", u"Import Custom Item", None))
#if QT_CONFIG(tooltip)
        self.simulate_crafting.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.simulate_crafting.setText(QCoreApplication.translate("MainWindow", u"Simulate Crafting", None))
        self.prefix_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.suffix_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.implicit_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.item_img_box.setText("")
        self.crafting_button.setText("")
        self.item_dps_box.setText("")
        self.item_header_text_label.setText("")
        self.item_properties.setText("")
        self.item_spacer_1.setText("")
        self.item_spacer_2.setText("")
        self.item_implicits.setText("")
        self.item_spacer_3.setText("")
        self.prefix_info_1.setText(QCoreApplication.translate("MainWindow", u"PrefixInfo1", None))
        self.prefix_1.setText(QCoreApplication.translate("MainWindow", u"Prefix1", None))
        self.prefix_info_2.setText(QCoreApplication.translate("MainWindow", u"PrefixInfo2", None))
        self.prefix_2.setText(QCoreApplication.translate("MainWindow", u"Prefix2", None))
        self.prefix_info_3.setText(QCoreApplication.translate("MainWindow", u"PrefixInfo3", None))
        self.prefix_3.setText(QCoreApplication.translate("MainWindow", u"Prefix3", None))
        self.suffix_info_1.setText(QCoreApplication.translate("MainWindow", u"SuffixInfo1", None))
        self.suffix_1.setText(QCoreApplication.translate("MainWindow", u"Suffix1", None))
        self.suffix_info_2.setText(QCoreApplication.translate("MainWindow", u"SuffixInfo2", None))
        self.suffix_2.setText(QCoreApplication.translate("MainWindow", u"Suffix2", None))
        self.suffix_info_3.setText(QCoreApplication.translate("MainWindow", u"SuffixInfo3", None))
        self.suffix_3.setText(QCoreApplication.translate("MainWindow", u"Suffix3", None))
        self.menuCrafting.setTitle(QCoreApplication.translate("MainWindow", u"Crafting", None))
        self.menuTrade_Info.setTitle(QCoreApplication.translate("MainWindow", u"Trade Info", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

