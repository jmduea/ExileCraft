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


import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple, Union

item_text = """
Item Class: Bows
Rarity: Rare
Honour Wing
Decimation Bow
--------
Bow
Physical Damage: 56-148 (augmented)
Elemental Damage: 74-132 (augmented), 127-221 (augmented)
Critical Strike Chance: 8.40% (augmented)
Attacks per Second: 1.20
--------
Requirements:
Level: 68
Dex: 170
--------
Sockets: G G G 
--------
Item Level: 86
--------
{ Implicit Modifier — Attack, Critical }
30(30-50)% increased Critical Strike Chance (implicit)
--------
{ Prefix Modifier "Reaver's" (Tier: 6) — Damage, Physical, Attack }
28(25-34)% increased Physical Damage
+61(47-72) to Accuracy Rating
{ Prefix Modifier "Scorching" (Tier: 5) — Damage, Elemental, Fire, Attack }
Adds 74(63-85) to 132(128-148) Fire Damage
{ Prefix Modifier "Polar" (Tier: 3) — Damage, Elemental, Cold, Attack }
Adds 127(99-136) to 221(200-232) Cold Damage
{ Suffix Modifier "of Incision" (Tier: 1) — Attack, Critical }
38(35-38)% increased Critical Strike Chance
{ Suffix Modifier "of Haast" (Tier: 1) — Elemental, Cold, Resistance }
+46(46-48)% to Cold Resistance
{ Suffix Modifier "of Lioneye" (Tier: 1) — Attack }
+756(625-780) to Accuracy Rating
"""

LOCALIZED_PAREN_LEFT = re.compile(r"^\s*(?:\(|（)")
LOCALIZED_PAREN_RIGHT = re.compile(r"(?:\)|）)\s*$")

PLACEHOLDER_MAP = [
    [[]],
    [[0], []],
    [[0, 1], [0], [1], []],
    [[0, 1, 2], [1, 2], [0, 2], [0, 1], [2], [1], [0]],
    [
        [0, 1, 2, 3],
        [1, 2, 3],
        [0, 2, 3],
        [0, 1, 3],
        [0, 1, 2],
        [2, 3],
        [1, 3],
        [1, 2],
        [0, 3],
        [0, 2],
        [0, 1],
    ],
]


class ITEM_TYPES(Enum):
    """
    Enum class representing different types of items.

    Attributes:
        ITEM: Represents a generic item.
        GEM: Represents a gem item.
        CURRENCY: Represents a currency item.

    """

    ITEM = 0
    GEM = 1
    CURRENCY = 2


class ItemRarity(Enum):
    """
    Represents the rarity of an item.

    The ItemRarity class is an enumeration that defines the possible rarities for an item.

    Attributes:
        Normal (str): The normal rarity.
        Magic (str): The magic rarity.
        Rare (str): The rare rarity.
        Unique (str): The unique rarity.
    """

    Normal = "Normal"
    Magic = "Magic"
    Rare = "Rare"
    Unique = "Unique"


class ModifierType(Enum):
    """

    The `ModifierType` class is an enumeration that represents the different types of modifiers in a system. It provides a set of predefined values that can be used to identify a modifier type.

    Attributes:
        - `Pseudo`: Represents a pseudo modifier type.
        - `Explicit`: Represents an explicit modifier type.
        - `Implicit`: Represents an implicit modifier type.
        - `Crafted`: Represents a crafted modifier type.
        - `Enchant`: Represents an enchant modifier type.
        - `Scourge`: Represents a scourge modifier type.
        - `Veiled`: Represents a veiled modifier type.
        - `Fractured`: Represents a fractured modifier type.

    Usage:
        The `ModifierType` enumeration can be used to categorize and differentiate between different types of modifiers. It provides a convenient and readable way to identify the type of a modifier.

    Example:
        - Checking if a modifier is of type `Explicit`:
            ```
            if modifier_type == ModifierType.Explicit:
                # Do something
            ```

        - Converting a string to a `ModifierType` value:
            ```
            type_str = "crafted"
            modifier_type = ModifierType[type_str.capitalize()]
            ```

        - Getting all the possible modifier types:
            ```
            all_types = [modifier_type for modifier_type in ModifierType]
            ```

        - Comparing two modifier types:
            ```
            type1 = ModifierType.Pseudo
            type2 = ModifierType.Implicit
            if type1 == type2:
                # Do something
            ```

        - Mapping a modifier type to a color:
            ```
            type_color_map = {
                ModifierType.Pseudo: "blue",
                ModifierType.Explicit: "red",
                ModifierType.Implicit: "green",
                # ...
            }
            ```

        - Storing a modifier type in a variable:
            ```
            modifier_type = ModifierType.Pseudo
            ```

    Notes:
        - The modifier types should be used consistently throughout the system to ensure clarity and maintainability.
        - The `ModifierType` enumeration is defined using the `Enum` class from the `enum` module.
        - The string representation of each modifier type is defined as a class attribute, e.g., `ModifierType.Pseudo.value` will return 'pseudo'.
        - The modifier types can be accessed using dot notation, e.g., `ModifierType.Explicit`.
        - The `ModifierType` enumeration is immutable and cannot be modified once defined.

    """

    Pseudo = "pseudo"
    Explicit = "explicit"
    Implicit = "implicit"
    Crafted = "crafted"
    Enchant = "enchant"
    Scourge = "scourge"
    Veiled = "veiled"
    Fractured = "fractured"


