
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QButtonGroup, QHBoxLayout, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class BaseGroupPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, base_group_page):
        if not base_group_page.objectName():
            base_group_page.setObjectName(u"base_group_page")
        base_group_page.resize(419, 198)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(base_group_page.sizePolicy().hasHeightForWidth())
        base_group_page.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(base_group_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.base_group_btns_container = QWidget(base_group_page)
        self.base_group_btns_container.setObjectName(u"base_group_btns_container")
        self.base_group_btns_container.setMinimumSize(QSize(400, 0))
        self.verticalLayout_5 = QVBoxLayout(self.base_group_btns_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.base_group_btns_row1 = QWidget(self.base_group_btns_container)
        self.base_group_btns_row1.setObjectName(u"base_group_btns_row1")
        self.horizontalLayout_3 = QHBoxLayout(self.base_group_btns_row1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.body_armour_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group = QButtonGroup(base_group_page)
        self.base_group_btns_group.setObjectName(u"base_group_btns_group")
        self.base_group_btns_group.addButton(self.body_armour_btn)
        self.body_armour_btn.setObjectName(u"body_armour_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body_armour_btn.sizePolicy().hasHeightForWidth())
        self.body_armour_btn.setSizePolicy(sizePolicy1)
        self.body_armour_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.body_armour_btn)

        self.boots_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group.addButton(self.boots_btn)
        self.boots_btn.setObjectName(u"boots_btn")
        sizePolicy1.setHeightForWidth(self.boots_btn.sizePolicy().hasHeightForWidth())
        self.boots_btn.setSizePolicy(sizePolicy1)
        self.boots_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.boots_btn)

        self.helmets_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group.addButton(self.helmets_btn)
        self.helmets_btn.setObjectName(u"helmets_btn")
        sizePolicy1.setHeightForWidth(self.helmets_btn.sizePolicy().hasHeightForWidth())
        self.helmets_btn.setSizePolicy(sizePolicy1)
        self.helmets_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.helmets_btn)

        self.gloves_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group.addButton(self.gloves_btn)
        self.gloves_btn.setObjectName(u"gloves_btn")
        sizePolicy1.setHeightForWidth(self.gloves_btn.sizePolicy().hasHeightForWidth())
        self.gloves_btn.setSizePolicy(sizePolicy1)
        self.gloves_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gloves_btn)

        self.verticalLayout_5.addWidget(self.base_group_btns_row1)

        self.base_group_btns_row2 = QWidget(self.base_group_btns_container)
        self.base_group_btns_row2.setObjectName(u"base_group_btns_row2")
        sizePolicy1.setHeightForWidth(self.base_group_btns_row2.sizePolicy().hasHeightForWidth())
        self.base_group_btns_row2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.base_group_btns_row2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.one_handed_weapons_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.one_handed_weapons_btn)
        self.one_handed_weapons_btn.setObjectName(u"one_handed_weapons_btn")
        sizePolicy1.setHeightForWidth(self.one_handed_weapons_btn.sizePolicy().hasHeightForWidth())
        self.one_handed_weapons_btn.setSizePolicy(sizePolicy1)
        self.one_handed_weapons_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.one_handed_weapons_btn)

        self.two_handed_weapons_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.two_handed_weapons_btn)
        self.two_handed_weapons_btn.setObjectName(u"two_handed_weapons_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.two_handed_weapons_btn.sizePolicy().hasHeightForWidth())
        self.two_handed_weapons_btn.setSizePolicy(sizePolicy2)
        self.two_handed_weapons_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.two_handed_weapons_btn)

        self.offhands_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.offhands_btn)
        self.offhands_btn.setObjectName(u"offhands_btn")
        sizePolicy2.setHeightForWidth(self.offhands_btn.sizePolicy().hasHeightForWidth())
        self.offhands_btn.setSizePolicy(sizePolicy2)
        self.offhands_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.offhands_btn)

        self.verticalLayout_5.addWidget(self.base_group_btns_row2, 0, Qt.AlignHCenter)

        self.base_group_btns_row3 = QWidget(self.base_group_btns_container)
        self.base_group_btns_row3.setObjectName(u"base_group_btns_row3")
        sizePolicy1.setHeightForWidth(self.base_group_btns_row3.sizePolicy().hasHeightForWidth())
        self.base_group_btns_row3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.base_group_btns_row3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.jewellery_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.jewellery_btn)
        self.jewellery_btn.setObjectName(u"jewellery_btn")
        sizePolicy1.setHeightForWidth(self.jewellery_btn.sizePolicy().hasHeightForWidth())
        self.jewellery_btn.setSizePolicy(sizePolicy1)
        self.jewellery_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.jewellery_btn)

        self.jewels_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.jewels_btn)
        self.jewels_btn.setObjectName(u"jewels_btn")
        sizePolicy1.setHeightForWidth(self.jewels_btn.sizePolicy().hasHeightForWidth())
        self.jewels_btn.setSizePolicy(sizePolicy1)
        self.jewels_btn.setCheckable(True)
        self.jewels_btn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.jewels_btn)

        self.cluster_jewels_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.cluster_jewels_btn)
        self.cluster_jewels_btn.setObjectName(u"cluster_jewels_btn")
        sizePolicy1.setHeightForWidth(self.cluster_jewels_btn.sizePolicy().hasHeightForWidth())
        self.cluster_jewels_btn.setSizePolicy(sizePolicy1)
        self.cluster_jewels_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.cluster_jewels_btn)

        self.flasks_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.flasks_btn)
        self.flasks_btn.setObjectName(u"flasks_btn")
        sizePolicy1.setHeightForWidth(self.flasks_btn.sizePolicy().hasHeightForWidth())
        self.flasks_btn.setSizePolicy(sizePolicy1)
        self.flasks_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.flasks_btn)

        self.verticalLayout_5.addWidget(self.base_group_btns_row3)

        self.verticalLayout.addWidget(self.base_group_btns_container)

        self.retranslateUi(base_group_page)

        QMetaObject.connectSlotsByName(base_group_page)

    # setupUi

    def retranslateUi(self, base_group_page):
        base_group_page.setWindowTitle(QCoreApplication.translate("base_group_page", u"Ui_Base_Group_Page", None))
        self.body_armour_btn.setText(QCoreApplication.translate("base_group_page", u"Body Armour", None))
        self.boots_btn.setText(QCoreApplication.translate("base_group_page", u"Boots", None))
        self.helmets_btn.setText(QCoreApplication.translate("base_group_page", u"Helmets", None))
        self.gloves_btn.setText(QCoreApplication.translate("base_group_page", u"Gloves", None))
        self.one_handed_weapons_btn.setText(QCoreApplication.translate("base_group_page", u"One Handed Weapons", None))
        self.two_handed_weapons_btn.setText(QCoreApplication.translate("base_group_page", u"Two Handed Weapons", None))
        self.offhands_btn.setText(QCoreApplication.translate("base_group_page", u"Offhands", None))
        self.jewellery_btn.setText(QCoreApplication.translate("base_group_page", u"Jewellery", None))
        self.jewels_btn.setText(QCoreApplication.translate("base_group_page", u"Jewels", None))
        self.cluster_jewels_btn.setText(QCoreApplication.translate("base_group_page", u"Cluster Jewels", None))
        self.flasks_btn.setText(QCoreApplication.translate("base_group_page", u"Flasks", None))
    # retranslateUi
