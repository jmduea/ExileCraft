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
from enum import Enum, EnumMeta, IntEnum

__all__ = [
    "item_class_whitelist",
    "item_class_map",
    "subtype_display_names",
    "domain_whitelist",
    "RARITY",
    "STAT_INTERPOLATION_TYPES",
    "MOD_MAX_STATS",
    "MOD_STATS_RANGE",
    "one_hand_weapon_types",
    "two_hand_weapon_types",
    "armour_types",
    "jewellery_types",
    "flask_types",
    "generation_type_whitelist",
    "subtype_tags_map",
    "armour_subtypes",
    "ITEM_PROPERTIES",
    "ITEM_REQUIREMENTS",
    "generation_type_blacklist",
    "ITEM_PROPERTIES_MAP",
    "INFLUENCE_LIST",
    "SPAWNABLE_ITEM_MOD_DOMAINS",
    "SPAWNABLE_ITEM_MOD_GENERATION_TYPES",
    "IMPLICIT_GENERATION_TYPES",
]

MOD_MAX_STATS = 6
MOD_STATS_RANGE = range(1, MOD_MAX_STATS + 1)

BLACKLISTED_ITEMS = ["Energy Blade"]

INFLUENCE_LIST = ["shaper", "elder", "crusader", "basilisk", "eyrie", "adjudicator"]

SPAWNABLE_ITEM_MOD_DOMAINS = ["item", "crafted"]

SPAWNABLE_ITEM_MOD_GENERATION_TYPES = [
    "prefix",
    "suffix",
    "corrupted",
    "enchantment",
    "archnemesis",
    "searing_exarch_implicit",
]
IMPLICIT_GENERATION_TYPES = [
    "corrupted",
    "enchantment",
    "archnemesis",
    "searing_exarch_implicit",
]

INFLUENCE_TAGS = {
    "Amulets": "amulet_{influence}",
    "Belts": "belt_{influence}",
    "Body Armour(dex/int)": "body_armour_{influence}",
    "Body Armour(dex)": "body_armour_{influence}",
    "Body Armour(int)": "body_armour_{influence}",
    "Body Armour(str/dex/int)": "body_armour_{influence}",
    "Body Armour(str/dex)": "body_armour_{influence}",
    "Body Armour(str/int)": "body_armour_{influence}",
    "Body Armour(str)": "body_armour_{influence}",
    "Boots(dex/int)": "boots_{influence}",
    "Boots(dex)": "boots_{influence}",
    "Boots(int)": "boots_{influence}",
    "Boots(str/dex)": "boots_{influence}",
    "Boots(str/int)": "boots_{influence}",
    "Boots(str)": "boots_{influence}",
    "Bows": "bow_{influence}",
    "Claws": "claw_{influence}",
    "Daggers": "dagger_{influence}",
    "Gloves(dex/int)": "gloves_{influence}",
    "Gloves(dex)": "gloves_{influence}",
    "Gloves(int)": "gloves_{influence}",
    "Gloves(str/dex)": "gloves_{influence}",
    "Gloves(str/int)": "gloves_{influence}",
    "Gloves(str)": "gloves_{influence}",
    "Helmet(dex/int)": "helmet_{influence}",
    "Helmet(dex)": "helmet_{influence}",
    "Helmet(int)": "helmet_{influence}",
    "Helmet(str/dex)": "helmet_{influence}",
    "Helmet(str/int)": "helmet_{influence}",
    "Helmet(str)": "helmet_{influence}",
    "One Hand Axes": "axe_{influence}",
    "One Hand Maces": "mace_{influence}",
    "One Hand Swords": "sword_{influence}",
    "Quivers": "quiver_{influence}",
    "Rings": "ring_{influence}",
    "Rune Daggers": "rune_dagger_{influence}",
    "Sceptres": "sceptre_{influence}",
    "Shields(dex/int)": "shield_{influence}",
    "Shields(dex)": "shield_{influence}",
    "Shields(int)": "shield_{influence}",
    "Shields(str/dex)": "shield_{influence}",
    "Shields(str/int)": "shield_{influence}",
    "Shields(str)": "shield_{influence}",
    "Staves": "staff_{influence}",
    "Two Hand Axes": "2h_axe_{influence}",
    "Two Hand Maces": "2h_mace_{influence}",
    "Two Hand Swords": "2h_sword_{influence}",
    "Wands": "wand_{influence}",
    "Warstaves": "warstaff_{influence}",
}

