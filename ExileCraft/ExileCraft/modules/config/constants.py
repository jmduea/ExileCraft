ITEM_CLASS_WHITELIST = {
    "LifeFlask",
    "ManaFlask",
    "HybridFlask",
    "Amulet",
    "Ring",
    "Claw",
    "Dagger",
    "Rune Dagger",
    "Wand",
    "One Hand Sword",
    "Thrusting One Hand Sword",
    "One Hand Axe",
    "One Hand Mace",
    "Bow",
    "Staff",
    "Warstaff",
    "Two Hand Sword",
    "Two Hand Axe",
    "Two Hand Mace",
    "Quiver",
    "Belt",
    "Gloves",
    "Boots",
    "Body Armour",
    "Helmet",
    "Shield",
    "Sceptre",
    "UtilityFlask",
    "UtilityFlaskCritical",
    "Jewel",
    "AbyssJewel",

}

ITEM_CLASS_BLACKLIST = {
    "LabyrinthTrinket",
    "MiscMapItem",
    "Leaguestone",
    "LabyrinthItem",
    "PantheonSoul",
    "UniqueFragment",
    "IncursionItem",
    "MetamorphosisDNA",
    "HideoutDoodad",
    "LabyrinthMapItem",
    "Incubator",
    "Microtransaction",
    "HarvestInfrastructure",
    "HarvestSeed",
    "HarvestPlantBooster",
    "Trinket",
    "HeistObjective",
    "HiddenItem",
    "ArchnemesisMod",
    "MemoryLine",
    "HeistContract",
    "HeistBlueprint",
    "HeistEquipmentWeapon",
    "HeistEquipmentTool",
    "HeistEquipmentUtility",
    "HeistEquipmentReward",
    "DivinationCard",
    "Map",
    "MapFragment",
    "AtlasRegionUpgradeItem",
    "ExpeditionLogbook",
    "IncubatorStackable",
    "AtlasUpgradeItem",
    "SentinelDrone",
    "DelveStackableSocketableCurrency",
    "DelveSocketableCurrency",
    "QuestItem",
    "StackableCurrency",
    "Active Skill Gem",
    "Support Skill Gem",
    "Currency",
    "FishingRod",
}

TAGS_MAP = {
    'Body Armour': {
        "Body Armour (dex)": ["armour", "dex_armour"],
        "Body Armour (dex/int)": ["armour", "dex_int_armour"],
        "Body Armour (dex/str)": ["armour", "dex_str_armour"],
        "Body Armour (dex/str/int)": ["armour", "dex_str_int_armour"],
        "Body Armour (str)": ["armour", "str_armour"],
        "Body Armour (str/int)": ["armour", "str_int_armour"],
        "Body Armour (int)": ["armour", "int_armour"],
    },
    'Boots': {
        "Boots (dex)": ["armour", "dex_armour"],
        "Boots (dex/int)": ["armour", "dex_int_armour"],
        "Boots (dex/str)": ["armour", "dex_str_armour"],
        "Body Armour (dex/str/int)": ["armour", "dex_str_int_armour"],
        "Body Armour (str)": ["armour", "str_armour"],
        "Body Armour (str/int)": ["armour", "str_int_armour"],
        "Body Armour (int)": ["armour", "int_armour"],
    },
}

ITEM_CLASS_SUBTYPES = {
    'Body Armour': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                     "str_dex_int_armour", "str_int_armour"},
    'Boots': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
              "str_int_armour"},
    'Gloves': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
               "str_int_armour"},
    'Helmets': {"ward_armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                "str_int_armour"},
    'Shields': {"dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour", "str_int_armour"},
    'Jewellery': {"amulet", "belt", "ring"},
    'One Handed Weapons': {"one_hand_weapon"},
    'Two Handed Weapons': {"two_hand_weapon"},
    'Offhands': {"shield", "quiver"},
    'Jewels': {"abyss_jewel_caster", "abyss_jewel_melee", "abyss_jewel_ranged", "abyss_jewel_summoner",
               "dexjewel",
               "intjewel", "strjewel"},
    'Cluster Jewels': {"expansion_jewel_large", "expansion_jewel_medium", "expansion_jewel_small"},
    'Flasks': {"hybrid_flask", "life_flask", "mana_flask", "utility_flask"}
}