class ItemInfluence(Enum):
    """
    Represents the possible influences an item can have in the game.

    Attributes:
        Crusader (str): The Crusader influence.
        Elder (str): The Elder influence.
        Hunter (str): The Hunter influence.
        Redeemer (str): The Redeemer influence.
        Shaper (str): The Shaper influence.
        Warlord (str): The Warlord influence.
    """

    Crusader = "Crusader"
    Elder = "Elder"
    Hunter = "Hunter"
    Redeemer = "Redeemer"
    Shaper = "Shaper"
    Warlord = "Warlord"


class ItemCategory(Enum):
    """A class representing the different categories of items in a game.

    Attributes:
        Map (str): The category for maps.
        CapturedBeast (str): The category for captured beasts.
        MetamorphSample (str): The category for metamorph samples.
        Helmet (str): The category for helmets.
        BodyArmour (str): The category for body armours.
        Gloves (str): The category for gloves.
        Boots (str): The category for boots.
        Shield (str): The category for shields.
        Amulet (str): The category for amulets.
        Belt (str): The category for belts.
        Ring (str): The category for rings.
        Flask (str): The category for flasks.
        AbyssJewel (str): The category for abyss jewels.
        Jewel (str): The category for jewels.
        Quiver (str): The category for quivers.
        Claw (str): The category for claws.
        Bow (str): The category for bows.
        Sceptre (str): The category for sceptres.
        Wand (str): The category for wands.
        FishingRod (str): The category for fishing rods.
        Staff (str): The category for staffs.
        Warstaff (str): The category for warstaffs.
        Dagger (str): The category for daggers.
        RuneDagger (str): The category for rune daggers.
        OneHandedAxe (str): The category for one-handed axes.
        TwoHandedAxe (str): The category for two-handed axes.
        OneHandedMace (str): The category for one-handed maces.
        TwoHandedMace (str): The category for two-handed maces.
        OneHandedSword (str): The category for one-handed swords.
        TwoHandedSword (str):"""

    Map = "Map"
    CapturedBeast = "Captured Beast"
    MetamorphSample = "Metamorph Sample"
    Helmet = "Helmet"
    BodyArmour = "Body Armour"
    Gloves = "Gloves"
    Boots = "Boots"
    Shield = "Shield"
    Amulet = "Amulet"
    Belt = "Belt"
    Ring = "Ring"
    Flask = "Flask"
    AbyssJewel = "Abyss Jewel"
    Jewel = "Jewel"
    Quiver = "Quiver"
    Claw = "Claw"
    Bow = "Bow"
    Sceptre = "Sceptre"
    Wand = "Wand"
    FishingRod = "Fishing Rod"
    Staff = "Staff"
    Warstaff = "Warstaff"
    Dagger = "Dagger"
    RuneDagger = "Rune Dagger"
    OneHandedAxe = "One Hand Axe"
    TwoHandedAxe = "Two Hand Axe"
    OneHandedMace = "One Hand Mace"
    TwoHandedMace = "Two Hand Mace"
    OneHandedSword = "One Hand Sword"
    TwoHandedSword = "Two Hand Sword"
    ClusterJewel = "Cluster Jewel"
    HeistBlueprint = "Heist Blueprint"
    HeistContract = "Heist Contract"
    HeistTool = "Heist Tool"
    HeistBrooch = "Heist Brooch"
    HeistGear = "Heist Gear"
    HeistCloak = "Heist Cloak"
    Trinket = "Trinket"
    Invitation = "Invitation"
    Gem = "Gem"
    Currency = "Currency"
    DivinationCard = "Divination Card"
    Voidstone = "Voidstone"
    Sentinel = "Sentinel"
    MemoryLine = "Memory Line"


class StatBetter(Enum):
    """
    A class representing statistical improvements.

    Attributes:
        NegativeRoll: An enum member representing a negative statistical improvement.
        PositiveRoll: An enum member representing a positive statistical improvement.
        NotComparable: An enum member representing an inability to compare statistical improvements.

    """

    NegativeRoll = -1
    PositiveRoll = 1
    NotComparable = 0


