
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QButtonGroup,
                               QFrame, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit, QMenu, QMenuBar,
                               QPushButton, QSizePolicy,
                               QSpacerItem, QStackedWidget, QTabWidget, QToolBox,
                               QVBoxLayout, QWidget)

from .customcursorbutton import CustomCursorButton
from .customtreeview import CustomTreeView
from . import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.action_start_over = QAction(MainWindow)
        self.action_start_over.setObjectName(u"action_start_over")
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
        self.crafting_simulator.setStyleSheet(u"border-image: url(:/images/assets/images/emubg.png);")
        self.landing_page = QWidget()
        self.landing_page.setObjectName(u"landing_page")
        sizePolicy.setHeightForWidth(self.landing_page.sizePolicy().hasHeightForWidth())
        self.landing_page.setSizePolicy(sizePolicy)
        self.landing_page.setStyleSheet(u"QPushButton {\n"
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
        self.landing_page_label = QLabel(self.landing_page_container)
        self.landing_page_label.setObjectName(u"landing_page_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.landing_page_label.sizePolicy().hasHeightForWidth())
        self.landing_page_label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Open Sans"])
        font2.setBold(True)
        self.landing_page_label.setFont(font2)
        self.landing_page_label.setStyleSheet(u"QWidget {\n"
"	border-image: none;\n"
"	border: 0px;\n"
"}\n"
"")
        self.landing_page_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_11.addWidget(self.landing_page_label, 0, Qt.AlignTop)

        self.start_crafting_project_btn = QPushButton(self.landing_page_container)
        self.start_crafting_project_btn.setObjectName(u"start_crafting_project_btn")
        sizePolicy.setHeightForWidth(self.start_crafting_project_btn.sizePolicy().hasHeightForWidth())
        self.start_crafting_project_btn.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.start_crafting_project_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.load_saved_project_btn = QPushButton(self.landing_page_container)
        self.load_saved_project_btn.setObjectName(u"load_saved_project_btn")

        self.verticalLayout_11.addWidget(self.load_saved_project_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.import_item_from_poe_btn = QPushButton(self.landing_page_container)
        self.import_item_from_poe_btn.setObjectName(u"import_item_from_poe_btn")
        sizePolicy.setHeightForWidth(self.import_item_from_poe_btn.sizePolicy().hasHeightForWidth())
        self.import_item_from_poe_btn.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.import_item_from_poe_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.landing_page_container, 0, Qt.AlignTop)

        self.crafting_simulator.addWidget(self.landing_page)
        self.crafting_page = QWidget()
        self.crafting_page.setObjectName(u"crafting_page")
        sizePolicy.setHeightForWidth(self.crafting_page.sizePolicy().hasHeightForWidth())
        self.crafting_page.setSizePolicy(sizePolicy)
        self.crafting_page.setStyleSheet(u"border-image: url(:/images/assets/images/emubg.png);")
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
        font3 = QFont()
        font3.setFamilies([u"fontin-smallcaps"])
        font3.setPointSize(9)
        self.common_crafting_methods.setFont(font3)
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
        self.custom_cursor_btns_group = QButtonGroup(MainWindow)
        self.custom_cursor_btns_group.setObjectName(u"custom_cursor_btns_group")
        self.custom_cursor_btns_group.addButton(self.method_transmute_btn)
        self.method_transmute_btn.setObjectName(u"method_transmute_btn")
        sizePolicy1.setHeightForWidth(self.method_transmute_btn.sizePolicy().hasHeightForWidth())
        self.method_transmute_btn.setSizePolicy(sizePolicy1)
        self.method_transmute_btn.setMinimumSize(QSize(0, 0))
        self.method_transmute_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_transmute_btn.setMouseTracking(True)
        self.method_transmute_btn.setContextMenuPolicy(Qt.NoContextMenu)
        icon2 = QIcon()
        icon2.addFile(u":/crafting_methods/assets/images/crafting_methods/method_transmute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_transmute_btn.setIcon(icon2)
        self.method_transmute_btn.setIconSize(QSize(30, 30))
        self.method_transmute_btn.setCheckable(True)
        self.method_transmute_btn.setChecked(False)

        self.horizontalLayout_8.addWidget(self.method_transmute_btn)

        self.method_alteration_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_alteration_btn)
        self.method_alteration_btn.setObjectName(u"method_alteration_btn")
        sizePolicy1.setHeightForWidth(self.method_alteration_btn.sizePolicy().hasHeightForWidth())
        self.method_alteration_btn.setSizePolicy(sizePolicy1)
        self.method_alteration_btn.setMinimumSize(QSize(0, 0))
        self.method_alteration_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_alteration_btn.setMouseTracking(True)
        icon3 = QIcon()
        icon3.addFile(u":/crafting_methods/assets/images/crafting_methods/method_alteration.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_alteration_btn.setIcon(icon3)
        self.method_alteration_btn.setIconSize(QSize(30, 30))
        self.method_alteration_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_alteration_btn)

        self.method_augmentation_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_augmentation_btn)
        self.method_augmentation_btn.setObjectName(u"method_augmentation_btn")
        sizePolicy1.setHeightForWidth(self.method_augmentation_btn.sizePolicy().hasHeightForWidth())
        self.method_augmentation_btn.setSizePolicy(sizePolicy1)
        self.method_augmentation_btn.setMinimumSize(QSize(0, 0))
        self.method_augmentation_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_augmentation_btn.setMouseTracking(True)
        icon4 = QIcon()
        icon4.addFile(u":/crafting_methods/assets/images/crafting_methods/method_augmentation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_augmentation_btn.setIcon(icon4)
        self.method_augmentation_btn.setIconSize(QSize(30, 30))
        self.method_augmentation_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_augmentation_btn)

        self.method_regal_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_regal_btn)
        self.method_regal_btn.setObjectName(u"method_regal_btn")
        sizePolicy1.setHeightForWidth(self.method_regal_btn.sizePolicy().hasHeightForWidth())
        self.method_regal_btn.setSizePolicy(sizePolicy1)
        self.method_regal_btn.setMinimumSize(QSize(0, 0))
        self.method_regal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_regal_btn.setMouseTracking(True)
        icon5 = QIcon()
        icon5.addFile(u":/crafting_methods/assets/images/crafting_methods/method_regal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_regal_btn.setIcon(icon5)
        self.method_regal_btn.setIconSize(QSize(30, 30))
        self.method_regal_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_regal_btn)

        self.method_alchemy_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_alchemy_btn)
        self.method_alchemy_btn.setObjectName(u"method_alchemy_btn")
        sizePolicy1.setHeightForWidth(self.method_alchemy_btn.sizePolicy().hasHeightForWidth())
        self.method_alchemy_btn.setSizePolicy(sizePolicy1)
        self.method_alchemy_btn.setMinimumSize(QSize(0, 0))
        self.method_alchemy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_alchemy_btn.setMouseTracking(True)
        icon6 = QIcon()
        icon6.addFile(u":/crafting_methods/assets/images/crafting_methods/method_alchemy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_alchemy_btn.setIcon(icon6)
        self.method_alchemy_btn.setIconSize(QSize(30, 30))
        self.method_alchemy_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_alchemy_btn)

        self.method_chaos_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_chaos_btn)
        self.method_chaos_btn.setObjectName(u"method_chaos_btn")
        sizePolicy1.setHeightForWidth(self.method_chaos_btn.sizePolicy().hasHeightForWidth())
        self.method_chaos_btn.setSizePolicy(sizePolicy1)
        self.method_chaos_btn.setMinimumSize(QSize(0, 0))
        self.method_chaos_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_chaos_btn.setMouseTracking(True)
        icon7 = QIcon()
        icon7.addFile(u":/crafting_methods/assets/images/crafting_methods/method_chaos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_chaos_btn.setIcon(icon7)
        self.method_chaos_btn.setIconSize(QSize(30, 30))
        self.method_chaos_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_chaos_btn)

        self.method_exalted_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_exalted_btn)
        self.method_exalted_btn.setObjectName(u"method_exalted_btn")
        sizePolicy1.setHeightForWidth(self.method_exalted_btn.sizePolicy().hasHeightForWidth())
        self.method_exalted_btn.setSizePolicy(sizePolicy1)
        self.method_exalted_btn.setMinimumSize(QSize(0, 0))
        self.method_exalted_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_exalted_btn.setMouseTracking(True)
        icon8 = QIcon()
        icon8.addFile(u":/crafting_methods/assets/images/crafting_methods/method_exalted.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_exalted_btn.setIcon(icon8)
        self.method_exalted_btn.setIconSize(QSize(30, 30))
        self.method_exalted_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_exalted_btn)

        self.method_scour_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_scour_btn)
        self.method_scour_btn.setObjectName(u"method_scour_btn")
        sizePolicy1.setHeightForWidth(self.method_scour_btn.sizePolicy().hasHeightForWidth())
        self.method_scour_btn.setSizePolicy(sizePolicy1)
        self.method_scour_btn.setMinimumSize(QSize(0, 0))
        self.method_scour_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_scour_btn.setMouseTracking(True)
        icon9 = QIcon()
        icon9.addFile(u":/crafting_methods/assets/images/crafting_methods/method_scour.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_scour_btn.setIcon(icon9)
        self.method_scour_btn.setIconSize(QSize(30, 30))
        self.method_scour_btn.setCheckable(True)
        self.method_scour_btn.setChecked(False)

        self.horizontalLayout_8.addWidget(self.method_scour_btn)

        self.method_annul_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_annul_btn)
        self.method_annul_btn.setObjectName(u"method_annul_btn")
        sizePolicy1.setHeightForWidth(self.method_annul_btn.sizePolicy().hasHeightForWidth())
        self.method_annul_btn.setSizePolicy(sizePolicy1)
        self.method_annul_btn.setMinimumSize(QSize(0, 0))
        self.method_annul_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_annul_btn.setMouseTracking(True)
        icon10 = QIcon()
        icon10.addFile(u":/crafting_methods/assets/images/crafting_methods/method_annul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_annul_btn.setIcon(icon10)
        self.method_annul_btn.setIconSize(QSize(30, 30))
        self.method_annul_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_annul_btn)

        self.method_crusader_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_crusader_btn)
        self.method_crusader_btn.setObjectName(u"method_crusader_btn")
        sizePolicy1.setHeightForWidth(self.method_crusader_btn.sizePolicy().hasHeightForWidth())
        self.method_crusader_btn.setSizePolicy(sizePolicy1)
        self.method_crusader_btn.setMinimumSize(QSize(0, 0))
        self.method_crusader_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_crusader_btn.setMouseTracking(True)
        icon11 = QIcon()
        icon11.addFile(u":/crafting_methods/assets/images/crafting_methods/method_crusader.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_crusader_btn.setIcon(icon11)
        self.method_crusader_btn.setIconSize(QSize(30, 30))
        self.method_crusader_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_crusader_btn)

        self.method_hunter_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_hunter_btn)
        self.method_hunter_btn.setObjectName(u"method_hunter_btn")
        sizePolicy1.setHeightForWidth(self.method_hunter_btn.sizePolicy().hasHeightForWidth())
        self.method_hunter_btn.setSizePolicy(sizePolicy1)
        self.method_hunter_btn.setMinimumSize(QSize(0, 0))
        self.method_hunter_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_hunter_btn.setMouseTracking(True)
        icon12 = QIcon()
        icon12.addFile(u":/crafting_methods/assets/images/crafting_methods/method_hunter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_hunter_btn.setIcon(icon12)
        self.method_hunter_btn.setIconSize(QSize(30, 30))
        self.method_hunter_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_hunter_btn)

        self.method_redeemer_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_redeemer_btn)
        self.method_redeemer_btn.setObjectName(u"method_redeemer_btn")
        sizePolicy1.setHeightForWidth(self.method_redeemer_btn.sizePolicy().hasHeightForWidth())
        self.method_redeemer_btn.setSizePolicy(sizePolicy1)
        self.method_redeemer_btn.setMinimumSize(QSize(0, 0))
        self.method_redeemer_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_redeemer_btn.setMouseTracking(True)
        icon13 = QIcon()
        icon13.addFile(u":/crafting_methods/assets/images/crafting_methods/method_redeemer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_redeemer_btn.setIcon(icon13)
        self.method_redeemer_btn.setIconSize(QSize(30, 30))
        self.method_redeemer_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_redeemer_btn)

        self.method_warlord_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_warlord_btn)
        self.method_warlord_btn.setObjectName(u"method_warlord_btn")
        sizePolicy1.setHeightForWidth(self.method_warlord_btn.sizePolicy().hasHeightForWidth())
        self.method_warlord_btn.setSizePolicy(sizePolicy1)
        self.method_warlord_btn.setMinimumSize(QSize(0, 0))
        self.method_warlord_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_warlord_btn.setMouseTracking(True)
        icon14 = QIcon()
        icon14.addFile(u":/crafting_methods/assets/images/crafting_methods/method_warlord.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_warlord_btn.setIcon(icon14)
        self.method_warlord_btn.setIconSize(QSize(30, 30))
        self.method_warlord_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_warlord_btn)

        self.method_blessed_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_blessed_btn)
        self.method_blessed_btn.setObjectName(u"method_blessed_btn")
        sizePolicy1.setHeightForWidth(self.method_blessed_btn.sizePolicy().hasHeightForWidth())
        self.method_blessed_btn.setSizePolicy(sizePolicy1)
        self.method_blessed_btn.setMinimumSize(QSize(0, 0))
        self.method_blessed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_blessed_btn.setMouseTracking(True)
        icon15 = QIcon()
        icon15.addFile(u":/crafting_methods/assets/images/crafting_methods/method_blessed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_blessed_btn.setIcon(icon15)
        self.method_blessed_btn.setIconSize(QSize(30, 30))
        self.method_blessed_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_blessed_btn)

        self.method_divine_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_divine_btn)
        self.method_divine_btn.setObjectName(u"method_divine_btn")
        sizePolicy1.setHeightForWidth(self.method_divine_btn.sizePolicy().hasHeightForWidth())
        self.method_divine_btn.setSizePolicy(sizePolicy1)
        self.method_divine_btn.setMinimumSize(QSize(0, 0))
        self.method_divine_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_divine_btn.setMouseTracking(True)
        icon16 = QIcon()
        icon16.addFile(u":/crafting_methods/assets/images/crafting_methods/method_divine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_divine_btn.setIcon(icon16)
        self.method_divine_btn.setIconSize(QSize(30, 30))
        self.method_divine_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_divine_btn)

        self.method_veiled_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_veiled_btn)
        self.method_veiled_btn.setObjectName(u"method_veiled_btn")
        sizePolicy1.setHeightForWidth(self.method_veiled_btn.sizePolicy().hasHeightForWidth())
        self.method_veiled_btn.setSizePolicy(sizePolicy1)
        self.method_veiled_btn.setMinimumSize(QSize(0, 0))
        self.method_veiled_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_veiled_btn.setMouseTracking(True)
        icon17 = QIcon()
        icon17.addFile(u":/crafting_methods/assets/images/crafting_methods/method_veiled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_veiled_btn.setIcon(icon17)
        self.method_veiled_btn.setIconSize(QSize(30, 30))
        self.method_veiled_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_veiled_btn)

        self.method_woke_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_woke_btn)
        self.method_woke_btn.setObjectName(u"method_woke_btn")
        sizePolicy1.setHeightForWidth(self.method_woke_btn.sizePolicy().hasHeightForWidth())
        self.method_woke_btn.setSizePolicy(sizePolicy1)
        self.method_woke_btn.setMinimumSize(QSize(0, 0))
        self.method_woke_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_woke_btn.setMouseTracking(True)
        icon18 = QIcon()
        icon18.addFile(u":/crafting_methods/assets/images/crafting_methods/method_woke.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_woke_btn.setIcon(icon18)
        self.method_woke_btn.setIconSize(QSize(30, 30))
        self.method_woke_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_woke_btn)

        self.method_maven_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_maven_btn)
        self.method_maven_btn.setObjectName(u"method_maven_btn")
        sizePolicy1.setHeightForWidth(self.method_maven_btn.sizePolicy().hasHeightForWidth())
        self.method_maven_btn.setSizePolicy(sizePolicy1)
        self.method_maven_btn.setMinimumSize(QSize(0, 0))
        self.method_maven_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_maven_btn.setMouseTracking(True)
        icon19 = QIcon()
        icon19.addFile(u":/crafting_methods/assets/images/crafting_methods/method_maven.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_maven_btn.setIcon(icon19)
        self.method_maven_btn.setIconSize(QSize(30, 30))
        self.method_maven_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_maven_btn)

        self.method_fracturing_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_fracturing_btn)
        self.method_fracturing_btn.setObjectName(u"method_fracturing_btn")
        sizePolicy1.setHeightForWidth(self.method_fracturing_btn.sizePolicy().hasHeightForWidth())
        self.method_fracturing_btn.setSizePolicy(sizePolicy1)
        self.method_fracturing_btn.setMinimumSize(QSize(0, 0))
        self.method_fracturing_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_fracturing_btn.setMouseTracking(True)
        icon20 = QIcon()
        icon20.addFile(u":/crafting_methods/assets/images/crafting_methods/method_fracturing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_fracturing_btn.setIcon(icon20)
        self.method_fracturing_btn.setIconSize(QSize(30, 30))
        self.method_fracturing_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_fracturing_btn)

        self.locus_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.locus_btn)
        self.locus_btn.setObjectName(u"locus_btn")
        sizePolicy1.setHeightForWidth(self.locus_btn.sizePolicy().hasHeightForWidth())
        self.locus_btn.setSizePolicy(sizePolicy1)
        self.locus_btn.setMinimumSize(QSize(0, 0))
        self.locus_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.locus_btn.setMouseTracking(True)
        icon21 = QIcon()
        icon21.addFile(u":/images/assets/images/locus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.locus_btn.setIcon(icon21)
        self.locus_btn.setIconSize(QSize(30, 30))
        self.locus_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.locus_btn)

        self.method_vaal_btn = CustomCursorButton(self.common_crafting_methods)
        self.custom_cursor_btns_group.addButton(self.method_vaal_btn)
        self.method_vaal_btn.setObjectName(u"method_vaal_btn")
        sizePolicy1.setHeightForWidth(self.method_vaal_btn.sizePolicy().hasHeightForWidth())
        self.method_vaal_btn.setSizePolicy(sizePolicy1)
        self.method_vaal_btn.setMinimumSize(QSize(0, 0))
        self.method_vaal_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.method_vaal_btn.setMouseTracking(True)
        icon22 = QIcon()
        icon22.addFile(u":/crafting_methods/assets/images/crafting_methods/method_vaal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_vaal_btn.setIcon(icon22)
        self.method_vaal_btn.setIconSize(QSize(30, 30))
        self.method_vaal_btn.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.method_vaal_btn)


        self.verticalLayout_7.addWidget(self.common_crafting_methods)

        self.crafting_method_group_btns = QWidget(self.crafting_methods)
        self.crafting_method_group_btns.setObjectName(u"crafting_method_group_btns")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.crafting_method_group_btns.sizePolicy().hasHeightForWidth())
        self.crafting_method_group_btns.setSizePolicy(sizePolicy3)
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
        icon23 = QIcon()
        icon23.addFile(u":/crafting_methods/assets/images/crafting_methods/method_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_fossil_btn.setIcon(icon23)
        self.method_fossil_btn.setIconSize(QSize(30, 30))
        self.method_fossil_btn.setCheckable(True)
        self.method_fossil_btn.setAutoExclusive(True)

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
        icon24 = QIcon()
        icon24.addFile(u":/crafting_methods/assets/images/crafting_methods/method_harvest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_harvest_btn.setIcon(icon24)
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
        icon25 = QIcon()
        icon25.addFile(u":/crafting_methods/assets/images/crafting_methods/method_essence.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_essence_btn.setIcon(icon25)
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
        icon26 = QIcon()
        icon26.addFile(u":/crafting_methods/assets/images/crafting_methods/method_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catalyst_method_btn.setIcon(icon26)
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
        icon27 = QIcon()
        icon27.addFile(u":/crafting_methods/assets/images/crafting_methods/method_imprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_imprint_btn.setIcon(icon27)
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
        icon28 = QIcon()
        icon28.addFile(u":/crafting_methods/assets/images/crafting_methods/method_eldritch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_method_btn.setIcon(icon28)
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
        icon29 = QIcon()
        icon29.addFile(u":/crafting_methods/assets/images/crafting_methods/method_syndicate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_syndicate_btn.setIcon(icon29)
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
        icon30 = QIcon()
        icon30.addFile(u":/crafting_methods/assets/images/crafting_methods/method_crafting_bench.png", QSize(), QIcon.Normal, QIcon.Off)
        self.method_crafting_bench_btn.setIcon(icon30)
        self.method_crafting_bench_btn.setIconSize(QSize(30, 30))
        self.method_crafting_bench_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.method_crafting_bench_btn)


        self.verticalLayout_7.addWidget(self.crafting_method_group_btns, 0, Qt.AlignTop)

        self.crafting_method_pages = QStackedWidget(self.crafting_methods)
        self.crafting_method_pages.setObjectName(u"crafting_method_pages")
        self.crafting_method_pages.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.crafting_method_pages.sizePolicy().hasHeightForWidth())
        self.crafting_method_pages.setSizePolicy(sizePolicy3)
        self.crafting_method_pages.setStyleSheet(u"QStackedWidget {\n"
"background-color: none;\n"
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
"				text-shadow: 1px 1px #000;\n"
"				vertical-align: top;\n"
"           }\n"
"            QPushButton::hover "
                        "{\n"
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
        sizePolicy3.setHeightForWidth(self.fossil_crafts.sizePolicy().hasHeightForWidth())
        self.fossil_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fossil_btn_row1.sizePolicy().hasHeightForWidth())
        self.fossil_btn_row1.setSizePolicy(sizePolicy4)
        self.fossil_row1 = QHBoxLayout(self.fossil_btn_row1)
        self.fossil_row1.setSpacing(0)
        self.fossil_row1.setContentsMargins(0, 0, 0, 0)
        self.fossil_row1.setObjectName(u"fossil_row1")
        self.fossil_row1.setContentsMargins(0, 0, 0, 0)
        self.fossil_hide_button = QPushButton(self.fossil_btn_row1)
        self.fossil_hide_button.setObjectName(u"fossil_hide_button")
        self.fossil_hide_button.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.fossil_hide_button.sizePolicy().hasHeightForWidth())
        self.fossil_hide_button.setSizePolicy(sizePolicy5)
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
        self.fossil_hide_button.setCheckable(False)

        self.fossil_row1.addWidget(self.fossil_hide_button)

        self.fossil_label = QLabel(self.fossil_btn_row1)
        self.fossil_label.setObjectName(u"fossil_label")
        self.fossil_label.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.fossil_label.sizePolicy().hasHeightForWidth())
        self.fossil_label.setSizePolicy(sizePolicy5)

        self.fossil_row1.addWidget(self.fossil_label)

        self.abberant_fossil = QPushButton(self.fossil_btn_row1)
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
        icon31 = QIcon()
        icon31.addFile(u":/fossils/assets/images/fossils/aberrant_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abberant_fossil.setIcon(icon31)
        self.abberant_fossil.setIconSize(QSize(30, 30))
        self.abberant_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.abberant_fossil)

        self.aetheric_fossil = QPushButton(self.fossil_btn_row1)
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
        icon32 = QIcon()
        icon32.addFile(u":/fossils/assets/images/fossils/aetheric_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aetheric_fossil.setIcon(icon32)
        self.aetheric_fossil.setIconSize(QSize(30, 30))
        self.aetheric_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.aetheric_fossil)

        self.bound_fossil = QPushButton(self.fossil_btn_row1)
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
        icon33 = QIcon()
        icon33.addFile(u":/fossils/assets/images/fossils/bound_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bound_fossil.setIcon(icon33)
        self.bound_fossil.setIconSize(QSize(30, 30))
        self.bound_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.bound_fossil)

        self.corroded_fossil = QPushButton(self.fossil_btn_row1)
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
        icon34 = QIcon()
        icon34.addFile(u":/fossils/assets/images/fossils/corroded_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.corroded_fossil.setIcon(icon34)
        self.corroded_fossil.setIconSize(QSize(30, 30))
        self.corroded_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.corroded_fossil)

        self.dense_fossil = QPushButton(self.fossil_btn_row1)
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
        icon35 = QIcon()
        icon35.addFile(u":/fossils/assets/images/fossils/dense_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dense_fossil.setIcon(icon35)
        self.dense_fossil.setIconSize(QSize(30, 30))

        self.fossil_row1.addWidget(self.dense_fossil)

        self.faceted_fossil = QPushButton(self.fossil_btn_row1)
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
        icon36 = QIcon()
        icon36.addFile(u":/fossils/assets/images/fossils/faceted_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.faceted_fossil.setIcon(icon36)
        self.faceted_fossil.setIconSize(QSize(30, 30))
        self.faceted_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.faceted_fossil)

        self.frigid_fossil = QPushButton(self.fossil_btn_row1)
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
        icon37 = QIcon()
        icon37.addFile(u":/fossils/assets/images/fossils/frigid_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.frigid_fossil.setIcon(icon37)
        self.frigid_fossil.setIconSize(QSize(30, 30))
        self.frigid_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.frigid_fossil)

        self.jagged_fossil = QPushButton(self.fossil_btn_row1)
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
        icon38 = QIcon()
        icon38.addFile(u":/fossils/assets/images/fossils/jagged_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jagged_fossil.setIcon(icon38)
        self.jagged_fossil.setIconSize(QSize(30, 30))
        self.jagged_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.jagged_fossil)

        self.lucent_fossil = QPushButton(self.fossil_btn_row1)
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
        icon39 = QIcon()
        icon39.addFile(u":/fossils/assets/images/fossils/lucent_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lucent_fossil.setIcon(icon39)
        self.lucent_fossil.setIconSize(QSize(30, 30))
        self.lucent_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.lucent_fossil)

        self.metallic_fossil = QPushButton(self.fossil_btn_row1)
        self.fossil_btns_broup.addButton(self.metallic_fossil)
        self.metallic_fossil.setObjectName(u"metallic_fossil")
        self.metallic_fossil.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.metallic_fossil.sizePolicy().hasHeightForWidth())
        self.metallic_fossil.setSizePolicy(sizePolicy1)
        self.metallic_fossil.setCursor(QCursor(Qt.PointingHandCursor))
        icon40 = QIcon()
        icon40.addFile(u":/fossils/assets/images/fossils/metallic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.metallic_fossil.setIcon(icon40)
        self.metallic_fossil.setIconSize(QSize(30, 30))
        self.metallic_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.metallic_fossil)

        self.prismatic_fossil = QPushButton(self.fossil_btn_row1)
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
        icon41 = QIcon()
        icon41.addFile(u":/fossils/assets/images/fossils/prismatic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prismatic_fossil.setIcon(icon41)
        self.prismatic_fossil.setIconSize(QSize(30, 30))
        self.prismatic_fossil.setCheckable(True)

        self.fossil_row1.addWidget(self.prismatic_fossil)


        self.verticalLayout_24.addWidget(self.fossil_btn_row1)

        self.fossil_btn_row2 = QWidget(self.fossil_btns_container)
        self.fossil_btn_row2.setObjectName(u"fossil_btn_row2")
        self.fossil_btn_row2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.fossil_btn_row2.sizePolicy().hasHeightForWidth())
        self.fossil_btn_row2.setSizePolicy(sizePolicy4)
        self.fossil_row2 = QHBoxLayout(self.fossil_btn_row2)
        self.fossil_row2.setSpacing(0)
        self.fossil_row2.setContentsMargins(0, 0, 0, 0)
        self.fossil_row2.setObjectName(u"fossil_row2")
        self.fossil_row2.setContentsMargins(0, 0, 0, 0)
        self.pristine_fossil = QPushButton(self.fossil_btn_row2)
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
        icon42 = QIcon()
        icon42.addFile(u":/fossils/assets/images/fossils/pristine_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pristine_fossil.setIcon(icon42)
        self.pristine_fossil.setIconSize(QSize(30, 30))
        self.pristine_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.pristine_fossil)

        self.scorched_fossil = QPushButton(self.fossil_btn_row2)
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
        icon43 = QIcon()
        icon43.addFile(u":/fossils/assets/images/fossils/scorched_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scorched_fossil.setIcon(icon43)
        self.scorched_fossil.setIconSize(QSize(30, 30))
        self.scorched_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.scorched_fossil)

        self.serrated_fossil = QPushButton(self.fossil_btn_row2)
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
        icon44 = QIcon()
        icon44.addFile(u":/fossils/assets/images/fossils/serrated_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.serrated_fossil.setIcon(icon44)
        self.serrated_fossil.setIconSize(QSize(30, 30))
        self.serrated_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.serrated_fossil)

        self.shuddering_fossil = QPushButton(self.fossil_btn_row2)
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
        icon45 = QIcon()
        icon45.addFile(u":/fossils/assets/images/fossils/shuddering_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shuddering_fossil.setIcon(icon45)
        self.shuddering_fossil.setIconSize(QSize(30, 30))
        self.shuddering_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.shuddering_fossil)

        self.hollow_fossil = QPushButton(self.fossil_btn_row2)
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
        icon46 = QIcon()
        icon46.addFile(u":/fossils/assets/images/fossils/hollow_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hollow_fossil.setIcon(icon46)
        self.hollow_fossil.setIconSize(QSize(30, 30))
        self.hollow_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.hollow_fossil)

        self.sanctified_fossil = QPushButton(self.fossil_btn_row2)
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
        icon47 = QIcon()
        icon47.addFile(u":/fossils/assets/images/fossils/sanctified_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sanctified_fossil.setIcon(icon47)
        self.sanctified_fossil.setIconSize(QSize(30, 30))
        self.sanctified_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.sanctified_fossil)

        self.glyphic_fossil = QPushButton(self.fossil_btn_row2)
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
        icon48 = QIcon()
        icon48.addFile(u":/fossils/assets/images/fossils/glyphic_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.glyphic_fossil.setIcon(icon48)
        self.glyphic_fossil.setIconSize(QSize(30, 30))
        self.glyphic_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.glyphic_fossil)

        self.fundamental_fossil = QPushButton(self.fossil_btn_row2)
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
        icon49 = QIcon()
        icon49.addFile(u":/fossils/assets/images/fossils/fundamental_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fundamental_fossil.setIcon(icon49)
        self.fundamental_fossil.setIconSize(QSize(30, 30))
        self.fundamental_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.fundamental_fossil)

        self.deft_fossil = QPushButton(self.fossil_btn_row2)
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
        icon50 = QIcon()
        icon50.addFile(u":/fossils/assets/images/fossils/deft_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deft_fossil.setIcon(icon50)
        self.deft_fossil.setIconSize(QSize(30, 30))
        self.deft_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.deft_fossil)

        self.gilded_fossil = QPushButton(self.fossil_btn_row2)
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
        icon51 = QIcon()
        icon51.addFile(u":/fossils/assets/images/fossils/gilded_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gilded_fossil.setIcon(icon51)
        self.gilded_fossil.setIconSize(QSize(30, 30))
        self.gilded_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.gilded_fossil)

        self.perfect_fossil = QPushButton(self.fossil_btn_row2)
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
        icon52 = QIcon()
        icon52.addFile(u":/fossils/assets/images/fossils/perfect_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfect_fossil.setIcon(icon52)
        self.perfect_fossil.setIconSize(QSize(30, 30))
        self.perfect_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.perfect_fossil)

        self.tangled_fossil = QPushButton(self.fossil_btn_row2)
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
        icon53 = QIcon()
        icon53.addFile(u":/fossils/assets/images/fossils/tangled_fossil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tangled_fossil.setIcon(icon53)
        self.tangled_fossil.setIconSize(QSize(30, 30))
        self.tangled_fossil.setCheckable(True)

        self.fossil_row2.addWidget(self.tangled_fossil)


        self.verticalLayout_24.addWidget(self.fossil_btn_row2)


        self.verticalLayout_23.addWidget(self.fossil_btns_container, 0, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.fossil_crafts)
        self.harvest_crafts = QWidget()
        self.harvest_crafts.setObjectName(u"harvest_crafts")
        sizePolicy3.setHeightForWidth(self.harvest_crafts.sizePolicy().hasHeightForWidth())
        self.harvest_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.harvest_btn_row1.sizePolicy().hasHeightForWidth())
        self.harvest_btn_row1.setSizePolicy(sizePolicy6)
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
        self.custom_cursor_btns_group.addButton(self.harvest_add_remove_btn)
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
        icon54 = QIcon()
        icon54.addFile(u":/harvest/assets/images/harvest/harvest_augment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harvest_add_remove_btn.setIcon(icon54)
        self.harvest_add_remove_btn.setIconSize(QSize(30, 30))
        self.harvest_add_remove_btn.setCheckable(True)
        self.harvest_add_remove_btn.setChecked(False)
        self.harvest_add_remove_btn.setAutoExclusive(True)

        self.fossil_row1_2.addWidget(self.harvest_add_remove_btn)

        self.harvest_reroll_btn = CustomCursorButton(self.harvest_btn_row1)
        self.custom_cursor_btns_group.addButton(self.harvest_reroll_btn)
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
        icon55 = QIcon()
        icon55.addFile(u":/harvest/assets/images/harvest/harvest_reroll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harvest_reroll_btn.setIcon(icon55)
        self.harvest_reroll_btn.setIconSize(QSize(30, 30))
        self.harvest_reroll_btn.setCheckable(True)
        self.harvest_reroll_btn.setAutoExclusive(True)

        self.fossil_row1_2.addWidget(self.harvest_reroll_btn)

        self.harvest_resists_btn = CustomCursorButton(self.harvest_btn_row1)
        self.custom_cursor_btns_group.addButton(self.harvest_resists_btn)
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
        self.harvest_resists_btn.setIcon(icon24)
        self.harvest_resists_btn.setIconSize(QSize(30, 30))
        self.harvest_resists_btn.setCheckable(True)
        self.harvest_resists_btn.setAutoExclusive(True)

        self.fossil_row1_2.addWidget(self.harvest_resists_btn)

        self.harvest_high_tier_btn = CustomCursorButton(self.harvest_btn_row1)
        self.custom_cursor_btns_group.addButton(self.harvest_high_tier_btn)
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
        self.harvest_high_tier_btn.setIcon(icon24)
        self.harvest_high_tier_btn.setIconSize(QSize(30, 30))
        self.harvest_high_tier_btn.setCheckable(True)
        self.harvest_high_tier_btn.setAutoExclusive(True)

        self.fossil_row1_2.addWidget(self.harvest_high_tier_btn)

        self.harvest_other_btn = CustomCursorButton(self.harvest_btn_row1)
        self.custom_cursor_btns_group.addButton(self.harvest_other_btn)
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
        self.harvest_other_btn.setIcon(icon24)
        self.harvest_other_btn.setIconSize(QSize(30, 30))
        self.harvest_other_btn.setCheckable(True)
        self.harvest_other_btn.setAutoExclusive(True)

        self.fossil_row1_2.addWidget(self.harvest_other_btn)


        self.verticalLayout_45.addWidget(self.harvest_btn_row1, 0, Qt.AlignTop)

        self.harvest_methods_container = QFrame(self.harvest_btns_container)
        self.harvest_methods_container.setObjectName(u"harvest_methods_container")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.harvest_methods_container.sizePolicy().hasHeightForWidth())
        self.harvest_methods_container.setSizePolicy(sizePolicy7)
        self.harvest_methods_container.setFrameShape(QFrame.StyledPanel)
        self.harvest_methods_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.harvest_methods_container)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.harvest_method_stack = QStackedWidget(self.harvest_methods_container)
        self.harvest_method_stack.setObjectName(u"harvest_method_stack")
        sizePolicy7.setHeightForWidth(self.harvest_method_stack.sizePolicy().hasHeightForWidth())
        self.harvest_method_stack.setSizePolicy(sizePolicy7)
        self.harvest_add_remove_reforge_methods = QWidget()
        self.harvest_add_remove_reforge_methods.setObjectName(u"harvest_add_remove_reforge_methods")
        sizePolicy7.setHeightForWidth(self.harvest_add_remove_reforge_methods.sizePolicy().hasHeightForWidth())
        self.harvest_add_remove_reforge_methods.setSizePolicy(sizePolicy7)
        self.verticalLayout_41 = QVBoxLayout(self.harvest_add_remove_reforge_methods)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.harvest_add_remove_reforge_btn_container = QWidget(self.harvest_add_remove_reforge_methods)
        self.harvest_add_remove_reforge_btn_container.setObjectName(u"harvest_add_remove_reforge_btn_container")
        self.harvest_add_remove_reforge_btn_container.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.harvest_add_remove_reforge_btn_container.sizePolicy().hasHeightForWidth())
        self.harvest_add_remove_reforge_btn_container.setSizePolicy(sizePolicy4)
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
        self.attack_btn.setAutoExclusive(True)

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
        self.caster_btn.setAutoExclusive(True)

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
        self.chaos_btn.setAutoExclusive(True)

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
        self.cold_btn.setAutoExclusive(True)

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
        self.critical_btn.setAutoExclusive(True)

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
        self.defences_btn.setAutoExclusive(True)

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
        self.fire_btn.setAutoExclusive(True)

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
        self.life_btn.setAutoExclusive(True)

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
        self.lightning_btn.setAutoExclusive(True)

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
        self.physical_btn.setAutoExclusive(True)

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
        self.speed_btn.setAutoExclusive(True)

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
        self.influence_btn.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.influence_btn)


        self.verticalLayout_41.addWidget(self.harvest_add_remove_reforge_btn_container)

        self.harvest_method_stack.addWidget(self.harvest_add_remove_reforge_methods)
        self.harvest_resists_methods = QWidget()
        self.harvest_resists_methods.setObjectName(u"harvest_resists_methods")
        sizePolicy7.setHeightForWidth(self.harvest_resists_methods.sizePolicy().hasHeightForWidth())
        self.harvest_resists_methods.setSizePolicy(sizePolicy7)
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
        self.harvest_fire_to_cold_btn.setAutoExclusive(True)

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
        self.harvest_fire_to_lightning_btn.setAutoExclusive(True)

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
        self.harvest_cold_to_fire_btn.setAutoExclusive(True)

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
        self.harvest_cold_to_lightning_btn.setAutoExclusive(True)

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
        self.harvest_lightning_to_fire_btn.setAutoExclusive(True)

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
        self.harvest_lightning_to_cold_btn.setAutoExclusive(True)

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
        self.harvest_normal_to_magic_one_btn.setAutoExclusive(True)

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
        self.harvest_normal_to_magic_two_btn.setAutoExclusive(True)

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
        self.harvest_magic_to_rare_two_btn.setAutoExclusive(True)

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
        self.harvest_magic_to_rare_three_btn.setAutoExclusive(True)

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
        self.harvest_magic_to_rare_four_btn.setAutoExclusive(True)

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
        self.harvest_reforge_more_likely_btn.setAutoExclusive(True)

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
        self.harvest_reforge_less_likely_btn.setAutoExclusive(True)

        self.horizontalLayout_22.addWidget(self.harvest_reforge_less_likely_btn)


        self.verticalLayout_44.addWidget(self.harvest_resists_btns_3)

        self.harvest_method_stack.addWidget(self.harvest_other_methods)

        self.verticalLayout_40.addWidget(self.harvest_method_stack)


        self.verticalLayout_45.addWidget(self.harvest_methods_container, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.harvest_btns_container, 0, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.harvest_crafts)
        self.essence_crafts = QWidget()
        self.essence_crafts.setObjectName(u"essence_crafts")
        sizePolicy3.setHeightForWidth(self.essence_crafts.sizePolicy().hasHeightForWidth())
        self.essence_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy6.setHeightForWidth(self.t6_btn.sizePolicy().hasHeightForWidth())
        self.t6_btn.setSizePolicy(sizePolicy6)
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
        self.t6_btn.setAutoExclusive(True)

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
        self.t5_btn.setAutoExclusive(True)

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
        self.t4_btn.setAutoExclusive(True)

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
        self.t3_btn.setAutoExclusive(True)

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
        self.t2_btn.setAutoExclusive(True)

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
        self.t1_btn.setAutoExclusive(True)

        self.horizontalLayout_12.addWidget(self.t1_btn)


        self.gridLayout.addWidget(self.essence_tier_row, 2, 3, 1, 1, Qt.AlignHCenter)

        self.essences_row1 = QWidget(self.essence_crafts)
        self.essences_row1.setObjectName(u"essences_row1")
        sizePolicy4.setHeightForWidth(self.essences_row1.sizePolicy().hasHeightForWidth())
        self.essences_row1.setSizePolicy(sizePolicy4)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.essences_hide_btn.sizePolicy().hasHeightForWidth())
        self.essences_hide_btn.setSizePolicy(sizePolicy8)
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
        sizePolicy3.setHeightForWidth(self.essences_label.sizePolicy().hasHeightForWidth())
        self.essences_label.setSizePolicy(sizePolicy3)
        self.essences_label.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_10.addWidget(self.essences_label)

        self.essence_anger_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_anger_btn)
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
        icon56 = QIcon()
        icon56.addFile(u":/essences/assets/images/essences/essence_Anger.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_anger_btn.setIcon(icon56)
        self.essence_anger_btn.setIconSize(QSize(30, 30))
        self.essence_anger_btn.setCheckable(True)
        self.essence_anger_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_anger_btn)

        self.essence_anguish_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_anguish_btn)
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
        icon57 = QIcon()
        icon57.addFile(u":/essences/assets/images/essences/essence_Anguish.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_anguish_btn.setIcon(icon57)
        self.essence_anguish_btn.setIconSize(QSize(30, 30))
        self.essence_anguish_btn.setCheckable(True)
        self.essence_anguish_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_anguish_btn)

        self.essence_contempt_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_contempt_btn)
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
        icon58 = QIcon()
        icon58.addFile(u":/essences/assets/images/essences/essence_Contempt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_contempt_btn.setIcon(icon58)
        self.essence_contempt_btn.setIconSize(QSize(30, 30))
        self.essence_contempt_btn.setCheckable(True)
        self.essence_contempt_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_contempt_btn)

        self.essence_delirium_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_delirium_btn)
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
        icon59 = QIcon()
        icon59.addFile(u":/essences/assets/images/essences/essence_Delirium.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_delirium_btn.setIcon(icon59)
        self.essence_delirium_btn.setIconSize(QSize(30, 30))
        self.essence_delirium_btn.setCheckable(True)
        self.essence_delirium_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_delirium_btn)

        self.essence_doubt_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_doubt_btn)
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
        icon60 = QIcon()
        icon60.addFile(u":/essences/assets/images/essences/essence_Doubt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_doubt_btn.setIcon(icon60)
        self.essence_doubt_btn.setIconSize(QSize(30, 30))
        self.essence_doubt_btn.setCheckable(True)
        self.essence_doubt_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_doubt_btn)

        self.essence_dread_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_dread_btn)
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
        icon61 = QIcon()
        icon61.addFile(u":/essences/assets/images/essences/essence_Dread.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_dread_btn.setIcon(icon61)
        self.essence_dread_btn.setIconSize(QSize(30, 30))
        self.essence_dread_btn.setCheckable(True)
        self.essence_dread_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_dread_btn)

        self.essence_envy_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_envy_btn)
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
        icon62 = QIcon()
        icon62.addFile(u":/essences/assets/images/essences/essence_Envy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_envy_btn.setIcon(icon62)
        self.essence_envy_btn.setIconSize(QSize(30, 30))
        self.essence_envy_btn.setCheckable(True)
        self.essence_envy_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_envy_btn)

        self.essence_fear_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_fear_btn)
        self.essence_fear_btn.setObjectName(u"essence_fear_btn")
        self.essence_fear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_fear_btn.setStyleSheet(u"QPushButton {\n"
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
        icon63.addFile(u":/essences/assets/images/essences/essence_Fear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_fear_btn.setIcon(icon63)
        self.essence_fear_btn.setIconSize(QSize(30, 30))
        self.essence_fear_btn.setCheckable(True)
        self.essence_fear_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_fear_btn)

        self.essence_greed_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_greed_btn)
        self.essence_greed_btn.setObjectName(u"essence_greed_btn")
        self.essence_greed_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_greed_btn.setStyleSheet(u"QPushButton {\n"
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
        icon64.addFile(u":/essences/assets/images/essences/essence_Greed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_greed_btn.setIcon(icon64)
        self.essence_greed_btn.setIconSize(QSize(30, 30))
        self.essence_greed_btn.setCheckable(True)
        self.essence_greed_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_greed_btn)

        self.essence_hatred_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_hatred_btn)
        self.essence_hatred_btn.setObjectName(u"essence_hatred_btn")
        self.essence_hatred_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.essence_hatred_btn.setStyleSheet(u"QPushButton {\n"
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
        icon65.addFile(u":/essences/assets/images/essences/essence_Hatred.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_hatred_btn.setIcon(icon65)
        self.essence_hatred_btn.setIconSize(QSize(30, 30))
        self.essence_hatred_btn.setCheckable(True)
        self.essence_hatred_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_hatred_btn)

        self.essence_horror_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_horror_btn)
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
        icon66 = QIcon()
        icon66.addFile(u":/essences/assets/images/essences/essence_Horror.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_horror_btn.setIcon(icon66)
        self.essence_horror_btn.setIconSize(QSize(30, 30))
        self.essence_horror_btn.setCheckable(True)
        self.essence_horror_btn.setAutoExclusive(True)

        self.horizontalLayout_10.addWidget(self.essence_horror_btn)

        self.essence_hysteria_btn = CustomCursorButton(self.essences_row1)
        self.custom_cursor_btns_group.addButton(self.essence_hysteria_btn)
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
        icon67 = QIcon()
        icon67.addFile(u":/essences/assets/images/essences/essence_Hysteria.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_hysteria_btn.setIcon(icon67)
        self.essence_hysteria_btn.setIconSize(QSize(30, 30))
        self.essence_hysteria_btn.setCheckable(True)
        self.essence_hysteria_btn.setChecked(False)
        self.essence_hysteria_btn.setAutoExclusive(True)

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
        self.custom_cursor_btns_group.addButton(self.essence_insanity_btn)
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
        icon68 = QIcon()
        icon68.addFile(u":/essences/assets/images/essences/essence_Insanity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_insanity_btn.setIcon(icon68)
        self.essence_insanity_btn.setIconSize(QSize(30, 30))
        self.essence_insanity_btn.setCheckable(True)
        self.essence_insanity_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_insanity_btn)

        self.essence_loathing_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_loathing_btn)
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
        icon69 = QIcon()
        icon69.addFile(u":/essences/assets/images/essences/essence_Loathing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_loathing_btn.setIcon(icon69)
        self.essence_loathing_btn.setIconSize(QSize(30, 30))
        self.essence_loathing_btn.setCheckable(True)
        self.essence_loathing_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_loathing_btn)

        self.essence_misery_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_misery_btn)
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
        icon70 = QIcon()
        icon70.addFile(u":/essences/assets/images/essences/essence_Misery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_misery_btn.setIcon(icon70)
        self.essence_misery_btn.setIconSize(QSize(30, 30))
        self.essence_misery_btn.setCheckable(True)
        self.essence_misery_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_misery_btn)

        self.essence_rage_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_rage_btn)
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
        icon71 = QIcon()
        icon71.addFile(u":/essences/assets/images/essences/essence_Rage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_rage_btn.setIcon(icon71)
        self.essence_rage_btn.setIconSize(QSize(30, 30))
        self.essence_rage_btn.setCheckable(True)
        self.essence_rage_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_rage_btn)

        self.essence_scorn_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_scorn_btn)
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
        icon72 = QIcon()
        icon72.addFile(u":/essences/assets/images/essences/essence_Scorn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_scorn_btn.setIcon(icon72)
        self.essence_scorn_btn.setIconSize(QSize(30, 30))
        self.essence_scorn_btn.setCheckable(True)
        self.essence_scorn_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_scorn_btn)

        self.essence_sorrow_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_sorrow_btn)
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
        icon73 = QIcon()
        icon73.addFile(u":/essences/assets/images/essences/essence_Sorrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_sorrow_btn.setIcon(icon73)
        self.essence_sorrow_btn.setIconSize(QSize(30, 30))
        self.essence_sorrow_btn.setCheckable(True)
        self.essence_sorrow_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_sorrow_btn)

        self.essence_spite_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_spite_btn)
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
        icon74 = QIcon()
        icon74.addFile(u":/essences/assets/images/essences/essence_Spite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_spite_btn.setIcon(icon74)
        self.essence_spite_btn.setIconSize(QSize(30, 30))
        self.essence_spite_btn.setCheckable(True)
        self.essence_spite_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_spite_btn)

        self.essence_suffering_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_suffering_btn)
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
        icon75 = QIcon()
        icon75.addFile(u":/essences/assets/images/essences/essence_Suffering.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_suffering_btn.setIcon(icon75)
        self.essence_suffering_btn.setIconSize(QSize(30, 30))
        self.essence_suffering_btn.setCheckable(True)
        self.essence_suffering_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_suffering_btn)

        self.essence_torment_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_torment_btn)
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
        icon76 = QIcon()
        icon76.addFile(u":/essences/assets/images/essences/essence_Torment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_torment_btn.setIcon(icon76)
        self.essence_torment_btn.setIconSize(QSize(30, 30))
        self.essence_torment_btn.setCheckable(True)
        self.essence_torment_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_torment_btn)

        self.essence_woe_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_woe_btn)
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
        icon77 = QIcon()
        icon77.addFile(u":/essences/assets/images/essences/essence_Woe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_woe_btn.setIcon(icon77)
        self.essence_woe_btn.setIconSize(QSize(30, 30))
        self.essence_woe_btn.setCheckable(True)
        self.essence_woe_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_woe_btn)

        self.essence_wrath_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_wrath_btn)
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
        icon78 = QIcon()
        icon78.addFile(u":/essences/assets/images/essences/essence_Wrath.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_wrath_btn.setIcon(icon78)
        self.essence_wrath_btn.setIconSize(QSize(30, 30))
        self.essence_wrath_btn.setCheckable(True)
        self.essence_wrath_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_wrath_btn)

        self.essence_zeal_btn = CustomCursorButton(self.essences_row2)
        self.custom_cursor_btns_group.addButton(self.essence_zeal_btn)
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
        icon79 = QIcon()
        icon79.addFile(u":/essences/assets/images/essences/essence_Zeal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.essence_zeal_btn.setIcon(icon79)
        self.essence_zeal_btn.setIconSize(QSize(30, 30))
        self.essence_zeal_btn.setCheckable(True)
        self.essence_zeal_btn.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.essence_zeal_btn)


        self.gridLayout.addWidget(self.essences_row2, 1, 3, 1, 1, Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.essence_crafts)
        self.catalysts = QWidget()
        self.catalysts.setObjectName(u"catalysts")
        sizePolicy3.setHeightForWidth(self.catalysts.sizePolicy().hasHeightForWidth())
        self.catalysts.setSizePolicy(sizePolicy3)
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
        sizePolicy4.setHeightForWidth(self.catalyst_btn_row.sizePolicy().hasHeightForWidth())
        self.catalyst_btn_row.setSizePolicy(sizePolicy4)
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
        sizePolicy8.setHeightForWidth(self.catalysts_hide_btn.sizePolicy().hasHeightForWidth())
        self.catalysts_hide_btn.setSizePolicy(sizePolicy8)
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

        self.intrinsic_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.intrinsic_catalyst_btn)
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
        icon80 = QIcon()
        icon80.addFile(u":/catalysts/assets/images/catalysts/intrinsic_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.intrinsic_catalyst_btn.setIcon(icon80)
        self.intrinsic_catalyst_btn.setIconSize(QSize(30, 30))
        self.intrinsic_catalyst_btn.setCheckable(True)
        self.intrinsic_catalyst_btn.setChecked(False)
        self.intrinsic_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.intrinsic_catalyst_btn)

        self.abrasive_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.abrasive_catalyst_btn)
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
        icon81 = QIcon()
        icon81.addFile(u":/catalysts/assets/images/catalysts/abrasive_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.abrasive_catalyst_btn.setIcon(icon81)
        self.abrasive_catalyst_btn.setIconSize(QSize(30, 30))
        self.abrasive_catalyst_btn.setCheckable(True)
        self.abrasive_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.abrasive_catalyst_btn)

        self.prismatic_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.prismatic_catalyst_btn)
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
        icon82 = QIcon()
        icon82.addFile(u":/catalysts/assets/images/catalysts/prismatic_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prismatic_catalyst_btn.setIcon(icon82)
        self.prismatic_catalyst_btn.setIconSize(QSize(30, 30))
        self.prismatic_catalyst_btn.setCheckable(True)
        self.prismatic_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.prismatic_catalyst_btn)

        self.fertile_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.fertile_catalyst_btn)
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
        icon83 = QIcon()
        icon83.addFile(u":/catalysts/assets/images/catalysts/fertile_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fertile_catalyst_btn.setIcon(icon83)
        self.fertile_catalyst_btn.setIconSize(QSize(30, 30))
        self.fertile_catalyst_btn.setCheckable(True)
        self.fertile_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.fertile_catalyst_btn)

        self.imbued_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.imbued_catalyst_btn)
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
        icon84 = QIcon()
        icon84.addFile(u":/catalysts/assets/images/catalysts/imbued_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imbued_catalyst_btn.setIcon(icon84)
        self.imbued_catalyst_btn.setIconSize(QSize(30, 30))
        self.imbued_catalyst_btn.setCheckable(True)
        self.imbued_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.imbued_catalyst_btn)

        self.tempering_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.tempering_catalyst_btn)
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
        icon85 = QIcon()
        icon85.addFile(u":/catalysts/assets/images/catalysts/tempering_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tempering_catalyst_btn.setIcon(icon85)
        self.tempering_catalyst_btn.setIconSize(QSize(30, 30))
        self.tempering_catalyst_btn.setCheckable(True)
        self.tempering_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.tempering_catalyst_btn)

        self.turbulent_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.turbulent_catalyst_btn)
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
        icon86 = QIcon()
        icon86.addFile(u":/catalysts/assets/images/catalysts/turbulent_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turbulent_catalyst_btn.setIcon(icon86)
        self.turbulent_catalyst_btn.setIconSize(QSize(30, 30))
        self.turbulent_catalyst_btn.setCheckable(True)
        self.turbulent_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.turbulent_catalyst_btn)

        self.accelerating_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.accelerating_catalyst_btn)
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
        icon87 = QIcon()
        icon87.addFile(u":/catalysts/assets/images/catalysts/accelerating_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accelerating_catalyst_btn.setIcon(icon87)
        self.accelerating_catalyst_btn.setIconSize(QSize(30, 30))
        self.accelerating_catalyst_btn.setCheckable(True)
        self.accelerating_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.accelerating_catalyst_btn)

        self.unstable_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.unstable_catalyst_btn)
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
        icon88 = QIcon()
        icon88.addFile(u":/catalysts/assets/images/catalysts/unstable_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.unstable_catalyst_btn.setIcon(icon88)
        self.unstable_catalyst_btn.setIconSize(QSize(30, 30))
        self.unstable_catalyst_btn.setCheckable(True)
        self.unstable_catalyst_btn.setAutoExclusive(True)

        self.horizontalLayout_13.addWidget(self.unstable_catalyst_btn)

        self.noxious_catalyst_btn = CustomCursorButton(self.catalyst_btn_row)
        self.custom_cursor_btns_group.addButton(self.noxious_catalyst_btn)
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
        icon89 = QIcon()
        icon89.addFile(u":/catalysts/assets/images/catalysts/noxious_catalyst.png", QSize(), QIcon.Normal, QIcon.Off)
        self.noxious_catalyst_btn.setIcon(icon89)
        self.noxious_catalyst_btn.setIconSize(QSize(30, 30))
        self.noxious_catalyst_btn.setCheckable(True)
        self.noxious_catalyst_btn.setAutoExclusive(True)

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
        self.max_catalyst_btn.setAutoExclusive(True)

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
        self.single_catalys_btn.setAutoExclusive(True)

        self.horizontalLayout_14.addWidget(self.single_catalys_btn)


        self.verticalLayout_22.addWidget(self.catalyst_mode_row, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.crafting_method_pages.addWidget(self.catalysts)
        self.beast_crafts = QWidget()
        self.beast_crafts.setObjectName(u"beast_crafts")
        sizePolicy3.setHeightForWidth(self.beast_crafts.sizePolicy().hasHeightForWidth())
        self.beast_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy8.setHeightForWidth(self.beast_crafting_hide_btn.sizePolicy().hasHeightForWidth())
        self.beast_crafting_hide_btn.setSizePolicy(sizePolicy8)
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

        self.bprefix__to_suffix_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon90 = QIcon()
        icon90.addFile(u":/beasts/assets/images/beasts/bpretsuf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bprefix__to_suffix_btn.setIcon(icon90)
        self.bprefix__to_suffix_btn.setIconSize(QSize(30, 30))
        self.bprefix__to_suffix_btn.setCheckable(True)
        self.bprefix__to_suffix_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bprefix__to_suffix_btn)

        self.bsuffix_to_prefix_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon91 = QIcon()
        icon91.addFile(u":/beasts/assets/images/beasts/bsuftpre.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bsuffix_to_prefix_btn.setIcon(icon91)
        self.bsuffix_to_prefix_btn.setIconSize(QSize(30, 30))
        self.bsuffix_to_prefix_btn.setCheckable(True)
        self.bsuffix_to_prefix_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bsuffix_to_prefix_btn)

        self.bimprint_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon92 = QIcon()
        icon92.addFile(u":/beasts/assets/images/beasts/bimprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bimprint_btn.setIcon(icon92)
        self.bimprint_btn.setIconSize(QSize(30, 30))
        self.bimprint_btn.setCheckable(True)
        self.bimprint_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bimprint_btn)

        self.breroll_values_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon93 = QIcon()
        icon93.addFile(u":/beasts/assets/images/beasts/breroll.png", QSize(), QIcon.Normal, QIcon.Off)
        self.breroll_values_btn.setIcon(icon93)
        self.breroll_values_btn.setIconSize(QSize(30, 30))
        self.breroll_values_btn.setCheckable(True)
        self.breroll_values_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.breroll_values_btn)

        self.bcat_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon94 = QIcon()
        icon94.addFile(u":/beasts/assets/images/beasts/bcat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bcat_btn.setIcon(icon94)
        self.bcat_btn.setIconSize(QSize(30, 30))
        self.bcat_btn.setCheckable(True)
        self.bcat_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bcat_btn)

        self.bavian_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon95 = QIcon()
        icon95.addFile(u":/beasts/assets/images/beasts/bavian.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bavian_btn.setIcon(icon95)
        self.bavian_btn.setIconSize(QSize(30, 30))
        self.bavian_btn.setCheckable(True)
        self.bavian_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bavian_btn)

        self.bspider_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon96 = QIcon()
        icon96.addFile(u":/beasts/assets/images/beasts/bspider.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bspider_btn.setIcon(icon96)
        self.bspider_btn.setIconSize(QSize(30, 30))
        self.bspider_btn.setCheckable(True)
        self.bspider_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bspider_btn)

        self.bcrab_btn = QPushButton(self.beast_crafting_methods_btns)
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
        icon97 = QIcon()
        icon97.addFile(u":/beasts/assets/images/beasts/bcrab.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bcrab_btn.setIcon(icon97)
        self.bcrab_btn.setIconSize(QSize(30, 30))
        self.bcrab_btn.setCheckable(True)
        self.bcrab_btn.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.bcrab_btn)


        self.verticalLayout_29.addWidget(self.beast_crafting_methods_btns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer)

        self.crafting_method_pages.addWidget(self.beast_crafts)
        self.eldritch_crafts = QWidget()
        self.eldritch_crafts.setObjectName(u"eldritch_crafts")
        sizePolicy3.setHeightForWidth(self.eldritch_crafts.sizePolicy().hasHeightForWidth())
        self.eldritch_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.eldritch_btn_row1.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row1.setSizePolicy(sizePolicy3)
        self.fossil_row1_3 = QHBoxLayout(self.eldritch_btn_row1)
        self.fossil_row1_3.setSpacing(0)
        self.fossil_row1_3.setContentsMargins(0, 0, 0, 0)
        self.fossil_row1_3.setObjectName(u"fossil_row1_3")
        self.fossil_row1_3.setContentsMargins(0, 0, 0, 0)
        self.eldritch_hide_btn = QPushButton(self.eldritch_btn_row1)
        self.eldritch_hide_btn.setObjectName(u"eldritch_hide_btn")
        self.eldritch_hide_btn.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.eldritch_hide_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_hide_btn.setSizePolicy(sizePolicy5)
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
        self.eldritch_hide_btn.setCheckable(False)

        self.fossil_row1_3.addWidget(self.eldritch_hide_btn)

        self.eldritch_method_label = QLabel(self.eldritch_btn_row1)
        self.eldritch_method_label.setObjectName(u"eldritch_method_label")
        self.eldritch_method_label.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.eldritch_method_label.sizePolicy().hasHeightForWidth())
        self.eldritch_method_label.setSizePolicy(sizePolicy5)

        self.fossil_row1_3.addWidget(self.eldritch_method_label)

        self.eldritch_chaos_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.custom_cursor_btns_group.addButton(self.eldritch_chaos_btn)
        self.eldritch_chaos_btn.setObjectName(u"eldritch_chaos_btn")
        self.eldritch_chaos_btn.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.eldritch_chaos_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_chaos_btn.setSizePolicy(sizePolicy9)
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
        icon98 = QIcon()
        icon98.addFile(u":/eldritch/assets/images/eldritch/eldritch_chaos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_chaos_btn.setIcon(icon98)
        self.eldritch_chaos_btn.setIconSize(QSize(30, 30))
        self.eldritch_chaos_btn.setCheckable(True)
        self.eldritch_chaos_btn.setAutoExclusive(True)

        self.fossil_row1_3.addWidget(self.eldritch_chaos_btn)

        self.eldritch_exalted_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.custom_cursor_btns_group.addButton(self.eldritch_exalted_btn)
        self.eldritch_exalted_btn.setObjectName(u"eldritch_exalted_btn")
        self.eldritch_exalted_btn.setEnabled(True)
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.eldritch_exalted_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_exalted_btn.setSizePolicy(sizePolicy10)
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
        icon99 = QIcon()
        icon99.addFile(u":/eldritch/assets/images/eldritch/eldritch_exalted.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_exalted_btn.setIcon(icon99)
        self.eldritch_exalted_btn.setIconSize(QSize(30, 30))
        self.eldritch_exalted_btn.setCheckable(True)
        self.eldritch_exalted_btn.setAutoExclusive(True)

        self.fossil_row1_3.addWidget(self.eldritch_exalted_btn)

        self.eldritch_annul_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.custom_cursor_btns_group.addButton(self.eldritch_annul_btn)
        self.eldritch_annul_btn.setObjectName(u"eldritch_annul_btn")
        self.eldritch_annul_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.eldritch_annul_btn.sizePolicy().hasHeightForWidth())
        self.eldritch_annul_btn.setSizePolicy(sizePolicy10)
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
        icon100 = QIcon()
        icon100.addFile(u":/eldritch/assets/images/eldritch/eldritch_annul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eldritch_annul_btn.setIcon(icon100)
        self.eldritch_annul_btn.setIconSize(QSize(30, 30))
        self.eldritch_annul_btn.setCheckable(True)
        self.eldritch_annul_btn.setAutoExclusive(True)

        self.fossil_row1_3.addWidget(self.eldritch_annul_btn)

        self.orb_of_conflict_btn = CustomCursorButton(self.eldritch_btn_row1)
        self.custom_cursor_btns_group.addButton(self.orb_of_conflict_btn)
        self.orb_of_conflict_btn.setObjectName(u"orb_of_conflict_btn")
        self.orb_of_conflict_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.orb_of_conflict_btn.sizePolicy().hasHeightForWidth())
        self.orb_of_conflict_btn.setSizePolicy(sizePolicy10)
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
        icon101 = QIcon()
        icon101.addFile(u":/eldritch/assets/images/eldritch/orb_of_conflict.png", QSize(), QIcon.Normal, QIcon.Off)
        self.orb_of_conflict_btn.setIcon(icon101)
        self.orb_of_conflict_btn.setIconSize(QSize(30, 30))
        self.orb_of_conflict_btn.setCheckable(True)
        self.orb_of_conflict_btn.setAutoExclusive(True)

        self.fossil_row1_3.addWidget(self.orb_of_conflict_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row1)

        self.eldritch_btn_row2 = QWidget(self.eldritch_btns_container)
        self.eldritch_btn_row2.setObjectName(u"eldritch_btn_row2")
        self.eldritch_btn_row2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.eldritch_btn_row2.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_17 = QHBoxLayout(self.eldritch_btn_row2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lesser_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.custom_cursor_btns_group.addButton(self.lesser_ember_btn)
        self.lesser_ember_btn.setObjectName(u"lesser_ember_btn")
        self.lesser_ember_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.lesser_ember_btn.sizePolicy().hasHeightForWidth())
        self.lesser_ember_btn.setSizePolicy(sizePolicy10)
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
        icon102 = QIcon()
        icon102.addFile(u":/eldritch/assets/images/eldritch/lesser_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lesser_ember_btn.setIcon(icon102)
        self.lesser_ember_btn.setIconSize(QSize(30, 30))
        self.lesser_ember_btn.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.lesser_ember_btn, 0, Qt.AlignHCenter)

        self.greater_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.custom_cursor_btns_group.addButton(self.greater_ember_btn)
        self.greater_ember_btn.setObjectName(u"greater_ember_btn")
        self.greater_ember_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.greater_ember_btn.sizePolicy().hasHeightForWidth())
        self.greater_ember_btn.setSizePolicy(sizePolicy10)
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
        icon103 = QIcon()
        icon103.addFile(u":/eldritch/assets/images/eldritch/greater_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.greater_ember_btn.setIcon(icon103)
        self.greater_ember_btn.setIconSize(QSize(30, 30))
        self.greater_ember_btn.setCheckable(True)
        self.greater_ember_btn.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.greater_ember_btn)

        self.grand_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.custom_cursor_btns_group.addButton(self.grand_ember_btn)
        self.grand_ember_btn.setObjectName(u"grand_ember_btn")
        self.grand_ember_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.grand_ember_btn.sizePolicy().hasHeightForWidth())
        self.grand_ember_btn.setSizePolicy(sizePolicy10)
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
        icon104 = QIcon()
        icon104.addFile(u":/eldritch/assets/images/eldritch/grand_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grand_ember_btn.setIcon(icon104)
        self.grand_ember_btn.setIconSize(QSize(30, 30))
        self.grand_ember_btn.setCheckable(True)
        self.grand_ember_btn.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.grand_ember_btn)

        self.exceptional_ember_btn = CustomCursorButton(self.eldritch_btn_row2)
        self.custom_cursor_btns_group.addButton(self.exceptional_ember_btn)
        self.exceptional_ember_btn.setObjectName(u"exceptional_ember_btn")
        self.exceptional_ember_btn.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.exceptional_ember_btn.sizePolicy().hasHeightForWidth())
        self.exceptional_ember_btn.setSizePolicy(sizePolicy10)
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
        icon105 = QIcon()
        icon105.addFile(u":/eldritch/assets/images/eldritch/exceptional_eldritch_ember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exceptional_ember_btn.setIcon(icon105)
        self.exceptional_ember_btn.setIconSize(QSize(30, 30))
        self.exceptional_ember_btn.setCheckable(True)
        self.exceptional_ember_btn.setAutoExclusive(True)

        self.horizontalLayout_17.addWidget(self.exceptional_ember_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row2, 0, Qt.AlignHCenter)

        self.eldritch_btn_row3 = QWidget(self.eldritch_btns_container)
        self.eldritch_btn_row3.setObjectName(u"eldritch_btn_row3")
        sizePolicy3.setHeightForWidth(self.eldritch_btn_row3.sizePolicy().hasHeightForWidth())
        self.eldritch_btn_row3.setSizePolicy(sizePolicy3)
        self.horizontalLayout_16 = QHBoxLayout(self.eldritch_btn_row3)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lesser_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.custom_cursor_btns_group.addButton(self.lesser_ichor_btn)
        self.lesser_ichor_btn.setObjectName(u"lesser_ichor_btn")
        self.lesser_ichor_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.lesser_ichor_btn.sizePolicy().hasHeightForWidth())
        self.lesser_ichor_btn.setSizePolicy(sizePolicy6)
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
        icon106 = QIcon()
        icon106.addFile(u":/eldritch/assets/images/eldritch/lesser_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lesser_ichor_btn.setIcon(icon106)
        self.lesser_ichor_btn.setIconSize(QSize(30, 30))
        self.lesser_ichor_btn.setCheckable(True)
        self.lesser_ichor_btn.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.lesser_ichor_btn)

        self.greater_icho_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.custom_cursor_btns_group.addButton(self.greater_icho_btn)
        self.greater_icho_btn.setObjectName(u"greater_icho_btn")
        self.greater_icho_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.greater_icho_btn.sizePolicy().hasHeightForWidth())
        self.greater_icho_btn.setSizePolicy(sizePolicy6)
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
        icon107 = QIcon()
        icon107.addFile(u":/eldritch/assets/images/eldritch/greater_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.greater_icho_btn.setIcon(icon107)
        self.greater_icho_btn.setIconSize(QSize(30, 30))
        self.greater_icho_btn.setCheckable(True)
        self.greater_icho_btn.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.greater_icho_btn)

        self.grand_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.custom_cursor_btns_group.addButton(self.grand_ichor_btn)
        self.grand_ichor_btn.setObjectName(u"grand_ichor_btn")
        self.grand_ichor_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.grand_ichor_btn.sizePolicy().hasHeightForWidth())
        self.grand_ichor_btn.setSizePolicy(sizePolicy6)
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
        icon108 = QIcon()
        icon108.addFile(u":/eldritch/assets/images/eldritch/grand_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grand_ichor_btn.setIcon(icon108)
        self.grand_ichor_btn.setIconSize(QSize(30, 30))
        self.grand_ichor_btn.setCheckable(True)
        self.grand_ichor_btn.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.grand_ichor_btn)

        self.exceptional_ichor_btn = CustomCursorButton(self.eldritch_btn_row3)
        self.custom_cursor_btns_group.addButton(self.exceptional_ichor_btn)
        self.exceptional_ichor_btn.setObjectName(u"exceptional_ichor_btn")
        self.exceptional_ichor_btn.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.exceptional_ichor_btn.sizePolicy().hasHeightForWidth())
        self.exceptional_ichor_btn.setSizePolicy(sizePolicy6)
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
        icon109 = QIcon()
        icon109.addFile(u":/eldritch/assets/images/eldritch/exceptional_eldritch_ichor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exceptional_ichor_btn.setIcon(icon109)
        self.exceptional_ichor_btn.setIconSize(QSize(30, 30))
        self.exceptional_ichor_btn.setCheckable(True)
        self.exceptional_ichor_btn.setAutoExclusive(True)

        self.horizontalLayout_16.addWidget(self.exceptional_ichor_btn)


        self.verticalLayout_36.addWidget(self.eldritch_btn_row3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_18.addWidget(self.eldritch_btns_container)

        self.crafting_method_pages.addWidget(self.eldritch_crafts)
        self.syndicate_crafts = QWidget()
        self.syndicate_crafts.setObjectName(u"syndicate_crafts")
        sizePolicy3.setHeightForWidth(self.syndicate_crafts.sizePolicy().hasHeightForWidth())
        self.syndicate_crafts.setSizePolicy(sizePolicy3)
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
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.search_bar_container.sizePolicy().hasHeightForWidth())
        self.search_bar_container.setSizePolicy(sizePolicy11)
        self.horizontalLayout_3 = QHBoxLayout(self.search_bar_container)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.affix_search_bar = QLineEdit(self.search_bar_container)
        self.affix_search_bar.setObjectName(u"affix_search_bar")
        sizePolicy11.setHeightForWidth(self.affix_search_bar.sizePolicy().hasHeightForWidth())
        self.affix_search_bar.setSizePolicy(sizePolicy11)
        self.affix_search_bar.setMinimumSize(QSize(130, 30))
        self.affix_search_bar.setMaximumSize(QSize(1675555, 30))
        font4 = QFont()
        font4.setFamilies([u"Open Sans"])
        font4.setBold(False)
        font4.setItalic(False)
        self.affix_search_bar.setFont(font4)
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
        font5 = QFont()
        font5.setFamilies([u"Open Sans"])
        font5.setBold(True)
        font5.setItalic(False)
        self.crafting_history.setFont(font5)
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
        self.history_tab.setGeometry(QRect(0, 0, 160, 168))
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
        self.spending_tab.setGeometry(QRect(0, 0, 160, 168))
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
        self.export_tab.setGeometry(QRect(0, 0, 160, 168))
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
        sizePolicy11.setHeightForWidth(self.modpool_btns_layout.sizePolicy().hasHeightForWidth())
        self.modpool_btns_layout.setSizePolicy(sizePolicy11)
        self.modpool_btns_layout.setStyleSheet(u"QPushButton {\n"
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
        self.prefix_btn.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(84, 40, 109, 255), stop:1 rgba(108, 58, 136, 255));\n"
"opacity: 0.5;\n"
"}\n"
"QPushButton::hover {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(84, 40, 109, 255), stop:1 rgba(108, 58, 136, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: rgb(255, 255, 255);\n"
"text-shadow: 1px 1px #000;\n"
"}\n"
"QPushButton::checked {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(84, 40, 109, 255), stop:1 rgba(108, 58, 136, 255));\n"
"margin: 0px;\n"
"font-family: Open Sans;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba (0, 0, 0, 0.31);\n"
"border: 1px solid #000;\n"
"color: rgb(25"
                        "5, 255, 255);\n"
"text-shadow: 1px 1px #000;\n"
"}")
        self.prefix_btn.setCheckable(True)
        self.prefix_btn.setChecked(False)
        self.prefix_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.prefix_btn)

        self.suffix_btn = QPushButton(self.modpool_btns_layout)
        self.modpool_btns_group.addButton(self.suffix_btn)
        self.suffix_btn.setObjectName(u"suffix_btn")
        sizePolicy1.setHeightForWidth(self.suffix_btn.sizePolicy().hasHeightForWidth())
        self.suffix_btn.setSizePolicy(sizePolicy1)
        self.suffix_btn.setMinimumSize(QSize(0, 0))
        self.suffix_btn.setMaximumSize(QSize(16777215, 1677215))
        self.suffix_btn.setStyleSheet(u"background-color: rgb(48, 95, 121);\n"
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
        self.suffix_btn.setCheckable(True)
        self.suffix_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.suffix_btn)

        self.implicit_btn = QPushButton(self.modpool_btns_layout)
        self.modpool_btns_group.addButton(self.implicit_btn)
        self.implicit_btn.setObjectName(u"implicit_btn")
        sizePolicy1.setHeightForWidth(self.implicit_btn.sizePolicy().hasHeightForWidth())
        self.implicit_btn.setSizePolicy(sizePolicy1)
        self.implicit_btn.setStyleSheet(u"background-color: rgb(125, 69, 69);\n"
"\n"
"QPushButton::flat {\n"
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
        self.implicit_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.implicit_btn)


        self.verticalLayout_32.addWidget(self.modpool_btns_layout, 0, Qt.AlignTop)

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
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.item_description.sizePolicy().hasHeightForWidth())
        self.item_description.setSizePolicy(sizePolicy12)
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
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.item_description_layout.sizePolicy().hasHeightForWidth())
        self.item_description_layout.setSizePolicy(sizePolicy13)
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
        sizePolicy12.setHeightForWidth(self.item_header.sizePolicy().hasHeightForWidth())
        self.item_header.setSizePolicy(sizePolicy12)
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
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.item_header_text_label.sizePolicy().hasHeightForWidth())
        self.item_header_text_label.setSizePolicy(sizePolicy14)
        self.item_header_text_label.setMinimumSize(QSize(400, 54))
        self.item_header_text_label.setMaximumSize(QSize(400, 54))
        font6 = QFont()
        font6.setFamilies([u"Open Sans"])
        font6.setBold(False)
        font6.setItalic(False)
        font6.setKerning(True)
        self.item_header_text_label.setFont(font6)
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
        sizePolicy14.setHeightForWidth(self.affixes.sizePolicy().hasHeightForWidth())
        self.affixes.setSizePolicy(sizePolicy14)
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
        sizePolicy15 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.item_spacer_1.sizePolicy().hasHeightForWidth())
        self.item_spacer_1.setSizePolicy(sizePolicy15)
        self.item_spacer_1.setMaximumSize(QSize(400, 2))
        self.item_spacer_1.setBaseSize(QSize(0, 0))
        self.item_spacer_1.setTextFormat(Qt.RichText)
        self.item_spacer_1.setPixmap(QPixmap(u":/images/assets/images/item-sep.png"))
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
        sizePolicy15.setHeightForWidth(self.item_spacer_2.sizePolicy().hasHeightForWidth())
        self.item_spacer_2.setSizePolicy(sizePolicy15)
        self.item_spacer_2.setMaximumSize(QSize(400, 2))
        self.item_spacer_2.setBaseSize(QSize(0, 0))
        self.item_spacer_2.setTextFormat(Qt.RichText)
        self.item_spacer_2.setPixmap(QPixmap(u":/images/assets/images/item-sep.png"))
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
        sizePolicy15.setHeightForWidth(self.item_spacer_3.sizePolicy().hasHeightForWidth())
        self.item_spacer_3.setSizePolicy(sizePolicy15)
        self.item_spacer_3.setMaximumSize(QSize(400, 2))
        self.item_spacer_3.setBaseSize(QSize(0, 0))
        self.item_spacer_3.setTextFormat(Qt.RichText)
        self.item_spacer_3.setPixmap(QPixmap(u":/images/assets/images/item-sep.png"))
        self.item_spacer_3.setScaledContents(False)
        self.item_spacer_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_spacer_3)


        self.verticalLayout_5.addWidget(self.affixes)

        self.modifiers = QWidget(self.item_info_box)
        self.modifiers.setObjectName(u"modifiers")
        self.modifiers.setEnabled(False)
        sizePolicy13.setHeightForWidth(self.modifiers.sizePolicy().hasHeightForWidth())
        self.modifiers.setSizePolicy(sizePolicy13)
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
        self.prefix_info_1.setFont(font4)
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
        self.prefix_info_2.setFont(font4)
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
        self.prefix_info_3.setFont(font4)
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
        self.suffix_info_1.setFont(font4)
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
        self.suffix_info_2.setFont(font4)
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
        self.suffix_info_3.setFont(font4)
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
        self.menuCrafting.addAction(self.action_start_over)
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
        self.action_start_over.triggered.connect(MainWindow.resetOptions)
        self.start_crafting_project_btn.clicked.connect(MainWindow.show_wizard)
        self.clear_item_options.clicked.connect(MainWindow.resetOptions)
        self.fossil_hide_button.clicked.connect(self.crafting_method_pages.hide)
        self.harvest_hide_btn.clicked.connect(self.crafting_method_pages.hide)
        self.essences_hide_btn.clicked.connect(self.crafting_method_pages.hide)
        self.catalysts_hide_btn.clicked.connect(self.crafting_method_pages.hide)
        self.beast_crafting_hide_btn.clicked.connect(self.crafting_method_pages.hide)
        self.eldritch_hide_btn.clicked.connect(self.eldritch_btns_container.hide)

        self.crafting_simulator.setCurrentIndex(1)
        self.crafting_method_pages.setCurrentIndex(0)
        self.harvest_method_stack.setCurrentIndex(2)
        self.crafting_history.setCurrentIndex(2)
        self.crafting_history.layout().setSpacing(0)
        self.clear_item_options.setDefault(False)
        self.import_custom_item.setDefault(False)
        self.implicit_btn.setDefault(False)
        self.modpool_container.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExileCraft", None))
        self.action_start_over.setText(QCoreApplication.translate("MainWindow", u"Start Over", None))
        self.actionPOEDB_TW.setText(QCoreApplication.translate("MainWindow", u"POEDB.TW", None))
        self.actionPrice_Checker.setText(QCoreApplication.translate("MainWindow", u"Price Checker", None))
        self.actionPOE_NINJA.setText(QCoreApplication.translate("MainWindow", u"POE.NINJA", None))
        self.actionPATHOFEXILE_COM_TRADE.setText(QCoreApplication.translate("MainWindow", u"PATHOFEXILE.COM/TRADE", None))
        self.actionUI.setText(QCoreApplication.translate("MainWindow", u"UI", None))
        self.actionTrade.setText(QCoreApplication.translate("MainWindow", u"Trade", None))
        self.actionCrafting.setText(QCoreApplication.translate("MainWindow", u"Crafting", None))
        self.actionCrafting_Tutorials.setText(QCoreApplication.translate("MainWindow", u"Crafting Tutorials", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"Search for an affix", None))
        self.landing_page_label.setText(QCoreApplication.translate("MainWindow", u"Welcome To ExileCraft", None))
        self.start_crafting_project_btn.setText(QCoreApplication.translate("MainWindow", u"Start Crafting Project", None))
        self.load_saved_project_btn.setText(QCoreApplication.translate("MainWindow", u"Load Saved Project", None))
        self.import_item_from_poe_btn.setText(QCoreApplication.translate("MainWindow", u"Import Item Info From Path Of Exile", None))
