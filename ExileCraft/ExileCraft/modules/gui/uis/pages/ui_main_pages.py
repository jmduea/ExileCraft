# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesIVqXIp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget)
from ...assets import assets_rc


class Ui_MainPages(object):
        def setupUi(self, MainPages):
                if not MainPages.objectName():
                        MainPages.setObjectName(u"MainPages")
                MainPages.resize(602, 527)
                MainPages.setMinimumSize(QSize(602, 527))
                self.main_pages_layout = QVBoxLayout(MainPages)
                self.main_pages_layout.setSpacing(0)
                self.main_pages_layout.setObjectName(u"main_pages_layout")
                self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
                self.pages = QStackedWidget(MainPages)
                self.pages.setObjectName(u"pages")
                self.page_1 = QWidget()
                self.page_1.setObjectName(u"page_1")
                self.page_1.setMinimumSize(QSize(592, 517))
                self.page_1.setStyleSheet(u"font-size: 14pt")
                self.verticalLayout_5 = QVBoxLayout(self.page_1)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.crafting_zone_container = QFrame(self.page_1)
                self.crafting_zone_container.setObjectName(u"crafting_zone_container")
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.crafting_zone_container.sizePolicy().hasHeightForWidth())
                self.crafting_zone_container.setSizePolicy(sizePolicy)
                self.crafting_zone_container.setStyleSheet(u"QWidget {\n"
                                                           "           border-image: none;\n"
                                                           "           }\n"
                                                           "          ")
                self.horizontalLayout_4 = QHBoxLayout(self.crafting_zone_container)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.item_info_frame = QFrame(self.crafting_zone_container)
                self.item_info_frame.setObjectName(u"item_info_frame")
                sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(self.item_info_frame.sizePolicy().hasHeightForWidth())
                self.item_info_frame.setSizePolicy(sizePolicy1)
                self.item_info_frame.setFrameShape(QFrame.StyledPanel)
                self.item_info_frame.setFrameShadow(QFrame.Raised)
                self.verticalLayout_4 = QVBoxLayout(self.item_info_frame)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.item_header_frame = QFrame(self.item_info_frame)
                self.item_header_frame.setObjectName(u"item_header_frame")
                sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.item_header_frame.sizePolicy().hasHeightForWidth())
                self.item_header_frame.setSizePolicy(sizePolicy2)
                self.item_header_frame.setMinimumSize(QSize(400, 54))
                self.item_header_frame.setMaximumSize(QSize(400, 54))
                self.item_header_frame.setBaseSize(QSize(400, 44))
                self.item_header_frame.setContextMenuPolicy(Qt.NoContextMenu)
                self.item_header_layout = QVBoxLayout(self.item_header_frame)
                self.item_header_layout.setSpacing(0)
                self.item_header_layout.setObjectName(u"item_header_layout")
                self.item_header_layout.setContentsMargins(0, 0, 0, 0)
                self.item_header_label = QLabel(self.item_header_frame)
                self.item_header_label.setObjectName(u"item_header_label")
                self.item_header_label.setEnabled(True)
                sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
                sizePolicy3.setHorizontalStretch(0)
                sizePolicy3.setVerticalStretch(0)
                sizePolicy3.setHeightForWidth(self.item_header_label.sizePolicy().hasHeightForWidth())
                self.item_header_label.setSizePolicy(sizePolicy3)
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
                                                     "	background-image: url(:/images/images/item-header-normal.png);\n"
                                                     "}")
                self.item_header_label.setTextFormat(Qt.RichText)
                self.item_header_label.setScaledContents(False)
                self.item_header_label.setAlignment(Qt.AlignCenter)
                self.item_header_label.setWordWrap(True)

                self.item_header_layout.addWidget(self.item_header_label)

                self.verticalLayout_4.addWidget(self.item_header_frame)

                self.item_affix_frame = QFrame(self.item_info_frame)
                self.item_affix_frame.setObjectName(u"item_affix_frame")
                sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                sizePolicy4.setHorizontalStretch(0)
                sizePolicy4.setVerticalStretch(0)
                sizePolicy4.setHeightForWidth(self.item_affix_frame.sizePolicy().hasHeightForWidth())
                self.item_affix_frame.setSizePolicy(sizePolicy4)
                self.item_affix_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
                self.item_affix_frame.setFrameShape(QFrame.StyledPanel)
                self.item_affix_frame.setFrameShadow(QFrame.Raised)
                self.item_affix_layout = QVBoxLayout(self.item_affix_frame)
                self.item_affix_layout.setObjectName(u"item_affix_layout")
                self.item_properties = QLabel(self.item_affix_frame)
                self.item_properties.setObjectName(u"item_properties")
                sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
                sizePolicy5.setHorizontalStretch(0)
                sizePolicy5.setVerticalStretch(0)
                sizePolicy5.setHeightForWidth(self.item_properties.sizePolicy().hasHeightForWidth())
                self.item_properties.setSizePolicy(sizePolicy5)
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

                self.item_affix_layout.addWidget(self.item_properties)

                self.item_spacer_1 = QLabel(self.item_affix_frame)
                self.item_spacer_1.setObjectName(u"item_spacer_1")
                sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
                sizePolicy6.setHorizontalStretch(0)
                sizePolicy6.setVerticalStretch(0)
                sizePolicy6.setHeightForWidth(self.item_spacer_1.sizePolicy().hasHeightForWidth())
                self.item_spacer_1.setSizePolicy(sizePolicy6)
                self.item_spacer_1.setMaximumSize(QSize(400, 2))
                self.item_spacer_1.setBaseSize(QSize(0, 0))
                self.item_spacer_1.setTextFormat(Qt.RichText)
                self.item_spacer_1.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_1.setScaledContents(False)
                self.item_spacer_1.setAlignment(Qt.AlignCenter)

                self.item_affix_layout.addWidget(self.item_spacer_1)

                self.item_requirements = QLabel(self.item_affix_frame)
                self.item_requirements.setObjectName(u"item_requirements")
                sizePolicy5.setHeightForWidth(self.item_requirements.sizePolicy().hasHeightForWidth())
                self.item_requirements.setSizePolicy(sizePolicy5)
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

                self.item_affix_layout.addWidget(self.item_requirements)

                self.item_spacer_2 = QLabel(self.item_affix_frame)
                self.item_spacer_2.setObjectName(u"item_spacer_2")
                sizePolicy6.setHeightForWidth(self.item_spacer_2.sizePolicy().hasHeightForWidth())
                self.item_spacer_2.setSizePolicy(sizePolicy6)
                self.item_spacer_2.setMaximumSize(QSize(400, 2))
                self.item_spacer_2.setBaseSize(QSize(0, 0))
                self.item_spacer_2.setTextFormat(Qt.RichText)
                self.item_spacer_2.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_2.setScaledContents(False)
                self.item_spacer_2.setAlignment(Qt.AlignCenter)

                self.item_affix_layout.addWidget(self.item_spacer_2)

                self.item_implicits = QLabel(self.item_affix_frame)
                self.item_implicits.setObjectName(u"item_implicits")
                self.item_implicits.setEnabled(False)
                sizePolicy5.setHeightForWidth(self.item_implicits.sizePolicy().hasHeightForWidth())
                self.item_implicits.setSizePolicy(sizePolicy5)
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

                self.item_affix_layout.addWidget(self.item_implicits)

                self.item_spacer_3 = QLabel(self.item_affix_frame)
                self.item_spacer_3.setObjectName(u"item_spacer_3")
                self.item_spacer_3.setEnabled(False)
                sizePolicy6.setHeightForWidth(self.item_spacer_3.sizePolicy().hasHeightForWidth())
                self.item_spacer_3.setSizePolicy(sizePolicy6)
                self.item_spacer_3.setMaximumSize(QSize(400, 2))
                self.item_spacer_3.setBaseSize(QSize(0, 0))
                self.item_spacer_3.setTextFormat(Qt.RichText)
                self.item_spacer_3.setPixmap(QPixmap(u":/images/images/item-sep.png"))
                self.item_spacer_3.setScaledContents(False)
                self.item_spacer_3.setAlignment(Qt.AlignCenter)

                self.item_affix_layout.addWidget(self.item_spacer_3)

                self.verticalLayout_4.addWidget(self.item_affix_frame)

                self.item_mods_frame = QFrame(self.item_info_frame)
                self.item_mods_frame.setObjectName(u"item_mods_frame")
                self.item_mods_frame.setEnabled(False)
                sizePolicy4.setHeightForWidth(self.item_mods_frame.sizePolicy().hasHeightForWidth())
                self.item_mods_frame.setSizePolicy(sizePolicy4)
                self.item_mods_frame.setMinimumSize(QSize(400, 300))
                self.item_mods_frame.setMaximumSize(QSize(400, 16777215))
                self.item_mods_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
                self.item_mods_layout = QVBoxLayout(self.item_mods_frame)
                self.item_mods_layout.setObjectName(u"item_mods_layout")
                self.prefix_info_1 = QLabel(self.item_mods_frame)
                self.prefix_info_1.setObjectName(u"prefix_info_1")
                self.prefix_info_1.setEnabled(False)
                self.prefix_info_1.setMinimumSize(QSize(0, 0))
                font1 = QFont()
                font1.setFamilies([u"Open Sans"])
                font1.setBold(False)
                font1.setItalic(False)
                self.prefix_info_1.setFont(font1)
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

                self.item_mods_layout.addWidget(self.prefix_info_1, 0, Qt.AlignHCenter | Qt.AlignTop)

                self.prefix_1 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.prefix_1, 0, Qt.AlignHCenter)

                self.prefix_info_2 = QLabel(self.item_mods_frame)
                self.prefix_info_2.setObjectName(u"prefix_info_2")
                self.prefix_info_2.setEnabled(False)
                self.prefix_info_2.setMinimumSize(QSize(0, 0))
                self.prefix_info_2.setFont(font1)
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

                self.item_mods_layout.addWidget(self.prefix_info_2, 0, Qt.AlignHCenter | Qt.AlignTop)

                self.prefix_2 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.prefix_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

                self.prefix_info_3 = QLabel(self.item_mods_frame)
                self.prefix_info_3.setObjectName(u"prefix_info_3")
                self.prefix_info_3.setEnabled(False)
                self.prefix_info_3.setMinimumSize(QSize(0, 0))
                self.prefix_info_3.setFont(font1)
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

                self.item_mods_layout.addWidget(self.prefix_info_3, 0, Qt.AlignHCenter | Qt.AlignTop)

                self.prefix_3 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.prefix_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

                self.suffix_info_1 = QLabel(self.item_mods_frame)
                self.suffix_info_1.setObjectName(u"suffix_info_1")
                self.suffix_info_1.setEnabled(False)
                self.suffix_info_1.setMinimumSize(QSize(0, 0))
                self.suffix_info_1.setFont(font1)
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

                self.item_mods_layout.addWidget(self.suffix_info_1)

                self.suffix_1 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.suffix_1, 0, Qt.AlignHCenter | Qt.AlignVCenter)

                self.suffix_info_2 = QLabel(self.item_mods_frame)
                self.suffix_info_2.setObjectName(u"suffix_info_2")
                self.suffix_info_2.setEnabled(False)
                self.suffix_info_2.setMinimumSize(QSize(0, 0))
                self.suffix_info_2.setFont(font1)
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

                self.item_mods_layout.addWidget(self.suffix_info_2)

                self.suffix_2 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.suffix_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

                self.suffix_info_3 = QLabel(self.item_mods_frame)
                self.suffix_info_3.setObjectName(u"suffix_info_3")
                self.suffix_info_3.setEnabled(False)
                sizePolicy4.setHeightForWidth(self.suffix_info_3.sizePolicy().hasHeightForWidth())
                self.suffix_info_3.setSizePolicy(sizePolicy4)
                self.suffix_info_3.setMinimumSize(QSize(0, 0))
                self.suffix_info_3.setMaximumSize(QSize(16777215, 16))
                self.suffix_info_3.setFont(font1)
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

                self.item_mods_layout.addWidget(self.suffix_info_3)

                self.suffix_3 = QLabel(self.item_mods_frame)
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

                self.item_mods_layout.addWidget(self.suffix_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

                self.verticalLayout_4.addWidget(self.item_mods_frame)

                self.horizontalLayout_4.addWidget(self.item_info_frame)

                self.item_display_frame = QFrame(self.crafting_zone_container)
                self.item_display_frame.setObjectName(u"item_display_frame")
                sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
                sizePolicy7.setHorizontalStretch(0)
                sizePolicy7.setVerticalStretch(0)
                sizePolicy7.setHeightForWidth(self.item_display_frame.sizePolicy().hasHeightForWidth())
                self.item_display_frame.setSizePolicy(sizePolicy7)
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
                                                   "border: 0px;\n"
                                                   "background-color: none;\n"
                                                   "}")
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
                                                  "	background-image: url(:/images/images/item_box.png);\n"
                                                  "opacity: 0.8;\n"
                                                  "}\n"
                                                  "QLabel::hover{\n"
                                                  "background-color:#ffffff;\n"
                                                  "opacity: 1;\n"
                                                  "}")
                self.item_img_label.setScaledContents(True)
                self.item_img_label.setAlignment(Qt.AlignCenter)

                self.verticalLayout_3.addWidget(self.item_img_label)

                self.item_view_layout.addWidget(self.item_img_frame)

                self.crafting_btn_frame = QFrame(self.item_view_frame)
                self.crafting_btn_frame.setObjectName(u"crafting_btn_frame")
                sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
                sizePolicy8.setHorizontalStretch(0)
                sizePolicy8.setVerticalStretch(0)
                sizePolicy8.setHeightForWidth(self.crafting_btn_frame.sizePolicy().hasHeightForWidth())
                self.crafting_btn_frame.setSizePolicy(sizePolicy8)
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
                self.crafting_btn_label.setCursor(QCursor(Qt.PointingHandCursor))
                self.crafting_btn_label.setFocusPolicy(Qt.StrongFocus)
                self.crafting_btn_label.setStyleSheet(u"QLabel{\n"
                                                      "	background-image: url(:/images/images/craftbtn.png);\n"
                                                      "}\n"
                                                      "QLabel::hover{\n"
                                                      "	background-image: url(:/images/images/craftbtnov.png);\n"
                                                      "}")
                self.crafting_btn_label.setScaledContents(True)
                self.crafting_btn_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

                self.crafting_btn_layout.addWidget(self.crafting_btn_label)

                self.item_view_layout.addWidget(self.crafting_btn_frame, 0, Qt.AlignTop)

                self.verticalLayout_2.addWidget(self.item_view_frame)

                self.item_dps_frame = QFrame(self.item_display_frame)
                self.item_dps_frame.setObjectName(u"item_dps_frame")
                sizePolicy4.setHeightForWidth(self.item_dps_frame.sizePolicy().hasHeightForWidth())
                self.item_dps_frame.setSizePolicy(sizePolicy4)
                self.item_dps_frame.setFrameShape(QFrame.StyledPanel)
                self.item_dps_frame.setFrameShadow(QFrame.Raised)
                self.item_dps_layout = QVBoxLayout(self.item_dps_frame)
                self.item_dps_layout.setSpacing(6)
                self.item_dps_layout.setObjectName(u"item_dps_layout")
                self.item_dps_layout.setContentsMargins(10, 10, 10, 10)
                self.phys_dps_label = QLabel(self.item_dps_frame)
                self.phys_dps_label.setObjectName(u"phys_dps_label")
                sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
                sizePolicy9.setHorizontalStretch(0)
                sizePolicy9.setVerticalStretch(0)
                sizePolicy9.setHeightForWidth(self.phys_dps_label.sizePolicy().hasHeightForWidth())
                self.phys_dps_label.setSizePolicy(sizePolicy9)
                self.phys_dps_label.setMinimumSize(QSize(0, 30))
                self.phys_dps_label.setStyleSheet(u"QLabel {\n"
                                                  "border: 1px solid #edc57d;\n"
                                                  "background: #000;\n"
                                                  "padding: 2px 3px 4px 2px;\n"
                                                  "}")
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
                sizePolicy8.setHeightForWidth(self.ele_dps_label.sizePolicy().hasHeightForWidth())
                self.ele_dps_label.setSizePolicy(sizePolicy8)
                self.ele_dps_label.setMinimumSize(QSize(0, 30))
                self.ele_dps_label.setStyleSheet(u"QLabel {\n"
                                                 "border: 1px solid #edc57d;\n"
                                                 "background: #000;\n"
                                                 "padding: 2px 3px 4px 2px;\n"
                                                 "magin-bottom: 0px;\n"
                                                 "}")

                self.item_dps_layout.addWidget(self.ele_dps_label)

                self.total_dps_label = QLabel(self.item_dps_frame)
                self.total_dps_label.setObjectName(u"total_dps_label")
                sizePolicy8.setHeightForWidth(self.total_dps_label.sizePolicy().hasHeightForWidth())
                self.total_dps_label.setSizePolicy(sizePolicy8)
                self.total_dps_label.setMinimumSize(QSize(0, 30))
                self.total_dps_label.setStyleSheet(u"QLabel {\n"
                                                   "border: 1px solid #edc57d;\n"
                                                   "background: #000;\n"
                                                   "padding: 2px 3px 4px 2px;\n"
                                                   "magin-bottom: 0px;\n"
                                                   "}")

                self.item_dps_layout.addWidget(self.total_dps_label)

                self.affix_total_label = QLabel(self.item_dps_frame)
                self.affix_total_label.setObjectName(u"affix_total_label")
                sizePolicy8.setHeightForWidth(self.affix_total_label.sizePolicy().hasHeightForWidth())
                self.affix_total_label.setSizePolicy(sizePolicy8)
                self.affix_total_label.setMinimumSize(QSize(0, 30))
                self.affix_total_label.setStyleSheet(u"QLabel {\n"
                                                     "border: 1px solid #edc57d;\n"
                                                     "background: #000;\n"
                                                     "padding: 2px 3px 4px 2px;\n"
                                                     "magin-bottom: 0px;\n"
                                                     "}")

                self.item_dps_layout.addWidget(self.affix_total_label, 0, Qt.AlignTop)

                self.verticalLayout_2.addWidget(self.item_dps_frame, 0, Qt.AlignVCenter)

                self.horizontalLayout_4.addWidget(self.item_display_frame)

                self.verticalLayout_5.addWidget(self.crafting_zone_container)

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
                self.contents.setGeometry(QRect(0, 0, 582, 507))
                self.contents.setStyleSheet(u"background: transparent;")
                self.verticalLayout = QVBoxLayout(self.contents)
                self.verticalLayout.setSpacing(15)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(5, 5, 5, 5)
                self.title_label = QLabel(self.contents)
                self.title_label.setObjectName(u"title_label")
                self.title_label.setMaximumSize(QSize(16777215, 40))
                font2 = QFont()
                font2.setPointSize(16)
                self.title_label.setFont(font2)
                self.title_label.setStyleSheet(u"font-size: 16pt")
                self.title_label.setAlignment(Qt.AlignCenter)

                self.verticalLayout.addWidget(self.title_label)

                self.scroll_area.setWidget(self.contents)

                self.page_2_layout.addWidget(self.scroll_area)

                self.pages.addWidget(self.page_2)
                self.page_3 = QWidget()
                self.page_3.setObjectName(u"page_3")
                self.page_3.setStyleSheet(u"QFrame {\n"
                                          "	font-size: 16pt;\n"
                                          "}")
                self.page_3_layout = QVBoxLayout(self.page_3)
                self.page_3_layout.setObjectName(u"page_3_layout")
                self.empty_page_label = QLabel(self.page_3)
                self.empty_page_label.setObjectName(u"empty_page_label")
                self.empty_page_label.setFont(font2)
                self.empty_page_label.setAlignment(Qt.AlignCenter)

                self.page_3_layout.addWidget(self.empty_page_label)

                self.pages.addWidget(self.page_3)

                self.main_pages_layout.addWidget(self.pages)

                self.retranslateUi(MainPages)

                self.pages.setCurrentIndex(0)

                QMetaObject.connectSlotsByName(MainPages)

        # setupUi

        def retranslateUi(self, MainPages):
                MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
                self.item_header_label.setText("")
                self.item_properties.setText("")
                self.item_spacer_1.setText("")
                self.item_spacer_2.setText("")
                self.item_implicits.setText("")
                self.item_spacer_3.setText("")
                self.prefix_info_1.setText(QCoreApplication.translate("MainPages", u"PrefixInfo1", None))
                self.prefix_1.setText(QCoreApplication.translate("MainPages", u"Prefix1", None))
                self.prefix_info_2.setText(QCoreApplication.translate("MainPages", u"PrefixInfo2", None))
                self.prefix_2.setText(QCoreApplication.translate("MainPages", u"Prefix2", None))
                self.prefix_info_3.setText(QCoreApplication.translate("MainPages", u"PrefixInfo3", None))
                self.prefix_3.setText(QCoreApplication.translate("MainPages", u"Prefix3", None))
                self.suffix_info_1.setText(QCoreApplication.translate("MainPages", u"SuffixInfo1", None))
                self.suffix_1.setText(QCoreApplication.translate("MainPages", u"Suffix1", None))
                self.suffix_info_2.setText(QCoreApplication.translate("MainPages", u"SuffixInfo2", None))
                self.suffix_2.setText(QCoreApplication.translate("MainPages", u"Suffix2", None))
                self.suffix_info_3.setText(QCoreApplication.translate("MainPages", u"SuffixInfo3", None))
                self.suffix_3.setText(QCoreApplication.translate("MainPages", u"Suffix3", None))
                self.item_img_label.setText("")
                self.crafting_btn_label.setText("")
                self.phys_dps_label.setText(QCoreApplication.translate("MainPages",
                                                                       u"<html><head/><body><p><span style=\" color:#827a6c;\">pDPS : </span><span style=\" color:#8787fe;\">{}</span></p></body></html>",
                                                                       None))
                self.ele_dps_label.setText(QCoreApplication.translate("MainPages",
                                                                      u"<html><head/><body><p align=\"center\"><span style=\" color:#827a6c;\">eDPS : </span><span style=\" color:#8787fe;\">{}</span></p></body></html>",
                                                                      None))
                self.total_dps_label.setText(QCoreApplication.translate("MainPages",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" color:#827a6c;\">pDPS : </span><span style=\" color:#8787fe;\">{}</span></p></body></html>",
                                                                        None))
                self.affix_total_label.setText(QCoreApplication.translate("MainPages",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" color:#999999;\">P S C</span></p></body></html>",
                                                                          None))
                self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
                self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        # retranslateUi