@dataclass
class StatMatcher:
    """
    This class allows matching of a string representation of a statistic with additional criteria.

    Attributes:
        string (str): The string representation of the statistic.
        advanced (str, optional): Additional criteria to consider.
        negate (bool, optional): Flag indicating whether to negate the match.
        value (int, optional): The desired value for the statistic.
        oils (str, optional): The oils associated with the statistic.
    """

    string: str
    advanced: Optional[str] = None
    negate: Optional[bool] = None
    value: Optional[int] = None
    oils: Optional[str] = None


@dataclass
class StatRoll:
    """Generate random values within a specified range.

    Attributes:
        value (int): The current value of the StatRoll.
        min (int): The minimum possible value of the StatRoll.
        max (int): The maximum possible value of the StatRoll.

    Methods:
        generate_value: Generate a random value within the specified range.

    Example Usage:
        stat = StatRoll(5, 1, 10)
        stat.generate_value()
    """

    value: int
    min: int
    max: int


@dataclass
class TradeInfo:
    """
    Class to store trade information.

    Args:
        inverted (Optional[bool]): Indicates if the trade is inverted. Default is None.
        option (Optional[bool]): Indicates if the trade is an option. Default is None.
        ids (Dict[str, List[str]]): Dictionary mapping trade identifiers to lists of strings. Default is an empty dictionary.
    """

    inverted: Optional[bool] = None
    option: Optional[bool] = None
    ids: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class Anointment:
    """Represents an anointment with a roll and associated oils.

    Args:
        roll (int): The roll number of the anointment.
        oils (str): The oils used in the anointment.

    Attributes:
        roll (int): The roll number of the anointment.
        oils (str): The oils used in the anointment.

    """

    roll: int
    oils: str


@dataclass
class Stat:
    """

    The Stat class represents a stat in a game, with various attributes and methods for comparison and manipulation.

    Attributes:
        ref (str): The reference of the stat.
        trade (TradeInfo): Information about the stat for trading purposes.
        better (StatBetter): The comparison type of the stat. Defaults to StatBetter.NotComparable.
        dp (Optional[bool]): The flag indicating if the stat is a damage per second stat. Defaults to None.
        matchers (List[StatMatcher]): A list of matchers associated with the stat. Defaults to an empty list.
        from_area_mods (Optional[bool]): The flag indicating if the stat is derived from area modifiers. Defaults to None.
        from_heist_area_mods (Optional[bool]): The flag indicating if the stat is derived from heist area modifiers. Defaults to None.
        anointments (Optional[List[Anointment]]): A list of anointments associated with the stat. Defaults to None.

    """

    ref: str
    trade: TradeInfo  # Moved up
    better: StatBetter = StatBetter.NotComparable
    dp: Optional[bool] = None
    matchers: List[StatMatcher] = field(default_factory=list)
    from_area_mods: Optional[bool] = None
    from_heist_area_mods: Optional[bool] = None
    anointments: Optional[List[Anointment]] = None


@dataclass
class ModifierInfo:
    """

    This class represents information about a modifier in a game.

    Attributes:
        type (ModifierType): The type of the modifier.
        generation (Optional[Union["suffix", "prefix", "corrupted", "eldritch"]]): The generation type of the modifier. Can be one of the following:
            - "suffix": Indicates that the modifier is a suffix.
            - "prefix": Indicates that the modifier is a prefix.
            - "corrupted": Indicates that the modifier is corrupted.
            - "eldritch": Indicates that the modifier is eldritch.
        name (Optional[str]): The name of the modifier.
        tier (Optional[int]): The tier of the modifier.
        rank (Optional[int]): The rank of the modifier.
        tags (List[str]): A list of tags associated with the modifier.
        roll_incr (Optional[int]): The roll increment of the modifier.

    """

    type: ModifierType
    generation: Optional[Union["suffix", "prefix", "corrupted", "eldritch"]] = None
    name: Optional[str] = None
    tier: Optional[int] = None
    rank: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    roll_incr: Optional[int] = None


@dataclass
class RollInfo:
    """
    Information about a roll.

    Attributes
    ----------
    unscalable : bool
        Indicates if the roll is unscalable.

    legacy : Optional[bool]
        Indicates if the roll is a legacy roll.

    dp : bool
        Indicates if the roll is a data point roll.

    value : float
        The value of the roll.

    min : float
        The minimum value allowed for the roll.

    max : float
        The maximum value allowed for the roll.
    """

    unscalable: bool
    legacy: Optional[bool]
    dp: bool
    value: float
    min: float
    max: float


@dataclass
class ParsedStat:
    """
    Class: ParsedStat

    Represents a parsed statistical information.

    Attributes:
    - stat: The statistical information of type Stat.
    - translation: The matched translation for the statistical information.
    - roll: The roll information of type RollInfo, or None if not present.

    """

    stat: Stat
    translation: StatMatcher
    roll: Optional[RollInfo] = None