ITEM_CLASS_SUFFIXES = {
    "Body Armour": [
        " (dex)",
        " (dex/int)",
        " (int)",
        " (str)",
        " (str/dex)",
        " (str/dex/int)",
        " (str/int)",
    ],
    "Helmet": [
        " (dex)",
        " (dex/int)",
        " (int)",
        " (str)",
        " (str/dex)",
        " (str/dex/int)",
        " (str/int)",
        " (ward)",
    ],
    "Gloves": [
        " (dex)",
        " (dex/int)",
        " (int)",
        " (str)",
        " (str/dex)",
        " (str/dex/int)",
        " (str/int)",
        " (ward)",
    ],
    "Boots": [
        " (dex)",
        " (dex/int)",
        " (int)",
        " (str)",
        " (str/dex)",
        " (str/dex/int)",
        " (str/int)",
        " (ward)",
    ],
    "Shield": [
        " (dex)",
        " (dex/int)",
        " (int)",
        " (str)",
        " (str/dex)",
        " (str/dex/int)",
        " (str/int)",
    ],
}

item_types = [
    "Armour",
    "Jewellery",
    "One Handed Melee",
    "Two Handed Melee",
    "Amulet",
    "Belt",
    "Body Armour",
    "Boots",
    "Bow",
    "Claw",
    "Dagger",
    "Fishing Rod",
    "Flask",
    "Gloves",
    "Helmet",
    "Jewel",
    "One Handed Axe",
    "One Handed Mace",
    "One Handed Sword",
    "Quiver",
    "Ring",
    "Sceptre",
    "Shield",
    "Staff",
    "Two Handed Axe",
    "Two Handed Mace",
    "Two Handed Sword",
    "Wand",
]

one_hand_weapon_types = {
    "Claw",
    "Dagger",
    "Rune Dagger",
    "Wand",
    "One Hand Sword",
    "Thrusting One Hand Sword",
    "One Hand Axe",
    "One Hand Mace",
    "Sceptre",
}

two_hand_weapon_types = {
    "Bow",
    "Staff",
    "Warstaff",
    "Two Hand Sword",
    "Two Hand Axe",
    "Two Hand Mace",
}

offhand_types = {"Quiver"}

armour_types = {
    "Gloves",
    "Boots",
    "Body Armour",
    "Helmet",
    "Shield",
}

jewellery_types = {"Amulet": "amulet", "Ring": "ring", "Belt": "belt"}

flask_types = {
    "LifeFlask": "life_flask",
    "ManaFlask": "mana_flask",
    "HybridFlask": "hybrid_flask",
    "UtilityFlask": "utility_flask",
    "UtilityFlaskCritical": "utility_flask_critical",
}

jewel_types = {"Jewel", "AbyssJewel", ""}

item_class_whitelist = {
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
    "FishingRod",
    "Jewel",
    "AbyssJewel",
}

item_class_blacklist = {
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
}

domain_whitelist = [
    "item",
    "flask",
    "crafted",
    "jewel",
    "abyss_jewel",
    "delve_fossil",
    "synthesis",
    "affliction_jewel",
    "heist_gear",
    "trinket",
    "unveiled_modifier",
    "misc",
]

generation_type_whitelist = [
    "prefix",
    "suffix",
    "corrupted",
    "enchantment",
    "essence",
    "bestiary",
    "synthesis",
    "exarch_implicit",
    "eater_implicit",
    "flask_enchantment_instilling",
    "flask_enchantment_enkindling",
]

generation_type_blacklist = [
    "nemesis",
    "bloodlines",
    "torment",
    "tempest",
    "talisman",
    "blight_tower",
    "delve_area",
    "scourge_detriment",
    "scourge_gimmick",
    "scourge_benefit",
    "synthesis_globals",
    "monster_affliction",
    "archnemesis",
]

armour_subtypes = {
    "Body Armour": {
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_dex_int_armour",
        "str_int_armour",
    },
    "Boots": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Gloves": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Helmet": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Shield": {
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
}

