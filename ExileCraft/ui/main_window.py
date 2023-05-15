from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from ..ui.mainwindow_ui import Ui_MainWindow
from ..ui.base_selection import BaseSelection
from ..ui.item_selection import ItemSelection
from ..ui.landing_page import LandingPage
from ..ui.item_options import ItemOptions
from ..ui.customtreemodel import CustomTreeModel
from ..ui.ui_updater import UiUpdater
from ..db.database_handler import DatabaseHandler
from ..ui import item_stats_updater
from ..db import item_mods_retriever


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowOpacity(0.85)
        self.db_handler = DatabaseHandler()
        self.item_stats_updater = item_stats_updater
        self.item_mods_retriever = item_mods_retriever
        item_selection_page = ItemSelection()
        base_selection_page = BaseSelection()
        # base_selection_page.populate_buttons('Some Class', item_selection_page)
        # Set window style and flags
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Initialize UiUpdater
        self.ui_updater = UiUpdater(
            self.item_header_text_label,
            self.ItemProperties,
            self.ItemRequirements,
            self.ItemImplicits,
            self.ItemSpacer3,
            self.Modifiers,
            self.item_img_box,
            self
        )

        # Create landing page and item options page
        self.landing_page = LandingPage()
        self.item_options_page = ItemOptions()

        # Add pages to the crafting simulator
        self.crafting_simulator.addWidget(self.landing_page)
        self.crafting_simulator.addWidget(self.item_options_page)
        self.crafting_simulator.setCurrentIndex(0)

        # Connect "Previous" and "Next" buttons to functions
        self.base_selection_page.connect_buttons(self.go_to_previous_page, self.go_to_next_page)
        self.base_selection_page.base_selected.connect(self.open_item_selection_page)
        self.item_selection_page.connect_buttons(self.go_to_previous_page, self.go_to_next_page)
        self.item_selection_page.item_selected.connect(self.open_item_options_page)
        self.proceed_btn.clicked.connect(self.proceed)

        # Connect the signal to a method that updates the model
        headers = ["Name", "Level", "Stats", "Tags", "Mods", "Weight"]
        item_name = "Shabby Jerkin"
        all_results = self.item_mods_retriever.get_mods_for_item_class(self, item_name)
        generation_type = 'prefix'
        self.model = CustomTreeModel(headers, item_name, all_results, generation_type)
        self.prefix_tree_view.setModel(self.model)
        self.modpool_tabs.currentChanged.connect(self.update_tree_view)

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

    def changePage(self, page_index):
        if self.crafting_simulator.currentIndex() == 0:
            self.crafting_simulator.setCurrentIndex(1)
        else:
            # Change the page in the crafting simulator
            self.crafting_simulator.setCurrentIndex(page_index)

    def resetOptions(self):
        self.changePage(0)

    def open_base_selection_page(self, item_class_name):
        print(f'{item_class_name} button clicked')
        self.db_handler.update_item_class_id(item_class_name)
        self.base_selection_page.update_header_label(item_class_name)
        # Populate buttons in the base selection page
        self.base_selection_page.populate_buttons(item_class_name)
        # Switch to the base selection page
        self.changePage(2)

    def open_item_selection_page(self, item_class_id, item_subtype):
        print(f'{item_subtype}, {item_class_id} button clicked')
        self.item_selection_page.update_header_label(item_class_id, item_subtype)
        self.item_selection_page.populate_with_subtype(item_class_id, item_subtype)
        self.changePage(3)

    def open_item_options_page(self, base_item_name):
        self.db_handler.insert_base_item_into_crafting_project(base_item_name)
        self.changePage(4)

    # Connect landing page buttons to their respective functions
    def on_body_armours_btn_clicked(self):
        self.open_base_selection_page("Body Armour")

    def on_gloves_btn_clicked(self):
        self.open_base_selection_page("Gloves")

    def on_boots_btn_clicked(self):
        self.open_base_selection_page("Boots")

    def on_helmets_btn_clicked(self):
        self.open_base_selection_page("Helmets")

    def on_jewellery_btn_clicked(self):
        self.open_base_selection_page("Jewellery")

    def on_cluster_jewels_btn_clicked(self):
        self.open_base_selection_page("Cluster Jewels")

    def on_flasks_btn_clicked(self):
        self.open_base_selection_page("Flasks")

    def on_one_handed_weapons_btn_clicked(self):
        self.open_base_selection_page("One Handed Weapons")

    def on_two_handed_weapons_btn_clicked(self):
        self.open_base_selection_page("Two Handed Weapons")

    def on_offhands_btn_clicked(self):
        self.open_base_selection_page("Offhands")

    def on_jewels_btn_clicked(self):
        self.open_base_selection_page("Jewels")

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

    def set_item_influences(self):
        pass

    def set_item_level(self):
        pass

    def set_item_quality(self):
        pass

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