@dataclass
class ParsedModifier:
    """
    ParsedModifier Class

    A class that represents a parsed modifier.

    Attributes:
        info (ModifierInfo): The information about the modifier.
        stats (List[ParsedStat]): The list of parsed statistics associated with the modifier.

    """

    info: ModifierInfo
    stats: List[ParsedStat]


class StatString:
    """
    A class for statistical analysis of strings.

    Attributes:
    - string: The input string for analysis.
    - unscalable: A boolean value indicating whether the string is unscalable.
    """

    string: str
    unscalable: bool


@dataclass
class StatSource:
    """

    Class: StatSource

    Represents a source of a statistical modifier for a specific stat.

    Attributes:
    - modifier (ParsedModifier): The modifier associated with the stat source.
    - stat (ParsedStat): The stat associated with the stat source.
    - contributes (Optional[StatRoll]): The stat roll that contributes to the stat source. Default is None.

    """

    modifier: ParsedModifier
    stat: ParsedStat
    contributes: Optional[StatRoll] = None


@dataclass
class StatCalculated:
    """
    Represents a calculated statistic.

    Attributes:
        stat (Stat): The base statistic.
        type (ModifierType): The type of modifier applied.
        sources (List[StatSource]): The sources contributing to the calculated statistic.

    """

    stat: Stat
    type: ModifierType
    sources: List[StatSource]


@dataclass
class Sockets:
    """
    A class representing sockets.

    Attributes:
        linked (int): The number of linked sockets.
        white (int): The number of white sockets.
        color_str (str): The color of the sockets.

    """

    linked: int
    white: int
    color_str: str


@dataclass
class StackSize:
    """Class representing the size of a stack.

    Attributes:
        value (int): The current size of the stack.
        max (int): The maximum allowed size of the stack.

    """

    value: int
    max: int


@dataclass
class UnknownModifier:
    """
    Represents an unknown modifier.

    Args:
        text (str): The text of the modifier.
        type (ModifierType): The type of the modifier.
    """

    text: str
    type: ModifierType


@dataclass
class Heist:
    """
    Heist

    This class represents a heist operation.

    Attributes:
        wings_revealed (int): The number of wings revealed in the heist.
        target (Union[Enchants, Trinkets, Gems, Replicas]): The target for the heist.

    """

    wings_revealed: int
    target: Union["Enchants", "Trinkets", "Gems", "Replicas"]


@dataclass
class DropEntry:
    """
    DropEntry

    A class representing a drop entry.

    Attributes:
        query (List[str]): The list of query words.
        items (List[str]): The list of item names.

    """

    query: List[str]
    items: List[str]


@dataclass
class Disc:
    """
    Class representing a Disc.

    Args:
        propAR (Optional[bool]): Property AR.
        propEV (Optional[bool]): Property EV.
        propES (Optional[bool]): Property ES.
        has_implicit (Optional[Dict[str, any]]): Dictionary of implicit properties.
        has_explicit (Optional[Dict[str, any]]): Dictionary of explicit properties.
        section_text (Optional[str]): Section text.
        map_tier (Optional[Union["W", "Y", "R"]]): Map tier.

    Attributes:
        propAR (Optional[bool]): Property AR.
        propEV (Optional[bool]): Property EV.
        propES (Optional[bool]): Property ES.
        has_implicit (Optional[Dict[str, any]]): Dictionary of implicit properties.
        has_explicit (Optional[Dict[str, any]]): Dictionary of explicit properties.
        section_text (Optional[str]): Section text.
        map_tier (Optional[Union["W", "Y", "R"]]): Map tier.
    """

    propAR: Optional[bool] = None
    propEV: Optional[bool] = None
    propES: Optional[bool] = None
    has_implicit: Optional[Dict[str, any]] = None
    has_explicit: Optional[Dict[str, any]] = None
    section_text: Optional[str] = None
    map_tier: Optional[Union["W", "Y", "R"]] = None


@dataclass
class Craftable:
    """
    A class representing a craftable item.

    Attributes:
        category (ItemCategory): The category of the craftable item.
        corrupted (bool, optional): Indicates whether the item is corrupted. Defaults to None.
        unique_only (bool, optional): Indicates whether the item is unique-only. Defaults to None.
    """

    category: ItemCategory
    corrupted: Optional[bool] = None
    unique_only: Optional[bool] = None


@dataclass
class Unique:
    """
    A class that represents a unique object.

    Attributes:
        base: The base type of the unique object.
        fixed_stats: The fixed statistics of the unique object.

    """

    base: Any  # BaseType['ref_name']
    fixed_stats: Optional[List[Any]] = None  # Stat['ref']


@dataclass
class Map:
    """
    Represents a Map object.

    Attributes:
        screenshot (str): The screenshot of the map. Optional, default is None.
    """

    screenshot: Optional[str] = None


