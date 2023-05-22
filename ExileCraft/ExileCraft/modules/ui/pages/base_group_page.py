from PySide6.QtCore import (Property, QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QButtonGroup, QHBoxLayout, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget, QWizard, QWizardPage)


class BaseGroupPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._buttonObjectName = ''

    @Property(str)
    def buttonObjectName(self):
        return self._buttonObjectName

    @buttonObjectName.setter
    def buttonObjectName(self, value):
        self._buttonObjectName = value

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

        self.boot_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group.addButton(self.boot_btn)
        self.boot_btn.setObjectName(u"boot_btn")
        sizePolicy1.setHeightForWidth(self.boot_btn.sizePolicy().hasHeightForWidth())
        self.boot_btn.setSizePolicy(sizePolicy1)
        self.boot_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.boot_btn)

        self.helmet_btn = QPushButton(self.base_group_btns_row1)
        self.base_group_btns_group.addButton(self.helmet_btn)
        self.helmet_btn.setObjectName(u"helmet_btn")
        sizePolicy1.setHeightForWidth(self.helmet_btn.sizePolicy().hasHeightForWidth())
        self.helmet_btn.setSizePolicy(sizePolicy1)
        self.helmet_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.helmet_btn)

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
        self.one_hand_weapon_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.one_hand_weapon_btn)
        self.one_hand_weapon_btn.setObjectName(u"one_hand_weapon_btn")
        sizePolicy1.setHeightForWidth(self.one_hand_weapon_btn.sizePolicy().hasHeightForWidth())
        self.one_hand_weapon_btn.setSizePolicy(sizePolicy1)
        self.one_hand_weapon_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.one_hand_weapon_btn)

        self.two_hand_weapon_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.two_hand_weapon_btn)
        self.two_hand_weapon_btn.setObjectName(u"two_hand_weapon_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.two_hand_weapon_btn.sizePolicy().hasHeightForWidth())
        self.two_hand_weapon_btn.setSizePolicy(sizePolicy2)
        self.two_hand_weapon_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.two_hand_weapon_btn)

        self.offhand_btn = QPushButton(self.base_group_btns_row2)
        self.base_group_btns_group.addButton(self.offhand_btn)
        self.offhand_btn.setObjectName(u"offhand_btn")
        sizePolicy2.setHeightForWidth(self.offhand_btn.sizePolicy().hasHeightForWidth())
        self.offhand_btn.setSizePolicy(sizePolicy2)
        self.offhand_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.offhand_btn)

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

        self.jewel_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.jewel_btn)
        self.jewel_btn.setObjectName(u"jewel_btn")
        sizePolicy1.setHeightForWidth(self.jewel_btn.sizePolicy().hasHeightForWidth())
        self.jewel_btn.setSizePolicy(sizePolicy1)
        self.jewel_btn.setCheckable(True)
        self.jewel_btn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.jewel_btn)

        self.cluster_jewel_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.cluster_jewel_btn)
        self.cluster_jewel_btn.setObjectName(u"cluster_jewel_btn")
        sizePolicy1.setHeightForWidth(self.cluster_jewel_btn.sizePolicy().hasHeightForWidth())
        self.cluster_jewel_btn.setSizePolicy(sizePolicy1)
        self.cluster_jewel_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.cluster_jewel_btn)

        self.flask_btn = QPushButton(self.base_group_btns_row3)
        self.base_group_btns_group.addButton(self.flask_btn)
        self.flask_btn.setObjectName(u"flask_btn")
        sizePolicy1.setHeightForWidth(self.flask_btn.sizePolicy().hasHeightForWidth())
        self.flask_btn.setSizePolicy(sizePolicy1)
        self.flask_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.flask_btn)

        self.verticalLayout_5.addWidget(self.base_group_btns_row3)

        self.verticalLayout.addWidget(self.base_group_btns_container)

        self.retranslateUi(base_group_page)

        QMetaObject.connectSlotsByName(base_group_page)

    # setupUi

    def retranslateUi(self, base_group_page):
        base_group_page.setWindowTitle(QCoreApplication.translate("base_group_page", u"Ui_Base_Group_Page", None))
        self.body_armour_btn.setText(QCoreApplication.translate("base_group_page", u"Body Armour", None))
        self.boot_btn.setText(QCoreApplication.translate("base_group_page", u"Boots", None))
        self.helmet_btn.setText(QCoreApplication.translate("base_group_page", u"Helmets", None))
        self.gloves_btn.setText(QCoreApplication.translate("base_group_page", u"Gloves", None))
        self.one_hand_weapon_btn.setText(QCoreApplication.translate("base_group_page", u"One Handed Weapons", None))
        self.two_hand_weapon_btn.setText(QCoreApplication.translate("base_group_page", u"Two Handed Weapons", None))
        self.offhand_btn.setText(QCoreApplication.translate("base_group_page", u"Offhands", None))
        self.jewellery_btn.setText(QCoreApplication.translate("base_group_page", u"Jewellery", None))
        self.jewel_btn.setText(QCoreApplication.translate("base_group_page", u"Jewels", None))
        self.cluster_jewel_btn.setText(QCoreApplication.translate("base_group_page", u"Cluster Jewels", None))
        self.flask_btn.setText(QCoreApplication.translate("base_group_page", u"Flasks", None))
    # retranslateUi
