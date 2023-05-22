import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QVBoxLayout, QWizard, QWizardPage

from .ui_item_options_wizard import UiItemOptionsWizard  # the Python file generated from your .ui file
from ..pages.wizard_start_page import WizardStartPage
from ..pages.base_group_page import BaseGroupPage


class ItemOptionsWizard(QtWidgets.QWizard):
    def __init__(self, parent=None, *args, **kwargs):
        super(ItemOptionsWizard, self).__init__(parent)
        self.ui = UiItemOptionsWizard()
        self.wizard_start_page = WizardStartPage()
        self.addPage(self.wizard_start_page)
        self.base_group_page = BaseGroupPage()
        self.addPage(self.base_group_page)
        self.ui.setupUi(self)

        self.custom_back_button = QtWidgets.QPushButton("Back")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton1, self.custom_back_button)
        self.custom_back_button.clicked.connect(self.custom_back_button_clicked)
        self.custom_next_button = QtWidgets.QPushButton("Next")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton2, self.custom_next_button)
        self.custom_next_button.clicked.connect(self.custom_next_button_clicked)
        self.custom_finish_button = QtWidgets.QPushButton("Finish")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton3, self.custom_finish_button)
        self.previousId = None
        self.originalNextId = self.nextId
        self.currentIdChanged.connect(self.update_previous_id)
        self.base_group = ""
        self.base_group_type = ""
        self.base_item = ""
        self.base_ilvl = ""
        self.base_quality = ""
        self.base_influences = ""
        self.next_page_name = ""
        # Connect the custom buttons to the appropriate slots
        self.custom_finish_button.clicked.connect(self.accept)
        self.setButtonLayout([
            QWizard.WizardButton.CustomButton2
        ])
        self.update_button_layout()
        self.currentIdChanged.connect(self.update_button_layout)
        self.base_group_page.base_group_btns_group.buttonClicked.connect(self.store_base_group)
        self.pageAdded.connect(self.change_to_added_page)

    def update_previous_id(self, current_id):
        self.previousId = current_id

    def change_to_added_page(self, page_id):
        self.nextId = lambda: page_id
        self.next()
        self.update_button_layout()

    def update_button_layout(self):
        _id = self.currentId()
        if _id != 0:
            self.setButtonLayout([
                QWizard.WizardButton.CustomButton1,
                QWizard.WizardButton.CustomButton2
            ])
        elif _id == 0:
            self.setButtonLayout([
                QWizard.WizardButton.CustomButton2
            ])
        elif _id == 5:
            self.setButtonLayout([
                QWizard.WizardButton.CustomButton1,
                QWizard.WizardButton.CustomButton3
            ])

    def custom_next_button_clicked(self):
        self.nextId = self.originalNextId
        self.next()

    def custom_back_button_clicked(self):
        if self.currentId() > 1:
            self.removePage(self.currentId())
        if self.previousId is not None:
            self.nextId = lambda: self.previousId
            self.back()

    def store_base_group(self, button):
        # Button is the clicked button
        if self.currentPage() == self.base_group_page:
            # If the button is checked, store its text
            self.base_group = button.objectName()
            self.next_page_name = self.base_group.replace("_btn", "_types_page.ui")
            print(self.next_page_name)
            self.loadPage()
        else:
            # If the button is unchecked, clear the stored text
            self.base_group = ""

    def loadPage(self):
        if not self.next_page_name:
            return
        abs_page_path = f"C:/Users/spark/PycharmProjects/ExileCraft/ExileCraft/ExileCraft/modules/ui/ui_files/{self.next_page_name}"
        ui_file = QFile(abs_page_path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"cannot open {abs_page_path}")
            sys.exit(-1)

        loader = QUiLoader()
        page = loader.load(ui_file)
        ui_file.close()

        if not page:
            print(loader.errorString())
            sys.exit(-1)

        new_page = QWizardPage()  # Create new QWizardPage instance
        layout = QVBoxLayout()  # Create a vertical layout
        layout.addWidget(page)  # Add your loaded UI to the layout
        new_page.setLayout(layout)  # Set the layout for your page

        self.addPage(new_page)  # Add the new QWizardPage instance to the wizard

        self.nextId()
