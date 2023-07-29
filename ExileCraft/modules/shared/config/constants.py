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

from enum import auto, Enum, EnumMeta, IntEnum

__all__ = [
    "MOD_DOMAIN",
    "MOD_GENERATION_TYPE",
    "item_class_whitelist",
    "item_class_map",
    "subtype_display_names",
    "domain_whitelist",
    "RARITY",
    "SOCKET_COLOUR",
    "STAT_INTERPOLATION_TYPES",
    "WORD_LISTS",
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
]

MOD_MAX_STATS = 6
MOD_STATS_RANGE = range(1, MOD_MAX_STATS + 1)

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

jewel_subtypes = {"Jewel": {}}
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
    "(dex)": "dex_armour",
    "(dex/int)": "dex_int_armour",
    "(int)": "int_armour",
    "(str)": "str_armour",
    "(str/dex)": "str_dex_armour",
    "(str/dex/int)": "str_dex_int_armour",
    "(str/int)": "str_int_armour",
    "(Ward)": "ward_armour",
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


class MOD_DOMAIN(str, Enum):
    """
    Representation of mod domains.

    This constant is primarily used in relation to mods.min.json.

    Attributes
    ----------
    ITEM
        Generic item domain (but excluding items that have their own domain)
    FLASK
        Flask domain
    MONSTER
        Monster domain
    CHEST
        Chest domain, i.e. strongboxes or other type of chest-like
        containers
    AREA
        Area domain, i.e. for the various zones of Path of Exile
    UNKNOWN1
    UNKNOWN2
    UNKNOWN3
    MASTER
        See CRAFTED
    CRAFTED
        Domain for crafted mods (previously MASTER)
    MISC
        Miscellaneous domain for jewel stuff, item limits, corruptions, etc
    ATLAS
        Atlas domain for modifiers that appear when using a sextant orb on the
        atlas
    LEAGUESTONE
        Leaguestone domain for modifiers that appear on league stones
    ABYSS_JEWEL
        Domain for modifiers that appear on Abyss jewels
    MAP_DEVICE
        For implicit modifiers that can be applied through the map device
        For example, vaal fragments or soul flasks
    DELVE
        For delve modifiers
    DELVE_AREA
        For modifiers appearing on delve areas
    SYNTHESIS_GLOBALS
        Synthesis global modifiers for areas
    SYNTHESIS_BONUS
        Synthesis modifiers that grant a bonus to other modifiers
    AFFLICTION_JEWEL
        Modifiers for the affliction jewels
    HEIST_AREA
    HEIST_NPC
    HEIST_TRINKET
    UNKNOWN4
    UNDEFINED
    """

    ITEM = (
        "item"  # Generic item domain (but excluding items that have their own domain)
    )
    FLASK = "flask"  # Flask domain
    MONSTER = "monster"  # Monster domain
    CHEST = (
        "chest"  # Chest domain, i.e. strongboxes or other type of chest-like containers
    )
    AREA = "area"  # Area domain, i.e. for the various zones of Path of Exile
    UNKNOWN = "unknown1"
    UNKNOWN2 = "unknown2"
    UNKNOWN3 = "unknown3"
    CRAFTED = "crafted"  # Domain for crafted mods (previously MASTER)
    MISC = "misc"  # Miscellaneous domain for jewel stuff, item limits, corruptions, etc
    ATLAS = (
        "atlas"  # Atlas domain for modifiers that appear when using a sextant orb on
    )
    # the atlas
    LEAGUESTONE = "leaguestone"  # Leaguestone domain for modifiers that appear on
    # league stones
    ABYSS_JEWEL = "abyss_jewel"  # Domain for modifiers that appear on Abyss jewels
    MAP_DEVICE = "map_device"  # For implicit modifiers that can be applied through the
    # map
    # device
    DELVE = "delve"  # For delve modifiers
    DELVE_AREA = "delve_area"  # For modifiers appearing on delve areas
    SYNTHESIS_GLOBALS = "synthesis_globals"  # Synthesis global modifiers for areas
    SYNTHESIS_BONUS = (
        "synthesis_bonus"  # Synthesis modifiers that grant a bonus to other modifiers
    )
    AFFLICTION_JEWEL = "affliction_jewel"  # Modifiers for the affliction jewels
    HEIST_AREA = "heist_area"
    HEIST_NPC = "heist_npc"
    HEIST_TRINKET = "heist_trinket"
    UNKNOWN4 = "unknown4"
    UNDEFINED = "undefined"

    # Legacy Names
    MASTER = CRAFTED  # See CRAFTED
    JEWEL = MISC  # See MISC


