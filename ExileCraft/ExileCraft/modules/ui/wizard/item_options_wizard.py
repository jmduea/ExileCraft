from PySide6 import QtWidgets
from PySide6.QtWidgets import QWizard

from .ui_item_options_wizard import UiItemOptionsWizard  # the Python file generated from your .ui file
from ...tray import hotkey_methods


class ItemOptionsWizard(QtWidgets.QWizard):
    def __init__(self, parent=None, *args, **kwargs):
        super(ItemOptionsWizard, self).__init__(parent)
        self.ui = UiItemOptionsWizard()
        self.ui.setupUi(self)

        self.custom_back_button = QtWidgets.QPushButton("Back")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton1, self.custom_back_button)
        self.custom_back_button.clicked.connect(self.custom_back_button_clicked)
        self.custom_next_button = QtWidgets.QPushButton("Next")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton2, self.custom_next_button)
        self.custom_next_button.clicked.connect(self.custom_next_button_clicked)
        self.custom_finish_button = QtWidgets.QPushButton("Finish")
        QtWidgets.QWizard.setButton(self, QWizard.WizardButton.CustomButton3, self.custom_finish_button)
        self.base_group = ""
        self.base_group_type = ""
        self.base_item = ""
        self.base_ilvl = ""
        self.base_quality = ""
        self.base_influences = ""
        # Connect the custom buttons to the appropriate slots
        self.custom_finish_button.clicked.connect(self.accept)
        self.setButtonLayout([
            QWizard.WizardButton.CustomButton2
        ])
        self.update_button_layout()
        self.currentIdChanged.connect(self.update_button_layout)

    def update_button_layout(self):
        _id = self.currentId()
        if 0 < _id < 5:
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
        self.update_button_layout()
        self.next()

    def custom_back_button_clicked(self):
        self.update_button_layout()
        self.back()

    def store_base_group(self, button):
        # This slot is called when the button is toggled
        if self.currentId() == 1:
            if button.isChecked():
                # If the button is checked, store its text
                self.base_group = button.text()
                print(self.base_group)
            else:
                # If the button is unchecked, clear the stored text
                self.base_group = ""
            self.ui.base_selection_page.base_selection.set_base_group(self.base_group)
            self.ui.base_selection_page.base_selection.populate_buttons(self.base_group)
        elif self.currentId() == 2:
            if button.isChecked():
                self.base_group_type = button.text()
                print(self.base_group_type)
            else:
                self.base_group_type = ""
        elif self.currentId() == 3:
            if button.isChecked():
                self.base_item = button.text()
                print(self.base_item)
            else:
                self.base_item = ""