BTN_STYLESHEET = (
            "QPushButton {"
            "    border: 1px solid #000;"
            "       border-top-width: 1px;"
            "       border-right-width: 1px;"
            "       border-bottom-width: 1px;"
            "       border-left-width: 1px;"
            "       border-top-style: solid;"
            "       border-right-style: solid;"
            "       border-bottom-style: solid;"
            "       border-left-style: solid;"
            "       border-top-color: rgb(0, 0, 0);"
            "       border-right-color: rgb(0, 0, 0);"
            "       border-bottom-color: rgb(0, 0, 0);"
            "       border-left-color: rgb(0, 0, 0);"
            "       border-image-source: initial;"
            "       border-image-slice: initial;"
            "       border-image-width: initial;"
            "       border-image-outset: initial;"
            "       border-image-repeat: initial;"
            "    border-radius: 4px;"
            "    background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #1e1e1e, stop: 1 #3c3c3c);"
            "    border-image: none;"
            "    color: #FFF;"
            "    text-shadow: 1px 1px #000;"
            "    box-shadow: inset 0 1px 1px #666, 0 1px 2px rgba(0,0,0,0.31);"
            "    padding: 0px 10px;"
            "    margin: 7px;"
            "    font-family: Open Sans;"
            "    font-size: 16px;"
            "    font-weight: bold;"
            "    height: 36px;"
            "    line-height: 36px;"
            "    text-align: center;"
            "}"
            "QPushButton:hover {"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0 y2: 1,"
            "                                       stop: 0 #2d2d2d, stop: 1 #4b4b4b);"
            "}"
            "QPushButton:pressed {"
            "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,"
            "                                      stop: 0 #4b4b4b, stop: 1 #2d2d2d);"
            "}"
            "QPushButton:flat {"
            "    border: none; /* no border for a flat push button */"
            "}"
            )

LABEL_STYLESHEET = (
            "QWidget {"
            "    border-image: none;"
            "    background-blend-mode: overlay;"
            "}"
            "QLabel {"
            "    text-align: center;"
            "    padding: 5px 10px;"
            "    font-size: 16px;"
            "    background-color: #444;"
            "       background-image: initial;"
            "       background-position-x: initial;"
            "       background-position-y: initial;"
            "       background-size: initial;"
            "       background-repeat-x: initial;"
            "       background-repeat-y: initial;"
            "       background-attachment: initial;"
            "       background-origin: initial;"
            "       background-clip: initial;"
            "    width: 100%;"
            "    box-sizing: border-box;"
            "    color: #FFF;"
            "    font-family: Open Sans;"
            "}"
            )

SUBTYPE_DISPLAY_NAMES = {
            "armour": "{}",
            "ward_armour": "{}(Ward)",
            "dex_armour": "{}(dex)",
            "dex_int_armour": "{}(dex/int)",
            "int_armour": "{}(int)",
            "str_armour": "{}(str)",
            "str_dex_armour": "{}(str/dex)",
            "str_dex_int_armour": "{}(str/dex/int)",
            "str_int_armour": "{}(str/int)",
            "amulet": "Amulet",
            "life_flask": "Life Flask",
            "mana_flask": "Mana Flask",
            "hybrid_flask": "Hybrid Flask",
            "utility_flask": "Utility Flask",
            "ring": "Ring",
            "belt": "Belt",
            "abyss_jewel_ranged": "Searching Eye Jewel",
            "abyss_jewel_caster": "Hypnotic Eye Jewel",
            "abyss_jewel_summoner": "Ghastly Eye Jewel",
            "abyss_jewel_melee": "Murderous Eye Jewel",
            "dexjewel": "Viridian Jewel",
            "intjewel": "Cobalt Jewel",
            "strjewel": "Crimson Jewel",
            "shield": "Shields",
            "quiver": "Quivers",
            "expansion_jewel_small": "Small Cluster Jewel",
            "expansion_jewel_medium": "Medium Cluster Jewel",
            "expansion_jewel_large": "Large Cluster Jewel"
            }

ALL_SUBTYPES = {"armour", "dex_armour", "dex_int_armour", "int_armour", "str_armour", "str_dex_armour",
                "str_dex_int_armour", "str_int_armour"
                }
