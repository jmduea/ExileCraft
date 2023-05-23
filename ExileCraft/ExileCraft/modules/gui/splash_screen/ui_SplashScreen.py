# -*- coding: utf-8 -*-

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
#

################################################################################
## Form generated from reading UI file 'SplashScreenzRVOUe.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QLabel, QProgressBar, QSizePolicy, QVBoxLayout, QWidget)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.setWindowModality(Qt.ApplicationModal)
        SplashScreen.resize(680, 400)
        SplashScreen.setMaximumSize(QSize(680, 400))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame {\n"
                                             "	background-color: rgb(38, 39, 40);\n"
                                             "	color: rgb(255, 255, 255);\n"
                                             "	border-radius: 10px;\n"
                                             "}")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.app_name_label = QLabel(self.drop_shadow_frame)
        self.app_name_label.setObjectName(u"app_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_name_label.sizePolicy().hasHeightForWidth())
        self.app_name_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(40)
        self.app_name_label.setFont(font)
        self.app_name_label.setTextFormat(Qt.RichText)
        self.app_name_label.setScaledContents(False)
        self.app_name_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.app_name_label, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.app_description_label = QLabel(self.drop_shadow_frame)
        self.app_description_label.setObjectName(u"app_description_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_description_label.sizePolicy().hasHeightForWidth())
        self.app_description_label.setSizePolicy(sizePolicy1)
        self.app_description_label.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(14)
        self.app_description_label.setFont(font1)
        self.app_description_label.setStyleSheet(u"color: rgb(159, 159, 159)")
        self.app_description_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.app_description_label, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.progress_bar = QProgressBar(self.drop_shadow_frame)
        self.progress_bar.setObjectName(u"progress_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy2)
        self.progress_bar.setMinimumSize(QSize(600, 0))
        self.progress_bar.setStyleSheet(u"QProgressBar {;\n"
                                        "	background-color: rgb(159, 159, 159);\n"
                                        "	color: rgb(200, 200, 200);\n"
                                        "	border-style: none;\n"
                                        "	border-radius: 10px;\n"
                                        "	text-align: center;\n"
                                        "}\n"
                                        "QProgressBar::chunk {\n"
                                        "	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.511, stop:0 rgba(189, 122, 36, 255), stop:1 rgba(241, 183, 125, 255));\n"
                                        "	border-radius: 10px;\n"
                                        "}")
        self.progress_bar.setValue(24)

        self.verticalLayout_2.addWidget(self.progress_bar, 0, Qt.AlignHCenter)

        self.loading_label = QLabel(self.drop_shadow_frame)
        self.loading_label.setObjectName(u"loading_label")
        sizePolicy1.setHeightForWidth(self.loading_label.sizePolicy().hasHeightForWidth())
        self.loading_label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        self.loading_label.setFont(font2)
        self.loading_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.loading_label)

        self.credits_label = QLabel(self.drop_shadow_frame)
        self.credits_label.setObjectName(u"credits_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.credits_label.sizePolicy().hasHeightForWidth())
        self.credits_label.setSizePolicy(sizePolicy3)
        self.credits_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.credits_label, 0, Qt.AlignRight)

        self.verticalLayout.addWidget(self.drop_shadow_frame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.app_name_label.setText(QCoreApplication.translate("SplashScreen",
                                                               u"<html><head/><body><p><img src=\":/icons/assets/icons/vendor.ico\"/><span style=\" font-size:48pt; font-weight:700;\">Exile</span><span style=\" font-size:48pt;\">Craft</span></p></body></html>",
                                                               None))
        self.app_description_label.setText(QCoreApplication.translate("SplashScreen",
                                                                      u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Crafting</span><span style=\" font-size:14pt;\"> Simulator</span></p></body></html>",
                                                                      None))
        self.loading_label.setText(QCoreApplication.translate("SplashScreen",
                                                              u"<html><head/><body><p><span style=\" color:#9f9f9f;\">loading...</span></p></body></html>",
                                                              None))
        self.credits_label.setText(QCoreApplication.translate("SplashScreen",
                                                              u"<html><head/><body><p><span style=\" font-weight:700;\">Created By: </span>Jon Duea</p></body></html>",
                                                              None))
    # retranslateUi
