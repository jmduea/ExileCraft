import PySide6
from PySide6 import QtWidgets
from .item_options_wizard_ui import Ui_ItemOptionsWizard  # the Python file generated from your .ui file


class ItemOptionsWizard(PySide6.QtWidgets.QWizard, Ui_ItemOptionsWizard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect the buttonClicked signal of the QButtonGroups to slots
        # self.wizard_base_group_btns.buttonClicked.connect(self.enable_next_button)
        # self.buttonGroup2.buttonClicked.connect(self.enable_next_button)
        # self.buttonGroup3.buttonClicked.connect(self.enable_next_button)
    def changePage(self):
        page = self.currentPage()
        if page == self.wizard_start_page:  # second page
            # Return the index of the third page
            return self.wizard_base_groups_page
        elif page == self.wizard_base_groups_page:
            # Return the index of the fourth page
            return self.wizard_base_selection_page
        elif page == self.wizard_base_selection_page:
            return self.wizard_item_selection_page
        elif page == self.wizard_item_selection_page:
            return self.wizard_item_options_page
        elif page == self.wizard_item_options_page:
            return self.wizard_confirm_options_page
        else:
            return super(Ui_ItemOptionsWizard, self).change()  # default behavior

    def enable_next_button(self):
        self.button(QtWidgets.QWizard.NextButton).setEnabled(True)