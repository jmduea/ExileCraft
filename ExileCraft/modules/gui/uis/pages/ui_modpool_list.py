# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################

################################################################################
## Form generated from reading UI file 'modpool_listzKHmZE.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QBrush, QColor, QCursor,
                           QFont, QGradient, QLinearGradient, QPalette)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QButtonGroup,
                               QFrame, QHBoxLayout, QPushButton,
                               QSizePolicy, QStackedWidget, QTreeView, QVBoxLayout,
                               QWidget)


class Ui_modpool_list(object):
        def setupUi(self, modpool_list):
                if not modpool_list.objectName():
                        modpool_list.setObjectName(u"modpool_list")
                modpool_list.resize(458, 514)
                modpool_list.setStyleSheet(u"QStackedWidget > QWidget {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(75, 75, 75, 255));\n"
                                           "	border-left: 1px solid;\n"
                                           "	border-right: 1px solid;\n"
                                           "	border-top: none;\n"
                                           "	border-bottom: none;\n"
                                           "}\n"
                                           "QHeaderView::section {\n"
                                           "	background-color: rgb(0, 0, 0);\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "	padding: 2px 2px 2px 10px\n"
                                           "}\n"
                                           "QHeaderView::up-arrow {\n"
                                           "	image: url(:/images/assets/images/up_arrow.png);\n"
                                           "}\n"
                                           "QHeaderView::down-arrow {\n"
                                           "	image: url(:/images/assets/images/down_arrow.png);\n"
                                           "}\n"
                                           "QTreeView {\n"
                                           "	background-color: rgb(51, 51, 51);\n"
                                           "	alternate-background-color: rgb(99, 99, 99);\n"
                                           "	border-left: 1px solid;\n"
                                           "	border-right: 1px solid;\n"
                                           "	border-top: none;\n"
                                           "	border-bottom: none;\n"
                                           "	color: rgb(255, 255, 255);\n"
                                           "	show-decoration-selected: 1;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "	color: white;\n"
                                           "	margin: 0px;\n"
                                           "	border: 2px groove;\n"
                                           "	font-family: Segoe Ui;\n"
                                           "	text-shadow: 1px 1px #000;\n"
                                           "	"
                                           "padding: 5px 5px 5px 5px;\n"
                                           "}\n"
                                           "QPushButton::hover {\n"
                                           "	border: 2px outset;\n"
                                           "}\n"
                                           "QPushButton::pressed {\n"
                                           "	border: 2px inset;\n"
                                           "}\n"
                                           "QPushButton::checked {\n"
                                           "	border: 2px solid;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#prefix_btn {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(112, 91, 124, 255), stop:1 rgba(112, 91, 124, 255));\n"
                                           "}\n"
                                           "QPushButton#prefix_btn::hover {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(84, 40, 109, 			255), stop:1 rgba(108, 58, 136, 255));\n"
                                           "}\n"
                                           "QPushButton#prefix_btn::pressed {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(84, 40, 109, 			255), stop:0 rgba(108, 58, 136, 255));\n"
                                           "}\n"
                                           "QPushButton#prefix_btn::checked {\n"
                                           "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(134, 69, 172, 255), stop:1 rgba(138, 71, 177, 255));\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#suffix_btn {\n"
                                           "	background-color: qlineargradient(spre"
                                           "ad:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 88, 98, 255), stop:1 rgba(84, 105, 116, 255));\n"
                                           "	border-right: none;\n"
                                           "	border-left: none;\n"
                                           "}\n"
                                           "QPushButton#suffix_btn::hover {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(40, 84, 109, 255), stop:1 rgba(58, 108, 136, 255));\n"
                                           "}\n"
                                           "QPushButton#suffix_btn::pressed {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(40, 84, 109, 255), stop:0 rgba(58, 108, 136, 255));\n"
                                           "}\n"
                                           "QPushButton#suffix_btn::checked {\n"
                                           "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(60, 119, 152, 255), stop:1 rgba(63, 124, 159, 255));\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#implicit_btn {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(95, 69, 69, 255), stop:1 rgba(106, 67, 67, 255));\n"
                                           "}\n"
                                           "QPushButton#implicit_btn::hover {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(109, 60"
                                           ", 60, 			255), stop:1 rgba(136, 75, 75, 255));\n"
                                           "}\n"
                                           "QPushButton#implicit_btn::pressed {\n"
                                           "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(109, 60, 60, 			255), stop:0 rgba(136, 75, 75, 255));\n"
                                           "}\n"
                                           "QPushButton#implicit_btn::checked {\n"
                                           "	background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(180, 99, 99, 255), stop:1 rgba(150, 83, 83, 255));\n"
                                           "}\n"
                                           "\n"
                                           "QFrame#modpool_list_frame {\n"
                                           "border: none;\n"
                                           "}\n"
                                           "QFrame#modpool_btn_frame {\n"
                                           "border: none;\n"
                                           "}")
                self.verticalLayout = QVBoxLayout(modpool_list)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(10, 10, 10, 10)
                self.modpool_list_frame = QFrame(modpool_list)
                self.modpool_list_frame.setObjectName(u"modpool_list_frame")
                palette = QPalette()
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
                font = QFont()
                font.setPointSize(14)
                font.setBold(True)
                self.modpool_btns_frame.setFont(font)
                self.modpool_btns_frame.setCursor(QCursor(Qt.PointingHandCursor))
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
                self.modpool_btn_group = QButtonGroup(modpool_list)
                self.modpool_btn_group.setObjectName(u"modpool_btn_group")
                self.modpool_btn_group.addButton(self.prefix_btn)
                self.prefix_btn.setObjectName(u"prefix_btn")
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.prefix_btn.sizePolicy().hasHeightForWidth())
                self.prefix_btn.setSizePolicy(sizePolicy)
                palette1 = QPalette()
                brush = QBrush(QColor(255, 255, 255, 255))
                brush.setStyle(Qt.SolidPattern)
                palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
                gradient = QLinearGradient(0.5, 0, 0.5, 1)
                gradient.setSpread(QGradient.PadSpread)
                gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient.setColorAt(0, QColor(112, 91, 124, 255))
                gradient.setColorAt(1, QColor(112, 91, 124, 255))
                brush1 = QBrush(gradient)
                palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
                palette1.setBrush(QPalette.Active, QPalette.Text, brush)
                palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
                gradient1 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient1.setSpread(QGradient.PadSpread)
                gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient1.setColorAt(0, QColor(112, 91, 124, 255))
                gradient1.setColorAt(1, QColor(112, 91, 124, 255))
                brush2 = QBrush(gradient1)
                palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
                gradient2 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient2.setSpread(QGradient.PadSpread)
                gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient2.setColorAt(0, QColor(112, 91, 124, 255))
                gradient2.setColorAt(1, QColor(112, 91, 124, 255))
                brush3 = QBrush(gradient2)
                palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
                brush4 = QBrush(QColor(255, 255, 255, 128))
                brush4.setStyle(Qt.SolidPattern)
                # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
                # endif
                palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                gradient3 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient3.setSpread(QGradient.PadSpread)
                gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient3.setColorAt(0, QColor(112, 91, 124, 255))
                gradient3.setColorAt(1, QColor(112, 91, 124, 255))
                brush5 = QBrush(gradient3)
                palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
                palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
                palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
                gradient4 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient4.setSpread(QGradient.PadSpread)
                gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient4.setColorAt(0, QColor(112, 91, 124, 255))
                gradient4.setColorAt(1, QColor(112, 91, 124, 255))
                brush6 = QBrush(gradient4)
                palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
                gradient5 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient5.setSpread(QGradient.PadSpread)
                gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient5.setColorAt(0, QColor(112, 91, 124, 255))
                gradient5.setColorAt(1, QColor(112, 91, 124, 255))
                brush7 = QBrush(gradient5)
                palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
                # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
                # endif
                palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
                gradient6 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient6.setSpread(QGradient.PadSpread)
                gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient6.setColorAt(0, QColor(112, 91, 124, 255))
                gradient6.setColorAt(1, QColor(112, 91, 124, 255))
                brush8 = QBrush(gradient6)
                palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
                palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
                palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
                gradient7 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient7.setSpread(QGradient.PadSpread)
                gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient7.setColorAt(0, QColor(112, 91, 124, 255))
                gradient7.setColorAt(1, QColor(112, 91, 124, 255))
                brush9 = QBrush(gradient7)
                palette1.setBrush(QPalette.Disabled, QPalette.Base, brush9)
                gradient8 = QLinearGradient(0.5, 0, 0.5, 1)
                gradient8.setSpread(QGradient.PadSpread)
                gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
                gradient8.setColorAt(0, QColor(112, 91, 124, 255))
                gradient8.setColorAt(1, QColor(112, 91, 124, 255))
                brush10 = QBrush(gradient8)
                palette1.setBrush(QPalette.Disabled, QPalette.Window, brush10)
                # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
                # endif
                self.prefix_btn.setPalette(palette1)
                font1 = QFont()
                font1.setFamilies([u"Segoe Ui"])
                font1.setPointSize(14)
                font1.setBold(True)
                self.prefix_btn.setFont(font1)
                self.prefix_btn.setCursor(QCursor(Qt.PointingHandCursor))
                self.prefix_btn.setFocusPolicy(Qt.NoFocus)
                self.prefix_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.prefix_btn.setCheckable(True)

                self.modpool_btn_layout.addWidget(self.prefix_btn, 0, Qt.AlignTop)

                self.suffix_btn = QPushButton(self.modpool_btns_frame)
                self.modpool_btn_group.addButton(self.suffix_btn)
                self.suffix_btn.setObjectName(u"suffix_btn")
                sizePolicy.setHeightForWidth(self.suffix_btn.sizePolicy().hasHeightForWidth())
                self.suffix_btn.setSizePolicy(sizePolicy)
                self.suffix_btn.setFont(font1)
                self.suffix_btn.setCursor(QCursor(Qt.PointingHandCursor))
                self.suffix_btn.setFocusPolicy(Qt.NoFocus)
                self.suffix_btn.setContextMenuPolicy(Qt.NoContextMenu)
                self.suffix_btn.setStyleSheet(u"")
                self.suffix_btn.setCheckable(True)

                self.modpool_btn_layout.addWidget(self.suffix_btn, 0, Qt.AlignTop)

                self.implicit_btn = QPushButton(self.modpool_btns_frame)
                self.modpool_btn_group.addButton(self.implicit_btn)
                self.implicit_btn.setObjectName(u"implicit_btn")
                sizePolicy.setHeightForWidth(self.implicit_btn.sizePolicy().hasHeightForWidth())
                self.implicit_btn.setSizePolicy(sizePolicy)
                self.implicit_btn.setFont(font1)
                self.implicit_btn.setCursor(QCursor(Qt.PointingHandCursor))
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
                self.verticalLayout_2 = QVBoxLayout(self.prefix_group_page)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.prefix_tree = QTreeView(self.prefix_group_page)
                self.prefix_tree.setObjectName(u"prefix_tree")
                self.prefix_tree.setFrameShape(QFrame.NoFrame)
                self.prefix_tree.setFrameShadow(QFrame.Plain)
                self.prefix_tree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
                self.prefix_tree.setProperty("showDropIndicator", True)
                self.prefix_tree.setAlternatingRowColors(True)
                self.prefix_tree.setSelectionBehavior(QAbstractItemView.SelectItems)
                self.prefix_tree.setRootIsDecorated(False)
                self.prefix_tree.setUniformRowHeights(True)
                self.prefix_tree.setAnimated(True)
                self.prefix_tree.setAllColumnsShowFocus(False)
                self.prefix_tree.setHeaderHidden(False)
                self.prefix_tree.header().setDefaultSectionSize(47)
                self.prefix_tree.header().setHighlightSections(False)
                self.prefix_tree.header().setProperty("showSortIndicator", False)

                self.verticalLayout_2.addWidget(self.prefix_tree)

                self.modpool_group_pages.addWidget(self.prefix_group_page)
                self.suffix_list_page = QWidget()
                self.suffix_list_page.setObjectName(u"suffix_list_page")
                self.modpool_group_pages.addWidget(self.suffix_list_page)
                self.implicit_list_page = QWidget()
                self.implicit_list_page.setObjectName(u"implicit_list_page")
                self.modpool_group_pages.addWidget(self.implicit_list_page)

                self.modpool_list_layout.addWidget(self.modpool_group_pages)

                self.verticalLayout.addWidget(self.modpool_list_frame)

                self.retranslateUi(modpool_list)

                self.modpool_group_pages.setCurrentIndex(0)

                QMetaObject.connectSlotsByName(modpool_list)

        # setupUi

        def retranslateUi(self, modpool_list):
                modpool_list.setWindowTitle(QCoreApplication.translate("modpool_list", u"Form", None))
                self.prefix_btn.setText(QCoreApplication.translate("modpool_list", u"PREFIXES", None))
                self.suffix_btn.setText(QCoreApplication.translate("modpool_list", u"SUFFIXES", None))
                self.implicit_btn.setText(QCoreApplication.translate("modpool_list", u"IMPLICITS", None))
        # retranslateUi