@dataclass
class Gem:
    """
    Gem Class

    This class represents a gem in a video game. It contains various attributes that describe the gem.

    Attributes:
        vaal (Optional[bool]): Indicates if the gem is a Vaal gem.
        awakened (Optional"""

    vaal: Optional[bool] = None
    awakened: Optional[bool] = None
    alt_quality: Optional[List[str]] = None
    normal_variant: Optional[Any] = None  # BaseType['ref_name']


@dataclass
class Armour:
    """
    Armour class represents a piece of equipment with various defensive attributes.

    Attributes:
        ar (Optional[Tuple[int, int]]): The "armour rating" attribute, representing the range of possible values for the armour rating.
        ev (Optional[Tuple[int, int]]): The "evasion rating" attribute, representing the range of possible values for the evasion rating.
        es (Optional[Tuple[int, int]]): The "energy shield" attribute, representing the range of possible values for the energy shield.
        ward (Optional[Tuple[int, int]]): The "ward" attribute, representing the range of possible values for the ward.

    Note:
        The attributes ar, ev, es, and ward are tuples containing a minimum and maximum value. The minimum value must be less than or equal to the maximum value.

    Example usage:
        armor = Armour(ar=(50, 100), ev=(0, 50))

        # Modifying the attributes
        armor.ar = (100, 150)
        armor.ev = (30, 70)
        armor.es = (200, 300)
        armor.ward = (10, 20)
    """

    ar: Optional[Tuple[int, int]] = None
    ev: Optional[Tuple[int, int]] = None
    es: Optional[Tuple[int, int]] = None
    ward: Optional[Tuple[int, int]] = None


@dataclass
class BaseType:
    """
    Class: BaseType

    Represents a base type in the game.

    Attributes:
    - name (str): The name of the base type.
    - ref_name (str): The reference name of the base type.
    - namespace (Union["DIVINATION_CARD", "CAPTURED_BEAST", "UNIQUE", "ITEM", "GEM"]): The namespace of the base type.
    - icon (str): The icon representing the base type.
    - w (Optional[int]): The width of the base type. Defaults to None.
    - h (Optional[int]): The height of the base type. Defaults to None.
    - trade_tag (Optional[str]): The trade tag of the base type. Defaults to None.
    - trade_disc (Optional[str]): The trade discard reason of the base type. Defaults to None.
    - disc (Optional[Disc]): The description of the base type. Defaults to None.
    - craftable (Optional[Craftable]): The craftable information of the base type. Defaults to None.
    - unique (Optional[Unique]): The unique information of the base type. Defaults to None.
    - map (Optional[Map]): The map information of the base type. Defaults to None.
    - gem (Optional[Gem]): The gem information of the base type. Defaults to None.
    - armour (Optional[Armour]): The armour information of the base type. Defaults to None.
    """

    name: str
    ref_name: str
    namespace: Union["DIVINATION_CARD", "CAPTURED_BEAST", "UNIQUE", "ITEM", "GEM"]
    icon: str
    w: Optional[int] = None
    h: Optional[int] = None
    trade_tag: Optional[str] = None
    trade_disc: Optional[str] = None
    disc: Optional[Disc] = None
    craftable: Optional[Craftable] = None
    unique: Optional[Unique] = None
    map: Optional[Map] = None
    gem: Optional[Gem] = None
    armour: Optional[Armour] = None


@dataclass
class ParsedItem:
    """Represents a parsed item in a game."""

    info: BaseType
    raw_text: str
    rarity: Optional[ItemRarity] = None
    item_level: Optional[int] = None
    armour_ar: Optional[int] = None
    armour_ev: Optional[int] = None
    armour_es: Optional[int] = None
    armour_ward: Optional[int] = None
    armour_block: Optional[int] = None
    base_percentile: Optional[float] = None
    weapon_crit: Optional[float] = None
    weapon_as: Optional[float] = None
    weapon_physical: Optional[float] = None
    weapon_elemental: Optional[float] = None
    map_blighted: Optional[Union["Blighted", "Blight-ravaged"]] = None
    map_tier: Optional[int] = None
    gem_level: Optional[int] = None
    gem_alt_quality: Optional[
        Union["Anomalous", "Divergent", "Phantasmal", "Superior"]
    ] = None
    area_level: Optional[int] = None
    talisman_tier: Optional[int] = None
    quality: Optional[int] = None
    sockets: Optional[Sockets] = None
    stack_size: Optional[StackSize] = None
    is_unidentified: bool = False
    is_corrupted: bool = False
    is_unmodifiable: Optional[bool] = None
    is_mirrored: Optional[bool] = None
    influences: List[ItemInfluence] = field(default_factory=list)
    logbook_area_mods: Optional[List[List[ParsedModifier]]] = None
    sentinel_charge: Optional[int] = None
    is_synthesised: Optional[bool] = None
    is_fractured: Optional[bool] = None
    is_veiled: Optional[bool] = None
    is_foil: Optional[bool] = None
    stats_by_type: List[StatCalculated] = field(default_factory=list)
    new_mods: List[ParsedModifier] = field(default_factory=list)
    unknown_modifiers: List[UnknownModifier] = field(default_factory=list)
    heist: Optional[Heist] = None
    category: Optional[ItemCategory] = None