#if QT_CONFIG(tooltip)
        self.method_transmute_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Upgrades a Normal Item to a Magic Item</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_transmute_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_alteration_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Reforges a Magic Item with new random properties</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_alteration_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_augmentation_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Enchants a Magic Item with a new random property</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_augmentation_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_regal_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Upgrades a Magic Item to a Rare Item</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_regal_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_alchemy_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Upgrades a Normal Item to a Rare Item</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.method_alchemy_btn.setText("")
#if QT_CONFIG(tooltip)
        self.method_chaos_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#8787fe;\">Reforges a Rare Item with new random modifiers</span></p></body></html>", None))
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
#if QT_CONFIG(tooltip)
        self.abberant_fossil.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#8787fe;\">More: Chaos</span></p><p><span style=\" font-size:12pt; color:#8787fe;\">No: Lightning</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
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
        self.essence_fear_btn.setText(QCoreApplication.translate("MainWindow", u"Fear", None))
        self.essence_greed_btn.setText(QCoreApplication.translate("MainWindow", u"Greed", None))
        self.essence_hatred_btn.setText(QCoreApplication.translate("MainWindow", u"Hatred", None))
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
        self.prefix_btn.setText(QCoreApplication.translate("MainWindow", u"Prefixes", None))
        self.suffix_btn.setText(QCoreApplication.translate("MainWindow", u"Suffixes", None))
        self.implicit_btn.setText(QCoreApplication.translate("MainWindow", u"Implicits", None))
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