item_class_map = {
    "Body Armour": {
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_dex_int_armour",
        "str_int_armour",
    },
    "Boots": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Gloves": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Helmet": {
        "ward_armour",
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Shield": {
        "dex_armour",
        "dex_int_armour",
        "int_armour",
        "str_armour",
        "str_dex_armour",
        "str_int_armour",
    },
    "Amulet": {"amulet"},
    "Belt": {"belt"},
    "Ring": {"ring"},
    "One Handed Weapons": {
        "claw",
        "attack_dagger",
        "dagger",
        "axe",
        "mace",
        "sword",
        "sceptre",
        "rapier",
        "wand",
    },
    "Two Handed Weapons": {
        "bow",
        "staff",
        "two_hand_axe",
        "two_hand_sword",
        "warstaff",
        "two_hand_mace",
    },
    "Offhand": {"quiver", "shield"},
    "Jewel": {"abyss_jewel", "jewel"},
    "HybridFlask": {"hybrid_flask"},
    "LifeFlask": {"life_flask"},
    "ManaFlask": {"mana_flask"},
    "UtilityFlask": {"utility_flask"},
    "UtilityFlaskCritical": {"utility_flask_critical"},
}

subtype_display_names = {
    "abyss_jewel": "AbyssJewel",
    "jewel": "Jewel",
    "focus_can_roll_minion_modifiers": "Bone Spirit Shield",
    "claw": "Claw",
    "weapon_can_roll_minion_modifiers": "Convoking Wand",
    "attack_dagger": "Dagger",
    "dagger": "Rune Dagger",
    "axe": "One Hand Axe",
    "mace": "One Hand Mace",
    "sword": "One Hand Sword",
    "sceptre": "Sceptre",
    "rapier": "Thrusting One Hand Sword",
    "wand": "Wand",
    "armour": "{}",
    "bow": "Bow",
    "staff": "Staff",
    "warstaff": "Warstaff",
    "two_hand_axe": "Two Hand Axe",
    "two_hand_sword": "Two Hand Sword",
    "two_hand_mace": "Two Hand Mace",
    "ward_armour": "{}(Ward)",
    "dex_armour": "{}(dex)",
    "dex_int_armour": "{}(dex/int)",
    "int_armour": "{}(int)",
    "str_armour": "{}(str)",
    "str_dex_armour": "{}(str/dex)",
    "str_dex_int_armour": "{}(str/dex/int)",
    "str_int_armour": "{}(str/int)",
    "amulet": "Amulet",
    "life_flask": "LifeFlask",
    "mana_flask": "ManaFlask",
    "hybrid_flask": "HybridFlask",
    "utility_flask": "UtilityFlask",
    "critical_utility_flask": "Utility Flask Critical",
    "ring": "Ring",
    "belt": "Belt",
    "abyss_jewel_ranged": "Searching Eye Jewel",
    "abyss_jewel_caster": "Hypnotic Eye Jewel",
    "abyss_jewel_summoner": "Ghastly Eye Jewel",
    "abyss_jewel_melee": "Murderous Eye Jewel",
    "dexjewel": "Viridian Jewel",
    "intjewel": "Cobalt Jewel",
    "strjewel": "Crimson Jewel",
    "shield": "Shield",
    "quiver": "Quiver",
    "expansion_jewel_small": "Small Cluster Jewel",
    "expansion_jewel_medium": "Medium Cluster Jewel",
    "expansion_jewel_large": "Large Cluster Jewel",
    "helmet": "Helmet",
}

reversed_class_names = {
    v.format(k) if "{}" in v else v: k for k, v in subtype_display_names.items()
}

all_subtypes = {
    "armour",
    "dex_armour",
    "dex_int_armour",
    "int_armour",
    "str_armour",
    "str_dex_armour",
    "str_dex_int_armour",
    "str_int_armour",
}

subtype_tags_map = {
    "dex": "dex_armour",
    "dex/int": "dex_int_armour",
    "int": "int_armour",
    "str": "str_armour",
    "str/dex": "str_dex_armour",
    "str/dex/int": "str_dex_int_armour",
    "str/int": "str_int_armour",
    "ward": "ward_armour",
}

ITEM_PROPERTIES = [
    # ("Quality", "quality", "#8787fe"),
    ("Block", "block", "#fff"),
    ("Armour", "average_armour", "#8787fe"),
    ("Energy Shield", "average_energy_shield", "#8787fe"),
    ("Evasion", "average_evasion", "#8787fe"),
    ("Ward", "average_ward", "#8787fe"),
    ("Physical Damage", ("physical_damage_min", "physical_damage_max"), "#8787fe"),
    ("Elemental Damage", ("elemental_damage_min", "elemental_damage_max"), "#8787fe"),
    ("Chaos Damage", ("chaos_damage_min", "chaos_damage_max"), "#8787fe"),
    ("Critical Strike Chance", "critical_strike_chance", "#fff"),
    ("Attacks Per Second", "attack_time", "#fff"),
]

