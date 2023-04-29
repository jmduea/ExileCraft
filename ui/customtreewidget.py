from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtWidgets import QTreeWidget, QWidget, QHeaderView, QHBoxLayout, QVBoxLayout, QLabel, QStyledItemDelegate, \
    QStyleOptionViewItem, QStyle
import json
from ExileCraft.databasehandler import DatabaseHandler
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import Qt, QModelIndex, QSize


class CustomItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Get the default size hint from the base class
        size = super(CustomItemDelegate, self).sizeHint(option, index)

        # Get the item associated with the index
        tree_widget = index.model().parent()
        item = tree_widget.itemFromIndex(index)

        if item is not None:
            # Calculate the maximum height required for all columns
            max_height = 0
            for column in range(item.treeWidget().columnCount()):
                # Get the text for the current column
                text = item.text(column)

                # Calculate the size required to fit the text
                text_rect = option.fontMetrics.boundingRect(option.rect, 0, text)

                # Update the maximum height
                max_height = max(max_height, text_rect.height())

            # Add some padding to the height
            max_height += 10

            # Update the height of the size hint
            size.setHeight(max_height)

        return size


class PillBadge(QWidget):
    def __init__(self, text, background_color, text_color, parent=None):
        super().__init__(parent)
        self.text = text
        self.background_color = background_color
        self.text_color = text_color
        self.setMinimumWidth(30)
        self.setMaximumWidth(60)
        self.setMinimumHeight(20)
        self.setMaximumHeight(20)
        self.setStyleSheet(""" 
            display: inline-block;
            background-color: #282828;
            background-color: transparent;
            font-size: 12px;
            line-height: 1;
            color: #fafafa;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: 20px;
        """)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.setBrush(self.background_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), self.height() // 2, self.height() // 2)

        # Draw the text
        painter.setPen(QPen(self.text_color))
        painter.setFont(self.font())
        painter.drawText(self.rect(), Qt.AlignCenter, self.text)


