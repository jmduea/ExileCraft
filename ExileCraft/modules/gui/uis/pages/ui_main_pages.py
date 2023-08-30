# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesVifCDz.ui'
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
    QIcon,
    QPixmap,
)
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName("MainPages")
        MainPages.resize(839, 890)
        MainPages.setMinimumSize(QSize(691, 890))
        MainPages.setStyleSheet(
            "QStackedWidget#pages QWidget#crafting_emu_page, #crafting_calc_page {\n"
            "                border-image: url(:/images/images/emubg.png);\n"
            "                }\n"
            "    QWidget#mod_widget_layout {\n"
            "    font-weight: bold;\n"
            "    font: 14px;\n"
            "    }\n"
            "            "
        )
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName("main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName("pages")
        self.pages.setMinimumSize(QSize(602, 527))
        self.pages.setFrameShape(QFrame.NoFrame)
        self.crafting_emu_page = QWidget()
        self.crafting_emu_page.setObjectName("crafting_emu_page")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.crafting_emu_page.sizePolicy().hasHeightForWidth()
        )
        self.crafting_emu_page.setSizePolicy(sizePolicy)
        self.crafting_emu_page.setMinimumSize(QSize(592, 517))
        self.crafting_emu_page.setStyleSheet("")
        self.crafting_emu_layout = QGridLayout(self.crafting_emu_page)
        self.crafting_emu_layout.setSpacing(9)
        self.crafting_emu_layout.setObjectName("crafting_emu_layout")
        self.crafting_emu_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout_spacer = QVBoxLayout()
        self.right_layout_spacer.setSpacing(0)
        self.right_layout_spacer.setObjectName("right_layout_spacer")

        self.crafting_emu_layout.addLayout(self.right_layout_spacer, 1, 3, 1, 1)

        self.left_layout_spacer = QVBoxLayout()
        self.left_layout_spacer.setSpacing(0)
        self.left_layout_spacer.setObjectName("left_layout_spacer")

        self.crafting_emu_layout.addLayout(self.left_layout_spacer, 1, 0, 1, 1)

        self.item_display_frame = QFrame(self.crafting_emu_page)
        self.item_display_frame.setObjectName("item_display_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.item_display_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_display_frame.setSizePolicy(sizePolicy1)
        self.item_display_frame.setFrameShape(QFrame.NoFrame)
        self.item_display_frame.setFrameShadow(QFrame.Raised)
        self.item_display_layout = QVBoxLayout(self.item_display_frame)
        self.item_display_layout.setObjectName("item_display_layout")
        self.item_view_frame = QFrame(self.item_display_frame)
        self.item_view_frame.setObjectName("item_view_frame")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.item_view_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_view_frame.setSizePolicy(sizePolicy2)
        self.item_view_frame.setMinimumSize(QSize(128, 269))
        self.item_view_frame.setMaximumSize(QSize(145, 269))
        self.item_view_frame.setMouseTracking(False)
        self.item_view_frame.setStyleSheet(
            "QWidget{\n"
            "              border: 0px;\n"
            "              background-color: none;\n"
            "              }\n"
            "             "
        )
        self.item_view_layout = QVBoxLayout(self.item_view_frame)
        self.item_view_layout.setSpacing(0)
        self.item_view_layout.setObjectName("item_view_layout")
        self.item_view_layout.setContentsMargins(0, 0, 0, 0)
        self.item_img_frame = QFrame(self.item_view_frame)
        self.item_img_frame.setObjectName("item_img_frame")
        self.item_img_frame.setMinimumSize(QSize(0, 228))
        self.item_img_frame.setFrameShape(QFrame.StyledPanel)
        self.item_img_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.item_img_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.item_img_label = QLabel(self.item_img_frame)
        self.item_img_label.setObjectName("item_img_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.item_img_label.sizePolicy().hasHeightForWidth()
        )
        self.item_img_label.setSizePolicy(sizePolicy3)
        self.item_img_label.setMinimumSize(QSize(128, 228))
        self.item_img_label.setMaximumSize(QSize(128, 228))
        self.item_img_label.setStyleSheet(
            "QLabel{\n"
            "                    background-image:\n"
            "                    url(:/images/images/item_box.png);\n"
            "                    opacity: 0.8;\n"
            "                    }\n"
            "                    QLabel.item_img_label:hover{\n"
            "                    background-color:#ffffff;\n"
            "                    opacity: 1;\n"
            "                    }\n"
            "                   "
        )
        self.item_img_label.setScaledContents(True)
        self.item_img_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.item_img_label)

        self.item_view_layout.addWidget(self.item_img_frame)

        self.crafting_btn_frame = QFrame(self.item_view_frame)
        self.crafting_btn_frame.setObjectName("crafting_btn_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.crafting_btn_frame.sizePolicy().hasHeightForWidth()
        )
        self.crafting_btn_frame.setSizePolicy(sizePolicy4)
        self.crafting_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.crafting_btn_frame.setFrameShadow(QFrame.Raised)
        self.crafting_btn_layout = QVBoxLayout(self.crafting_btn_frame)
        self.crafting_btn_layout.setSpacing(0)
        self.crafting_btn_layout.setObjectName("crafting_btn_layout")
        self.crafting_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.crafting_btn_label = QLabel(self.crafting_btn_frame)
        self.crafting_btn_label.setObjectName("crafting_btn_label")
        sizePolicy3.setHeightForWidth(
            self.crafting_btn_label.sizePolicy().hasHeightForWidth()
        )
        self.crafting_btn_label.setSizePolicy(sizePolicy3)
        self.crafting_btn_label.setMinimumSize(QSize(0, 39))
        self.crafting_btn_label.setMaximumSize(QSize(128, 39))
        self.crafting_btn_label.setCursor(QCursor(Qt.ArrowCursor))
        self.crafting_btn_label.setFocusPolicy(Qt.StrongFocus)
        self.crafting_btn_label.setStyleSheet(
            "QLabel{\n"
            "                    background-image:\n"
            "                    url(:/images/images/craftbtn.png);\n"
            "                    }\n"
            "                    QLabel::hover{\n"
            "                    background-image:\n"
            "                    url(:/images/images/craftbtnov.png);\n"
            "                    }\n"
            "                   "
        )
        self.crafting_btn_label.setScaledContents(True)

        self.crafting_btn_layout.addWidget(self.crafting_btn_label)

        self.item_view_layout.addWidget(self.crafting_btn_frame, 0, Qt.AlignTop)

        self.item_display_layout.addWidget(self.item_view_frame)

        self.item_dps_frame = QFrame(self.item_display_frame)
        self.item_dps_frame.setObjectName("item_dps_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.item_dps_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_dps_frame.setSizePolicy(sizePolicy5)
        self.item_dps_frame.setFrameShape(QFrame.NoFrame)
        self.item_dps_frame.setFrameShadow(QFrame.Raised)
        self.item_dps_layout = QVBoxLayout(self.item_dps_frame)
        self.item_dps_layout.setSpacing(6)
        self.item_dps_layout.setObjectName("item_dps_layout")
        self.item_dps_layout.setContentsMargins(10, 10, 10, 10)
        self.phys_dps_label = QLabel(self.item_dps_frame)
        self.phys_dps_label.setObjectName("phys_dps_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.phys_dps_label.sizePolicy().hasHeightForWidth()
        )
        self.phys_dps_label.setSizePolicy(sizePolicy6)
        self.phys_dps_label.setMinimumSize(QSize(0, 30))
        self.phys_dps_label.setStyleSheet(
            "QLabel {\n"
            "                 border: 1px solid #edc57d;\n"
            "                 background: #000;\n"
            "                 padding: 2px 3px 4px 2px;\n"
            "                 }\n"
            "                "
        )
        self.phys_dps_label.setFrameShape(QFrame.NoFrame)
        self.phys_dps_label.setFrameShadow(QFrame.Plain)
        self.phys_dps_label.setLineWidth(0)
        self.phys_dps_label.setMidLineWidth(0)
        self.phys_dps_label.setScaledContents(False)
        self.phys_dps_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.phys_dps_label.setMargin(0)

        self.item_dps_layout.addWidget(self.phys_dps_label)

        self.ele_dps_label = QLabel(self.item_dps_frame)
        self.ele_dps_label.setObjectName("ele_dps_label")
        sizePolicy4.setHeightForWidth(
            self.ele_dps_label.sizePolicy().hasHeightForWidth()
        )
        self.ele_dps_label.setSizePolicy(sizePolicy4)
        self.ele_dps_label.setMinimumSize(QSize(0, 30))
        self.ele_dps_label.setStyleSheet(
            "QLabel {\n"
            "                 border: 1px solid #edc57d;\n"
            "                 background: #000;\n"
            "                 padding: 2px 3px 4px 2px;\n"
            "                 magin-bottom: 0px;\n"
            "                 }\n"
            "                "
        )

        self.item_dps_layout.addWidget(self.ele_dps_label)

        self.total_dps_label = QLabel(self.item_dps_frame)
        self.total_dps_label.setObjectName("total_dps_label")
        sizePolicy4.setHeightForWidth(
            self.total_dps_label.sizePolicy().hasHeightForWidth()
        )
        self.total_dps_label.setSizePolicy(sizePolicy4)
        self.total_dps_label.setMinimumSize(QSize(0, 30))
        self.total_dps_label.setStyleSheet(
            "QLabel {\n"
            "                 border: 1px solid #edc57d;\n"
            "                 background: #000;\n"
            "                 padding: 2px 3px 4px 2px;\n"
            "                 magin-bottom: 0px;\n"
            "                 }\n"
            "                "
        )

        self.item_dps_layout.addWidget(self.total_dps_label)

        self.affix_total_label = QLabel(self.item_dps_frame)
        self.affix_total_label.setObjectName("affix_total_label")
        sizePolicy4.setHeightForWidth(
            self.affix_total_label.sizePolicy().hasHeightForWidth()
        )
        self.affix_total_label.setSizePolicy(sizePolicy4)
        self.affix_total_label.setMinimumSize(QSize(0, 30))
        self.affix_total_label.setStyleSheet(
            "QLabel {\n"
            "                 border: 1px solid #edc57d;\n"
            "                 background: #000;\n"
            "                 padding: 2px 3px 4px 2px;\n"
            "                 magin-bottom: 0px;\n"
            "                 }\n"
            "                "
        )

        self.item_dps_layout.addWidget(self.affix_total_label, 0, Qt.AlignTop)

        self.item_display_layout.addWidget(self.item_dps_frame)

        self.item_display_layout.setStretch(0, 5)
        self.item_display_layout.setStretch(1, 2)

        self.crafting_emu_layout.addWidget(self.item_display_frame, 1, 2, 1, 1)

        self.item_info_container = QWidget(self.crafting_emu_page)
        self.item_info_container.setObjectName("item_info_container")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(
            self.item_info_container.sizePolicy().hasHeightForWidth()
        )
        self.item_info_container.setSizePolicy(sizePolicy7)
        self.item_info_container.setMinimumSize(QSize(400, 0))
        self.item_info_container.setMaximumSize(QSize(400, 16777215))
        self.item_info_container.setStyleSheet("background-color: black;")
        self.verticalLayout_4 = QVBoxLayout(self.item_info_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.item_info_frame = QFrame(self.item_info_container)
        self.item_info_frame.setObjectName("item_info_frame")
        sizePolicy7.setHeightForWidth(
            self.item_info_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_info_frame.setSizePolicy(sizePolicy7)
        self.item_info_frame.setMinimumSize(QSize(400, 0))
        self.item_info_frame.setMaximumSize(QSize(400, 16777215))
        self.item_info_frame.setFrameShape(QFrame.StyledPanel)
        self.item_info_frame.setFrameShadow(QFrame.Raised)
        self.item_info_layout = QVBoxLayout(self.item_info_frame)
        self.item_info_layout.setSpacing(0)
        self.item_info_layout.setObjectName("item_info_layout")
        self.item_info_layout.setContentsMargins(0, 0, 0, 0)
        self.item_header_frame = QFrame(self.item_info_frame)
        self.item_header_frame.setObjectName("item_header_frame")
        sizePolicy3.setHeightForWidth(
            self.item_header_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_header_frame.setSizePolicy(sizePolicy3)
        self.item_header_layout = QVBoxLayout(self.item_header_frame)
        self.item_header_layout.setSpacing(0)
        self.item_header_layout.setObjectName("item_header_layout")
        self.item_header_layout.setContentsMargins(0, 0, 0, 0)
        self.item_header_label = QLabel(self.item_header_frame)
        self.item_header_label.setObjectName("item_header_label")
        self.item_header_label.setEnabled(True)
        sizePolicy3.setHeightForWidth(
            self.item_header_label.sizePolicy().hasHeightForWidth()
        )
        self.item_header_label.setSizePolicy(sizePolicy3)
        self.item_header_label.setMinimumSize(QSize(400, 54))
        self.item_header_label.setMaximumSize(QSize(400, 54))
        font = QFont()
        font.setFamilies(["Open Sans"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.item_header_label.setFont(font)
        self.item_header_label.setStyleSheet(
            "QLabel {\n"
            "                                                                                background-image:\n"
            "                                                                                url(:/images/images/item-header-normal.png);\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_header_label.setTextFormat(Qt.RichText)
        self.item_header_label.setScaledContents(False)
        self.item_header_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.item_header_label.setWordWrap(True)

        self.item_header_layout.addWidget(self.item_header_label)

        self.item_info_layout.addWidget(self.item_header_frame, 0, Qt.AlignTop)

        self.item_affix_frame = QFrame(self.item_info_frame)
        self.item_affix_frame.setObjectName("item_affix_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(
            self.item_affix_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_affix_frame.setSizePolicy(sizePolicy8)
        self.item_affix_frame.setMinimumSize(QSize(400, 0))
        self.item_affix_frame.setMaximumSize(QSize(400, 16777215))
        self.item_affix_layout = QVBoxLayout(self.item_affix_frame)
        self.item_affix_layout.setSpacing(0)
        self.item_affix_layout.setObjectName("item_affix_layout")
        self.item_affix_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.item_affix_layout.setContentsMargins(0, 0, 0, 0)
        self.item_properties = QWidget(self.item_affix_frame)
        self.item_properties.setObjectName("item_properties")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(10)
        sizePolicy9.setHeightForWidth(
            self.item_properties.sizePolicy().hasHeightForWidth()
        )
        self.item_properties.setSizePolicy(sizePolicy9)
        self.item_properties.setMinimumSize(QSize(400, 0))
        self.item_properties.setMaximumSize(QSize(400, 16777215))
        self.properties_layout = QVBoxLayout(self.item_properties)
        self.properties_layout.setSpacing(0)
        self.properties_layout.setObjectName("properties_layout")
        self.properties_layout.setContentsMargins(0, 0, 0, 0)
        self.item_quality_label = QLabel(self.item_properties)
        self.item_quality_label.setObjectName("item_quality_label")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(
            self.item_quality_label.sizePolicy().hasHeightForWidth()
        )
        self.item_quality_label.setSizePolicy(sizePolicy10)
        self.item_quality_label.setMinimumSize(QSize(400, 0))
        self.item_quality_label.setMaximumSize(QSize(400, 40))
        self.item_quality_label.setAlignment(Qt.AlignCenter)
        self.item_quality_label.setIndent(0)

        self.properties_layout.addWidget(self.item_quality_label)

        self.item_properties_label = QLabel(self.item_properties)
        self.item_properties_label.setObjectName("item_properties_label")
        sizePolicy10.setHeightForWidth(
            self.item_properties_label.sizePolicy().hasHeightForWidth()
        )
        self.item_properties_label.setSizePolicy(sizePolicy10)
        self.item_properties_label.setMinimumSize(QSize(400, 0))
        self.item_properties_label.setMaximumSize(QSize(400, 400))
        self.item_properties_label.setStyleSheet(
            "QLabel{\n"
            "                                                                                color: #827a6c;\n"
            "                                                                                font-size: 14px;\n"
            "																				padding: 2px 10px;\n"
            "                                                                                text-align: center;\n"
            "                                                                                margin-bottom: 5px ;\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_properties_label.setTextFormat(Qt.RichText)
        self.item_properties_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.item_properties_label.setIndent(0)

        self.properties_layout.addWidget(self.item_properties_label)

        self.item_spacer_1 = QLabel(self.item_properties)
        self.item_spacer_1.setObjectName("item_spacer_1")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(
            self.item_spacer_1.sizePolicy().hasHeightForWidth()
        )
        self.item_spacer_1.setSizePolicy(sizePolicy11)
        self.item_spacer_1.setMinimumSize(QSize(400, 0))
        self.item_spacer_1.setMaximumSize(QSize(400, 2))
        self.item_spacer_1.setBaseSize(QSize(0, 0))
        self.item_spacer_1.setStyleSheet(
            "QLabel {\n"
            "                                                                                border-image: none;\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_spacer_1.setTextFormat(Qt.RichText)
        self.item_spacer_1.setPixmap(QPixmap(":/images/images/item-sep.png"))
        self.item_spacer_1.setScaledContents(False)
        self.item_spacer_1.setAlignment(Qt.AlignCenter)

        self.properties_layout.addWidget(self.item_spacer_1)

        self.item_affix_layout.addWidget(self.item_properties)

        self.item_requirements = QWidget(self.item_affix_frame)
        self.item_requirements.setObjectName("item_requirements")
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(2)
        sizePolicy12.setHeightForWidth(
            self.item_requirements.sizePolicy().hasHeightForWidth()
        )
        self.item_requirements.setSizePolicy(sizePolicy12)
        self.item_requirements.setMinimumSize(QSize(400, 0))
        self.item_requirements.setMaximumSize(QSize(400, 60))
        self.item_requirements_layout = QVBoxLayout(self.item_requirements)
        self.item_requirements_layout.setSpacing(0)
        self.item_requirements_layout.setObjectName("item_requirements_layout")
        self.item_requirements_layout.setContentsMargins(0, 0, 0, 0)
        self.item_level_label = QLabel(self.item_requirements)
        self.item_level_label.setObjectName("item_level_label")
        sizePolicy10.setHeightForWidth(
            self.item_level_label.sizePolicy().hasHeightForWidth()
        )
        self.item_level_label.setSizePolicy(sizePolicy10)
        self.item_level_label.setMinimumSize(QSize(400, 0))
        self.item_level_label.setMaximumSize(QSize(400, 20))
        self.item_level_label.setTabletTracking(False)
        self.item_level_label.setAlignment(Qt.AlignCenter)
        self.item_level_label.setIndent(0)

        self.item_requirements_layout.addWidget(self.item_level_label)

        self.item_requirements_label = QLabel(self.item_requirements)
        self.item_requirements_label.setObjectName("item_requirements_label")
        sizePolicy10.setHeightForWidth(
            self.item_requirements_label.sizePolicy().hasHeightForWidth()
        )
        self.item_requirements_label.setSizePolicy(sizePolicy10)
        self.item_requirements_label.setMinimumSize(QSize(400, 0))
        self.item_requirements_label.setMaximumSize(QSize(400, 25))
        self.item_requirements_label.setStyleSheet(
            "QLabel{\n"
            "                                                                                color: #827a6c;\n"
            "                                                                                padding: 2px 10px;\n"
            "                                                                                font-size: 14px;\n"
            "                                                                                line-height: 14px;\n"
            "                                                                                text-align: center;\n"
            "                                                                                margin: 0;\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_requirements_label.setLineWidth(0)
        self.item_requirements_label.setMidLineWidth(0)
        self.item_requirements_label.setTextFormat(Qt.RichText)
        self.item_requirements_label.setScaledContents(False)
        self.item_requirements_label.setAlignment(Qt.AlignCenter)
        self.item_requirements_label.setIndent(0)

        self.item_requirements_layout.addWidget(self.item_requirements_label)

        self.item_spacer_2 = QLabel(self.item_requirements)
        self.item_spacer_2.setObjectName("item_spacer_2")
        sizePolicy11.setHeightForWidth(
            self.item_spacer_2.sizePolicy().hasHeightForWidth()
        )
        self.item_spacer_2.setSizePolicy(sizePolicy11)
        self.item_spacer_2.setMinimumSize(QSize(400, 0))
        self.item_spacer_2.setMaximumSize(QSize(400, 2))
        self.item_spacer_2.setBaseSize(QSize(0, 0))
        self.item_spacer_2.setStyleSheet(
            "QLabel {\n"
            "                                                                                border-image: none;\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_spacer_2.setTextFormat(Qt.RichText)
        self.item_spacer_2.setPixmap(QPixmap(":/images/images/item-sep.png"))
        self.item_spacer_2.setScaledContents(False)
        self.item_spacer_2.setAlignment(Qt.AlignCenter)

        self.item_requirements_layout.addWidget(self.item_spacer_2, 0, Qt.AlignBottom)

        self.item_affix_layout.addWidget(self.item_requirements)

        self.item_implicits = QWidget(self.item_affix_frame)
        self.item_implicits.setObjectName("item_implicits")
        self.item_implicits.setEnabled(False)
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(5)
        sizePolicy13.setHeightForWidth(
            self.item_implicits.sizePolicy().hasHeightForWidth()
        )
        self.item_implicits.setSizePolicy(sizePolicy13)
        self.item_implicits.setMinimumSize(QSize(400, 0))
        self.item_implicits.setMaximumSize(QSize(400, 90))
        self.implicits_layout = QVBoxLayout(self.item_implicits)
        self.implicits_layout.setSpacing(0)
        self.implicits_layout.setObjectName("implicits_layout")
        self.implicits_layout.setContentsMargins(0, 0, 0, 0)
        self.item_implicits_label = QLabel(self.item_implicits)
        self.item_implicits_label.setObjectName("item_implicits_label")
        self.item_implicits_label.setEnabled(False)
        sizePolicy10.setHeightForWidth(
            self.item_implicits_label.sizePolicy().hasHeightForWidth()
        )
        self.item_implicits_label.setSizePolicy(sizePolicy10)
        self.item_implicits_label.setMinimumSize(QSize(400, 0))
        self.item_implicits_label.setMaximumSize(QSize(400, 90))
        self.item_implicits_label.setStyleSheet(
            "QLabel{\n"
            "                                                                                color: #8787fe;\n"
            "                                                                                padding: 2px 10px;\n"
            "                                                                                font-size: 14px;\n"
            "                                                                                line-height: 14px;\n"
            "                                                                                text-align: center;\n"
            "                                                                                margin: 0;\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_implicits_label.setLineWidth(1)
        self.item_implicits_label.setTextFormat(Qt.RichText)
        self.item_implicits_label.setAlignment(Qt.AlignCenter)
        self.item_implicits_label.setWordWrap(True)

        self.implicits_layout.addWidget(self.item_implicits_label)

        self.item_affix_layout.addWidget(self.item_implicits, 0, Qt.AlignHCenter)

        self.item_spacer_3 = QLabel(self.item_affix_frame)
        self.item_spacer_3.setObjectName("item_spacer_3")
        self.item_spacer_3.setEnabled(False)
        sizePolicy11.setHeightForWidth(
            self.item_spacer_3.sizePolicy().hasHeightForWidth()
        )
        self.item_spacer_3.setSizePolicy(sizePolicy11)
        self.item_spacer_3.setMinimumSize(QSize(400, 0))
        self.item_spacer_3.setMaximumSize(QSize(400, 2))
        self.item_spacer_3.setBaseSize(QSize(0, 0))
        self.item_spacer_3.setStyleSheet(
            "QLabel {\n"
            "                                                                                border-image: none;\n"
            "																				background-color: rgb(0, 0, 0);\n"
            "                                                                                }\n"
            "                                                                            "
        )
        self.item_spacer_3.setTextFormat(Qt.RichText)
        self.item_spacer_3.setPixmap(QPixmap(":/images/images/item-sep.png"))
        self.item_spacer_3.setScaledContents(False)
        self.item_spacer_3.setAlignment(Qt.AlignCenter)

        self.item_affix_layout.addWidget(self.item_spacer_3)

        self.item_info_layout.addWidget(self.item_affix_frame)

        self.item_mod_frame = QFrame(self.item_info_frame)
        self.item_mod_frame.setObjectName("item_mod_frame")
        sizePolicy14 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(10)
        sizePolicy14.setHeightForWidth(
            self.item_mod_frame.sizePolicy().hasHeightForWidth()
        )
        self.item_mod_frame.setSizePolicy(sizePolicy14)
        self.item_mod_frame.setMinimumSize(QSize(400, 0))
        self.item_mod_frame.setMaximumSize(QSize(400, 16777215))
        self.item_mod_layout = QVBoxLayout(self.item_mod_frame)
        self.item_mod_layout.setSpacing(0)
        self.item_mod_layout.setObjectName("item_mod_layout")
        self.item_mod_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.item_mod_layout.setContentsMargins(0, 0, 0, 0)
        self.prefix_1 = QWidget(self.item_mod_frame)
        self.prefix_1.setObjectName("prefix_1")
        sizePolicy15 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.prefix_1.sizePolicy().hasHeightForWidth())
        self.prefix_1.setSizePolicy(sizePolicy15)
        self.prefix_1.setMinimumSize(QSize(400, 0))
        self.prefix_1.setMaximumSize(QSize(400, 80))
        self.prefix_1_layout = QVBoxLayout(self.prefix_1)
        self.prefix_1_layout.setSpacing(0)
        self.prefix_1_layout.setObjectName("prefix_1_layout")
        self.prefix_1_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.prefix_1_layout.setContentsMargins(0, 0, 0, 0)
        self.prefix_info_1 = QLabel(self.prefix_1)
        self.prefix_info_1.setObjectName("prefix_info_1")
        self.prefix_info_1.setEnabled(True)
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(
            self.prefix_info_1.sizePolicy().hasHeightForWidth()
        )
        self.prefix_info_1.setSizePolicy(sizePolicy16)
        self.prefix_info_1.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies(["Open Sans"])
        font1.setBold(False)
        font1.setItalic(False)
        self.prefix_info_1.setFont(font1)
        self.prefix_info_1.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.prefix_info_1.setTextFormat(Qt.RichText)
        self.prefix_info_1.setAlignment(Qt.AlignCenter)

        self.prefix_1_layout.addWidget(self.prefix_info_1, 0, Qt.AlignTop)

        self.prefix_1_stat_text = QLabel(self.prefix_1)
        self.prefix_1_stat_text.setObjectName("prefix_1_stat_text")
        self.prefix_1_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.prefix_1_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.prefix_1_stat_text.setSizePolicy(sizePolicy15)
        self.prefix_1_stat_text.setMinimumSize(QSize(400, 0))
        self.prefix_1_stat_text.setMaximumSize(QSize(400, 16777215))
        self.prefix_1_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.prefix_1_stat_text.setTextFormat(Qt.RichText)
        self.prefix_1_stat_text.setAlignment(Qt.AlignCenter)

        self.prefix_1_layout.addWidget(self.prefix_1_stat_text, 0, Qt.AlignTop)

        self.item_mod_layout.addWidget(self.prefix_1)

        self.prefix_2 = QWidget(self.item_mod_frame)
        self.prefix_2.setObjectName("prefix_2")
        sizePolicy15.setHeightForWidth(self.prefix_2.sizePolicy().hasHeightForWidth())
        self.prefix_2.setSizePolicy(sizePolicy15)
        self.prefix_2.setMinimumSize(QSize(400, 0))
        self.prefix_2.setMaximumSize(QSize(400, 80))
        self.prefix_2_layout = QVBoxLayout(self.prefix_2)
        self.prefix_2_layout.setSpacing(0)
        self.prefix_2_layout.setObjectName("prefix_2_layout")
        self.prefix_2_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.prefix_2_layout.setContentsMargins(0, 0, 0, 0)
        self.prefix_info_2 = QLabel(self.prefix_2)
        self.prefix_info_2.setObjectName("prefix_info_2")
        self.prefix_info_2.setEnabled(True)
        sizePolicy16.setHeightForWidth(
            self.prefix_info_2.sizePolicy().hasHeightForWidth()
        )
        self.prefix_info_2.setSizePolicy(sizePolicy16)
        self.prefix_info_2.setMinimumSize(QSize(0, 0))
        self.prefix_info_2.setFont(font1)
        self.prefix_info_2.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.prefix_info_2.setTextFormat(Qt.RichText)
        self.prefix_info_2.setAlignment(Qt.AlignCenter)

        self.prefix_2_layout.addWidget(self.prefix_info_2, 0, Qt.AlignTop)

        self.prefix_2_stat_text = QLabel(self.prefix_2)
        self.prefix_2_stat_text.setObjectName("prefix_2_stat_text")
        self.prefix_2_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.prefix_2_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.prefix_2_stat_text.setSizePolicy(sizePolicy15)
        self.prefix_2_stat_text.setMinimumSize(QSize(0, 0))
        self.prefix_2_stat_text.setMaximumSize(QSize(400, 16777215))
        self.prefix_2_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.prefix_2_stat_text.setTextFormat(Qt.RichText)
        self.prefix_2_stat_text.setAlignment(Qt.AlignCenter)

        self.prefix_2_layout.addWidget(self.prefix_2_stat_text)

        self.item_mod_layout.addWidget(self.prefix_2)

        self.prefix_3 = QWidget(self.item_mod_frame)
        self.prefix_3.setObjectName("prefix_3")
        sizePolicy15.setHeightForWidth(self.prefix_3.sizePolicy().hasHeightForWidth())
        self.prefix_3.setSizePolicy(sizePolicy15)
        self.prefix_3.setMinimumSize(QSize(400, 0))
        self.prefix_3.setMaximumSize(QSize(400, 80))
        self.prefix_3_layout = QVBoxLayout(self.prefix_3)
        self.prefix_3_layout.setSpacing(0)
        self.prefix_3_layout.setObjectName("prefix_3_layout")
        self.prefix_3_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.prefix_3_layout.setContentsMargins(0, 0, 0, 0)
        self.prefix_info_3 = QLabel(self.prefix_3)
        self.prefix_info_3.setObjectName("prefix_info_3")
        self.prefix_info_3.setEnabled(True)
        sizePolicy16.setHeightForWidth(
            self.prefix_info_3.sizePolicy().hasHeightForWidth()
        )
        self.prefix_info_3.setSizePolicy(sizePolicy16)
        self.prefix_info_3.setMinimumSize(QSize(0, 0))
        self.prefix_info_3.setFont(font1)
        self.prefix_info_3.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.prefix_info_3.setTextFormat(Qt.RichText)
        self.prefix_info_3.setAlignment(Qt.AlignCenter)

        self.prefix_3_layout.addWidget(self.prefix_info_3)

        self.prefix_3_stat_text = QLabel(self.prefix_3)
        self.prefix_3_stat_text.setObjectName("prefix_3_stat_text")
        self.prefix_3_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.prefix_3_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.prefix_3_stat_text.setSizePolicy(sizePolicy15)
        self.prefix_3_stat_text.setMinimumSize(QSize(0, 0))
        self.prefix_3_stat_text.setMaximumSize(QSize(400, 16777215))
        self.prefix_3_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.prefix_3_stat_text.setTextFormat(Qt.RichText)
        self.prefix_3_stat_text.setAlignment(Qt.AlignCenter)

        self.prefix_3_layout.addWidget(self.prefix_3_stat_text)

        self.item_mod_layout.addWidget(self.prefix_3)

        self.suffix_2 = QWidget(self.item_mod_frame)
        self.suffix_2.setObjectName("suffix_2")
        sizePolicy15.setHeightForWidth(self.suffix_2.sizePolicy().hasHeightForWidth())
        self.suffix_2.setSizePolicy(sizePolicy15)
        self.suffix_2.setMinimumSize(QSize(400, 0))
        self.suffix_2.setMaximumSize(QSize(400, 80))
        self.suffix_2_layout = QVBoxLayout(self.suffix_2)
        self.suffix_2_layout.setSpacing(0)
        self.suffix_2_layout.setObjectName("suffix_2_layout")
        self.suffix_2_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.suffix_2_layout.setContentsMargins(0, 0, 0, 0)
        self.suffix_2_info = QLabel(self.suffix_2)
        self.suffix_2_info.setObjectName("suffix_2_info")
        self.suffix_2_info.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_2_info.sizePolicy().hasHeightForWidth()
        )
        self.suffix_2_info.setSizePolicy(sizePolicy15)
        self.suffix_2_info.setMinimumSize(QSize(400, 0))
        self.suffix_2_info.setMaximumSize(QSize(400, 16777215))
        self.suffix_2_info.setFont(font1)
        self.suffix_2_info.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.suffix_2_info.setTextFormat(Qt.RichText)
        self.suffix_2_info.setAlignment(Qt.AlignCenter)

        self.suffix_2_layout.addWidget(self.suffix_2_info)

        self.suffix_2_stat_text = QLabel(self.suffix_2)
        self.suffix_2_stat_text.setObjectName("suffix_2_stat_text")
        self.suffix_2_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_2_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.suffix_2_stat_text.setSizePolicy(sizePolicy15)
        self.suffix_2_stat_text.setMinimumSize(QSize(400, 0))
        self.suffix_2_stat_text.setMaximumSize(QSize(400, 16777215))
        self.suffix_2_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.suffix_2_stat_text.setTextFormat(Qt.RichText)
        self.suffix_2_stat_text.setAlignment(Qt.AlignCenter)

        self.suffix_2_layout.addWidget(self.suffix_2_stat_text)

        self.item_mod_layout.addWidget(self.suffix_2)

        self.suffix_1 = QWidget(self.item_mod_frame)
        self.suffix_1.setObjectName("suffix_1")
        sizePolicy15.setHeightForWidth(self.suffix_1.sizePolicy().hasHeightForWidth())
        self.suffix_1.setSizePolicy(sizePolicy15)
        self.suffix_1.setMinimumSize(QSize(400, 0))
        self.suffix_1.setMaximumSize(QSize(400, 80))
        self.suffix_1_layout = QVBoxLayout(self.suffix_1)
        self.suffix_1_layout.setSpacing(0)
        self.suffix_1_layout.setObjectName("suffix_1_layout")
        self.suffix_1_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.suffix_1_layout.setContentsMargins(0, 0, 0, 0)
        self.suffix_1_info = QLabel(self.suffix_1)
        self.suffix_1_info.setObjectName("suffix_1_info")
        self.suffix_1_info.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_1_info.sizePolicy().hasHeightForWidth()
        )
        self.suffix_1_info.setSizePolicy(sizePolicy15)
        self.suffix_1_info.setMinimumSize(QSize(400, 0))
        self.suffix_1_info.setMaximumSize(QSize(400, 16777215))
        self.suffix_1_info.setFont(font1)
        self.suffix_1_info.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.suffix_1_info.setTextFormat(Qt.RichText)
        self.suffix_1_info.setAlignment(Qt.AlignCenter)

        self.suffix_1_layout.addWidget(self.suffix_1_info)

        self.suffix_1_stat_text = QLabel(self.suffix_1)
        self.suffix_1_stat_text.setObjectName("suffix_1_stat_text")
        self.suffix_1_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_1_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.suffix_1_stat_text.setSizePolicy(sizePolicy15)
        self.suffix_1_stat_text.setMinimumSize(QSize(400, 0))
        self.suffix_1_stat_text.setMaximumSize(QSize(400, 16777215))
        self.suffix_1_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.suffix_1_stat_text.setTextFormat(Qt.RichText)
        self.suffix_1_stat_text.setAlignment(Qt.AlignCenter)

        self.suffix_1_layout.addWidget(self.suffix_1_stat_text)

        self.item_mod_layout.addWidget(self.suffix_1)

        self.suffix_3 = QWidget(self.item_mod_frame)
        self.suffix_3.setObjectName("suffix_3")
        sizePolicy15.setHeightForWidth(self.suffix_3.sizePolicy().hasHeightForWidth())
        self.suffix_3.setSizePolicy(sizePolicy15)
        self.suffix_3.setMinimumSize(QSize(400, 0))
        self.suffix_3.setMaximumSize(QSize(400, 80))
        self.suffix_3_layout = QVBoxLayout(self.suffix_3)
        self.suffix_3_layout.setSpacing(0)
        self.suffix_3_layout.setObjectName("suffix_3_layout")
        self.suffix_3_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.suffix_3_layout.setContentsMargins(0, 0, 0, 0)
        self.suffix_3_info = QLabel(self.suffix_3)
        self.suffix_3_info.setObjectName("suffix_3_info")
        self.suffix_3_info.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_3_info.sizePolicy().hasHeightForWidth()
        )
        self.suffix_3_info.setSizePolicy(sizePolicy15)
        self.suffix_3_info.setMinimumSize(QSize(400, 0))
        self.suffix_3_info.setMaximumSize(QSize(400, 16777215))
        self.suffix_3_info.setFont(font1)
        self.suffix_3_info.setStyleSheet(
            "QLabel {\n"
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
            "                                                                            "
        )
        self.suffix_3_info.setTextFormat(Qt.RichText)
        self.suffix_3_info.setAlignment(Qt.AlignCenter)

        self.suffix_3_layout.addWidget(self.suffix_3_info)

        self.suffix_3_stat_text = QLabel(self.suffix_3)
        self.suffix_3_stat_text.setObjectName("suffix_3_stat_text")
        self.suffix_3_stat_text.setEnabled(True)
        sizePolicy15.setHeightForWidth(
            self.suffix_3_stat_text.sizePolicy().hasHeightForWidth()
        )
        self.suffix_3_stat_text.setSizePolicy(sizePolicy15)
        self.suffix_3_stat_text.setMinimumSize(QSize(400, 0))
        self.suffix_3_stat_text.setMaximumSize(QSize(400, 16777215))
        self.suffix_3_stat_text.setStyleSheet(
            "QLabel {\n"
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
            "                                                                       "
        )
        self.suffix_3_stat_text.setTextFormat(Qt.RichText)
        self.suffix_3_stat_text.setAlignment(Qt.AlignCenter)

        self.suffix_3_layout.addWidget(self.suffix_3_stat_text)

        self.item_mod_layout.addWidget(self.suffix_3)

        self.item_mod_layout.setStretch(0, 3)
        self.item_mod_layout.setStretch(1, 3)
        self.item_mod_layout.setStretch(2, 3)
        self.item_mod_layout.setStretch(3, 3)
        self.item_mod_layout.setStretch(4, 3)
        self.item_mod_layout.setStretch(5, 3)

        self.item_info_layout.addWidget(self.item_mod_frame)

        self.verticalLayout_4.addWidget(self.item_info_frame)

        self.crafting_emu_layout.addWidget(self.item_info_container, 1, 1, 1, 1)

        self.mod_widget_layout = QHBoxLayout()
        self.mod_widget_layout.setSpacing(0)
        self.mod_widget_layout.setObjectName("mod_widget_layout")
        self.mod_widget_layout.setContentsMargins(-1, 0, -1, -1)

        self.crafting_emu_layout.addLayout(self.mod_widget_layout, 2, 0, 1, 4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.crafting_emu_layout.addLayout(self.horizontalLayout, 0, 0, 1, 4)

        self.crafting_emu_layout.setRowStretch(0, 1)
        self.crafting_emu_layout.setRowStretch(1, 3)
        self.crafting_emu_layout.setRowStretch(2, 12)
        self.crafting_emu_layout.setColumnStretch(0, 1)
        self.crafting_emu_layout.setColumnStretch(1, 4)
        self.crafting_emu_layout.setColumnStretch(2, 3)
        self.crafting_emu_layout.setColumnStretch(3, 1)
        self.pages.addWidget(self.crafting_emu_page)
        self.crafting_calc_page = QWidget()
        self.crafting_calc_page.setObjectName("crafting_calc_page")
        self.crafting_calc_page.setStyleSheet(
            "QFrame {\n"
            "        border-image: none;\n"
            "        font-size: 16pt;\n"
            "        }\n"
            "       "
        )
        self.crafting_calc_vertical_layout = QVBoxLayout(self.crafting_calc_page)
        self.crafting_calc_vertical_layout.setSpacing(0)
        self.crafting_calc_vertical_layout.setObjectName(
            "crafting_calc_vertical_layout"
        )
        self.crafting_calc_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.crafting_calclayout = QVBoxLayout()
        self.crafting_calclayout.setObjectName("crafting_calclayout")
        self.crafting_calclayout.setContentsMargins(0, 0, 0, 0)
        self.search_bar_frame = QFrame(self.crafting_calc_page)
        self.search_bar_frame.setObjectName("search_bar_frame")
        sizePolicy4.setHeightForWidth(
            self.search_bar_frame.sizePolicy().hasHeightForWidth()
        )
        self.search_bar_frame.setSizePolicy(sizePolicy4)
        self.search_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.search_bar_frame.setFrameShadow(QFrame.Raised)
        self.search_bar_layout = QHBoxLayout(self.search_bar_frame)
        self.search_bar_layout.setSpacing(10)
        self.search_bar_layout.setObjectName("search_bar_layout")
        self.search_bar_layout.setContentsMargins(0, 10, 0, 10)
        self.search_bar = QLineEdit(self.search_bar_frame)
        self.search_bar.setObjectName("search_bar")
        sizePolicy5.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy5)
        self.search_bar.setStyleSheet(
            "QLineEdit {\n"
            "border-image: none;\n"
            "background-color: black;\n"
            "color: #FFEEBB;\n"
            "height: 40px;\n"
            "line-height: 40px;\n"
            "padding: 0px 25px 0px 10px;\n"
            "vertical-align: top;\n"
            "border: none;\n"
            "font-size: 16px;\n"
            "}\n"
            ""
        )
        self.search_bar.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.search_bar_layout.addWidget(self.search_bar)

        self.reset_btn = QPushButton(self.search_bar_frame)
        self.reset_btn.setObjectName("reset_btn")
        sizePolicy17 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.reset_btn.sizePolicy().hasHeightForWidth())
        self.reset_btn.setSizePolicy(sizePolicy17)
        font2 = QFont()
        font2.setBold(True)
        self.reset_btn.setFont(font2)
        self.reset_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "line-height: 36px;\n"
            "font-weight: bold;\n"
            "font-size: 16px;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #999;\n"
            "padding: 0px 10px;\n"
            "text-shadow: 0 1px 2px #6f1c0e, 0 1px 0 #6f1c0e;\n"
            "color: #fff;\n"
            "box-shadow: inset 0 1px 1px #94dda6, 0 1px 2px rgba(0,0,0,0.61);\n"
            "border-color: #1d692d;\n"
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(93, 187, 115, 255), stop:1 rgba(45, 144, 71, 255));\n"
            "}"
        )

        self.search_bar_layout.addWidget(self.reset_btn)

        self.import_btn = QPushButton(self.search_bar_frame)
        self.import_btn.setObjectName("import_btn")
        sizePolicy17.setHeightForWidth(self.import_btn.sizePolicy().hasHeightForWidth())
        self.import_btn.setSizePolicy(sizePolicy17)
        self.import_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "line-height: 36px;\n"
            "font-weight: bold;\n"
            "font-size: 16px;\n"
            "border-radius: 4px;\n"
            "border: 1px solid #999;\n"
            "padding: 0px 10px;\n"
            "text-shadow: 0 1px 2px #6f1c0e, 0 1px 0 #6f1c0e;\n"
            "color: #fff;\n"
            "box-shadow: inset 0 1px 1px #94dda6, 0 1px 2px rgba(0,0,0,0.61);\n"
            "border-color: #1d692d;\n"
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(93, 187, 115, 255), stop:1 rgba(45, 144, 71, 255));\n"
            "}"
        )

        self.search_bar_layout.addWidget(self.import_btn)

        self.lineEdit = QLineEdit(self.search_bar_frame)
        self.lineEdit.setObjectName("lineEdit")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy18)
        self.lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "border-image: none;\n"
            "background-color: black;\n"
            "color: #FFEEBB;\n"
            "height: 40px;\n"
            "line-height: 40px;\n"
            "padding: 0px 25px 0px 10px;\n"
            "vertical-align: top;\n"
            "border: none;\n"
            "font-size: 16px;\n"
            "}\n"
            ""
        )

        self.search_bar_layout.addWidget(self.lineEdit)

        self.crafting_calclayout.addWidget(self.search_bar_frame)

        self.label = QLabel(self.crafting_calc_page)
        self.label.setObjectName("label")
        sizePolicy19 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy19)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)

        self.crafting_calclayout.addWidget(self.label)

        self.crafting_calc_btns_frame = QFrame(self.crafting_calc_page)
        self.crafting_calc_btns_frame.setObjectName("crafting_calc_btns_frame")
        sizePolicy4.setHeightForWidth(
            self.crafting_calc_btns_frame.sizePolicy().hasHeightForWidth()
        )
        self.crafting_calc_btns_frame.setSizePolicy(sizePolicy4)
        self.crafting_method_options = QGridLayout(self.crafting_calc_btns_frame)
        self.crafting_method_options.setSpacing(0)
        self.crafting_method_options.setObjectName("crafting_method_options")
        self.crafting_method_options.setContentsMargins(0, 0, 0, 0)
        self.fossil_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.fossil_calc_btn.setObjectName("fossil_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.fossil_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.fossil_calc_btn.setSizePolicy(sizePolicy5)
        self.fossil_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(
            ":/crafting_methods/images/crafting_methods/method_fossil.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.fossil_calc_btn.setIcon(icon)
        self.fossil_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.fossil_calc_btn, 1, 0, 1, 1)

        self.exalt_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.exalt_calc_btn.setObjectName("exalt_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.exalt_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.exalt_calc_btn.setSizePolicy(sizePolicy5)
        self.exalt_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(
            ":/crafting_methods/images/crafting_methods/method_exalted.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.exalt_calc_btn.setIcon(icon1)
        self.exalt_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.exalt_calc_btn, 1, 3, 1, 1)

        self.essences_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.essences_calc_btn.setObjectName("essences_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.essences_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.essences_calc_btn.setSizePolicy(sizePolicy5)
        self.essences_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(
            ":/crafting_methods/images/crafting_methods/method_essence.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.essences_calc_btn.setIcon(icon2)
        self.essences_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.essences_calc_btn, 1, 1, 1, 1)

        self.chaos_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.chaos_calc_btn.setObjectName("chaos_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.chaos_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.chaos_calc_btn.setSizePolicy(sizePolicy5)
        self.chaos_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon3 = QIcon()
        icon3.addFile(
            ":/crafting_methods/images/crafting_methods/method_chaos.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.chaos_calc_btn.setIcon(icon3)
        self.chaos_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.chaos_calc_btn, 1, 2, 1, 1)

        self.alch_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.alch_calc_btn.setObjectName("alch_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.alch_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.alch_calc_btn.setSizePolicy(sizePolicy5)
        self.alch_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            ":/crafting_methods/images/crafting_methods/method_alchemy.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.alch_calc_btn.setIcon(icon4)
        self.alch_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.alch_calc_btn, 1, 4, 1, 1)

        self.hunter_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.hunter_calc_btn.setObjectName("hunter_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.hunter_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.hunter_calc_btn.setSizePolicy(sizePolicy5)
        self.hunter_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile(
            ":/crafting_methods/images/crafting_methods/method_hunter.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.hunter_calc_btn.setIcon(icon5)
        self.hunter_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.hunter_calc_btn, 3, 0, 1, 1)

        self.redeemer_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.redeemer_calc_btn.setObjectName("redeemer_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.redeemer_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.redeemer_calc_btn.setSizePolicy(sizePolicy5)
        self.redeemer_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon6 = QIcon()
        icon6.addFile(
            ":/crafting_methods/images/crafting_methods/method_redeemer.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.redeemer_calc_btn.setIcon(icon6)
        self.redeemer_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.redeemer_calc_btn, 3, 1, 1, 1)

        self.warlord_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.warlord_calc_btn.setObjectName("warlord_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.warlord_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.warlord_calc_btn.setSizePolicy(sizePolicy5)
        self.warlord_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon7 = QIcon()
        icon7.addFile(
            ":/crafting_methods/images/crafting_methods/method_warlord.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.warlord_calc_btn.setIcon(icon7)
        self.warlord_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.warlord_calc_btn, 3, 2, 1, 1)

        self.annul_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.annul_calc_btn.setObjectName("annul_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.annul_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.annul_calc_btn.setSizePolicy(sizePolicy5)
        self.annul_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon8 = QIcon()
        icon8.addFile(
            ":/crafting_methods/images/crafting_methods/method_annul.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.annul_calc_btn.setIcon(icon8)
        self.annul_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.annul_calc_btn, 3, 3, 1, 1)

        self.metacraft_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.metacraft_calc_btn.setObjectName("metacraft_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.metacraft_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.metacraft_calc_btn.setSizePolicy(sizePolicy5)
        self.metacraft_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon9 = QIcon()
        icon9.addFile(
            ":/crafting_methods/images/crafting_methods/method_meta.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.metacraft_calc_btn.setIcon(icon9)
        self.metacraft_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.metacraft_calc_btn, 3, 4, 1, 1)

        self.crusader_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.crusader_calc_btn.setObjectName("crusader_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.crusader_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.crusader_calc_btn.setSizePolicy(sizePolicy5)
        self.crusader_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon10 = QIcon()
        icon10.addFile(
            ":/crafting_methods/images/crafting_methods/method_crusader.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.crusader_calc_btn.setIcon(icon10)
        self.crusader_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.crusader_calc_btn, 2, 4, 1, 1)

        self.regal_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.regal_calc_btn.setObjectName("regal_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.regal_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.regal_calc_btn.setSizePolicy(sizePolicy5)
        self.regal_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon11 = QIcon()
        icon11.addFile(
            ":/crafting_methods/images/crafting_methods/method_regal.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.regal_calc_btn.setIcon(icon11)
        self.regal_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.regal_calc_btn, 2, 3, 1, 1)

        self.transmute_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.transmute_calc_btn.setObjectName("transmute_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.transmute_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.transmute_calc_btn.setSizePolicy(sizePolicy5)
        self.transmute_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon12 = QIcon()
        icon12.addFile(
            ":/crafting_methods/images/crafting_methods/method_transmute.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.transmute_calc_btn.setIcon(icon12)
        self.transmute_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.transmute_calc_btn, 2, 2, 1, 1)

        self.aug_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.aug_calc_btn.setObjectName("aug_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.aug_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.aug_calc_btn.setSizePolicy(sizePolicy5)
        self.aug_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon13 = QIcon()
        icon13.addFile(
            ":/crafting_methods/images/crafting_methods/method_augmentation.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.aug_calc_btn.setIcon(icon13)
        self.aug_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.aug_calc_btn, 2, 1, 1, 1)

        self.alt_calc_btn = QPushButton(self.crafting_calc_btns_frame)
        self.alt_calc_btn.setObjectName("alt_calc_btn")
        sizePolicy5.setHeightForWidth(
            self.alt_calc_btn.sizePolicy().hasHeightForWidth()
        )
        self.alt_calc_btn.setSizePolicy(sizePolicy5)
        self.alt_calc_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "background-color: #444;\n"
            "text-shadow: 1px 1px #000;\n"
            "padding: 10px;\n"
            "border-right: 1px solid #333;\n"
            "border-bottom: 1px solid #333;\n"
            "color: #fff;\n"
            "}"
        )
        icon14 = QIcon()
        icon14.addFile(
            ":/crafting_methods/images/crafting_methods/method_alteration.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.alt_calc_btn.setIcon(icon14)
        self.alt_calc_btn.setIconSize(QSize(30, 30))

        self.crafting_method_options.addWidget(self.alt_calc_btn, 2, 0, 1, 1)

        self.crafting_method_options.setRowStretch(0, 5)
        self.crafting_method_options.setRowStretch(1, 5)
        self.crafting_method_options.setRowStretch(2, 5)
        self.crafting_method_options.setRowStretch(3, 5)
        self.crafting_method_options.setColumnStretch(0, 10)
        self.crafting_method_options.setColumnStretch(1, 10)
        self.crafting_method_options.setColumnStretch(2, 10)
        self.crafting_method_options.setColumnStretch(3, 10)
        self.crafting_method_options.setColumnStretch(4, 10)

        self.crafting_calclayout.addWidget(self.crafting_calc_btns_frame)

        self.affix_search_bar_frame = QFrame(self.crafting_calc_page)
        self.affix_search_bar_frame.setObjectName("affix_search_bar_frame")
        sizePolicy5.setHeightForWidth(
            self.affix_search_bar_frame.sizePolicy().hasHeightForWidth()
        )
        self.affix_search_bar_frame.setSizePolicy(sizePolicy5)
        self.affix_search_bar_frame.setFrameShape(QFrame.NoFrame)
        self.affix_search_bar_frame.setFrameShadow(QFrame.Raised)
        self.affix_search_bar_layout = QHBoxLayout(self.affix_search_bar_frame)
        self.affix_search_bar_layout.setSpacing(10)
        self.affix_search_bar_layout.setObjectName("affix_search_bar_layout")
        self.affix_search_bar_layout.setContentsMargins(10, 10, 10, 10)
        self.affix_search_bar = QLineEdit(self.affix_search_bar_frame)
        self.affix_search_bar.setObjectName("affix_search_bar")
        sizePolicy6.setHeightForWidth(
            self.affix_search_bar.sizePolicy().hasHeightForWidth()
        )
        self.affix_search_bar.setSizePolicy(sizePolicy6)
        self.affix_search_bar.setStyleSheet(
            "QLineEdit {\n"
            "border-image: none;\n"
            "background-color: black;\n"
            "color: #FFEEBB;\n"
            "height: 40px;\n"
            "line-height: 40px;\n"
            "padding: 0px 25px 0px 10px;\n"
            "vertical-align: top;\n"
            "border: none;\n"
            "font-size: 16px;\n"
            "}\n"
            ""
        )

        self.affix_search_bar_layout.addWidget(self.affix_search_bar)

        self.close_filters_btn = QPushButton(self.affix_search_bar_frame)
        self.close_filters_btn.setObjectName("close_filters_btn")
        sizePolicy1.setHeightForWidth(
            self.close_filters_btn.sizePolicy().hasHeightForWidth()
        )
        self.close_filters_btn.setSizePolicy(sizePolicy1)
        self.close_filters_btn.setMaximumSize(QSize(16777215, 40))
        self.close_filters_btn.setFont(font2)
        self.close_filters_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 16px;\n"
            "font-weight: bold;\n"
            "border-radius: 4px;\n"
            "padding: 0px 10px;\n"
            "box-shadow: inset 0 1px 1px #1574d4, 0 1px 2px rgba(14, 84, 156,0.31);\n"
            "border: 1px solid #093663;\n"
            "text-shadow: 1px 1px #093663;\n"
            "color: #FFF;\n"
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(14, 95, 176, 255), stop:1 rgba(3, 173, 252, 255));\n"
            "}"
        )

        self.affix_search_bar_layout.addWidget(self.close_filters_btn)

        self.open_groups_btn = QPushButton(self.affix_search_bar_frame)
        self.open_groups_btn.setObjectName("open_groups_btn")
        sizePolicy20 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(
            self.open_groups_btn.sizePolicy().hasHeightForWidth()
        )
        self.open_groups_btn.setSizePolicy(sizePolicy20)
        self.open_groups_btn.setMaximumSize(QSize(16777215, 40))
        self.open_groups_btn.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "vertical-align: middle;\n"
            "font-weight: bold;\n"
            "font-size: 16px;\n"
            "border-radius: 4px;\n"
            "padding: 0px 10px;\n"
            "box-shadow: inset 0 1px 1px #e6b15f, 0 1px 2px rgba(0,0,0,0.61);\n"
            "border: 1px sold #90701b;\n"
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(239, 232, 158, 255), stop:1 rgba(252, 199, 121, 255));\n"
            "color: #333;\n"
            "text-shadow: 1px 1px #FFF;\n"
            "}"
        )

        self.affix_search_bar_layout.addWidget(self.open_groups_btn)

        self.open_groups_label = QLabel(self.affix_search_bar_frame)
        self.open_groups_label.setObjectName("open_groups_label")
        sizePolicy21 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(
            self.open_groups_label.sizePolicy().hasHeightForWidth()
        )
        self.open_groups_label.setSizePolicy(sizePolicy21)
        self.open_groups_label.setMaximumSize(QSize(16777215, 100))
        self.open_groups_label.setWordWrap(True)

        self.affix_search_bar_layout.addWidget(self.open_groups_label)

        self.affix_search_bar_layout.setStretch(0, 20)
        self.affix_search_bar_layout.setStretch(1, 5)
        self.affix_search_bar_layout.setStretch(2, 5)
        self.affix_search_bar_layout.setStretch(3, 20)

        self.crafting_calclayout.addWidget(self.affix_search_bar_frame)

        self.frame = QFrame(self.crafting_calc_page)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(30, 20, 75, 24))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "border-image: none;\n"
            "font-size: 14px;\n"
            "box-shadow: 2px 2px 3px 0px rgba(0,0,0,0.25);\n"
            "color: #00e120 !important;\n"
            "padding: 3px 5px;\n"
            "opacity: 0.5;\n"
            "background-color: transparent;\n"
            "border: 1px solid #00e120;\n"
            "}"
        )

        self.crafting_calclayout.addWidget(self.frame)

        self.crafting_calclayout.setStretch(0, 2)
        self.crafting_calclayout.setStretch(1, 10)
        self.crafting_calclayout.setStretch(2, 2)
        self.crafting_calclayout.setStretch(3, 20)

        self.crafting_calc_vertical_layout.addLayout(self.crafting_calclayout)

        self.pages.addWidget(self.crafting_calc_page)

        self.main_pages_layout.addWidget(self.pages)

        # if QT_CONFIG(shortcut)
        self.open_groups_label.setBuddy(self.open_groups_btn)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", "Form", None))
        self.item_img_label.setText("")
        self.crafting_btn_label.setText("")
        self.phys_dps_label.setText(
            QCoreApplication.translate(
                "MainPages",
                "<html><head/><body><p><span\n"
                '                 style=" color:#827a6c;">pDPS\n'
                '                 : </span><span style="\n'
                '                 color:#8787fe;">{}</span></p></body></html>\n'
                "                ",
                None,
            )
        )
        self.ele_dps_label.setText(
            QCoreApplication.translate(
                "MainPages",
                "<html><head/><body><p\n"
                '                 align="center"><span\n'
                '                 style=" color:#827a6c;">eDPS\n'
                '                 : </span><span style="\n'
                '                 color:#8787fe;">{}</span></p></body></html>\n'
                "                ",
                None,
            )
        )
        self.total_dps_label.setText(
            QCoreApplication.translate(
                "MainPages",
                "<html><head/><body><p\n"
                '                 align="center"><span\n'
                '                 style=" color:#827a6c;">pDPS\n'
                '                 : </span><span style="\n'
                '                 color:#8787fe;">{}</span></p></body></html>\n'
                "                ",
                None,
            )
        )
        self.affix_total_label.setText(
            QCoreApplication.translate(
                "MainPages",
                "<html><head/><body><p\n"
                '                 align="center"><span\n'
                '                 style=" color:#999999;">P S\n'
                "                 C</span></p></body></html>\n"
                "                ",
                None,
            )
        )
        self.item_header_label.setText("")
        self.item_spacer_1.setText("")
        self.item_spacer_2.setText("")
        self.item_implicits_label.setText("")
        self.item_spacer_3.setText("")
        self.prefix_info_2.setText("")
        self.prefix_2_stat_text.setText("")
        self.prefix_info_3.setText("")
        self.prefix_3_stat_text.setText("")
        self.suffix_2_info.setText("")
        self.suffix_2_stat_text.setText("")
        self.suffix_1_info.setText("")
        self.suffix_1_stat_text.setText("")
        self.suffix_3_info.setText("")
        self.suffix_3_stat_text.setText("")
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(
            QCoreApplication.translate("MainPages", "Search for a base or item", None)
        )
        self.reset_btn.setText(QCoreApplication.translate("MainPages", "Reset", None))
        self.import_btn.setText(
            QCoreApplication.translate("MainPages", "Import Item", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainPages",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Choose a crafting method</span><span style=" font-size:12pt;"> REQUIRED</span></p></body></html>',
                None,
            )
        )
        self.fossil_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Fossils", None)
        )
        self.exalt_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Exalted Orb", None)
        )
        self.essences_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Essences", None)
        )
        self.chaos_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Chaos Orb", None)
        )
        self.alch_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Orb of Alchemy", None)
        )
        self.hunter_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Hunter's Exalted Orb", None)
        )
        self.redeemer_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Redeemer's Exalted Orb", None)
        )
        self.warlord_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Warlord's Exalted Orb", None)
        )
        self.annul_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Orb of Annulment", None)
        )
        self.metacraft_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Metacraft", None)
        )
        self.crusader_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Crusader's Exalted Orb", None)
        )
        self.regal_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Regal Orb", None)
        )
        self.transmute_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Orb of transmutation", None)
        )
        self.aug_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Orb of Augmentation", None)
        )
        self.alt_calc_btn.setText(
            QCoreApplication.translate("MainPages", "Orb of Alteration", None)
        )
        self.affix_search_bar.setText("")
        self.affix_search_bar.setPlaceholderText(
            QCoreApplication.translate("MainPages", "Search for an affix", None)
        )
        self.close_filters_btn.setText(
            QCoreApplication.translate("MainPages", "Close filters", None)
        )
        self.open_groups_btn.setText(
            QCoreApplication.translate("MainPages", "Open all groups", None)
        )
        self.open_groups_label.setText(
            QCoreApplication.translate(
                "MainPages",
                '<html><head/><body><p><span style=" font-size:14pt; color:#ffeebb;">LEFT </span><span style=" font-size:14pt; color:#ffffff;">click to expand and add modifiers as requirements.</span></p></body></html>',
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainPages", "PushButton", None)
        )

    # retranslateUi
