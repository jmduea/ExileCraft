# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################

"""
    This file contains constants used by the GUI.


"""

# BTN_HOME CONSTANTS
BTN_HOME = "btn_home"
ICON_HOME = "icon_home.svg"
HOME = "Home"
TOOLTIP_HOME = "Home Page"

# BTN_PAGE_2 CONSTANTS
BTN_PAGE_2 = "btn_page_2"

# BTN_PAGE_3 CONSTANTS
BTN_PAGE_3 = "btn_page_3"
ICON_SEND = "icon_send.svg"
CRAFTING_SIMULATOR = "Crafting Simulator"
TOOLTIP_SIMULATE = "Simulate Crafting Methods"

# BTN_INFO CONSTANTS
BTN_INFO = "btn_info"

# BTN_CLOSE_LEFT_COLUMN CONSTANTS
BTN_CLOSE_LEFT_COLUMN = "btn_close_left_column"

# BTN_SETTINGS CONSTANTS
BTN_SETTINGS = "btn_settings"

# BTN_TOP_SETTINGS CONSTANTS
BTN_TOP_SETTINGS = "btn_top_settings"

# BTN FUNCTIONS
BUTTON_FUNCTIONS = {
    BTN_HOME: "select_menu_and_load_page",
    BTN_PAGE_2: "select_menu_and_load_page",
    BTN_PAGE_3: "select_menu_and_load_page",
    BTN_INFO: "btn_info_clicked",
    BTN_CLOSE_LEFT_COLUMN: "btn_close_left_column_clicked",
    BTN_SETTINGS: "btn_settings_clicked",
    BTN_TOP_SETTINGS: "btn_top_settings_clicked",
}

# MENU CONSTANTS
ADD_LEFT_MENUS = [
    {
        "btn_icon": "icon_home.svg",
        "btn_id": "btn_home",
        "btn_text": "Home",
        "btn_tooltip": "Home page",
        "show_top": True,
        "is_active": True,
    },
    {
        "btn_icon": "icon_send.svg",
        "btn_id": "btn_page_3",
        "btn_text": "Crafting Simulator",
        "btn_tooltip": "Simulate Crafting Methods",
        "show_top": True,
        "is_active": False,
    },
    {
        "btn_icon": "icon_info.svg",
        "btn_id": "btn_info",
        "btn_text": "Open Item Info",
        "btn_tooltip": "Open Item Info",
        "show_top": False,
        "is_active": False,
    },
    {
        "btn_icon": "icon_settings.svg",
        "btn_id": "btn_settings",
        "btn_text": "Open Settings",
        "btn_tooltip": "Open Settings",
        "show_top": False,
        "is_active": False,
    },
]

ADD_TITLE_BAR_MENUS = [
    {
        "btn_icon": "icon_search.svg",
        "btn_id": "btn_search",
        "btn_tooltip": "Search",
        "is_active": False,
    },
    {
        "btn_icon": "icon_more_options.svg",
        "btn_id": "btn_top_settings",
        "btn_tooltip": "Crafting Methods",
        "is_active": False,
    },
]
