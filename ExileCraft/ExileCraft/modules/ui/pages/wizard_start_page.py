from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
                               QSizePolicy, QVBoxLayout, QWidget, QWizard, QWizardPage)


class WizardStartPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, wizard_start_page):
        if not wizard_start_page.objectName():
            wizard_start_page.setObjectName(u"wizard_start_page")
        wizard_start_page.setWindowModality(Qt.NonModal)
        wizard_start_page.resize(403, 249)
        self.verticalLayout = QVBoxLayout(wizard_start_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wizard_start_page_container = QWidget(wizard_start_page)
        self.wizard_start_page_container.setObjectName(u"wizard_start_page_container")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wizard_start_page_container.sizePolicy().hasHeightForWidth())
        self.wizard_start_page_container.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.wizard_start_page_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wizard_start_project_name = QWidget(self.wizard_start_page_container)
        self.wizard_start_project_name.setObjectName(u"wizard_start_project_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wizard_start_project_name.sizePolicy().hasHeightForWidth())
        self.wizard_start_project_name.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.wizard_start_project_name)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.project_name_label = QLabel(self.wizard_start_project_name)
        self.project_name_label.setObjectName(u"project_name_label")

        self.horizontalLayout.addWidget(self.project_name_label)

        self.project_name_input = QLineEdit(self.wizard_start_project_name)
        self.project_name_input.setObjectName(u"project_name_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.project_name_input.sizePolicy().hasHeightForWidth())
        self.project_name_input.setSizePolicy(sizePolicy2)
        self.project_name_input.setFrame(True)

        self.horizontalLayout.addWidget(self.project_name_input)

        self.verticalLayout_2.addWidget(self.wizard_start_project_name)

        self.verticalLayout.addWidget(self.wizard_start_page_container)

        self.widget = QWidget(wizard_start_page)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        # if QT_CONFIG(shortcut)
        self.project_name_label.setBuddy(self.project_name_input)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(wizard_start_page)

        QMetaObject.connectSlotsByName(wizard_start_page)

    # setupUi

    def retranslateUi(self, wizard_start_page):
        wizard_start_page.setWindowTitle(QCoreApplication.translate("wizard_start_page", u"Item Options Wizard", None))
        self.project_name_label.setText(QCoreApplication.translate("wizard_start_page", u"Project Name:", None))
        self.project_name_input.setPlaceholderText(
            QCoreApplication.translate("wizard_start_page", u"Type name of the project here", None))
    # retranslateUi
