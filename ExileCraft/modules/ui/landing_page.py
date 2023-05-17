from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class LandingPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Form")
        self.resize(1196, 723)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setFamily("fontin-smallcaps")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.base_groups_container = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_groups_container.sizePolicy().hasHeightForWidth())
        self.base_groups_container.setSizePolicy(sizePolicy)
        self.base_groups_container.setMinimumSize(QtCore.QSize(600, 400))
        self.base_groups_container.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.base_groups_container.setStyleSheet("QWidget {\n"
"    border-image: url(assets/images/emubg.png);\n"
"}\n"
"QLabel {\n"
" border: 3px ridge #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-blend-mode: overlay;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    border-image: none;\n"
"}\n"
"QMenuBar {\n"
"    border: 3px ridge #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-blend-mode: overlay;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    border-image: none;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    border: 3px ridge #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-blend-mode: overlay;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font: fontin-smallcaps;\n"
"    border:0px inset #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #686d71);\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"\n"
"QToolBox {\n"
"    font: fontin-smallcaps;\n"
"    border:0px ridge #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #686d71);\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    font-family: fontin;\n"
"    border:0px ridge #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"QWidget {\n"
"    font-family: fontin-smallcaps;\n"
"    border:1px ridge #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
"}\n"
"QLabel {\n"
"    font-family: fontin;\n"
"    border:1px groove #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
"}\n"
"\n"
"QComboBox {\n"
"    font-family: fontin;\n"
"    border:1px outset #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #686d71);\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"QStackedWidget {\n"
"    font-family: fontin;\n"
"    border:1px inset #8f8f91;\n"
"    border-radius: 0px;\n"
"    background-blend-mode: overlay;\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"\n"
"QToolTip {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #686d71);\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px outset #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    filter: drop-shadow(8 px 8px 10px gray);\n"
"    border-image: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 1px inset #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.base_groups_container.setObjectName("base_groups_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.base_groups_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.base_groups_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setObjectName("header")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.base_group_label = QtWidgets.QLabel(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_group_label.sizePolicy().hasHeightForWidth())
        self.base_group_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("fontin")
        font.setPointSize(14)
        self.base_group_label.setFont(font)
        self.base_group_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.base_group_label.setObjectName("base_group_label")
        self.verticalLayout_2.addWidget(self.base_group_label)
        self.verticalLayout.addWidget(self.header)
        self.base_group_btns = QtWidgets.QWidget(self.base_groups_container)
        self.base_group_btns.setObjectName("base_group_btns")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.base_group_btns)
        self.gridLayout_2.setContentsMargins(20, 0, 20, 20)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gloves_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.gloves_btn.setObjectName("gloves_btn")
        self.gridLayout_2.addWidget(self.gloves_btn, 0, 2, 1, 1)
        self.body_armours_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.body_armours_btn.setObjectName("body_armours_btn")
        self.gridLayout_2.addWidget(self.body_armours_btn, 0, 0, 1, 1)
        self.boots_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.boots_btn.setObjectName("boots_btn")
        self.gridLayout_2.addWidget(self.boots_btn, 0, 1, 1, 1)
        self.helmets_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.helmets_btn.setObjectName("helmets_btn")
        self.gridLayout_2.addWidget(self.helmets_btn, 1, 0, 1, 1)
        self.jewellery_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.jewellery_btn.setObjectName("jewellery_btn")
        self.gridLayout_2.addWidget(self.jewellery_btn, 1, 1, 1, 1)
        self.cluster_jewels_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.cluster_jewels_btn.setObjectName("cluster_jewels_btn")
        self.gridLayout_2.addWidget(self.cluster_jewels_btn, 3, 0, 1, 1)
        self.flasks_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.flasks_btn.setObjectName("flasks_btn")
        self.gridLayout_2.addWidget(self.flasks_btn, 3, 1, 1, 1)
        self.heist_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.heist_btn.setObjectName("heist_btn")
        self.gridLayout_2.addWidget(self.heist_btn, 3, 2, 1, 1)
        self.invitations_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.invitations_btn.setObjectName("invitations_btn")
        self.gridLayout_2.addWidget(self.invitations_btn, 4, 0, 1, 1)
        self.maps_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.maps_btn.setObjectName("maps_btn")
        self.gridLayout_2.addWidget(self.maps_btn, 4, 2, 1, 1)
        self.one_handed_weapons_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.one_handed_weapons_btn.setObjectName("one_handed_weapons_btn")
        self.gridLayout_2.addWidget(self.one_handed_weapons_btn, 1, 2, 1, 1)
        self.two_handed_weapons_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.two_handed_weapons_btn.setObjectName("two_handed_weapons_btn")
        self.gridLayout_2.addWidget(self.two_handed_weapons_btn, 2, 0, 1, 1)
        self.offhands_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.offhands_btn.setObjectName("offhands_btn")
        self.gridLayout_2.addWidget(self.offhands_btn, 2, 1, 1, 1)
        self.jewels_btn = QtWidgets.QPushButton(self.base_group_btns)
        self.jewels_btn.setObjectName("jewels_btn")
        self.gridLayout_2.addWidget(self.jewels_btn, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.base_group_btns)
        self.verticalLayout_3.addWidget(self.base_groups_container)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.base_group_label.setText(_translate("Form", "Choose a Base Group"))
        self.gloves_btn.setText(_translate("Form", "Gloves"))
        self.body_armours_btn.setText(_translate("Form", "Body Armours"))
        self.boots_btn.setText(_translate("Form", "Boots"))
        self.helmets_btn.setText(_translate("Form", "Helmets"))
        self.jewellery_btn.setText(_translate("Form", "Jewellery"))
        self.cluster_jewels_btn.setText(_translate("Form", "Cluster Jewels"))
        self.flasks_btn.setText(_translate("Form", "Flasks"))
        self.heist_btn.setText(_translate("Form", "Heist"))
        self.invitations_btn.setText(_translate("Form", "Invitations"))
        self.maps_btn.setText(_translate("Form", "Maps"))
        self.one_handed_weapons_btn.setText(_translate("Form", "One Handed Weapons"))
        self.two_handed_weapons_btn.setText(_translate("Form", "Two Handed Weapons"))
        self.offhands_btn.setText(_translate("Form", "Offhands"))
        self.jewels_btn.setText(_translate("Form", "Jewels"))