class PillBadgeItem(QTreeWidgetItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextAlignment(0, Qt.AlignLeft | Qt.AlignVCenter)
        self.setTextAlignment(1, Qt.AlignLeft | Qt.AlignVCenter)
        self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.setData(0, Qt.UserRole, [])
        self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def setNormalText(self, column: int, text: str):
        super().setText(column, text)

    def setCustomWidget(self, column: int, widget: QWidget):
        self.treeWidget().setItemWidget(self, column, widget)
        self.setTextAlignment(3, Qt.AlignLeft)

    def setText(self, column: int, text: str):
        if column == 0:
            # Set the text to an empty string
            super().setText(column, '')
            # Add the badges to the item data
            badges = text.split(',')
            self.setData(0, Qt.UserRole, badges)
        else:
            # For all other columns, set the text normally
            super().setText(column, text)


class CustomTreeWidget(QTreeWidget):
    def __init__(self, all_results):
        super().__init__()
        self.db_handler = DatabaseHandler()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        header = self.header()
        # Set the number of columns
        self.setColumnCount(6)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Fixed)
        self.setColumnWidth(1, 20)  # Second column width
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.setColumnWidth(2, 100)  # Third column width
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.setColumnWidth(3, 100)  # Fourth column width
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        self.setColumnWidth(4, 20)
        header.setSectionResizeMode(5, QHeaderView.Fixed)
        self.setColumnWidth(5, 20)

        self.setItemDelegate(CustomItemDelegate(self))
        self.setHeaderHidden(True)
        self.setStyleSheet("""
            QWidget {
                background-color: #282828;
                border: 0px;
            }
            QTreeWidget::item {
                background-color: #282828;
                border: 0px;
                margin: 0;
                padding: 3px;
            }
            QLabel {
                color: #8888ff;
                border: 0px;
                margin: 0;
                padding: 0;
                font-size: 16px;
            }
        """)

    def _create_pill_badge(self, text, background_color, text_color):
        return PillBadge(text, background_color, text_color, parent=self)

    def _create_pill_badges(self, tags, background_color, text_color):
        badges = []
        for tag in tags:
            badge = PillBadge(tag, background_color, text_color, parent=self)
            badges.append(badge)
        return badges

    def populate_with_mod_data(self, all_results, generation_type):
        self.clear()
        # Filter the results based on the generation_type
        filtered_results = [mod for mod in all_results if mod[4] == generation_type]
        # Create a dictionary to store mod groups and their mods
        mod_groups = {}
        # Iterate through mods_data and add them to the dictionary
        for mod in filtered_results:
            mod_group = mod[6]
            if mod_group not in mod_groups:
                mod_groups[mod_group] = []
            mod_groups[mod_group].append(mod)

        # Iterate through mod_groups and add them to the QTreeWidget
        for mod_group, mods in mod_groups.items():
            # Extract the stats for the mod group
            mod_group_stats = json.loads(mods[0][7])

            # Get the translation text for each stat without filling the placeholder values
            stat_translations = []
            for stat in mod_group_stats:
                stat_id = stat["id"]
                translation_text = self.db_handler.get_translation_text_by_id(stat_id)
                if translation_text is not None:
                    stat_translations.append(translation_text)

            # Join the translation texts and display them as the mod group text
            translated_mod_group = "\n".join(stat_translations).replace('{0}', '#').replace('{1}', '#')

            # Extract the additional information
            tags = json.loads(mods[0][10])
            total_mods = len(mods)
            highest_required_level = max([mod[2] for mod in mods])
            total_spawn_weight = 0
            for mod in mod_groups[mod_group]:
                weight_dict = json.loads(mod[14])
                if "weight" in weight_dict and str(weight_dict["weight"]).isdigit():
                    total_spawn_weight += int(weight_dict["weight"])

            # Format the mod group display text
            mod_group_display_text = f"{translated_mod_group}"

            # Create a parent item for the mod group
            mod_group_item = PillBadgeItem(self)
            mod_group_label = QLabel(mod_group_display_text)
            mod_group_item.setCustomWidget(0, mod_group_label)

            badges_container = QWidget()
            badges_container.setAutoFillBackground(False)
            badges_layout = QHBoxLayout()
            badges_layout.setSpacing(5)
            badges_layout.setContentsMargins(0, 0, 0, 0)
            badges_container.setLayout(badges_layout)
            # Create tag_badges based on the tags variable
            tag_badges = [PillBadge(tag, QColor("blue"), QColor("white")) for tag in tags]

            # Add the pill badges for implicit tags to the layout
            for badge in tag_badges:
                badges_layout.addWidget(badge)

            mod_group_item.setCustomWidget(2, badges_container)
            total_mods_badge = PillBadge(str(total_mods), QColor("#00bc8c"), QColor("white"))
            mod_group_item.setCustomWidget(3, total_mods_badge)
            highest_required_level_badge = PillBadge(str(highest_required_level), QColor("#7e7e7e"), QColor("white"))
            mod_group_item.setCustomWidget(4, highest_required_level_badge)
            total_spawn_weight_badge = PillBadge(str(total_spawn_weight), QColor("#e74c3c"), QColor("white"))
            mod_group_item.setCustomWidget(5, total_spawn_weight_badge)
            sorted_mods = sorted(mods, key=lambda mod: mod[2])

            # Add child items for the mods in the mod group
            for mod in sorted_mods:
                mod_item = PillBadgeItem(mod_group_item)
                # Extract the required data
                name = mod[1]
                required_level = mod[2]
                stats = mod[7]
                stats_list = json.loads(stats)
                translated_stats = []
                for stat in stats_list:
                    stat_id = stat["id"]
                    min_value = stat["min"]
                    max_value = stat["max"]
                    # Query the database for the translation_text
                    translation_text = self.db_handler.get_translation_text_by_id(stat_id)
                    if translation_text is not None:
                        placeholder_count = translation_text.count("{")
                        if placeholder_count == 1:
                            if min_value == max_value:
                                value_range = f"+{min_value}"
                                translated_stat = translation_text.format(value_range)
                            else:
                                value_range = f"+({min_value}-{max_value})"
                                translated_stat = translation_text.format(value_range)
                            translated_stats.append(translated_stat)
                        elif placeholder_count == 2:
                            translated_stat = translation_text.format(min_value, max_value)
                            translated_stats.append(translated_stat)

                implicit_tags = mod[10]
                spawn_weights = mod[14]  # Use index 14 instead of 12
                highest_weight = 0
                if spawn_weights:
                    weight_dict = json.loads(spawn_weights)
                    if "weight" in weight_dict and str(weight_dict["weight"]).isdigit():
                        highest_weight = int(weight_dict["weight"])
                # Format the text
                stats_text = "\n".join(translated_stats)
                # Convert implicit_tags JSON string to a list and then to a string without brackets
                implicit_tags_list = json.loads(implicit_tags)

                name_label = QLabel(name)
                mod_item.setCustomWidget(0, name_label)

                level_label = QLabel(str(required_level))
                mod_item.setCustomWidget(1, level_label)

                stats_label = QLabel(stats_text)
                mod_item.setCustomWidget(2, stats_label)

                # Create pill badges for implicit_tags_str and highest_weight
                implicit_tags_badges = self._create_pill_badges(implicit_tags_list, QColor("blue"), QColor("white"))

                # Create a new QWidget to hold all pill badges
                badges_container = QWidget()
                badges_container.setAutoFillBackground(False)
                badges_layout = QHBoxLayout()
                badges_layout.setSpacing(5)
                badges_layout.setContentsMargins(0, 0, 0, 0)
                badges_container.setLayout(badges_layout)

                # Add the pill badges for implicit tags to the layout
                for badge in implicit_tags_badges:
                    badges_layout.addWidget(badge)

                mod_item.setCustomWidget(3, badges_container)

                highest_weight_badge = self._create_pill_badge(str(highest_weight), QColor("blue"), QColor("white"))
                mod_item.setCustomWidget(5, highest_weight_badge)

