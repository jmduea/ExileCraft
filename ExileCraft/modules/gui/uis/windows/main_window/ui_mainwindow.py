from typing import Any, Dict

from PySide6.QtWidgets import QFrame, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget

from modules.gui.core.functions import Functions
from modules.gui.core.json_settings import Settings
from modules.gui.core.json_themes import Themes
from modules.gui.uis.columns.ui_right_column import Ui_RightColumn
from modules.gui.uis.pages.ui_main_pages import Ui_MainPages
from modules.gui.widgets.py_credits_bar import PyCredits
from modules.gui.widgets.py_left_column import PyLeftColumn
from modules.gui.widgets.py_left_menu import PyLeftMenu
from modules.gui.widgets.py_title_bar import PyTitleBar
from modules.gui.widgets.py_window import PyWindow


class UiMainWindow:
    def setup_ui(self, parent: QMainWindow) -> None:
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        try:
            # Load Settings
            settings = Settings()
            self.settings: Dict[str, Any] = settings.items
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.settings = {}

        try:
            # Load Theme
            themes = Themes()
            self.themes: Dict[str, Any] = themes.items
        except Exception as e:
            print(f"Error loading themes: {e}")
            self.themes = {}

        # Set Initial Parameters
        parent.resize(
            self.settings.get("startup_size", [800, 600])[0],
            self.settings.get("startup_size", [800, 600])[1],
        )
        parent.setMinimumSize(
            self.settings.get("minimum_size", [400, 300])[0],
            self.settings.get("minimum_size", [400, 300])[1],
        )

        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(
            f"""
                    font: {self.settings.get("font", {}).get("text_size", 10)}pt "{self.settings.get("font", {}).get("family", "Arial")}";
                    color: {self.themes.get("app_color", {}).get("text_foreground", "black")};
                """
        )

        self.central_widget_layout = QVBoxLayout(self.central_widget)
        self.central_widget_layout.setContentsMargins(10, 10, 10, 10)

        # Load Py Window Custom Widget
        self.window = PyWindow(
            parent,
            bg_color=self.themes.get("app_color", {}).get("bg_one", "white"),
            border_color=self.themes.get("app_color", {}).get("bg_two", "gray"),
            text_color=self.themes.get("app_color", {}).get("text_foreground", "black"),
        )

        # Add Py Window to Central Widget
        self.central_widget_layout.addWidget(self.window)

        # Add Left Menu Frame
        left_menu_margin = self.settings.get("left_menu_content_margins", 10)
        left_menu_minimum = self.settings.get("lef_menu_size", {}).get("minimum", 200)
        self.left_menu_frame = QFrame()
        self.left_menu_frame.setMaximumSize(
            left_menu_minimum + (left_menu_margin * 2), 17280
        )
        self.left_menu_frame.setMinimumSize(
            left_menu_minimum + (left_menu_margin * 2), 0
        )

        # Left Menu Layout
        self.left_menu_layout = QHBoxLayout(self.left_menu_frame)
        self.left_menu_layout.setContentsMargins(
            left_menu_margin, left_menu_margin, left_menu_margin, left_menu_margin
        )

        # Add Custom Left Menu
        self.left_menu = PyLeftMenu(
            parent=self.left_menu_frame,
            app_parent=self.central_widget,  # For tooltip parent
            dark_one=self.themes.get("app_color", {}).get("dark_one", "black"),
            dark_three=self.themes.get("app_color", {}).get("dark_three", "gray"),
            dark_four=self.themes.get("app_color", {}).get("dark_four", "darkgray"),
            bg_one=self.themes.get("app_color", {}).get("bg_one", "white"),
            icon_color=self.themes.get("app_color", {}).get("icon_color", "black"),
            icon_color_hover=self.themes.get("app_color", {}).get("icon_hover", "blue"),
            icon_color_pressed=self.themes.get("app_color", {}).get(
                "icon_pressed", "red"
            ),
            icon_color_active=self.themes.get("app_color", {}).get(
                "icon_active", "green"
            ),
            context_color=self.themes.get("app_color", {}).get(
                "context_color", "yellow"
            ),
            text_foreground=self.themes.get("app_color", {}).get(
                "text_foreground", "black"
            ),
            text_active=self.themes.get("app_color", {}).get("text_active", "blue"),
        )
        self.left_menu_layout.addWidget(self.left_menu)

        # Add Left Column
        self.left_column_frame = QFrame()
        self.left_column_frame.setMaximumWidth(
            self.settings.get("left_column_size", {}).get("minimum", 200)
        )
        self.left_column_frame.setMinimumWidth(
            self.settings.get("left_column_size", {}).get("minimum", 200)
        )
        self.left_column_frame.setStyleSheet(
            f"background: {self.themes.get('app_color', {}).get('bg_two', 'gray')}"
        )

        # Add Layout to Left Column
        self.left_column_layout = QVBoxLayout(self.left_column_frame)
        self.left_column_layout.setContentsMargins(0, 0, 0, 0)

        # Add custom left menu widget
        self.left_column = PyLeftColumn(
            parent,
            app_parent=self.central_widget,
            text_title="Settings Left Frame",
            text_title_size=self.settings.get("font", {}).get("title_size", 12),
            text_title_color=self.themes.get("app_color", {}).get(
                "text_foreground", "black"
            ),
            icon_path=Functions.set_svg_icon("icon_settings.svg"),
            dark_one=self.themes.get("app_color", {}).get("dark_one", "black"),
            bg_color=self.themes.get("app_color", {}).get("bg_three", "white"),
            btn_color=self.themes.get("app_color", {}).get("bg_three", "white"),
            btn_color_hover=self.themes.get("app_color", {}).get("bg_two", "gray"),
            btn_color_pressed=self.themes.get("app_color", {}).get(
                "bg_one", "lightgray"
            ),
            icon_color=self.themes.get("app_color", {}).get("icon_color", "black"),
            icon_color_hover=self.themes.get("app_color", {}).get("icon_hover", "blue"),
            context_color=self.themes.get("app_color", {}).get(
                "context_color", "yellow"
            ),
            icon_color_pressed=self.themes.get("app_color", {}).get(
                "icon_pressed", "red"
            ),
            icon_close_path=Functions.set_svg_icon("icon_close.svg"),
        )
        self.left_column_layout.addWidget(self.left_column)

        # Add Right Widgets
        self.right_app_frame = QFrame()

        # Add Right App Layout
        self.right_app_layout = QVBoxLayout(self.right_app_frame)
        self.right_app_layout.setContentsMargins(3, 3, 3, 3)
        self.right_app_layout.setSpacing(6)

        # Add Title Bar Frame
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setMinimumHeight(40)
        self.title_bar_frame.setMaximumHeight(40)
        self.title_bar_layout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Add Custom Title Bar
        self.title_bar = PyTitleBar(
            parent,
            logo_width=100,
            app_parent=self.central_widget,
            logo_image="exilecraft.svg",
            bg_color=self.themes.get("app_color", {}).get("bg_two", "gray"),
            div_color=self.themes.get("app_color", {}).get("bg_three", "lightgray"),
            btn_bg_color=self.themes.get("app_color", {}).get("bg_two", "gray"),
            btn_bg_color_hover=self.themes.get("app_color", {}).get(
                "bg_three", "lightgray"
            ),
            btn_bg_color_pressed=self.themes.get("app_color", {}).get(
                "bg_one", "white"
            ),
            icon_color=self.themes.get("app_color", {}).get("icon_color", "black"),
            icon_color_hover=self.themes.get("app_color", {}).get("icon_hover", "blue"),
            icon_color_pressed=self.themes.get("app_color", {}).get(
                "icon_pressed", "red"
            ),
            icon_color_active=self.themes.get("app_color", {}).get(
                "icon_active", "green"
            ),
            context_color=self.themes.get("app_color", {}).get(
                "context_color", "yellow"
            ),
            dark_one=self.themes.get("app_color", {}).get("dark_one", "black"),
            text_foreground=self.themes.get("app_color", {}).get(
                "text_foreground", "black"
            ),
            radius=8,
            font_family=self.settings.get("font", {}).get("family", "Arial"),
            title_size=self.settings.get("font", {}).get("title_size", 12),
            is_custom_title_bar=self.settings.get("custom_title_bar", False),
        )
        self.title_bar_layout.addWidget(self.title_bar)

        # Add Content Area
        self.content_area_frame = QFrame()

        # Create Content Area Layout
        self.content_area_layout = QHBoxLayout(self.content_area_frame)
        self.content_area_layout.setContentsMargins(0, 0, 0, 0)
        self.content_area_layout.setSpacing(0)

        # Left Content
        self.content_area_left_frame = QFrame()

        # Import Main Pages to Content Area
        self.load_pages = Ui_MainPages()
        self.load_pages.setupUi(self.content_area_left_frame)

        # Right Bar
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(
            self.settings.get("right_column_size", {}).get("minimum", 200)
        )
        self.right_column_frame.setMaximumWidth(
            self.settings.get("right_column_size", {}).get("minimum", 200)
        )

        # Import Right Column
        self.content_area_right_layout = QVBoxLayout(self.right_column_frame)
        self.content_area_right_layout.setContentsMargins(5, 5, 5, 5)
        self.content_area_right_layout.setSpacing(0)

        # Right BG
        self.content_area_right_bg_frame = QFrame()
        self.content_area_right_bg_frame.setObjectName("content_area_right_bg_frame")
        self.content_area_right_bg_frame.setStyleSheet(
            f"""
                #content_area_right_bg_frame {{
                    border-radius: 8px;
                    background-color: {self.themes.get("app_color", {}).get("bg_two", "gray")};
                }}
                """
        )

        # Add Bg
        self.content_area_right_layout.addWidget(self.content_area_right_bg_frame)

        # Add Right Pages to Right Column
        self.right_column = Ui_RightColumn()
        self.right_column.setupUi(self.content_area_right_bg_frame)

        # Add to Layouts
        self.content_area_layout.addWidget(self.content_area_left_frame)
        self.content_area_layout.addWidget(self.right_column_frame)

        # Credits/Bottom App Frame
        self.credits_frame = QFrame()
        self.credits_frame.setMinimumHeight(26)
        self.credits_frame.setMaximumHeight(26)

        # Create Layout
        self.credits_layout = QVBoxLayout(self.credits_frame)
        self.credits_layout.setContentsMargins(0, 0, 0, 0)

        # Add Credits Custom Widget
        self.credits = PyCredits(
            bg_two=self.themes.get("app_color", {}).get("bg_two", "gray"),
            copyright=self.settings.get("copyright", ""),
            version=self.settings.get("version", ""),
            font_family=self.settings.get("font", {}).get("family", "Arial"),
            text_size=self.settings.get("font", {}).get("text_size", 10),
            text_description_color=self.themes.get("app_color", {}).get(
                "text_description", "gray"
            ),
        )
        # Add to Layout
        self.credits_layout.addWidget(self.credits)

        # Add widgets to right layout
        self.right_app_layout.addWidget(self.title_bar_frame)
        self.right_app_layout.addWidget(self.content_area_frame)
        self.right_app_layout.addWidget(self.credits_frame)

        # Add Widgets to PyWindow
        self.window.layout.addWidget(self.left_menu_frame)
        self.window.layout.addWidget(self.left_column_frame)
        self.window.layout.addWidget(self.right_app_frame)

        # Add Central Widget and set content margins
        parent.setCentralWidget(self.central_widget)