def _regex_build_single_re(k, v):
    """
    Parameters
    ----------
    k : Any
        The key for the regular expression pattern.
    v : Dict[str, Union[str, Any]]
        The value corresponding to the key.

    Returns
    -------
    str
        The built regular expression pattern.

    """
    if "re" in v:
        return f"{v['re']}: (?P<{k}>.*)$"
    elif "re2" in v:
        return v["re2"]


def _regex_update_singular_dict(singular_dict):
    """
    Parameters
    ----------
    singular_dict : Dict[str, Any]
        A dictionary representing the singular items to be updated. The keys are strings,
        representing the pattern to be matched, and the values are dictionaries containing
        information about the matching pattern.

    Returns
    -------
    None

    """
    for k, v in singular_dict.items():
        v["re_compiled"] = re.compile(_regex_build_single_re(k, v), re.UNICODE)


def _regex_build_from_handler_dict(handler_dict):
    """
    Parameters
    ----------
    handler_dict : Dict[Any, Any]
        A dictionary containing the handler keys and values.

    Returns
    -------
    re.Pattern
        The compiled regular expression pattern.

    """
    conditionals = [_regex_build_single_re(k, v) for k, v in handler_dict.items()]
    return re.compile("|".join(conditionals), re.MULTILINE | re.UNICODE)


_re_suffix = re.compile("^.+ (?P<suffix>of [\S]+)$", re.UNICODE)

_re_prefix = re.compile("^(?P<prefix>[\S]+) .+$", re.UNICODE)

_re_is_jewel = re.compile("(" "(Viridian|Cobalt|Crimson) Jewel" ")", re.UNICODE)

_re_is_vaal_fragment = re.compile(
    "("
    "Sacrifice at (Dawn|Midnight|Noon|Dusk)|"
    "Mortal (Rage|Hope|Ignorance|Grief)"
    ")",
    re.UNICODE,
)
_re_is_map = re.compile("(" "Map" ")", re.UNICODE)
_re_help_text_item_name = re.compile("(Jewel|Map)", re.UNICODE)
_re_sockets_split = re.compile("( |-)", re.UNICODE)
_re_sockets = re.compile(r"^Sockets: (?P<sockets>.+)$", re.MULTILINE)
_re_singular = {
    "limit": {"re": "\nLimited to\n", "func": int},
    "item_level": {"re": "\nItem Level\n", "func": int},
    "gem_tags": {"re2": r"^(?P<gem_tags>[^:]+)$", "func": lambda s: s.split(", ")},
}
_re_requirement = re.compile(
    "^Requirements:",
    # No multi line, match start of section
    re.UNICODE,
)
_requirement_handlers = {
    "required_level": {"re": "Level", "func": int},
    "required_str": {"re": "Str", "func": int},
    "required_dex": {"re": "Dex", "func": int},
    "required_int": {"re": "Int", "func": int},
}
_stat_handlers = {
    ITEM_TYPES.ITEM: {
        "map_tier": {"re": "Map Tier", "func": int},
        "item_quantity": {"re": "Item Quantity", "func": lambda s: int(s.strip("%"))},
        "item_rarity": {"re": "Item Rarity", "func": lambda s: int(s.strip("%"))},
        "pack_size": {"re": "Monster Pack Size", "func": lambda s: int(s.strip("%"))},
        "quality": {"re": "Quality", "func": lambda s: int(s.strip("%"))},
        "armour": {"re": "Armour", "func": int},
        "evasion": {"re": "Evasion Rating", "func": int},
        "energy_shield": {"re": "Energy Shield", "func": int},
        "physical_damage": {
            "re": "Physical Damage",
            "func": lambda s: [int(s2) for s2 in s.split("-")],
        },
        "elemental_damage": {
            "re": "Elemental Damage",
            "func": lambda s: [
                [int(s3) for s3 in s2.split("-")] for s2 in s.split(", ")
            ],
        },
        "chaos_damage": {
            "re": "Chaos Damage",
            "func": lambda s: [int(s2) for s2 in s.split("-")],
        },
        "critical_strike_chance": {
            "re": "Critical Strike Chance",
            "func": lambda s: float(s.strip("%")),
        },
        "attacks_per_second": {"re": "Attacks per Second", "func": lambda s: float(s)},
        "item_class": {"re2": r"^(?P<item_class>[^:]+)$", "func": lambda s: s},
    },
    ITEM_TYPES.GEM: {
        "gem_level": {"re": "Level", "func": int},
        "mana_cost": {"re": "Mana Cost", "func": int},
        "mana_reserved": {"re": "Mana Reserved", "func": lambda s: int(s.strip("%"))},
        "mana_multiplier": {
            "re": "Mana Multiplier",
            "func": lambda s: int(s.strip("%")),
        },
        "souls_per_use": {"re": "Souls Per Use", "func": int},
        "stored_uses": {
            "re2": r"^Can Store (?P<stored_uses>[0-9]+) Use(?:|s)$",
            "func": int,
        },
        "cooldown_time": {
            "re": "Cooldown Time",
            "func": lambda s: float(s.strip(" sec")),
        },
        "cast_time": {"re": "Cast Time", "func": lambda s: float(s.strip(" sec"))},
        "critical_strike_chance": {
            "re": "Critical Strike Chance",
            "func": lambda s: float(s.strip("%")),
        },
        "damage_effectiveness": {
            "re": "Damage Effectiveness",
            "func": lambda s: int(s.strip("%")) / 100,
        },
        "quality": {"re": "Quality", "func": lambda s: int(s.strip("%"))},
        "experience": {
            "re": "Experience",
            "func": lambda s: [int(s2.replace(".", "")) for s2 in s.split("/")],
        },
    },
    ITEM_TYPES.CURRENCY: {
        "stack_size": {
            "re": "Stack Size",
            "func": lambda s: [int(s2) for s2 in s.split("/")],
        }
    },
}
_re_stat_handlers = {
    ITEM_TYPES.ITEM: _regex_build_from_handler_dict(_stat_handlers[ITEM_TYPES.ITEM]),
    ITEM_TYPES.GEM: _regex_build_from_handler_dict(_stat_handlers[ITEM_TYPES.GEM]),
    ITEM_TYPES.CURRENCY: _regex_build_from_handler_dict(
        _stat_handlers[ITEM_TYPES.CURRENCY]
    ),
}
_re_split = re.compile(r"^\-{8}$", re.UNICODE | re.MULTILINE)
_re_split_newline = re.compile("(?:(?:\r|)\n)", re.UNICODE)
_re_replace = re.compile(r" \((augmented|unmet)\)", re.UNICODE)
_re_rarity = re.compile(r"Rarity:\s+(\w+)", re.UNICODE | re.MULTILINE)
_re_requirement_handlers = _regex_build_from_handler_dict(_requirement_handlers)
_re_item_level = re.compile(
    r"^Item Level: (?P<item_level>\d+)$", re.UNICODE | re.MULTILINE
)
_re_requirement_level = re.compile(r"^Level: (?P<required_level>\d+)$", re.MULTILINE)
_re_requirement_dex = re.compile(r"^Dex: (?P<required_dex>\d+)$", re.MULTILINE)
_re_requirement_str = re.compile(r"^Str: (?P<required_str>\d+)$", re.MULTILINE)
_re_requirement_int = re.compile(r"^Int: (?P<required_int>\d+)$", re.MULTILINE)


