# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################
import os

from PySide6 import QtGui
from PySide6.QtCore import QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton

from modules.data import database_manager
from modules.data.database_manager import DatabaseManager, ItemManager
from modules.gui.uis.windows.main_window.ui_mainwindow import UI_MainWindow
from modules.gui.widgets import PyWindow


class MainFunctions:
    """
    A class used to control the main functions of the UI.

    ...

    Attributes
    ----------
    ui : object
        An instance of the UI_MainWindow class.


    Methods
    -------
    set_page(page)
        Sets the current widget to the given page.
    set_left_column_menu(menu, title, icon_path)
        Sets the current widget of the left column menu, updates the title and icon.
    left_column_is_visible()
        Returns a boolean indicating if the left column is visible.
    right_column_is_visible()
        Returns a boolean indicating if the right column is visible.
    set_right_column_menu(menu)
        Sets the current widget of the right column menu.
    get_title_bar_btn(object_name)
        Returns the QPushButton with the given object name in the title bar.
    get_left_menu_btn(object_name)
        Returns the QPushButton with the given object name in the left menu.
    toggle_left_column()
        Toggles the visibility of the left column.
    toggle_right_column()
        Toggles the visibility of the right column.
    start_box_animation(left_box_width, right_box_width, direction)
        Starts the animation for the left and right boxes.
    """

    def __init__(self):
        """Initializes an instance of the MainFunctions class."""
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    def set_page(self, page):
        """Sets the current widget to the given page."""
        self.ui.load_pages.pages.setCurrentWidget(page)

    def set_left_column_menu(self, menu, title, icon_path):
        """
        Sets the current widget of the left column menu, updates the title and icon.

        Parameters:
        menu (QWidget): The widget to set as the current widget.
        title (str): The title to set for the left column menu.
        icon_path (str): The path to the icon for the left column menu.
        """
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    def left_column_is_visible(self):
        """Returns a boolean indicating if the left column is visible."""
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def right_column_is_visible(self):
        """Returns a boolean indicating if the right column is visible."""
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    def set_right_column_menu(self, menu):
        """Sets the current widget of the right column menu."""
        self.ui.right_column.menus.setCurrentWidget(menu)

    def get_title_bar_btn(self, object_name):
        """
        Returns the QPushButton with the given object name in the title bar.

        Parameters:
        object_name (str): The object name of the QPushButton.
        """
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    def get_left_menu_btn(self, object_name):
        """
        Returns the QPushButton with the given object name in the left menu.

        Parameters:
        object_name (str): The object name of the QPushButton.
        """
        return self.ui.left_menu.findChild(QPushButton, object_name)

    def toggle_left_column(self):
        """Toggles the visibility of the left column."""
        # Get columns actual size
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        """Toggles the visibility of the right column."""
        # Get columns actual size
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        """
        Starts the animation for the left and right boxes.

        Parameters:
        left_box_width (int): The current width of the left box.
        right_box_width (int): The current width of the right box.
        direction (str): The direction of the animation ("left" or "right").
        """
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()


