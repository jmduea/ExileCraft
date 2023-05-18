from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QShowEvent

from .ui_mainwindow import Ui_MainWindow
from .customtreemodel import CustomTreeModel
from .wizard.item_options_wizard import ItemOptionsWizard
from ..db.ui_updater import UiUpdater
from ..db.database_handler import DatabaseHandler
from ..db import item_mods_retriever, item_stats_updater
from .slots.buttons import ButtonHandler

# fossil button index = 0
# harvest button index = 1
# essence button index = 2
# catalyst button index = 3
# beast craft buttons index = 4
# eldritch craft buttons index = 5
# syndicate craft buttons index = 6


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        with open("modules/ui/assets/stylesheets/main_stylesheet.qss", "r") as f:
            self.setStyleSheet(f.read())
        self.setWindowOpacity(0.95)
        self.wizard = ItemOptionsWizard()
        self.wizard.custom_finish_button.clicked.connect(self.on_wizard_finished)
        self.db_handler = DatabaseHandler()
        self.button_handler = ButtonHandler
        self.item_stats_updater = item_stats_updater
        self.item_mods_retriever = item_mods_retriever
        self.button_handler = ButtonHandler()
        # Set window style and flags
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Initialize UiUpdater
        self.ui_updater = UiUpdater(
            self.item_header_text_label,
            self.item_properties,
            self.item_requirements,
            self.item_implicits,
            self.item_spacer_3,
            self.modifiers,
            self.item_img_box,
            self
        )

        # Add pages to the crafting simulator
        self.crafting_simulator.addWidget(self.landing_page)
        self.crafting_simulator.setCurrentIndex(0)

        # Connect the signal to a method that updates the model
        headers = ["Name", "Level", "Stats", "Tags", "Mods", "Weight"]
        item_name = "Shabby Jerkin"
        all_results = self.item_mods_retriever.get_mods_for_item_class(self, item_name)
        generation_type = 'prefix'
        self.model = CustomTreeModel(headers, item_name, all_results, generation_type)
        self.prefix_tree_view.setModel(self.model)
        #self.modpool_tabs.clicked.connect(self.update_tree_view)

    def is_prefix_view_active(self):
        """Check if the prefix_tree_view is active.

        :return: True if the prefix_tree_view is visible and is enabled, False otherwise.
        """
        return self.prefix_tree_view.isVisible() and self.prefix_tree_view.isEnabled()

    def is_suffix_view_active(self):
        """Check if the suffix_tree_view is active.

        :return: True if the suffix_tree_view is visible and is enabled, False otherwise.
        """
        return self.suffix_tree_view.isVisible() and self.suffix_tree_view.isEnabled()

    def is_implicit_view_active(self):
        """Check if the implicit_tree_view is active.

        :return: True if the implicit_tree_view is visible and is enabled, False otherwise.
        """
        return self.implicit_tree_view.isVisible() and self.implicit_tree_view.isEnabled()

    def show_wizard(self):
        wizard = ItemOptionsWizard()
        wizard.setWindowFlags(Qt.WindowStaysOnTopHint)
        if wizard.exec():
            self.show()

    def on_wizard_finished(self):
        self.crafting_simulator.setCurrentIndex(1)

    def changePage(self, page_index):
        if self.crafting_simulator.currentIndex() == 0:
            self.crafting_simulator.setCurrentIndex(1)
        else:
            # Change the page in the crafting simulator
            self.crafting_simulator.setCurrentIndex(page_index)

    def resetOptions(self):
        self.changePage(0)

    def go_to_previous_page(self):
        # Go to the previous page in the crafting simulator
        current_index = self.crafting_simulator.currentIndex()
        if current_index > 0:
            for i in reversed(range(self.layout().count())):
                self.layout().itemAt(i).widget().setParent(None)
            self.changePage(current_index - 1)

    def go_to_next_page(self):
        # Go to the next page in the crafting simulator
        current_index = self.crafting_simulator.currentIndex()
        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)
        if current_index < self.crafting_simulator.count() - 1:
            self.changePage(current_index + 1)

    def proceed(self):
        # Proceed to the next page if on the third page
        current_index = self.crafting_simulator.currentIndex()
        if current_index == 4:
            crafting_project_data = self.db_handler.get_crafting_project_data()
            print(crafting_project_data)
            self.changePage(current_index + 1)

    def update_item_stats(self):
        base_item_name = self.db_handler.get_last_crafting_project_base_item_id()
        self.ui_updater.set_item_view_box_background(base_item_name)
        if base_item_name is not None:
            self.item_stats_updater.update_item_stats(self, base_item_name)

    def update_tree_view(self):
        # Get the new data for the model
        headers = ["Name", "Level", "Stats", "Tags", "Mods", "Weight"]
        item_name = self.db_handler.get_last_crafting_project_base_item_id()
        all_results = self.item_mods_retriever.get_mods_for_item_class(self, item_name)

        # Determine the active view and set the generation_type accordingly
        if self.is_prefix_view_active():
            generation_type = 'prefix'
            active_tree_view = self.prefix_tree_view
        elif self.is_suffix_view_active():
            generation_type = 'suffix'
            active_tree_view = self.suffix_tree_view
        elif self.is_implicit_view_active():
            generation_type = ['eater_implicit', 'exarch_implicit']
            active_tree_view = self.implicit_tree_view
        else:
            raise RuntimeError("No valid tree view is currently active.")

        # Update the model data and re-populate it
        self.model.update_data(headers, item_name, all_results, generation_type)
        self.model.update_and_populate(generation_type)

        # Set the model for the active tree view
        active_tree_view.setModel(self.model)

    def set_item_influences(self, button_id, checked, influence_btns, checked_btns, max_checked_buttons=2):
        sender = influence_btns.button(button_id)
        if checked:
            checked_btns.append(sender)
            if len(checked_btns) > max_checked_buttons:
                oldest_button = checked_btns.pop(0)
                oldest_button.setChecked(False)
        self.db_handler.update_item_influences(influence_btns)

    def on_influence_button_toggled(self, button_id, checked):
        # Call set_item_influences from ButtonHandler instance
        self.button_handler.set_item_influences(button_id, checked, self.influence_btns, self.checked_btns)