def split_item_text(item_text: str) -> List[str]:
    """
    Splits the given item text into a list of strings.

    Parameters
    ----------
    item_text : str
        The item text to be split.

    Returns
    -------
    list[str]
        A list of strings resulting from splitting the item text.

    """
    return _re_split.split(item_text.strip())


def parse_rarity(item_text: str) -> ItemRarity | None:
    """
    Parameters
    ----------
    item_text : str
        The text of the item, which may contain information about its rarity.

    Returns
    -------
    ItemRarity | None
        The rarity of the item, if it can be parsed from the item text. Returns None if no rarity is found or if the parsing fails.

    """
    if rarity_match := _re_rarity.search(item_text):
        rarity = rarity_match.group(1)
        return ItemRarity[rarity]
    return None


def parse_item_level(item_text: str) -> Optional[int]:
    """
    Parameters
    ----------
    item_text : str
        The text of the item.

    Returns
    -------
    Optional[int]
        The parsed item level as an integer, or None if the item level cannot be parsed.
    """
    item_level_match = _re_item_level.search(item_text)
    if item_level_match:
        return int(item_level_match.group("item_level"))
    return None


def parse_singular(item_section: str) -> Dict[str, Any]:
    """
    Parameters
    ----------
    item_section : str
        The singular item section to be parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the parsed values from the singular item section.

    Notes
    -----
    This method takes a singular item section and parses it to extract specific key-value pairs. The item_section parameter should be a string representation of the singular item section.

    The method uses a regular expression matching approach to identify the patterns in the item_section and extract the corresponding values. The parsed values are then stored in a dictionary with their corresponding keys.

    The method returns a dictionary containing the parsed values. The keys of the dictionary represent the specific elements extracted from the singular item section, while the values represent the corresponding extracted values.

    Example usage:
    --------------
    item_section = "Example item section"
    result = parse_singular(item_section)
    """
    result = {}
    for k, v in _re_singular.items():
        if match := v["re_compiled"].match(item_section):
            result[k] = v["func"](match.group(k))
    return result