class ComboboxUpdater:
    """
    This class is responsible for updating the QComboBox and QSpinBox objects in the GUI. It
    takes in several QComboBox and QSpinBox objects, and updates their values based on the user's
    selections. It also handles the display of item images, properties, requirements, and implicits.

    Attributes:
        base_group_combobox (QComboBox): A combobox that displays the available base item
        groups.
        base_combobox (QComboBox): A combobox that displays the available bases.
        base_item_combobox (QComboBox): A combobox that displays the available base item types.
        item_level_spinbox (QSpinBox): A spinbox that allows the user to select an item level.
        item_quality_spinbox (QSpinBox): A spinbox that allows the user to select an item quality
        level.
        item_img_label (QLabel): A label that displays the image of the selected item.
        item_properties_label (QLabel): A label that displays the properties of the selected item.
        item_requirements_label (QLabel): A label that displays the requirements of the selected
        item.
        item_level_label (QLabel): A label that displays the selected item level.
        item_quality_label (QLabel): A label that displays the selected item quality level.
        item_header_label (QLabel): A label that displays the header of the selected item.
        item_implicits_container (QWidget): A container that holds the implicits label.
        item_implicits_label (QLabel): A label that displays the implicits of the selected item.
        item_spacer_3 (QSpacerItem): A spacer item used for layout purposes.
        prefix_1_container (QWidget): A container that holds the prefix 1 label.
        prefix_2_container (QWidget): A container that holds the prefix 2 label.
        prefix_3_container (QWidget): A container that holds the prefix 3 label.
        suffix_1_container (QWidget): A container that holds the suffix 1 label.
        suffix_2_container (QWidget): A container that holds the suffix 2 label.
        suffix_3_container (QWidget): A container that holds the suffix 3 label.
    """

    def __init__(
        self,
        base_group_combobox,
        base_combobox,
        base_item_combobox,
        item_level_spinbox,
        item_quality_spinbox,
        item_img_label,
        item_properties_label,
        item_requirements_label,
        item_level_label,
        item_quality_label,
        item_header_label,
        item_implicits_container,
        item_implicits_label,
        item_spacer_3,
        prefix_1_container,
        prefix_2_container,
        prefix_3_container,
        suffix_1_container,
        suffix_2_container,
        suffix_3_container,
    ):
        super().__init__()
        self.window = PyWindow
        self.base_group_combobox = base_group_combobox
        self.base_group_combobox.setCurrentIndex(-1)
        self.base_combobox = base_combobox
        self.base_item_combobox = base_item_combobox
        self.item_level_spinbox = item_level_spinbox
        self.item_quality_spinbox = item_quality_spinbox
        self.item_img_label = item_img_label
        self.item_properties_label = item_properties_label
        self.item_requirements_label = item_requirements_label
        self.item_level_label = item_level_label
        self.item_quality_label = item_quality_label
        self.item_header_label = item_header_label
        self.item_implicits_container = item_implicits_container
        self.item_implicits_label = item_implicits_label
        self.item_spacer_3 = item_spacer_3
        self.prefix_1_container = prefix_1_container
        self.prefix_2_container = prefix_2_container
        self.prefix_3_container = prefix_3_container
        self.suffix_1_container = suffix_1_container
        self.suffix_2_container = suffix_2_container
        self.suffix_3_container = suffix_3_container
        self.items_cache = {}
        self.item_class = None
        self.base_item = None
        self.item_level = (
            self.item_level_spinbox.value() if self.item_level_spinbox.value() else 0
        )
        self.item_quality = (
            self.item_quality_spinbox.value()
            if self.item_quality_spinbox.value()
            else 0
        )

    def update_base_combobox(self):
        """
        Updates the base combobox based on the currently selected item_class in the base group combobox.
        """

        # Get database session
        db_url = database_manager.db_url
        db_manager = DatabaseManager(db_url)
        item_class_manager = ItemManager()
        session = db_manager.get_session()

        # Get base item groups from database
        subtype_display_names = (
            item_class_manager.get_item_class_subtypes_and_display_names(
                session, item_class_name=self.base_group_combobox.currentText()
            )
        )

        self.base_combobox.clear()
        self.base_combobox.setEnabled(True)

        for display_name in subtype_display_names:
            self.base_combobox.addItem(display_name)

    def update_base_item_combobox(self, index):
        """
        Retrieves the base items for the combobox based on the selected index.

        Args:
            index (int): The index of the selected item in the base combobox.
        """
        if self.base_combobox.itemText(index) is not None:
            db_url = database_manager.db_url
            db_manager = DatabaseManager(db_url)
            item_manager = ItemManager()
            session = db_manager.get_session()

            self.items_cache = {}
            subtype_display_name = self.base_combobox.currentText()
            base_items = item_manager.get_base_items_from_subtype_display_name(
                session, subtype_display_name
            )

            self.base_item_combobox.clear()
            self.base_item_combobox.setEnabled(True)

            if (
                base_items is not None
                and self.base_combobox.itemText(index) is not None
            ):
                for base_item in base_items:
                    self.base_item_combobox.addItem(base_item.name)
                    self.items_cache[base_item.name] = base_item

        self.item_level_spinbox.setEnabled(True)
        self.item_quality_spinbox.setEnabled(True)

    def set_item_view_box_background(self):
        """
        Sets the background of the item view box to the image of the currently selected item.

        This method fetches the name of the currently selected item from the base item combo box,
        modifies the name to match the naming convention of the item images, constructs the path to
        the image, and then attempts to load and display the image in the item view box.

        If the image fails to load or an error occurs during the process, a message is printed to
        the console. If the image is loaded successfully, it is displayed in the item view box and
        is centered and not scaled.

        Raises:
        Exception: If an error occurs when loading the image.
        """

        item_name = self.base_item_combobox.currentText()
        current_item = self.items_cache.get(item_name)

        if current_item is None:
            return
        print(current_item.properties)
        visual_identity = current_item.visual_identity

        current_file_path = "modules/gui/assets/images/items"
        image_path = os.path.join(current_file_path, visual_identity.name + ".png")

        try:
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print(f"Failed to load image at {image_path}")
            else:
                self.item_img_label.setPixmap(pixmap)
                self.item_img_label.setAlignment(Qt.AlignCenter)
                self.item_img_label.setScaledContents(False)
        except Exception as e:
            print(f"Error loading image: {e}")

    def clear_item_view_box_background(self):
        """
        Clears the background image of a label widget assigned to the item_img_label attribute of the load_pages
        object in the current instance of a class.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        self.item_img_label.setPixmap(QPixmap())

    def set_item_header_label(self):
        """
         Update the item header label in the load_pages object by retrieving the currently selected item from the
         base_item_combobox object in the left_column object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        item_name = self.base_item_combobox.currentText()
        item_name_str = f"Crafting Project:\n{item_name}"
        self.item_header_label.setText(item_name_str)

    def set_item_level(self):
        """
        Sets the item level value from the item_level_spinbox object in the left_column object and updates the HTML
        formatted label to display the item level in the load_pages object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        item_level_value = self.item_level_spinbox.value()
        self.item_level = self.item_level_spinbox.value()
        current_item = self.items_cache.get(self.base_item_combobox.currentText())
        if current_item:
            current_item.item_level = self.item_level
            item_level = str(item_level_value)
            item_html = (
                f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Item Level: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#fff;">{item_level}</span></p>'
            )
            self.item_level_label.setText(item_html)
        else:
            return

    def set_item_quality(self):
        """
        Sets the item quality value from the item_quality_spinbox object in the left_column object and updates the
        HTML formatted label to display the item quality percentage in the load_pages object.

        Args:
            self: The current instance of the class where the method is called.

        Returns:
            None
        """
        item_quality_value = self.item_quality_spinbox.value()
        self.item_quality = self.item_quality_spinbox.value()
        current_item = self.items_cache.get(self.base_item_combobox.currentText())
        if current_item:
            current_item.quality = self.item_quality
            item_quality = str(item_quality_value)
            quality_html = (
                f'<p align="center"><span style=" font-size:11pt; color:#827a6c;">Quality: </span>'
                f'<span style=" font-size:11pt; font-weight:bold; color:#8787fe;">{item_quality}%</span></p>'
            )
            self.item_quality_label.setText(quality_html)
        else:
            return
        # self.item_properties_label.setText(current_item.formatted_properties())

    @staticmethod
    def format_implicit_string(current_item):
        """
        Formats the implicit properties of an item for display in the GUI.

        This method takes a string of implicit properties, calculates the average stat for each property, and formats
        these properties into an HTML string that can be displayed in the GUI.

        Args:
            current_item (object): An instance of an item.

        Returns:
            str: A string containing the formatted implicit properties, ready to be displayed in the GUI.
        """

        item_implicits = current_item.implicit_translation
        if not item_implicits:
            return ""
        else:
            stat_translation_string = item_implicits[2:-3]
            # Format the implicit string
            implicit_formatted = (
                (
                    f'<p style="line-height:1.2; padding-bottom:.05em;" align="center">'
                    f'<span style=" font-size:10.5pt; color:#8787fe;">'
                    f"{stat_translation_string}</span></p>"
                )
                if stat_translation_string
                else ""
            )

            return implicit_formatted

    def update_implicit_label(self, current_item):
        if current_item:
            implicit_formatted = self.format_implicit_string(current_item)

            if implicit_formatted != "":
                # Set the text of the implicit label
                self.item_spacer_3.setEnabled(True)
                self.item_spacer_3.show()
                self.item_implicits_container.setEnabled(True)
                self.item_implicits_container.show()
                self.item_implicits_label.setEnabled(True)
                self.item_implicits_label.show()
                self.item_implicits_label.setText(implicit_formatted)
            else:
                self.item_spacer_3.hide()
                self.item_implicits_label.hide()

    def update_labels(self):
        item_name = self.base_item_combobox.currentText()
        current_item = self.items_cache.get(item_name)
        if current_item is None:
            return
        current_item.item_level = self.item_level
        current_item.quality = self.item_quality
        self.item_requirements_label.setText(current_item.formatted_requirements())
        self.item_properties_label.setText(current_item.formatted_properties())
        self.update_implicit_label(current_item)

    def clear_labels(self):
        """
        Clears the text of the item requirements, properties, and implicits labels,
        and hides the implicits container and spacer.
        """
        self.item_requirements_label.clear()
        self.item_properties_label.clear()
        self.item_implicits_label.clear()
        self.item_implicits_container.hide()
        self.item_spacer_3.hide()
