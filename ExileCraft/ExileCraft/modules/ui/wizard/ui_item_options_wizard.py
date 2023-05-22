# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_options_wizardOsYMFk.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QSizePolicy, QVBoxLayout, QWizard, QWizardPage)

from ..pages.base_group_page import BaseGroupPage
from ..pages.wizard_start_page import WizardStartPage


class UiItemOptionsWizard(object):
    def setupUi(self, UiItemOptionsWizard):
        if not UiItemOptionsWizard.objectName():
            UiItemOptionsWizard.setObjectName(u"UiItemOptionsWizard")
        UiItemOptionsWizard.setWindowModality(Qt.NonModal)
        UiItemOptionsWizard.resize(500, 253)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UiItemOptionsWizard.sizePolicy().hasHeightForWidth())
        UiItemOptionsWizard.setSizePolicy(sizePolicy)
        UiItemOptionsWizard.setMinimumSize(QSize(473, 253))
        UiItemOptionsWizard.setMaximumSize(QSize(16775, 16755))
        UiItemOptionsWizard.setSizeGripEnabled(False)
        UiItemOptionsWizard.setModal(True)
        UiItemOptionsWizard.setWizardStyle(QWizard.ClassicStyle)
        UiItemOptionsWizard.setOptions(
            QWizard.HaveCustomButton1 | QWizard.HaveCustomButton2 | QWizard.HaveCustomButton3 | QWizard.NoBackButtonOnStartPage | QWizard.NoDefaultButton)
        UiItemOptionsWizard.setCurrentId(0)
        self.wizard_start_page = QWizardPage()
        self.wizard_start_page.setObjectName(u"wizard_start_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wizard_start_page.sizePolicy().hasHeightForWidth())
        self.wizard_start_page.setSizePolicy(sizePolicy1)
        self.wizard_start_page.setMinimumSize(QSize(342, 0))
        self.wizard_start_page.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.wizard_start_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.start_page = WizardStartPage(self.wizard_start_page)
        self.start_page.setObjectName(u"start_page")

        self.verticalLayout_4.addWidget(self.start_page)

        UiItemOptionsWizard.setPage(0, self.wizard_start_page)
        self.wizard_base_group_page = QWizardPage()
        self.wizard_base_group_page.setObjectName(u"wizard_base_group_page")
        sizePolicy.setHeightForWidth(self.wizard_base_group_page.sizePolicy().hasHeightForWidth())
        self.wizard_base_group_page.setSizePolicy(sizePolicy)
        self.wizard_base_group_page.setMinimumSize(QSize(452, 0))
        self.verticalLayout = QVBoxLayout(self.wizard_base_group_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.base_group_page = BaseGroupPage(self.wizard_base_group_page)
        self.base_group_page.setObjectName(u"base_group_page")
        sizePolicy1.setHeightForWidth(self.base_group_page.sizePolicy().hasHeightForWidth())
        self.base_group_page.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.base_group_page)

        UiItemOptionsWizard.setPage(1, self.wizard_base_group_page)
        self.wizard_confirm_options_page = QWizardPage()
        self.wizard_confirm_options_page.setObjectName(u"wizard_confirm_options_page")
        UiItemOptionsWizard.setPage(5, self.wizard_confirm_options_page)

        self.retranslateUi(UiItemOptionsWizard)

        QMetaObject.connectSlotsByName(UiItemOptionsWizard)

    # setupUi

    def retranslateUi(self, UiItemOptionsWizard):
        UiItemOptionsWizard.setWindowTitle(QCoreApplication.translate("UiItemOptionsWizard", u"Item Options", None))
        self.wizard_start_page.setTitle(
            QCoreApplication.translate("UiItemOptionsWizard", u"Start a Crafting Project", None))
        self.wizard_start_page.setSubTitle(QCoreApplication.translate("UiItemOptionsWizard",
                                                                      u"Start a new crafting project with the name of your choice",
                                                                      None))
        self.wizard_base_group_page.setTitle(
            QCoreApplication.translate("UiItemOptionsWizard", u"Select A Base Group", None))
    # retranslateUi