ITEM_PROPERTIES_MAP = {
    "Armour": {
        "armour_min": "min",
        "armour_max": "max",
        "evasion_min": "min",
        "evasion_max": "max",
        "energy_shield_min": "min",
        "energy_shield_max": "max",
        "ward_min": "min",
        "ward_max": "max",
        "block": "block",
        "movement_penalty": "movement_speed",
    },
    "One Hand Weapon": {
        "attack_time": "attack_time",
        "critical_strike_chance": "critical_strike_chance",
        "physical_damage_min": "physical_damage_min",
        "physical_damage_max": "physical_damage_max",
        "range": "range",
    },
    "Two Hand Weapon": {
        "attack_time": "attack_time",
        "critical_strike_chance": "critical_strike_chance",
        "physical_damage_min": "physical_damage_min",
        "physical_damage_max": "physical_damage_max",
        "range": "range",
    },
    "Flask": {
        "buff_id": "id",
        "buff_stat": "stat",
        "implicits": "implicits",
        "charges_max": "charges_max",
        "charges_per_use": "charges_per_use",
        "duration": "duration",
        "life_per_use": "life_per_use",
        "mana_per_use": "mana_per_use",
    },
}
ITEM_REQUIREMENTS = [
    ("Requires Level", "level", "#fff"),
    ("STR", "strength", "#fff"),
    ("DEX", "dexterity", "#fff"),
    ("INT", "intelligence", "#fff"),
]


class IntEnumMetaOverride(EnumMeta):
    def __getitem__(self, item):
        if isinstance(item, int):
            return self(item)
        else:
            return IntEnum.__getitem__(self, item)


class IntEnumOverride(IntEnum, metaclass=IntEnumMetaOverride):
    pass


class STAT_INTERPOLATION_TYPES(IntEnumOverride):
    """
    Representation of stat interpolation types (StatInterpolationTypes.dat)

    Primarily used by GrantedEffects.dat

    Attributes
    ----------
    CONSTANT
        Constant scaling
    LINEAR
        Linear scaling
    EXPONENTIAL
        Exponential scaling

        .. code-block:: none

            skill_base =
                (
                    GameConstants -> SkillDamageBaseEffectiveness +
                    (GameConstants -> SkillDamageIncrementalEffectiveness * (
                        MonsterLevel - 1
                    ))
                ) *
                GrantedEffects['BaseEffectiveness'] *
                (1+GrantedEffects['IncrementalEffectiveness') ** (MonsterLevel - 1)

    """

    CONSTANT = 1
    LINEAR = 2
    EXPONENTIAL = 3


class RARITY(Enum, metaclass=IntEnumMetaOverride):
    """
    Representation of the possible rarities for items and monsters.

    Attributes
    ----------
    NORMAL : RARITY
        Normal rarity ("white" colour)
    MAGIC : RARITY
        Magic rarity ("blue" colour)
    RARE : RARITY
        Rare rarity ("yellow" colour)
    UNIQUE : RARITY
        Unique rarity ("brown" colour)
    ANY : RARITY
        Any rarity
    id : int
        When accessing a :class:`RARITY` instance (e.x. :attr:`RARITY.NORMAL`)
        the id attribute denotes the integer that is sometimes used in the game
        files to represent the colour
    name_upper : str
        When accessing a :class:`RARITY` instance (e.x. :attr:`RARITY.NORMAL`)
        the upper attribute represents the textual representation with an upper
        case starting letter
    name_lower : str
        When accessing a :class:`RARITY` instance (e.x. :attr:`RARITY.NORMAL`)
        the lower attribute represents the textual representation with a lower
        case starting letter
    colour : str
        When accessing a :class:`RARITY` instance (e.x. :attr:`RARITY.NORMAL`)
        the colour attribute represents the textual representation of the
        associated colour
    """

    NORMAL = (1, "Normal", "normal", "white")
    MAGIC = (2, "Magic", "magic", "blue")
    RARE = (3, "Rare", "rare", "yellow")
    UNIQUE = (4, "Unique", "unique", "brown")
    ANY = (5, "Any", "any", "any")

    def __new__(cls, _id, upper, lower, colour):
        obj = object.__new__(cls)
        obj._value_ = _id
        obj.id = _id
        obj.name_upper = upper
        obj.name_lower = lower
        obj.colour = colour
        return obj
