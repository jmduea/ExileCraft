# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_options_wizard.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget, QWizard, QWizardPage)

from ..pages.base_selection import BaseSelection
from ..pages.item_selection import ItemSelection
from . import wizard_assets_rc

class Ui_ItemOptionsWizard(object):
    def setupUi(self, ItemOptionsWizard):
        if not ItemOptionsWizard.objectName():
            ItemOptionsWizard.setObjectName(u"ItemOptionsWizard")
        ItemOptionsWizard.setWindowModality(Qt.ApplicationModal)
        ItemOptionsWizard.resize(473, 253)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ItemOptionsWizard.sizePolicy().hasHeightForWidth())
        ItemOptionsWizard.setSizePolicy(sizePolicy)
        ItemOptionsWizard.setMinimumSize(QSize(473, 253))
        ItemOptionsWizard.setMaximumSize(QSize(16775, 16755))
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/vendor.ico", QSize(), QIcon.Normal, QIcon.Off)
        ItemOptionsWizard.setWindowIcon(icon)
        ItemOptionsWizard.setSizeGripEnabled(False)
        ItemOptionsWizard.setModal(False)
        ItemOptionsWizard.setWizardStyle(QWizard.ClassicStyle)
        ItemOptionsWizard.setOptions(QWizard.IndependentPages|QWizard.NoBackButtonOnStartPage)
        ItemOptionsWizard.setCurrentId(0)
        self.wizard_start_page = QWizardPage()
        self.wizard_start_page.setObjectName(u"wizard_start_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wizard_start_page.sizePolicy().hasHeightForWidth())
        self.wizard_start_page.setSizePolicy(sizePolicy1)
        self.wizard_start_page.setMinimumSize(QSize(342, 0))
        self.wizard_start_page.setMaximumSize(QSize(342, 113))
        self.wizard_start_page.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.wizard_start_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wizard_start_page_container = QWidget(self.wizard_start_page)
        self.wizard_start_page_container.setObjectName(u"wizard_start_page_container")
        sizePolicy1.setHeightForWidth(self.wizard_start_page_container.sizePolicy().hasHeightForWidth())
        self.wizard_start_page_container.setSizePolicy(sizePolicy1)
        self.wizard_start_page_container.setStyleSheet(u"border-image: none;")
        self.verticalLayout = QVBoxLayout(self.wizard_start_page_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wizard_start_page_options = QWidget(self.wizard_start_page_container)
        self.wizard_start_page_options.setObjectName(u"wizard_start_page_options")
        sizePolicy1.setHeightForWidth(self.wizard_start_page_options.sizePolicy().hasHeightForWidth())
        self.wizard_start_page_options.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.wizard_start_page_options)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wizard_start_project_name = QWidget(self.wizard_start_page_options)
        self.wizard_start_project_name.setObjectName(u"wizard_start_project_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wizard_start_project_name.sizePolicy().hasHeightForWidth())
        self.wizard_start_project_name.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.wizard_start_project_name)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.project_name_label = QLabel(self.wizard_start_project_name)
        self.project_name_label.setObjectName(u"project_name_label")

        self.horizontalLayout.addWidget(self.project_name_label)

        self.project_name_input = QLineEdit(self.wizard_start_project_name)
        self.project_name_input.setObjectName(u"project_name_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.project_name_input.sizePolicy().hasHeightForWidth())
        self.project_name_input.setSizePolicy(sizePolicy3)
        self.project_name_input.setFrame(True)

        self.horizontalLayout.addWidget(self.project_name_input)


        self.verticalLayout_2.addWidget(self.wizard_start_project_name)


        self.verticalLayout.addWidget(self.wizard_start_page_options)


        self.verticalLayout_3.addWidget(self.wizard_start_page_container)

        ItemOptionsWizard.setPage(0, self.wizard_start_page)
        self.wizard_base_groups_page = QWizardPage()
        self.wizard_base_groups_page.setObjectName(u"wizard_base_groups_page")
        sizePolicy.setHeightForWidth(self.wizard_base_groups_page.sizePolicy().hasHeightForWidth())
        self.wizard_base_groups_page.setSizePolicy(sizePolicy)
        self.wizard_base_groups_page.setMinimumSize(QSize(452, 0))
        self.verticalLayout_4 = QVBoxLayout(self.wizard_base_groups_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.base_group_btns = QWidget(self.wizard_base_groups_page)
        self.base_group_btns.setObjectName(u"base_group_btns")
        self.base_group_btns.setMinimumSize(QSize(400, 0))
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
        self.verticalLayout_5 = QVBoxLayout(self.base_group_btns)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.base_group_btns_row1 = QWidget(self.base_group_btns)
        self.base_group_btns_row1.setObjectName(u"base_group_btns_row1")
        self.horizontalLayout_3 = QHBoxLayout(self.base_group_btns_row1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.body_armours_btn = QPushButton(self.base_group_btns_row1)
        self.wizard_base_group_btns = QButtonGroup(ItemOptionsWizard)
        self.wizard_base_group_btns.setObjectName(u"wizard_base_group_btns")
        self.wizard_base_group_btns.addButton(self.body_armours_btn)
        self.body_armours_btn.setObjectName(u"body_armours_btn")
        sizePolicy.setHeightForWidth(self.body_armours_btn.sizePolicy().hasHeightForWidth())
        self.body_armours_btn.setSizePolicy(sizePolicy)
        self.body_armours_btn.setStyleSheet(u"QPushButton {\n"
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
        self.body_armours_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.body_armours_btn)

        self.boots_btn = QPushButton(self.base_group_btns_row1)
        self.wizard_base_group_btns.addButton(self.boots_btn)
        self.boots_btn.setObjectName(u"boots_btn")
        sizePolicy.setHeightForWidth(self.boots_btn.sizePolicy().hasHeightForWidth())
        self.boots_btn.setSizePolicy(sizePolicy)
        self.boots_btn.setStyleSheet(u"QPushButton {\n"
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
        self.boots_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.boots_btn)

        self.helmets_btn = QPushButton(self.base_group_btns_row1)
        self.wizard_base_group_btns.addButton(self.helmets_btn)
        self.helmets_btn.setObjectName(u"helmets_btn")
        sizePolicy.setHeightForWidth(self.helmets_btn.sizePolicy().hasHeightForWidth())
        self.helmets_btn.setSizePolicy(sizePolicy)
        self.helmets_btn.setStyleSheet(u"QPushButton {\n"
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
        self.helmets_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.helmets_btn)

        self.gloves_btn = QPushButton(self.base_group_btns_row1)
        self.wizard_base_group_btns.addButton(self.gloves_btn)
        self.gloves_btn.setObjectName(u"gloves_btn")
        sizePolicy.setHeightForWidth(self.gloves_btn.sizePolicy().hasHeightForWidth())
        self.gloves_btn.setSizePolicy(sizePolicy)
        self.gloves_btn.setStyleSheet(u"QPushButton {\n"
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
        self.gloves_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gloves_btn)


        self.verticalLayout_5.addWidget(self.base_group_btns_row1)

        self.base_group_btns_row2 = QWidget(self.base_group_btns)
        self.base_group_btns_row2.setObjectName(u"base_group_btns_row2")
        sizePolicy.setHeightForWidth(self.base_group_btns_row2.sizePolicy().hasHeightForWidth())
        self.base_group_btns_row2.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.base_group_btns_row2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.one_handed_weapons_btn = QPushButton(self.base_group_btns_row2)
        self.wizard_base_group_btns.addButton(self.one_handed_weapons_btn)
        self.one_handed_weapons_btn.setObjectName(u"one_handed_weapons_btn")
        sizePolicy.setHeightForWidth(self.one_handed_weapons_btn.sizePolicy().hasHeightForWidth())
        self.one_handed_weapons_btn.setSizePolicy(sizePolicy)
        self.one_handed_weapons_btn.setStyleSheet(u"QPushButton {\n"
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
        self.one_handed_weapons_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.one_handed_weapons_btn)

        self.two_handed_weapons_btn = QPushButton(self.base_group_btns_row2)
        self.wizard_base_group_btns.addButton(self.two_handed_weapons_btn)
        self.two_handed_weapons_btn.setObjectName(u"two_handed_weapons_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.two_handed_weapons_btn.sizePolicy().hasHeightForWidth())
        self.two_handed_weapons_btn.setSizePolicy(sizePolicy4)
        self.two_handed_weapons_btn.setStyleSheet(u"QPushButton {\n"
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
        self.two_handed_weapons_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.two_handed_weapons_btn)

        self.offhands_btn = QPushButton(self.base_group_btns_row2)
        self.wizard_base_group_btns.addButton(self.offhands_btn)
        self.offhands_btn.setObjectName(u"offhands_btn")
        sizePolicy4.setHeightForWidth(self.offhands_btn.sizePolicy().hasHeightForWidth())
        self.offhands_btn.setSizePolicy(sizePolicy4)
        self.offhands_btn.setStyleSheet(u"QPushButton {\n"
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
        self.offhands_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.offhands_btn)


        self.verticalLayout_5.addWidget(self.base_group_btns_row2, 0, Qt.AlignHCenter)

        self.base_group_btns_row3 = QWidget(self.base_group_btns)
        self.base_group_btns_row3.setObjectName(u"base_group_btns_row3")
        sizePolicy.setHeightForWidth(self.base_group_btns_row3.sizePolicy().hasHeightForWidth())
        self.base_group_btns_row3.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.base_group_btns_row3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.jewellery_btn = QPushButton(self.base_group_btns_row3)
        self.wizard_base_group_btns.addButton(self.jewellery_btn)
        self.jewellery_btn.setObjectName(u"jewellery_btn")
        sizePolicy.setHeightForWidth(self.jewellery_btn.sizePolicy().hasHeightForWidth())
        self.jewellery_btn.setSizePolicy(sizePolicy)
        self.jewellery_btn.setStyleSheet(u"QPushButton {\n"
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
        self.jewellery_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.jewellery_btn)

        self.jewels_btn = QPushButton(self.base_group_btns_row3)
        self.wizard_base_group_btns.addButton(self.jewels_btn)
        self.jewels_btn.setObjectName(u"jewels_btn")
        sizePolicy.setHeightForWidth(self.jewels_btn.sizePolicy().hasHeightForWidth())
        self.jewels_btn.setSizePolicy(sizePolicy)
        self.jewels_btn.setStyleSheet(u"QPushButton {\n"
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
        self.jewels_btn.setCheckable(True)
        self.jewels_btn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.jewels_btn)

        self.cluster_jewels_btn = QPushButton(self.base_group_btns_row3)
        self.wizard_base_group_btns.addButton(self.cluster_jewels_btn)
        self.cluster_jewels_btn.setObjectName(u"cluster_jewels_btn")
        sizePolicy.setHeightForWidth(self.cluster_jewels_btn.sizePolicy().hasHeightForWidth())
        self.cluster_jewels_btn.setSizePolicy(sizePolicy)
        self.cluster_jewels_btn.setStyleSheet(u"QPushButton {\n"
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
        self.cluster_jewels_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.cluster_jewels_btn)

        self.flasks_btn = QPushButton(self.base_group_btns_row3)
        self.wizard_base_group_btns.addButton(self.flasks_btn)
        self.flasks_btn.setObjectName(u"flasks_btn")
        sizePolicy.setHeightForWidth(self.flasks_btn.sizePolicy().hasHeightForWidth())
        self.flasks_btn.setSizePolicy(sizePolicy)
        self.flasks_btn.setStyleSheet(u"QPushButton {\n"
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
        self.flasks_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.flasks_btn)


        self.verticalLayout_5.addWidget(self.base_group_btns_row3)


        self.verticalLayout_4.addWidget(self.base_group_btns, 0, Qt.AlignHCenter)

        ItemOptionsWizard.setPage(1, self.wizard_base_groups_page)
        self.wizard_base_selection_page = QWizardPage()
        self.wizard_base_selection_page.setObjectName(u"wizard_base_selection_page")
        self.verticalLayout_6 = QVBoxLayout(self.wizard_base_selection_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.base_selection_page = BaseSelection(self.wizard_base_selection_page)
        self.base_selection_page.setObjectName(u"base_selection_page")

        self.verticalLayout_6.addWidget(self.base_selection_page)

        ItemOptionsWizard.setPage(2, self.wizard_base_selection_page)
        self.wizard_item_selection_page = QWizardPage()
        self.wizard_item_selection_page.setObjectName(u"wizard_item_selection_page")
        self.verticalLayout_7 = QVBoxLayout(self.wizard_item_selection_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.item_selection_page = ItemSelection(self.wizard_item_selection_page)
        self.item_selection_page.setObjectName(u"item_selection_page")

        self.verticalLayout_7.addWidget(self.item_selection_page)

        ItemOptionsWizard.setPage(3, self.wizard_item_selection_page)
        self.wizard_item_options_page = QWizardPage()
        self.wizard_item_options_page.setObjectName(u"wizard_item_options_page")
        ItemOptionsWizard.setPage(4, self.wizard_item_options_page)
        self.wizard_confirm_options_page = QWizardPage()
        self.wizard_confirm_options_page.setObjectName(u"wizard_confirm_options_page")
        ItemOptionsWizard.setPage(5, self.wizard_confirm_options_page)
#if QT_CONFIG(shortcut)
        self.project_name_label.setBuddy(self.project_name_input)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ItemOptionsWizard)

        QMetaObject.connectSlotsByName(ItemOptionsWizard)
    # setupUi

    def retranslateUi(self, ItemOptionsWizard):
        ItemOptionsWizard.setWindowTitle(QCoreApplication.translate("ItemOptionsWizard", u"Item Options", None))
        self.wizard_start_page.setTitle(QCoreApplication.translate("ItemOptionsWizard", u"Start a Crafting Project", None))
        self.wizard_start_page.setSubTitle(QCoreApplication.translate("ItemOptionsWizard", u"Start a new crafting project with the name of your choice", None))
        self.project_name_label.setText(QCoreApplication.translate("ItemOptionsWizard", u"Project Name:", None))
        self.project_name_input.setPlaceholderText(QCoreApplication.translate("ItemOptionsWizard", u"Type name of the project here", None))
        self.wizard_base_groups_page.setTitle(QCoreApplication.translate("ItemOptionsWizard", u"Select A Base Group", None))
        self.body_armours_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Body Armours", None))
        self.boots_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Boots", None))
        self.helmets_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Helmets", None))
        self.gloves_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Gloves", None))
        self.one_handed_weapons_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"One Handed Weapons", None))
        self.two_handed_weapons_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Two Handed Weapons", None))
        self.offhands_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Offhands", None))
        self.jewellery_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Jewellery", None))
        self.jewels_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Jewels", None))
        self.cluster_jewels_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Cluster Jewels", None))
        self.flasks_btn.setText(QCoreApplication.translate("ItemOptionsWizard", u"Flasks", None))
    # retranslateUi