class MOD_GENERATION_TYPE(Enum):
    """
    Representation of mod generation types.

    This constant is primarily used in relation to the Mods class.

    Attributes
    ----------
    PREFIX
        Prefix generation type
    SUFFIX
        Suffix generation type
    UNIQUE
        Whether the mod is directly given to an entity and not generanted by
        normal means.
        Commonly this can be found on unique monsters/items for example, but
        also as innate/implicit modifiers for example
    NEMESIS
        For 'nemesis' mods that can appear on monsters
    CORRUPTED
        For mods that are generated though item corruption
    BLOODLINES
        For 'bloodlines' mods that can appear on monsters
    TORMENT
        For 'torment' mods that can appear on monsters
    TEMPEST
        For 'tempest' mods that can appear on areas
    TALISMAN
        For 'talisman' mods that can appear on monsters
    ENCHANTMENT
        For the ascendancy/labyrinth enchantment mods that can appear on items
    ESSENCE
        For 'essence' mods that can appear on monsters
    BESTIARY
        For 'bestiary' modifiers that appear on bestiary monsters
    DELVE_AREA
        For modifiers that appear on delve areas
    SYNTHESIS_A
    SYNTHESIS_GLOBALS
    SYNTHESIS_BONUS
    BLIGHT
    MONSTER_AFFLICTION
    """

    PREFIX: str = "prefix"
    SUFFIX: str = "suffix"
    UNIQUE: str = "unique"
    NEMESIS: str = "nemesis"
    CORRUPTED: str = "corrupted"
    BLOODLINES: str = "bloodlines"
    TORMENT: str = "torment"
    TEMPEST: str = "tempest"
    TALISMAN: str = "talisman"
    ENCHANTMENT: str = "enchantment"
    ESSENCE: str = "essence"
    BESTIARY: str = "bestiary"
    DELVE_AREA: str = "delve_area"
    SYNTHESIS_A: str = "synthesis_a"
    SYNTHESIS_GLOBALS: str = "synthesis_globals"
    SYNTHESIS_BONUS: str = "synthesis_bonus"
    BLIGHT: str = "blight"
    BLIGHT_TOWER: str = "blight_tower"
    MONSTER_AFFLICTION: str = "monster_affliction"
    ARCHNEMESIS: str = "archnemesis"
    SEARING_EXARCH_IMPLICIT: str = "searing_exarch_implicit"


class WORD_LISTS(IntEnumOverride):
    """
    Representation of words lists ( Wordlists.dat )

    This constant is primarily used in relation to Words.dat

    Attributes
    ----------
    ITEM_PREFIX
        Prefix word of a randomly generated item name
    ITEM_SUFFIX
        Suffix word of a randomly generated item name; separate from the prefix
    MONSTER_PREFIX
        Prefix word of a randomly generated monster name.
    MONSTER_SUFFIX
        Suffix word of a randomly generated monster name; composite with the
        prefix
    MONSTER_TITLE
        Title ("the xxx") of a randomly generated monster name
    UNIQUE_ITEM
        Name of a unique item
    STRONGBOX_PREFIX
        Prefix word of a randomly generated strongbox name
    STRONGBOX_SUFFIX
        Suffix word of a randomly generated strongbox name; separate from the
        prefix
    ESSENCE
        Name of an essence
    """

    ITEM_PREFIX = 1
    ITEM_SUFFIX = 2
    MONSTER_PREFIX = 3
    MONSTER_SUFFIX = 4
    MONSTER_TITLE = 5
    UNIQUE_ITEM = 6
    STRONGBOX_PREFIX = 7
    STRONGBOX_SUFFIX = 8
    ESSENCE = 9


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


class SOCKET_COLOUR(Enum):
    """
    Representation of item socket colours.

    In some places in the game files these colours are referenced either by
    their id or by a character, so make sure to check which and use the
    according attribute.

    Attributes
    ----------
    RED : SocketColour
        Red sockets usually associated with Strength
    GREEN : SocketColour
        Green sockets usually associated with Dexterity
    BLUE : SocketColour
        Blue sockets usually associated with Intelligence
    WHITE : SocketColour
        White sockets
    char : str
        When accessing a :class:`SOCKET_COLOUR` instance (i.e.
        :attr:`SOCKET_COLOUR.BLUE`) the char attribute denotes the character
        that is sometimes used in the game files to represent the colour
    id : int
        When accessing a :class:`SOCKET_COLOUR` instance (i.e.
        :attr:`SOCKET_COLOUR.BLUE`) the id attribute denotes the integer
        that is sometimes used in the game files to represent the colour
    """

    # IDs are from CharacterStarItems.dat->Sockets and game testing
    R = ("R", 1)
    G = ("G", 2)
    B = ("B", 3)
    # I can't actually confirm this id=4, but seems logical
    W = ("W", 4)
    RED = R
    GREEN = G
    BLUE = B
    WHITE = W

    def __new__(cls, char, id):
        obj = object.__new__(cls)
        obj._value_ = char
        obj.char = char
        obj.id = id

        return obj


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


class ITEM_TYPES(Enum):
    ITEM = auto()
    GEM = auto()
    CURRENCY = auto()


class Influence(Enum):
    SHAPER = 1
    ELDER = 2
    CRUSADER = 3
    HUNTER = 4
    REDEEMER = 5
    WARLORD = 6
    NONE = 7