def parse_requirements_corrected_v3(
    item_text: str,
) -> tuple[int | None, int | None, int | None, int | None]:
    """
    Parameters
    ----------
    item_text : str
        The text containing the item requirements.

    Returns
    -------
    tuple[int | None, int | None, int | None, int | None]
        A tuple of four values representing the parsed requirements. Each value can be an integer or None depending on whether the corresponding requirement was found in the item_text.

    """
    required_level_match = _re_requirement_level.search(item_text)
    required_dex_match = _re_requirement_dex.search(item_text)
    required_str_match = _re_requirement_str.search(item_text)
    required_int_match = _re_requirement_int.search(item_text)

    required_level = (
        int(required_level_match.group("required_level"))
        if required_level_match
        else None
    )
    required_dex = (
        int(required_dex_match.group("required_dex")) if required_dex_match else None
    )
    required_str = (
        int(required_str_match.group("required_str")) if required_str_match else None
    )
    required_int = (
        int(required_int_match.group("required_int")) if required_int_match else None
    )

    return required_level, required_dex, required_str, required_int


def parse_stat(item_section: str, item_type: ITEM_TYPES) -> Dict[str, Any]:
    """
    Parameters
    ----------
    item_section : str
        The item section containing the statistical information.
    item_type : ITEM_TYPES
        The type of item for which the statistical information is being parsed.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the parsed statistical information.

    """
    result = {}
    match = _re_stat_handlers[item_type].match(item_section)
    if match:
        for k, v in _stat_handlers[item_type].items():
            if match.group(k):
                result[k] = v["func"](match.group(k))
    return result


def parse_sockets(item_text: str) -> Optional[Sockets]:
    """
    Parameters
    ----------
    item_text : str
        The string representing the item.

    Returns
    -------
    Optional[Sockets]
        The parsed Sockets object if the sockets information is found in the item text, otherwise None.

    """
    sockets_match = _re_sockets.search(item_text)
    if sockets_match:
        sockets_str = sockets_match.group("sockets")
        linked = sockets_str.count(" ")
        white = sockets_str.count("W")
        return Sockets(linked=linked, white=white, color_str=sockets_str)
    return None


def parse_modifiers(item_text: str) -> Tuple[List[str], List[str]]:
    """
    Parse the modifiers from the given item text.

    Parameters
    ----------
    item_text : str
        The text containing item modifiers.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple consisting of two lists. The first list contains the implicit modifiers, and the second list contains the explicit modifiers.

    """
    implicit_mods = []
    explicit_mods = []

    # Splitting the item text by the delimiter "-----"
    sections = item_text.split("-----")

    # Extracting implicit mods
    implicit_section_index = next(
        (i for i, section in enumerate(sections) if "Implicit Modifier" in section),
        None,
    )
    if implicit_section_index is not None:
        implicit_mods_text = sections[implicit_section_index].split("\n")[1:]
        implicit_mods = [mod.strip() for mod in implicit_mods_text if mod.strip()]

    # Extracting explicit mods (last section)
    explicit_mods_text = sections[-1].split("\n")[1:]
    explicit_mods = [mod.strip() for mod in explicit_mods_text if mod.strip()]

    return implicit_mods, explicit_mods


def parse_item(item_text: str) -> ParsedItem:
    """
    Parameters
    ----------
    item_text : str
        The text representing the item to be parsed.

    Returns
    -------
    ParsedItem
        The parsed item object containing various attributes.

    """
    # Parsing rarity
    rarity = parse_rarity(item_text)

    # Parsing item level
    item_level = parse_item_level(item_text)

    # Parsing sockets
    socket_obj = parse_sockets(item_text)
    sockets_linked = socket_obj.linked if socket_obj else 0
    sockets_white = socket_obj.white if socket_obj else 0
    sockets_str = socket_obj.color_str if socket_obj else ""

    # Parsing modifiers
    implicit_mods, explicit_mods = parse_modifiers(item_text)

    # Constructing implicit modifiers
    implicit_modifiers = [
        UnknownModifier(text=mod, type=ModifierType.Implicit) for mod in implicit_mods
    ]

    # Constructing explicit modifiers (placeholder, assuming all are unknown)
    explicit_modifiers = [
        UnknownModifier(text=mod, type=ModifierType.Explicit) for mod in explicit_mods
    ]

    # Constructing the ParsedItem instance
    parsed_item = ParsedItem(
        info=BaseType(
            name="Decimation Bow", ref_name="Decimation Bow", namespace="ITEM", icon=""
        ),
        raw_text=item_text,
        rarity=ItemRarity(rarity),
        item_level=item_level,
        sockets=Sockets(linked=sockets_linked, white=sockets_white),
        unknown_modifiers=implicit_modifiers + explicit_modifiers,
        heist={},  # Placeholder for heist information
        category=ItemCategory.Bow,
    )

    return parsed_item


if __name__ == "__main__":
    parsed_item = parse_item(item_text)
