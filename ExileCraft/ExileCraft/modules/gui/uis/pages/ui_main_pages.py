# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesePzyFt.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
                               QHBoxLayout, QHeaderView, QLabel, QLayout,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTreeView, QVBoxLayout, QWidget)
from ...assets import assets_rc


class Ui_MainPages(object):
        def setupUi(self, MainPages):
                if not MainPages.objectName():
                        MainPages.setObjectName(u"MainPages")
                MainPages.resize(602, 527)
                MainPages.setMinimumSize(QSize(602, 527))
                MainPages.setStyleSheet(u"QWidget{\n"
                                        "                border-image: url(:/images/images/emubg.png);\n"
                                        "                }\n"
                                        "\n"
                                        "            ")
        self.main_pages_layout = QVBoxLayout(MainPages)
                self.main_pages_layout.setSpacing(0)
                self.main_pages_layout.setObjectName(u"main_pages_layout")
                self.main_pages_layout.setContentsMargins(0, 0, 0, 0)
                self.pages = QStackedWidget(MainPages)
                self.pages.setObjectName(u"pages")
                self.pages.setMinimumSize(QSize(602, 527))
                self.page_1 = QWidget()
                self.page_1.setObjectName(u"page_1")
                self.page_1.setMinimumSize(QSize(592, 517))
                self.page_1.setStyleSheet(u"font-size: 14pt")
                self.verticalLayout_12 = QVBoxLayout(self.page_1)
                self.verticalLayout_12.setSpacing(6)
                self.verticalLayout_12.setObjectName(u"verticalLayout_12")
                self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
                self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_12.addItem(self.verticalSpacer)

                self.crafting_zone_container = QFrame(self.page_1)
                self.crafting_zone_container.setObjectName(u"crafting_zone_container")
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.crafting_zone_container.sizePolicy().hasHeightForWidth())
                self.crafting_zone_container.setSizePolicy(sizePolicy)
                self.crafting_zone_container.setStyleSheet(u"QWidget {\n"
                                                           "                                            border-image: none;\n"
                                                           "                                            }\n"
                                                           "                                        ")
                self.horizontalLayout_3 = QHBoxLayout(self.crafting_zone_container)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

                self.item_info_container = QWidget(self.crafting_zone_container)
                self.item_info_container.setObjectName(u"item_info_container")
                sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(self.item_info_container.sizePolicy().hasHeightForWidth())
                self.item_info_container.setSizePolicy(sizePolicy1)
                self.item_info_container.setMinimumSize(QSize(400, 0))
                self.item_info_container.setMaximumSize(QSize(400, 16777215))
                self.item_info_container.setStyleSheet(u"background-color: black;")
                self.verticalLayout_4 = QVBoxLayout(self.item_info_container)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.item_info_frame = QFrame(self.item_info_container)
                self.item_info_frame.setObjectName(u"item_info_frame")
                sizePolicy1.setHeightForWidth(self.item_info_frame.sizePolicy().hasHeightForWidth())
                self.item_info_frame.setSizePolicy(sizePolicy1)
                self.item_info_frame.setMinimumSize(QSize(400, 0))
                self.item_info_frame.setMaximumSize(QSize(400, 16777215))
                self.item_info_layout = QVBoxLayout(self.item_info_frame)
                self.item_info_layout.setSpacing(0)
                self.item_info_layout.setObjectName(u"item_info_layout")
                self.item_info_layout.setContentsMargins(0, 0, 0, 0)
                self.item_header_frame = QFrame(self.item_info_frame)
                self.item_header_frame.setObjectName(u"item_header_frame")
                sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.item_header_frame.sizePolicy().hasHeightForWidth())
                self.item_header_frame.setSizePolicy(sizePolicy2)
                self.item_header_layout = QVBoxLayout(self.item_header_frame)
                self.item_header_layout.setSpacing(0)
                self.item_header_layout.setObjectName(u"item_header_layout")
                self.item_header_layout.setContentsMargins(0, 0, 0, 0)
                self.item_header_label = QLabel(self.item_header_frame)
                self.item_header_label.setObjectName(u"item_header_label")
                self.item_header_label.setEnabled(True)
                sizePolicy2.setHeightForWidth(self.item_header_label.sizePolicy().hasHeightForWidth())
                self.item_header_label.setSizePolicy(sizePolicy2)
                self.item_header_label.setMinimumSize(QSize(400, 54))
                self.item_header_label.setMaximumSize(QSize(400, 54))
                font = QFont()
                font.setFamilies([u"Open Sans"])
                font.setPointSize(14)
                font.setBold(False)
                font.setItalic(False)
                font.setKerning(True)
                self.item_header_label.setFont(font)
                self.item_header_label.setStyleSheet(u"QLabel {\n"
                                                     "                                                                                background-image:\n"
                                                     "                                                                                url(:/images/images/item-header-normal.png);\n"
                                                     "                                                                                }\n"
                                                     "                                                                            ")
                self.item_header_label.setTextFormat(Qt.RichText)
                self.item_header_label.setScaledContents(False)
                self.item_header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                self.item_header_label.setWordWrap(True)

                self.item_header_layout.addWidget(self.item_header_label, 0, Qt.AlignHCenter | Qt.AlignTop)

                self.item_info_layout.addWidget(self.item_header_frame, 0, Qt.AlignTop)

                self.item_affix_frame = QFrame(self.item_info_frame)
                self.item_affix_frame.setObjectName(u"item_affix_frame")
                sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                sizePolicy3.setHorizontalStretch(0)
                sizePolicy3.setVerticalStretch(0)
                sizePolicy3.setHeightForWidth(self.item_affix_frame.sizePolicy().hasHeightForWidth())
                self.item_affix_frame.setSizePolicy(sizePolicy3)
                self.item_affix_frame.setMinimumSize(QSize(400, 0))
                self.item_affix_frame.setMaximumSize(QSize(400, 16777215))
                self.item_properties_layout = QVBoxLayout(self.item_affix_frame)
                self.item_properties_layout.setSpacing(0)
                self.item_properties_layout.setObjectName(u"item_properties_layout")
                self.item_properties_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
                self.item_properties_layout.setContentsMargins(0, 0, 0, 0)
                self.item_properties_container = QWidget(self.item_affix_frame)
                self.item_properties_container.setObjectName(u"item_properties_container")
                sizePolicy3.setHeightForWidth(self.item_properties_container.sizePolicy().hasHeightForWidth())
                self.item_properties_container.setSizePolicy(sizePolicy3)
                self.item_properties_container.setMinimumSize(QSize(400, 0))
                self.item_properties_container.setMaximumSize(QSize(400, 16777215))
                self.verticalLayout_11 = QVBoxLayout(self.item_properties_container)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName(u"verticalLayout_11")
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.item_quality_label = QLabel(self.item_properties_container)
                self.item_quality_label.setObjectName(u"item_quality_label")
                sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
                sizePolicy4.setHorizontalStretch(0)
                sizePolicy4.setVerticalStretch(0)
                sizePolicy4.setHeightForWidth(self.item_quality_label.sizePolicy().hasHeightForWidth())
                self.item_quality_label.setSizePolicy(sizePolicy4)
                self.item_quality_label.setMinimumSize(QSize(400, 0))
                self.item_quality_label.setMaximumSize(QSize(400, 30))
                self.item_quality_label.setAlignment(Qt.AlignCenter)
                self.item_quality_label.setIndent(0)

                self.verticalLayout_11.addWidget(self.item_quality_label)

                self.item_properties_label = QLabel(self.item_properties_container)
                self.item_properties_label.setObjectName(u"item_properties_label")
                sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
                sizePolicy5.setHorizontalStretch(0)
                sizePolicy5.setVerticalStretch(0)
                sizePolicy5.setHeightForWidth(self.item_properties_label.sizePolicy().hasHeightForWidth())
                self.item_properties_label.setSizePolicy(sizePolicy5)
                self.item_properties_label.setMinimumSize(QSize(400, 0))
                self.item_properties_label.setMaximumSize(QSize(400, 400))
                self.item_properties_label.setStyleSheet(u"QLabel{\n"
                                                         "                                                                                color: #827a6c;\n"
                                                         "                                                                                font-size: 14px;\n"
                                                         "																				padding: 2px 10px;\n"
                                                         "                                                                                text-align: center;\n"
                                                         "                                                                                margin-bottom: 5px ;\n"
                                                         "                                                                                }\n"
                                                         "                                                                            ")
                self.item_properties_label.setLineWidth(1)
                self.item_properties_label.setTextFormat(Qt.RichText)
                self.item_properties_label.setScaledContents(True)
                self.item_properties_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                self.item_properties_label.setMargin(0)
                self.item_properties_label.setIndent(0)

                self.verticalLayout_11.addWidget(self.item_properties_label, 0, Qt.AlignTop)

                self.item_spacer_1 = QLabel(self.item_properties_container)
                self.item_spacer_1.setObjectName(u"item_spacer_1")
                sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
                sizePolicy6.setHorizontalStretch(0)
                sizePolicy6.setVerticalStretch(0)
                sizePolicy6.setHeightForWidth(self.item_spacer_1.sizePolicy().hasHeightForWidth())
                self.item_spacer_1.setSizePolicy(sizePolicy6)
                self.item_spacer_1.setMinimumSize(QSize(400, 0))
                self.item_spacer_1.setMaximumSize(QSize(400, 2))
                self.item_spacer_1.setBaseSize(QSize(0, 0))
                self.item_spacer_1.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                border-image: none;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.item_spacer_1.setTextFormat(Qt.RichText)
                self.item_spacer_1.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_1.setScaledContents(False)
                self.item_spacer_1.setAlignment(Qt.AlignCenter)

                self.verticalLayout_11.addWidget(self.item_spacer_1)

                self.item_properties_layout.addWidget(self.item_properties_container, 0, Qt.AlignVCenter)

                self.item_requirements_container = QWidget(self.item_affix_frame)
                self.item_requirements_container.setObjectName(u"item_requirements_container")
                sizePolicy2.setHeightForWidth(self.item_requirements_container.sizePolicy().hasHeightForWidth())
                self.item_requirements_container.setSizePolicy(sizePolicy2)
                self.item_requirements_container.setMinimumSize(QSize(400, 0))
                self.item_requirements_container.setMaximumSize(QSize(400, 52))
                self.verticalLayout_13 = QVBoxLayout(self.item_requirements_container)
                self.verticalLayout_13.setSpacing(0)
                self.verticalLayout_13.setObjectName(u"verticalLayout_13")
                self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
                self.item_level_label = QLabel(self.item_requirements_container)
                self.item_level_label.setObjectName(u"item_level_label")
                sizePolicy2.setHeightForWidth(self.item_level_label.sizePolicy().hasHeightForWidth())
                self.item_level_label.setSizePolicy(sizePolicy2)
                self.item_level_label.setMinimumSize(QSize(400, 0))
                self.item_level_label.setMaximumSize(QSize(400, 20))
                self.item_level_label.setTabletTracking(False)
                self.item_level_label.setAlignment(Qt.AlignCenter)
                self.item_level_label.setIndent(0)

                self.verticalLayout_13.addWidget(self.item_level_label)

                self.item_requirements_label = QLabel(self.item_requirements_container)
                self.item_requirements_label.setObjectName(u"item_requirements_label")
                sizePolicy2.setHeightForWidth(self.item_requirements_label.sizePolicy().hasHeightForWidth())
                self.item_requirements_label.setSizePolicy(sizePolicy2)
                self.item_requirements_label.setMinimumSize(QSize(400, 0))
                self.item_requirements_label.setMaximumSize(QSize(400, 25))
                self.item_requirements_label.setStyleSheet(u"QLabel{\n"
                                                           "                                                                                color: #827a6c;\n"
                                                           "                                                                                padding: 2px 10px;\n"
                                                           "                                                                                font-size: 14px;\n"
                                                           "                                                                                line-height: 14px;\n"
                                                           "                                                                                text-align: center;\n"
                                                           "                                                                                margin: 0;\n"
                                                           "                                                                                }\n"
                                                           "                                                                            ")
                self.item_requirements_label.setLineWidth(0)
                self.item_requirements_label.setMidLineWidth(0)
                self.item_requirements_label.setTextFormat(Qt.RichText)
                self.item_requirements_label.setScaledContents(False)
                self.item_requirements_label.setAlignment(Qt.AlignCenter)
                self.item_requirements_label.setIndent(0)

                self.verticalLayout_13.addWidget(self.item_requirements_label)

                self.item_spacer_2 = QLabel(self.item_requirements_container)
                self.item_spacer_2.setObjectName(u"item_spacer_2")
                sizePolicy6.setHeightForWidth(self.item_spacer_2.sizePolicy().hasHeightForWidth())
                self.item_spacer_2.setSizePolicy(sizePolicy6)
                self.item_spacer_2.setMinimumSize(QSize(400, 0))
                self.item_spacer_2.setMaximumSize(QSize(400, 2))
                self.item_spacer_2.setBaseSize(QSize(0, 0))
                self.item_spacer_2.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                border-image: none;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.item_spacer_2.setTextFormat(Qt.RichText)
                self.item_spacer_2.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_2.setScaledContents(False)
                self.item_spacer_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_13.addWidget(self.item_spacer_2, 0, Qt.AlignBottom)

                self.item_properties_layout.addWidget(self.item_requirements_container, 0, Qt.AlignVCenter)

                self.item_implicits_container = QWidget(self.item_affix_frame)
                self.item_implicits_container.setObjectName(u"item_implicits_container")
                self.item_implicits_container.setEnabled(False)
                sizePolicy3.setHeightForWidth(self.item_implicits_container.sizePolicy().hasHeightForWidth())
                self.item_implicits_container.setSizePolicy(sizePolicy3)
                self.item_implicits_container.setMinimumSize(QSize(400, 0))
                self.item_implicits_container.setMaximumSize(QSize(400, 50))
                self.verticalLayout_18 = QVBoxLayout(self.item_implicits_container)
                self.verticalLayout_18.setSpacing(0)
                self.verticalLayout_18.setObjectName(u"verticalLayout_18")
                self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
                self.item_implicits_label = QLabel(self.item_implicits_container)
                self.item_implicits_label.setObjectName(u"item_implicits_label")
                self.item_implicits_label.setEnabled(False)
                sizePolicy3.setHeightForWidth(self.item_implicits_label.sizePolicy().hasHeightForWidth())
                self.item_implicits_label.setSizePolicy(sizePolicy3)
                self.item_implicits_label.setMinimumSize(QSize(400, 0))
                self.item_implicits_label.setMaximumSize(QSize(400, 50))
                self.item_implicits_label.setStyleSheet(u"QLabel{\n"
                                                        "                                                                                color: #8787fe;\n"
                                                        "                                                                                padding: 2px 10px;\n"
                                                        "                                                                                font-size: 14px;\n"
                                                        "                                                                                line-height: 14px;\n"
                                                        "                                                                                text-align: center;\n"
                                                        "                                                                                margin: 0;\n"
                                                        "                                                                                }\n"
                                                        "                                                                            ")
                self.item_implicits_label.setLineWidth(1)
                self.item_implicits_label.setTextFormat(Qt.RichText)
                self.item_implicits_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                self.item_implicits_label.setWordWrap(True)

                self.verticalLayout_18.addWidget(self.item_implicits_label)

                self.item_properties_layout.addWidget(self.item_implicits_container, 0,
                                                      Qt.AlignHCenter | Qt.AlignVCenter)

                self.item_spacer_3 = QLabel(self.item_affix_frame)
                self.item_spacer_3.setObjectName(u"item_spacer_3")
                self.item_spacer_3.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.item_spacer_3.sizePolicy().hasHeightForWidth())
                self.item_spacer_3.setSizePolicy(sizePolicy6)
                self.item_spacer_3.setMinimumSize(QSize(400, 0))
                self.item_spacer_3.setMaximumSize(QSize(400, 2))
                self.item_spacer_3.setBaseSize(QSize(0, 0))
                self.item_spacer_3.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                border-image: none;\n"
                                                 "																				background-color: rgb(0, 0, 0);\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.item_spacer_3.setTextFormat(Qt.RichText)
                self.item_spacer_3.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_3.setScaledContents(False)
                self.item_spacer_3.setAlignment(Qt.AlignCenter)

                self.item_properties_layout.addWidget(self.item_spacer_3)

                self.item_info_layout.addWidget(self.item_affix_frame, 0, Qt.AlignTop)

                self.item_mod_frame = QFrame(self.item_info_frame)
                self.item_mod_frame.setObjectName(u"item_mod_frame")
                sizePolicy3.setHeightForWidth(self.item_mod_frame.sizePolicy().hasHeightForWidth())
                self.item_mod_frame.setSizePolicy(sizePolicy3)
                self.item_mod_frame.setMinimumSize(QSize(400, 0))
                self.item_mod_frame.setMaximumSize(QSize(400, 16777215))
                self.item_mod_layout = QVBoxLayout(self.item_mod_frame)
                self.item_mod_layout.setSpacing(0)
                self.item_mod_layout.setObjectName(u"item_mod_layout")
                self.item_mod_layout.setSizeConstraint(QLayout.SetNoConstraint)
                self.item_mod_layout.setContentsMargins(0, 0, 0, 0)
                self.prefix_1_container = QWidget(self.item_mod_frame)
                self.prefix_1_container.setObjectName(u"prefix_1_container")
                sizePolicy3.setHeightForWidth(self.prefix_1_container.sizePolicy().hasHeightForWidth())
                self.prefix_1_container.setSizePolicy(sizePolicy3)
                self.prefix_1_container.setMinimumSize(QSize(400, 0))
                self.prefix_1_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_5 = QVBoxLayout(self.prefix_1_container)
                self.verticalLayout_5.setSpacing(0)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.prefix_info_1 = QLabel(self.prefix_1_container)
                self.prefix_info_1.setObjectName(u"prefix_info_1")
                self.prefix_info_1.setEnabled(False)
                sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
                sizePolicy7.setHorizontalStretch(0)
                sizePolicy7.setVerticalStretch(0)
                sizePolicy7.setHeightForWidth(self.prefix_info_1.sizePolicy().hasHeightForWidth())
                self.prefix_info_1.setSizePolicy(sizePolicy7)
                self.prefix_info_1.setMinimumSize(QSize(0, 0))
                font1 = QFont()
                font1.setFamilies([u"Open Sans"])
                font1.setBold(False)
                font1.setItalic(False)
                self.prefix_info_1.setFont(font1)
                self.prefix_info_1.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.prefix_info_1.setTextFormat(Qt.RichText)
                self.prefix_info_1.setAlignment(Qt.AlignCenter)

                self.verticalLayout_5.addWidget(self.prefix_info_1, 0, Qt.AlignTop)

                self.prefix_1 = QLabel(self.prefix_1_container)
                self.prefix_1.setObjectName(u"prefix_1")
                self.prefix_1.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.prefix_1.sizePolicy().hasHeightForWidth())
                self.prefix_1.setSizePolicy(sizePolicy6)
                self.prefix_1.setMinimumSize(QSize(400, 0))
                self.prefix_1.setMaximumSize(QSize(400, 16777215))
                self.prefix_1.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.prefix_1.setTextFormat(Qt.RichText)
                self.prefix_1.setAlignment(Qt.AlignCenter)

                self.verticalLayout_5.addWidget(self.prefix_1, 0, Qt.AlignTop)

                self.item_mod_layout.addWidget(self.prefix_1_container)

                self.prefix_2_container = QWidget(self.item_mod_frame)
                self.prefix_2_container.setObjectName(u"prefix_2_container")
                sizePolicy3.setHeightForWidth(self.prefix_2_container.sizePolicy().hasHeightForWidth())
                self.prefix_2_container.setSizePolicy(sizePolicy3)
                self.prefix_2_container.setMinimumSize(QSize(400, 0))
                self.prefix_2_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_6 = QVBoxLayout(self.prefix_2_container)
                self.verticalLayout_6.setSpacing(0)
                self.verticalLayout_6.setObjectName(u"verticalLayout_6")
                self.verticalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.prefix_info_2 = QLabel(self.prefix_2_container)
                self.prefix_info_2.setObjectName(u"prefix_info_2")
                self.prefix_info_2.setEnabled(False)
                sizePolicy7.setHeightForWidth(self.prefix_info_2.sizePolicy().hasHeightForWidth())
                self.prefix_info_2.setSizePolicy(sizePolicy7)
                self.prefix_info_2.setMinimumSize(QSize(0, 0))
                self.prefix_info_2.setFont(font1)
                self.prefix_info_2.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.prefix_info_2.setTextFormat(Qt.RichText)
                self.prefix_info_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_6.addWidget(self.prefix_info_2, 0, Qt.AlignTop)

                self.prefix_2 = QLabel(self.prefix_2_container)
                self.prefix_2.setObjectName(u"prefix_2")
                self.prefix_2.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.prefix_2.sizePolicy().hasHeightForWidth())
                self.prefix_2.setSizePolicy(sizePolicy6)
                self.prefix_2.setMinimumSize(QSize(0, 0))
                self.prefix_2.setMaximumSize(QSize(400, 16777215))
                self.prefix_2.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.prefix_2.setTextFormat(Qt.RichText)
                self.prefix_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_6.addWidget(self.prefix_2)

                self.item_mod_layout.addWidget(self.prefix_2_container, 0, Qt.AlignTop)

                self.prefix_3_container = QWidget(self.item_mod_frame)
                self.prefix_3_container.setObjectName(u"prefix_3_container")
                sizePolicy3.setHeightForWidth(self.prefix_3_container.sizePolicy().hasHeightForWidth())
                self.prefix_3_container.setSizePolicy(sizePolicy3)
                self.prefix_3_container.setMinimumSize(QSize(400, 0))
                self.prefix_3_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_7 = QVBoxLayout(self.prefix_3_container)
                self.verticalLayout_7.setSpacing(0)
                self.verticalLayout_7.setObjectName(u"verticalLayout_7")
                self.verticalLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.prefix_info_3 = QLabel(self.prefix_3_container)
                self.prefix_info_3.setObjectName(u"prefix_info_3")
                self.prefix_info_3.setEnabled(False)
                sizePolicy7.setHeightForWidth(self.prefix_info_3.sizePolicy().hasHeightForWidth())
                self.prefix_info_3.setSizePolicy(sizePolicy7)
                self.prefix_info_3.setMinimumSize(QSize(0, 0))
                self.prefix_info_3.setFont(font1)
                self.prefix_info_3.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.prefix_info_3.setTextFormat(Qt.RichText)
                self.prefix_info_3.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.prefix_info_3)

                self.prefix_3 = QLabel(self.prefix_3_container)
                self.prefix_3.setObjectName(u"prefix_3")
                self.prefix_3.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.prefix_3.sizePolicy().hasHeightForWidth())
                self.prefix_3.setSizePolicy(sizePolicy6)
                self.prefix_3.setMinimumSize(QSize(0, 0))
                self.prefix_3.setMaximumSize(QSize(400, 16777215))
                self.prefix_3.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.prefix_3.setTextFormat(Qt.RichText)
                self.prefix_3.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.prefix_3)

                self.item_mod_layout.addWidget(self.prefix_3_container)

                self.suffix_2_container = QWidget(self.item_mod_frame)
                self.suffix_2_container.setObjectName(u"suffix_2_container")
                sizePolicy3.setHeightForWidth(self.suffix_2_container.sizePolicy().hasHeightForWidth())
                self.suffix_2_container.setSizePolicy(sizePolicy3)
                self.suffix_2_container.setMinimumSize(QSize(400, 0))
                self.suffix_2_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_8 = QVBoxLayout(self.suffix_2_container)
                self.verticalLayout_8.setSpacing(0)
                self.verticalLayout_8.setObjectName(u"verticalLayout_8")
                self.verticalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.suffix_2_info = QLabel(self.suffix_2_container)
                self.suffix_2_info.setObjectName(u"suffix_2_info")
                self.suffix_2_info.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_2_info.sizePolicy().hasHeightForWidth())
                self.suffix_2_info.setSizePolicy(sizePolicy6)
                self.suffix_2_info.setMinimumSize(QSize(400, 0))
                self.suffix_2_info.setMaximumSize(QSize(400, 16777215))
                self.suffix_2_info.setFont(font1)
                self.suffix_2_info.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.suffix_2_info.setTextFormat(Qt.RichText)
                self.suffix_2_info.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.suffix_2_info)

                self.suffix_2 = QLabel(self.suffix_2_container)
                self.suffix_2.setObjectName(u"suffix_2")
                self.suffix_2.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_2.sizePolicy().hasHeightForWidth())
                self.suffix_2.setSizePolicy(sizePolicy6)
                self.suffix_2.setMinimumSize(QSize(400, 0))
                self.suffix_2.setMaximumSize(QSize(400, 16777215))
                self.suffix_2.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.suffix_2.setTextFormat(Qt.RichText)
                self.suffix_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.suffix_2)

                self.item_mod_layout.addWidget(self.suffix_2_container)

                self.suffix_1_container = QWidget(self.item_mod_frame)
                self.suffix_1_container.setObjectName(u"suffix_1_container")
                sizePolicy3.setHeightForWidth(self.suffix_1_container.sizePolicy().hasHeightForWidth())
                self.suffix_1_container.setSizePolicy(sizePolicy3)
                self.suffix_1_container.setMinimumSize(QSize(400, 0))
                self.suffix_1_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_9 = QVBoxLayout(self.suffix_1_container)
                self.verticalLayout_9.setSpacing(0)
                self.verticalLayout_9.setObjectName(u"verticalLayout_9")
                self.verticalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
                self.suffix_1_info = QLabel(self.suffix_1_container)
                self.suffix_1_info.setObjectName(u"suffix_1_info")
                self.suffix_1_info.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_1_info.sizePolicy().hasHeightForWidth())
                self.suffix_1_info.setSizePolicy(sizePolicy6)
                self.suffix_1_info.setMinimumSize(QSize(400, 0))
                self.suffix_1_info.setMaximumSize(QSize(400, 16777215))
                self.suffix_1_info.setFont(font1)
                self.suffix_1_info.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.suffix_1_info.setTextFormat(Qt.RichText)
                self.suffix_1_info.setAlignment(Qt.AlignCenter)

                self.verticalLayout_9.addWidget(self.suffix_1_info)

                self.suffix_1 = QLabel(self.suffix_1_container)
                self.suffix_1.setObjectName(u"suffix_1")
                self.suffix_1.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_1.sizePolicy().hasHeightForWidth())
                self.suffix_1.setSizePolicy(sizePolicy6)
                self.suffix_1.setMinimumSize(QSize(400, 0))
                self.suffix_1.setMaximumSize(QSize(400, 16777215))
                self.suffix_1.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.suffix_1.setTextFormat(Qt.RichText)
                self.suffix_1.setAlignment(Qt.AlignCenter)

                self.verticalLayout_9.addWidget(self.suffix_1)

                self.item_mod_layout.addWidget(self.suffix_1_container)

                self.suffix_3_container = QWidget(self.item_mod_frame)
                self.suffix_3_container.setObjectName(u"suffix_3_container")
                sizePolicy3.setHeightForWidth(self.suffix_3_container.sizePolicy().hasHeightForWidth())
                self.suffix_3_container.setSizePolicy(sizePolicy3)
                self.suffix_3_container.setMinimumSize(QSize(400, 0))
                self.suffix_3_container.setMaximumSize(QSize(400, 80))
                self.verticalLayout_10 = QVBoxLayout(self.suffix_3_container)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName(u"verticalLayout_10")
                self.verticalLayout_10.setSizeConstraint(QLayout.SetNoConstraint)
                self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.suffix_3_info = QLabel(self.suffix_3_container)
                self.suffix_3_info.setObjectName(u"suffix_3_info")
                self.suffix_3_info.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_3_info.sizePolicy().hasHeightForWidth())
                self.suffix_3_info.setSizePolicy(sizePolicy6)
                self.suffix_3_info.setMinimumSize(QSize(400, 0))
                self.suffix_3_info.setMaximumSize(QSize(400, 16777215))
                self.suffix_3_info.setFont(font1)
                self.suffix_3_info.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                color: #7f7f7f;\n"
                                                 "                                                                                text-transform: none;\n"
                                                 "                                                                                font-size: 12px;\n"
                                                 "                                                                                padding-bottom: 0px;\n"
                                                 "                                                                                padding-top: 2px;\n"
                                                 "                                                                                padding-right: 10px;\n"
                                                 "                                                                                padding-left: 10px;\n"
                                                 "                                                                                line-height: 14px;\n"
                                                 "                                                                                text-align: center;\n"
                                                 "                                                                                ma"
                                                 "rgin: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")
                self.suffix_3_info.setTextFormat(Qt.RichText)
                self.suffix_3_info.setAlignment(Qt.AlignCenter)

                self.verticalLayout_10.addWidget(self.suffix_3_info)

                self.suffix_3 = QLabel(self.suffix_3_container)
                self.suffix_3.setObjectName(u"suffix_3")
                self.suffix_3.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.suffix_3.sizePolicy().hasHeightForWidth())
                self.suffix_3.setSizePolicy(sizePolicy6)
                self.suffix_3.setMinimumSize(QSize(400, 0))
                self.suffix_3.setMaximumSize(QSize(400, 16777215))
                self.suffix_3.setStyleSheet(u"QLabel {\n"
                                            "                                                                                color: #8787fe;\n"
                                            "                                                                                font-size: 14px;\n"
                                            "                                                                                padding-bottom: 2px;\n"
                                            "                                                                                padding-top: 2px;\n"
                                            "                                                                                padding-right: 10px;\n"
                                            "                                                                                padding-left: 10px;\n"
                                            "                                                                                line-height: 14px;\n"
                                            "                                                                                text-align: center;\n"
                                            "                                                                                margin: 0px;\n"
                                            "                                                                                }\n"
                                            "     "
                                            "                                                                       ")
                self.suffix_3.setTextFormat(Qt.RichText)
                self.suffix_3.setAlignment(Qt.AlignCenter)

                self.verticalLayout_10.addWidget(self.suffix_3)

                self.item_mod_layout.addWidget(self.suffix_3_container)

                self.item_info_layout.addWidget(self.item_mod_frame, 0, Qt.AlignTop)

                self.verticalLayout_4.addWidget(self.item_info_frame, 0, Qt.AlignHCenter)

                self.horizontalLayout_3.addWidget(self.item_info_container, 0, Qt.AlignTop)

                self.horizontalSpacer = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_3.addItem(self.horizontalSpacer)

                self.item_display_frame = QFrame(self.crafting_zone_container)
                self.item_display_frame.setObjectName(u"item_display_frame")
                sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
                sizePolicy8.setHorizontalStretch(0)
                sizePolicy8.setVerticalStretch(0)
                sizePolicy8.setHeightForWidth(self.item_display_frame.sizePolicy().hasHeightForWidth())
                self.item_display_frame.setSizePolicy(sizePolicy8)
                self.item_display_frame.setFrameShape(QFrame.StyledPanel)
                self.item_display_frame.setFrameShadow(QFrame.Raised)
                self.verticalLayout_2 = QVBoxLayout(self.item_display_frame)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.item_view_frame = QFrame(self.item_display_frame)
                self.item_view_frame.setObjectName(u"item_view_frame")
                sizePolicy.setHeightForWidth(self.item_view_frame.sizePolicy().hasHeightForWidth())
                self.item_view_frame.setSizePolicy(sizePolicy)
                self.item_view_frame.setMinimumSize(QSize(128, 269))
                self.item_view_frame.setMaximumSize(QSize(145, 269))
        self.item_view_frame.setStyleSheet(u"QWidget{\n"
                                           "                                                                    border: 0px;\n"
                                           "                                                                    background-color: none;\n"
                                           "                                                                    }\n"
                                           "                                                                ")
        self.item_view_layout = QVBoxLayout(self.item_view_frame)
        self.item_view_layout.setSpacing(0)
        self.item_view_layout.setObjectName(u"item_view_layout")
        self.item_view_layout.setContentsMargins(0, 0, 0, 0)
        self.item_img_frame = QFrame(self.item_view_frame)
        self.item_img_frame.setObjectName(u"item_img_frame")
        self.item_img_frame.setMinimumSize(QSize(0, 228))
        self.item_img_frame.setFrameShape(QFrame.StyledPanel)
        self.item_img_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.item_img_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.item_img_label = QLabel(self.item_img_frame)
        self.item_img_label.setObjectName(u"item_img_label")
        sizePolicy2.setHeightForWidth(self.item_img_label.sizePolicy().hasHeightForWidth())
        self.item_img_label.setSizePolicy(sizePolicy2)
        self.item_img_label.setMinimumSize(QSize(128, 228))
        self.item_img_label.setMaximumSize(QSize(128, 228))
        self.item_img_label.setStyleSheet(u"QLabel{\n"
                                          "                                                                                            background-image:\n"
                                          "                                                                                            url(:/images/images/item_box.png);\n"
                                          "                                                                                            opacity: 0.8;\n"
                                          "                                                                                            }\n"
                                          "                                                                                            QLabel::hover{\n"
                                          "                                                                                            background-color:#ffffff;\n"
                                          "                                                                                            opacity: 1;\n"
                                          "                                                                                            }\n"
                                          "                                                                                        ")
                self.item_img_label.setScaledContents(True)
                self.item_img_label.setAlignment(Qt.AlignCenter)

                self.verticalLayout_3.addWidget(self.item_img_label)

                self.item_view_layout.addWidget(self.item_img_frame)

                self.crafting_btn_frame = QFrame(self.item_view_frame)
                self.crafting_btn_frame.setObjectName(u"crafting_btn_frame")
                sizePolicy7.setHeightForWidth(self.crafting_btn_frame.sizePolicy().hasHeightForWidth())
                self.crafting_btn_frame.setSizePolicy(sizePolicy7)
                self.crafting_btn_frame.setFrameShape(QFrame.StyledPanel)
                self.crafting_btn_frame.setFrameShadow(QFrame.Raised)
                self.crafting_btn_layout = QVBoxLayout(self.crafting_btn_frame)
                self.crafting_btn_layout.setSpacing(0)
                self.crafting_btn_layout.setObjectName(u"crafting_btn_layout")
                self.crafting_btn_layout.setContentsMargins(0, 0, 0, 0)
                self.crafting_btn_label = QLabel(self.crafting_btn_frame)
                self.crafting_btn_label.setObjectName(u"crafting_btn_label")
                sizePolicy2.setHeightForWidth(self.crafting_btn_label.sizePolicy().hasHeightForWidth())
                self.crafting_btn_label.setSizePolicy(sizePolicy2)
        self.crafting_btn_label.setMinimumSize(QSize(0, 39))
        self.crafting_btn_label.setMaximumSize(QSize(128, 39))
        self.crafting_btn_label.setCursor(QCursor(Qt.ArrowCursor))
        self.crafting_btn_label.setFocusPolicy(Qt.StrongFocus)
        self.crafting_btn_label.setStyleSheet(u"QLabel{\n"
                                              "                                                                                            background-image:\n"
                                              "                                                                                            url(:/images/images/craftbtn.png);\n"
                                              "                                                                                            }\n"
                                              "                                                                                            QLabel::hover{\n"
                                              "                                                                                            background-image:\n"
                                              "                                                                                            url(:/images/images/craftbtnov.png);\n"
                                              "                                                                                            }\n"
                                              "                                                                                        ")
        self.crafting_btn_label.setScaledContents(True)

                self.crafting_btn_layout.addWidget(self.crafting_btn_label)

                self.item_view_layout.addWidget(self.crafting_btn_frame, 0, Qt.AlignTop)

                self.verticalLayout_2.addWidget(self.item_view_frame)

                self.item_dps_frame = QFrame(self.item_display_frame)
                self.item_dps_frame.setObjectName(u"item_dps_frame")
                sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                sizePolicy9.setHorizontalStretch(0)
                sizePolicy9.setVerticalStretch(0)
                sizePolicy9.setHeightForWidth(self.item_dps_frame.sizePolicy().hasHeightForWidth())
                self.item_dps_frame.setSizePolicy(sizePolicy9)
                self.item_dps_frame.setFrameShape(QFrame.StyledPanel)
                self.item_dps_frame.setFrameShadow(QFrame.Raised)
                self.item_dps_layout = QVBoxLayout(self.item_dps_frame)
                self.item_dps_layout.setSpacing(6)
                self.item_dps_layout.setObjectName(u"item_dps_layout")
                self.item_dps_layout.setContentsMargins(10, 10, 10, 10)
                self.phys_dps_label = QLabel(self.item_dps_frame)
                self.phys_dps_label.setObjectName(u"phys_dps_label")
                sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
                sizePolicy10.setHorizontalStretch(0)
                sizePolicy10.setVerticalStretch(0)
                sizePolicy10.setHeightForWidth(self.phys_dps_label.sizePolicy().hasHeightForWidth())
                self.phys_dps_label.setSizePolicy(sizePolicy10)
                self.phys_dps_label.setMinimumSize(QSize(0, 30))
                self.phys_dps_label.setStyleSheet(u"QLabel {\n"
                                                  "                                                                                border: 1px solid #edc57d;\n"
                                                  "                                                                                background: #000;\n"
                                                  "                                                                                padding: 2px 3px 4px 2px;\n"
                                                  "                                                                                }\n"
                                                  "                                                                            ")
                self.phys_dps_label.setFrameShape(QFrame.NoFrame)
                self.phys_dps_label.setFrameShadow(QFrame.Plain)
                self.phys_dps_label.setLineWidth(0)
                self.phys_dps_label.setMidLineWidth(0)
                self.phys_dps_label.setScaledContents(False)
                self.phys_dps_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
                self.phys_dps_label.setMargin(0)

                self.item_dps_layout.addWidget(self.phys_dps_label)

                self.ele_dps_label = QLabel(self.item_dps_frame)
                self.ele_dps_label.setObjectName(u"ele_dps_label")
                sizePolicy7.setHeightForWidth(self.ele_dps_label.sizePolicy().hasHeightForWidth())
                self.ele_dps_label.setSizePolicy(sizePolicy7)
                self.ele_dps_label.setMinimumSize(QSize(0, 30))
                self.ele_dps_label.setStyleSheet(u"QLabel {\n"
                                                 "                                                                                border: 1px solid #edc57d;\n"
                                                 "                                                                                background: #000;\n"
                                                 "                                                                                padding: 2px 3px 4px 2px;\n"
                                                 "                                                                                magin-bottom: 0px;\n"
                                                 "                                                                                }\n"
                                                 "                                                                            ")

                self.item_dps_layout.addWidget(self.ele_dps_label)

                self.total_dps_label = QLabel(self.item_dps_frame)
                self.total_dps_label.setObjectName(u"total_dps_label")
                sizePolicy7.setHeightForWidth(self.total_dps_label.sizePolicy().hasHeightForWidth())
                self.total_dps_label.setSizePolicy(sizePolicy7)
                self.total_dps_label.setMinimumSize(QSize(0, 30))
                self.total_dps_label.setStyleSheet(u"QLabel {\n"
                                                   "                                                                                border: 1px solid #edc57d;\n"
                                                   "                                                                                background: #000;\n"
                                                   "                                                                                padding: 2px 3px 4px 2px;\n"
                                                   "                                                                                magin-bottom: 0px;\n"
                                                   "                                                                                }\n"
                                                   "                                                                            ")

                self.item_dps_layout.addWidget(self.total_dps_label)

                self.affix_total_label = QLabel(self.item_dps_frame)
                self.affix_total_label.setObjectName(u"affix_total_label")
                sizePolicy7.setHeightForWidth(self.affix_total_label.sizePolicy().hasHeightForWidth())
                self.affix_total_label.setSizePolicy(sizePolicy7)
                self.affix_total_label.setMinimumSize(QSize(0, 30))
                self.affix_total_label.setStyleSheet(u"QLabel {\n"
                                                     "                                                                                border: 1px solid #edc57d;\n"
                                                     "                                                                                background: #000;\n"
                                                     "                                                                                padding: 2px 3px 4px 2px;\n"
                                                     "                                                                                magin-bottom: 0px;\n"
                                                     "                                                                                }\n"
                                                     "                                                                            ")

                self.item_dps_layout.addWidget(self.affix_total_label, 0, Qt.AlignTop)

                self.verticalLayout_2.addWidget(self.item_dps_frame, 0, Qt.AlignVCenter)

                self.horizontalLayout_3.addWidget(self.item_display_frame)

                self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

                self.verticalLayout_12.addWidget(self.crafting_zone_container)

                self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_12.addItem(self.verticalSpacer_2)

                self.pages.addWidget(self.page_1)
                self.page_2 = QWidget()
                self.page_2.setObjectName(u"page_2")
                self.page_2_layout = QVBoxLayout(self.page_2)
                self.page_2_layout.setSpacing(5)
                self.page_2_layout.setObjectName(u"page_2_layout")
                self.page_2_layout.setContentsMargins(5, 5, 5, 5)
                self.scroll_area = QScrollArea(self.page_2)
                self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
                self.contents.setObjectName(u"contents")
                self.contents.setGeometry(QRect(0, 0, 592, 673))
                self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.modpool_list = QWidget(self.contents)
        self.modpool_list.setObjectName(u"modpool_list")
        self.modpool_list.setStyleSheet(u"QWidget {\n"
                                        "                                                            border-image: none;\n"
                                        "                                                            }\n"
                                        "\n"
                                        "                                                            QStackedWidget > QWidget {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75,\n"
                                        "                                                            75, 75, 255));\n"
                                        "                                                            border-left: 1px solid;\n"
                                        "                                                            border-right: 1px solid;\n"
                                        "                                                            border-top: none;\n"
                                        "                                                            border-bottom: none;\n"
                                        "                                                            }\n"
                                        "                                "
                                        "                            QHeaderView::section {\n"
                                        "                                                            background-color: rgb(0, 0, 0);\n"
                                        "                                                            color: rgb(255, 255, 255);\n"
                                        "                                                            padding: 2px 2px 2px 10px\n"
                                        "                                                            }\n"
                                        "                                                            QHeaderView::up-arrow {\n"
                                        "                                                            image: url(:/images/assets/images/up_arrow.png);\n"
                                        "                                                            }\n"
                                        "                                                            QHeaderView::down-arrow {\n"
                                        "                                                            image: url(:/images/assets/images/down_arrow.png);\n"
                                        "                                                            }\n"
                                        "                                                            QTreeView {\n"
                                        "             "
                                        "                                               background-color: rgb(51, 51, 51);\n"
                                        "                                                            alternate-background-color: rgb(99, 99, 99);\n"
                                        "                                                            border-left: 1px solid;\n"
                                        "                                                            border-right: 1px solid;\n"
                                        "                                                            border-top: none;\n"
                                        "                                                            border-bottom: none;\n"
                                        "                                                            color: rgb(255, 255, 255);\n"
                                        "                                                            show-decoration-selected: 1;\n"
                                        "                                                            }\n"
                                        "\n"
                                        "                                                            QPushButton{\n"
                                        "                                                            color: white;\n"
                                        "                                                            margin: 0px;\n"
                                        ""
                                        "                                                            border: 2px groove;\n"
                                        "                                                            font-family: Segoe Ui;\n"
                                        "                                                            text-shadow: 1px 1px #000;\n"
                                        "                                                            padding: 5px 5px 5px 5px;\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton::hover {\n"
                                        "                                                            border: 2px outset;\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton::pressed {\n"
                                        "                                                            border: 2px inset;\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton::checked {\n"
                                        "                                                 "
                                        "           border: 2px solid;\n"
                                        "                                                            }\n"
                                        "\n"
                                        "                                                            QPushButton#prefix_btn {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0.5, y1:0,\n"
                                        "                                                            x2:0.5, y2:1, stop:0 rgba(112, 91, 124, 255), stop:1\n"
                                        "                                                            rgba(112, 91, 124, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#prefix_btn::hover {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:0 rgba(84, 40, 109, 255), stop:1 rgba(108,\n"
                                        "                                                            58, 136, 255));\n"
                                        "            "
                                        "                                                }\n"
                                        "                                                            QPushButton#prefix_btn::pressed {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:1 rgba(84, 40, 109, 255), stop:0 rgba(108,\n"
                                        "                                                            58, 136, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#prefix_btn::checked {\n"
                                        "                                                            background-color: qlineargradient(spread:reflect, x1:0.5,\n"
                                        "                                                            y1:0, x2:0.5, y2:1, stop:0 rgba(134, 69, 172, 255), stop:1\n"
                                        "                                                            rgba(138, 71, 177, 255));\n"
                                        "                                                "
                                        "            }\n"
                                        "\n"
                                        "                                                            QPushButton#suffix_btn {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0.5, y1:0,\n"
                                        "                                                            x2:0.5, y2:1, stop:0 rgba(71, 88, 98, 255), stop:1 rgba(84,\n"
                                        "                                                            105, 116, 255));\n"
                                        "                                                            border-right: none;\n"
                                        "                                                            border-left: none;\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#suffix_btn::hover {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:0 rgba(40, 84, 109, 255), stop:1 rgba(58,\n"
                                        "          "
                                        "                                                  108, 136, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#suffix_btn::pressed {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:1 rgba(40, 84, 109, 255), stop:0 rgba(58,\n"
                                        "                                                            108, 136, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#suffix_btn::checked {\n"
                                        "                                                            background-color: qlineargradient(spread:reflect, x1:0.5,\n"
                                        "                                                            y1:0, x2:0.5, y2:1, stop:0 rgba(60, 119, 152, 255), stop:1\n"
                                        "                                                       "
                                        "     rgba(63, 124, 159, 255));\n"
                                        "                                                            }\n"
                                        "\n"
                                        "                                                            QPushButton#implicit_btn {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0.5, y1:0,\n"
                                        "                                                            x2:0.5, y2:1, stop:0 rgba(95, 69, 69, 255), stop:1 rgba(106,\n"
                                        "                                                            67, 67, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#implicit_btn::hover {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:0 rgba(109, 60, 60, 255), stop:1 rgba(136,\n"
                                        "                                                            75, 75, 255));\n"
                                        "           "
                                        "                                                 }\n"
                                        "                                                            QPushButton#implicit_btn::pressed {\n"
                                        "                                                            background-color: qlineargradient(spread:pad, x1:0, y1:0,\n"
                                        "                                                            x2:0, y2:1, stop:1 rgba(109, 60, 60, 255), stop:0 rgba(136,\n"
                                        "                                                            75, 75, 255));\n"
                                        "                                                            }\n"
                                        "                                                            QPushButton#implicit_btn::checked {\n"
                                        "                                                            background-color: qlineargradient(spread:reflect, x1:0.5,\n"
                                        "                                                            y1:0, x2:0.5, y2:0.5, stop:0 rgba(180, 99, 99, 255), stop:1\n"
                                        "                                                            rgba(150, 83, 83, 255));\n"
                                        "                                            "
                                        "                }\n"
                                        "\n"
                                        "                                                            QFrame#modpool_list_frame {\n"
                                        "                                                            border: none;\n"
                                        "                                                            }\n"
                                        "                                                            QFrame#modpool_btn_frame {\n"
                                        "                                                            border: none;\n"
                                        "                                                            }\n"
                                        "                                                        ")
        self.horizontalLayout = QHBoxLayout(self.modpool_list)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.modpool_list_frame = QFrame(self.modpool_list)
        self.modpool_list_frame.setObjectName(u"modpool_list_frame")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.modpool_list_frame.setPalette(palette)
        self.modpool_list_frame.setStyleSheet(u"")
        self.modpool_list_frame.setFrameShape(QFrame.NoFrame)
        self.modpool_list_frame.setFrameShadow(QFrame.Plain)
        self.modpool_list_layout = QVBoxLayout(self.modpool_list_frame)
        self.modpool_list_layout.setSpacing(0)
        self.modpool_list_layout.setObjectName(u"modpool_list_layout")
        self.modpool_list_layout.setContentsMargins(0, 0, 0, 0)
        self.modpool_btns_frame = QFrame(self.modpool_list_frame)
        self.modpool_btns_frame.setObjectName(u"modpool_btns_frame")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.modpool_btns_frame.setFont(font2)
        self.modpool_btns_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.modpool_btns_frame.setContextMenuPolicy(Qt.NoContextMenu)
                self.modpool_btns_frame.setFrameShape(QFrame.NoFrame)
                self.modpool_btns_frame.setFrameShadow(QFrame.Plain)
                self.modpool_btns_frame.setLineWidth(1)
                self.modpool_btns_frame.setMidLineWidth(1)
                self.modpool_btn_layout = QHBoxLayout(self.modpool_btns_frame)
                self.modpool_btn_layout.setSpacing(0)
                self.modpool_btn_layout.setObjectName(u"modpool_btn_layout")
                self.modpool_btn_layout.setContentsMargins(0, 0, 0, 0)
                self.prefix_btn = QPushButton(self.modpool_btns_frame)
                self.prefix_btn.setObjectName(u"prefix_btn")
                sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
                sizePolicy11.setHorizontalStretch(0)
                sizePolicy11.setVerticalStretch(0)
                sizePolicy11.setHeightForWidth(self.prefix_btn.sizePolicy().hasHeightForWidth())
                self.prefix_btn.setSizePolicy(sizePolicy11)
                palette1 = QPalette()
                brush1 = QBrush(QColor(255, 255, 255, 255))
                brush1.setStyle(Qt.SolidPattern)
                palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
                gradient = QLinearGradient(0.5, 0, 0.5, 1)
                gradient.setSpread(QGradient.PadSpread)
                gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient.setColorAt(0, QColor(112, 91, 124, 255))
                gradient.setColorAt(1, QColor(112, 91, 124, 255))
                brush2 = QBrush(gradient)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        gradient1 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(112, 91, 124, 255))
        gradient1.setColorAt(1, QColor(112, 91, 124, 255))
        brush3 = QBrush(gradient1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        gradient2 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(112, 91, 124, 255))
        gradient2.setColorAt(1, QColor(112, 91, 124, 255))
        brush4 = QBrush(gradient2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.SolidPattern)
                # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
                #endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        gradient3 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(112, 91, 124, 255))
        gradient3.setColorAt(1, QColor(112, 91, 124, 255))
        brush6 = QBrush(gradient3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        gradient4 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(112, 91, 124, 255))
        gradient4.setColorAt(1, QColor(112, 91, 124, 255))
        brush7 = QBrush(gradient4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        gradient5 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(112, 91, 124, 255))
        gradient5.setColorAt(1, QColor(112, 91, 124, 255))
        brush8 = QBrush(gradient5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
                #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
                #endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        gradient6 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(112, 91, 124, 255))
        gradient6.setColorAt(1, QColor(112, 91, 124, 255))
        brush9 = QBrush(gradient6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        gradient7 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(112, 91, 124, 255))
        gradient7.setColorAt(1, QColor(112, 91, 124, 255))
        brush10 = QBrush(gradient7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        gradient8 = QLinearGradient(0.5, 0, 0.5, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(112, 91, 124, 255))
        gradient8.setColorAt(1, QColor(112, 91, 124, 255))
        brush11 = QBrush(gradient8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush11)
                #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
                #endif
        self.prefix_btn.setPalette(palette1)
        font3 = QFont()
        font3.setFamilies([u"Segoe Ui"])
        font3.setPointSize(14)
        font3.setBold(True)
                self.prefix_btn.setFont(font3)
                self.prefix_btn.setCursor(QCursor(Qt.ArrowCursor))
                self.prefix_btn.setFocusPolicy(Qt.NoFocus)
                self.prefix_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.prefix_btn.setCheckable(True)

                self.modpool_btn_layout.addWidget(self.prefix_btn, 0, Qt.AlignTop)

                self.suffix_btn = QPushButton(self.modpool_btns_frame)
                self.suffix_btn.setObjectName(u"suffix_btn")
                sizePolicy11.setHeightForWidth(self.suffix_btn.sizePolicy().hasHeightForWidth())
                self.suffix_btn.setSizePolicy(sizePolicy11)
                self.suffix_btn.setFont(font3)
                self.suffix_btn.setCursor(QCursor(Qt.ArrowCursor))
                self.suffix_btn.setFocusPolicy(Qt.NoFocus)
                self.suffix_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.suffix_btn.setStyleSheet(u"")
                self.suffix_btn.setCheckable(True)

                self.modpool_btn_layout.addWidget(self.suffix_btn, 0, Qt.AlignTop)

                self.implicit_btn = QPushButton(self.modpool_btns_frame)
                self.implicit_btn.setObjectName(u"implicit_btn")
                sizePolicy11.setHeightForWidth(self.implicit_btn.sizePolicy().hasHeightForWidth())
                self.implicit_btn.setSizePolicy(sizePolicy11)
                self.implicit_btn.setFont(font3)
                self.implicit_btn.setCursor(QCursor(Qt.ArrowCursor))
                self.implicit_btn.setFocusPolicy(Qt.NoFocus)
                self.implicit_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.implicit_btn.setStyleSheet(u"")
                self.implicit_btn.setCheckable(True)
                self.implicit_btn.setFlat(False)

                self.modpool_btn_layout.addWidget(self.implicit_btn, 0, Qt.AlignTop)


        self.modpool_list_layout.addWidget(self.modpool_btns_frame, 0, Qt.AlignTop)

        self.modpool_group_pages = QStackedWidget(self.modpool_list_frame)
        self.modpool_group_pages.setObjectName(u"modpool_group_pages")
        self.prefix_group_page = QWidget()
        self.prefix_group_page.setObjectName(u"prefix_group_page")
        self.p = QVBoxLayout(self.prefix_group_page)
        self.p.setSpacing(0)
        self.p.setObjectName(u"p")
        self.p.setContentsMargins(0, 0, 0, 0)
        self.prefix_tree = QTreeView(self.prefix_group_page)
        self.prefix_tree.setObjectName(u"prefix_tree")
        sizePolicy.setHeightForWidth(self.prefix_tree.sizePolicy().hasHeightForWidth())
        self.prefix_tree.setSizePolicy(sizePolicy)
        self.prefix_tree.setFrameShape(QFrame.NoFrame)
        self.prefix_tree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.prefix_tree.setProperty("showDropIndicator", True)
        self.prefix_tree.setAlternatingRowColors(True)
        self.prefix_tree.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.prefix_tree.setRootIsDecorated(True)
        self.prefix_tree.setUniformRowHeights(True)
        self.prefix_tree.setAnimated(True)
        self.prefix_tree.setAllColumnsShowFocus(False)
        self.prefix_tree.setHeaderHidden(True)
        self.prefix_tree.header().setDefaultSectionSize(47)
        self.prefix_tree.header().setHighlightSections(False)
        self.prefix_tree.header().setProperty("showSortIndicator", False)

        self.p.addWidget(self.prefix_tree)

        self.modpool_group_pages.addWidget(self.prefix_group_page)
        self.suffix_list_page = QWidget()
        self.suffix_list_page.setObjectName(u"suffix_list_page")
        self.modpool_group_pages.addWidget(self.suffix_list_page)
        self.implicit_list_page = QWidget()
        self.implicit_list_page.setObjectName(u"implicit_list_page")
        self.modpool_group_pages.addWidget(self.implicit_list_page)

        self.modpool_list_layout.addWidget(self.modpool_group_pages)


        self.horizontalLayout.addWidget(self.modpool_list_frame)


        self.verticalLayout.addWidget(self.modpool_list)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
                                  "                                font-size: 16pt;\n"
                                  "                                }\n"
                                  "                            ")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)
        self.modpool_group_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
            MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
            self.item_header_label.setText("")
            self.item_quality_label.setText(QCoreApplication.translate("MainPages",
                                                                       u"<p align=\"center\"><span style=\" font-size:11pt; color:#827a6c;\">Quality: </span>\n"
                                                                       "<span style=\" font-size:11pt; font-weight:bold; color:#8787fe;\">0%</span></p>",
                                                                       None))
            self.item_spacer_1.setText("")
            self.item_level_label.setText(QCoreApplication.translate("MainPages",
                                                                     u"<p align=\"center\"><span style=\" font-size:11pt; color:#827a6c;\">Item Level: </span>\n"
                                                                     "<span style=\" font-size:11pt; font-weight:bold; color:#fff;\">0</span></p>",
                                                                     None))
            self.item_spacer_2.setText("")
            self.item_implicits_label.setText("")
            self.item_spacer_3.setText("")
            self.prefix_info_1.setText(QCoreApplication.translate("MainPages", u"test", None))
            self.prefix_1.setText(QCoreApplication.translate("MainPages", u"test", None))
            self.prefix_info_2.setText("")
            self.prefix_2.setText("")
            self.prefix_info_3.setText("")
            self.prefix_3.setText("")
            self.suffix_2_info.setText("")
            self.suffix_2.setText("")
            self.suffix_1_info.setText("")
            self.suffix_1.setText("")
            self.suffix_3_info.setText("")
            self.suffix_3.setText("")
            self.item_img_label.setText("")
            self.crafting_btn_label.setText("")
            self.phys_dps_label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span\n"
                                                                                "                                                                                style=\" color:#827a6c;\">pDPS\n"
                                                                                "                                                                                : </span><span style=\"\n"
                                                                                "                                                                                color:#8787fe;\">{}</span></p></body></html>\n"
                                                                                "                                                                            ",
                                                                   None))
            self.ele_dps_label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p\n"
                                                                               "                                                                                align=\"center\"><span\n"
                                                                               "                                                                                style=\" color:#827a6c;\">eDPS\n"
                                                                               "                                                                                : </span><span style=\"\n"
                                                                               "                                                                                color:#8787fe;\">{}</span></p></body></html>\n"
                                                                               "                                                                            ",
                                                                  None))
        self.total_dps_label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p\n"
                                                                             "                                                                                align=\"center\"><span\n"
                                                                             "                                                                                style=\" color:#827a6c;\">pDPS\n"
                                                                             "                                                                                : </span><span style=\"\n"
                                                                             "                                                                                color:#8787fe;\">{}</span></p></body></html>\n"
                                                                             "                                                                            ",
                                                                None))
        self.affix_total_label.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p\n"
                                                                               "                                                                                align=\"center\"><span\n"
                                                                               "                                                                                style=\" color:#999999;\">P S\n"
                                                                               "                                                                                C</span></p></body></html>\n"
                                                                               "                                                                            ",
                                                                  None))
        self.prefix_btn.setText(QCoreApplication.translate("MainPages", u"PREFIXES", None))
        self.suffix_btn.setText(QCoreApplication.translate("MainPages", u"SUFFIXES", None))
        self.implicit_btn.setText(QCoreApplication.translate("MainPages", u"IMPLICITS", None))
    # retranslateUi

