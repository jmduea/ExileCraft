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
    ITEM = 0
    GEM = 1
    CURRENCY = 2


class ItemRarity(Enum):
    Normal = "Normal"
    Magic = "Magic"
    Rare = "Rare"
    Unique = "Unique"


class ModifierType(Enum):
    Pseudo = "pseudo"
    Explicit = "explicit"
    Implicit = "implicit"
    Crafted = "crafted"
    Enchant = "enchant"
    Scourge = "scourge"
    Veiled = "veiled"
    Fractured = "fractured"


class ItemInfluence(Enum):
    Crusader = "Crusader"
    Elder = "Elder"
    Hunter = "Hunter"
    Redeemer = "Redeemer"
    Shaper = "Shaper"
    Warlord = "Warlord"


class ItemCategory(Enum):
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
    NegativeRoll = -1
    PositiveRoll = 1
    NotComparable = 0


@dataclass
class StatMatcher:
    string: str
    advanced: Optional[str] = None
    negate: Optional[bool] = None
    value: Optional[int] = None
    oils: Optional[str] = None


@dataclass
class StatRoll:
    value: int
    min: int
    max: int


@dataclass
class TradeInfo:
    inverted: Optional[bool] = None
    option: Optional[bool] = None
    ids: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class Anointment:
    roll: int
    oils: str


@dataclass
class Stat:
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
    type: ModifierType
    generation: Optional[Union["suffix", "prefix", "corrupted", "eldritch"]] = None
    name: Optional[str] = None
    tier: Optional[int] = None
    rank: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    roll_incr: Optional[int] = None


@dataclass
class RollInfo:
    unscalable: bool
    legacy: Optional[bool]
    dp: bool
    value: float
    min: float
    max: float


@dataclass
class ParsedStat:
    stat: Stat
    translation: StatMatcher
    roll: Optional[RollInfo] = None


@dataclass
class ParsedModifier:
    info: ModifierInfo
    stats: List[ParsedStat]


class StatString:
    string: str
    unscalable: bool


@dataclass
class StatSource:
    modifier: ParsedModifier
    stat: ParsedStat
    contributes: Optional[StatRoll] = None


@dataclass
class StatCalculated:
    stat: Stat
    type: ModifierType
    sources: List[StatSource]


@dataclass
class Sockets:
    linked: int
    white: int
    color_str: str


@dataclass
class StackSize:
    value: int
    max: int


@dataclass
class UnknownModifier:
    text: str
    type: ModifierType


@dataclass
class Heist:
    wings_revealed: int
    target: Union["Enchants", "Trinkets", "Gems", "Replicas"]


@dataclass
class DropEntry:
    query: List[str]
    items: List[str]


@dataclass
class Disc:
    propAR: Optional[bool] = None
    propEV: Optional[bool] = None
    propES: Optional[bool] = None
    has_implicit: Optional[Dict[str, any]] = None
    has_explicit: Optional[Dict[str, any]] = None
    section_text: Optional[str] = None
    map_tier: Optional[Union["W", "Y", "R"]] = None


@dataclass
class Craftable:
    category: ItemCategory
    corrupted: Optional[bool] = None
    unique_only: Optional[bool] = None


@dataclass
class Unique:
    base: Any  # BaseType['ref_name']
    fixed_stats: Optional[List[Any]] = None  # Stat['ref']


@dataclass
class Map:
    screenshot: Optional[str] = None


@dataclass
class Gem:
    vaal: Optional[bool] = None
    awakened: Optional[bool] = None
    alt_quality: Optional[List[str]] = None
    normal_variant: Optional[Any] = None  # BaseType['ref_name']


@dataclass
class Armour:
    ar: Optional[Tuple[int, int]] = None
    ev: Optional[Tuple[int, int]] = None
    es: Optional[Tuple[int, int]] = None
    ward: Optional[Tuple[int, int]] = None


@dataclass
class BaseType:
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
    if "re" in v:
        return f"{v['re']}: (?P<{k}>.*)$"
    elif "re2" in v:
        return v["re2"]


def _regex_update_singular_dict(singular_dict):
    for k, v in singular_dict.items():
        v["re_compiled"] = re.compile(_regex_build_single_re(k, v), re.UNICODE)


def _regex_build_from_handler_dict(handler_dict):
    conditionals = [_regex_build_single_re(k, v) for k, v in handler_dict.items()]
    return re.compile("|".join(conditionals), re.MULTILINE | re.UNICODE)


_re_suffix = re.compile(
    "^.+ (?P<suffix>of [\S]+)$",
    re.UNICODE,
)

_re_prefix = re.compile(
    "^(?P<prefix>[\S]+) .+$",
    re.UNICODE,
)

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
    "limit": {
        "re": "\nLimited to\n",
        "func": int,
    },
    "item_level": {
        "re": "\nItem Level\n",
        "func": int,
    },
    "gem_tags": {
        "re2": r"^(?P<gem_tags>[^:]+)$",
        "func": lambda s: s.split(", "),
    },
}
_re_requirement = re.compile(
    "^Requirements:",
    # No multi line, match start of section
    re.UNICODE,
)
_requirement_handlers = {
    "required_level": {
        "re": "Level",
        "func": int,
    },
    "required_str": {
        "re": "Str",
        "func": int,
    },
    "required_dex": {
        "re": "Dex",
        "func": int,
    },
    "required_int": {
        "re": "Int",
        "func": int,
    },
}
_stat_handlers = {
    ITEM_TYPES.ITEM: {
        "map_tier": {
            "re": "Map Tier",
            "func": int,
        },
        "item_quantity": {
            "re": "Item Quantity",
            "func": lambda s: int(s.strip("%")),
        },
        "item_rarity": {
            "re": "Item Rarity",
            "func": lambda s: int(s.strip("%")),
        },
        "pack_size": {
            "re": "Monster Pack Size",
            "func": lambda s: int(s.strip("%")),
        },
        "quality": {
            "re": "Quality",
            "func": lambda s: int(s.strip("%")),
        },
        "armour": {
            "re": "Armour",
            "func": int,
        },
        "evasion": {
            "re": "Evasion Rating",
            "func": int,
        },
        "energy_shield": {
            "re": "Energy Shield",
            "func": int,
        },
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
        "attacks_per_second": {
            "re": "Attacks per Second",
            "func": lambda s: float(s),
        },
        "item_class": {
            "re2": r"^(?P<item_class>[^:]+)$",
            "func": lambda s: s,
        },
    },
    ITEM_TYPES.GEM: {
        "gem_level": {
            "re": "Level",
            "func": int,
        },
        "mana_cost": {
            "re": "Mana Cost",
            "func": int,
        },
        "mana_reserved": {
            "re": "Mana Reserved",
            "func": lambda s: int(s.strip("%")),
        },
        "mana_multiplier": {
            "re": "Mana Multiplier",
            "func": lambda s: int(s.strip("%")),
        },
        "souls_per_use": {
            "re": "Souls Per Use",
            "func": int,
        },
        "stored_uses": {
            "re2": r"^Can Store (?P<stored_uses>[0-9]+) Use(?:|s)$",
            "func": int,
        },
        "cooldown_time": {
            "re": "Cooldown Time",
            "func": lambda s: float(s.strip(" sec")),
        },
        "cast_time": {
            "re": "Cast Time",
            "func": lambda s: float(s.strip(" sec")),
        },
        "critical_strike_chance": {
            "re": "Critical Strike Chance",
            "func": lambda s: float(s.strip("%")),
        },
        "damage_effectiveness": {
            "re": "Damage Effectiveness",
            "func": lambda s: int(s.strip("%")) / 100,
        },
        "quality": {
            "re": "Quality",
            "func": lambda s: int(s.strip("%")),
        },
        "experience": {
            "re": "Experience",
            "func": lambda s: [int(s2.replace(".", "")) for s2 in s.split("/")],
        },
    },
    ITEM_TYPES.CURRENCY: {
        "stack_size": {
            "re": "Stack Size",
            "func": lambda s: [int(s2) for s2 in s.split("/")],
        },
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
    return _re_split.split(item_text.strip())


def parse_rarity(item_text: str) -> ItemRarity | None:
    """Parse the rarity of the item from the given item text."""
    if rarity_match := _re_rarity.search(item_text):
        rarity = rarity_match.group(1)
        return ItemRarity[rarity]
    return None


def parse_item_level(item_text: str) -> Optional[int]:
    """Parse the item level of the item from the given item text."""
    item_level_match = _re_item_level.search(item_text)
    if item_level_match:
        return int(item_level_match.group("item_level"))
    return None


def parse_singular(item_section: str) -> Dict[str, Any]:
    result = {}
    for k, v in _re_singular.items():
        if match := v["re_compiled"].match(item_section):
            result[k] = v["func"](match.group(k))
    return result


def parse_requirements_corrected_v3(
    item_text: str,
) -> tuple[int | None, int | None, int | None, int | None]:
    """Parse the requirements of the item from the given item text using the corrected patterns."""
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
    result = {}
    match = _re_stat_handlers[item_type].match(item_section)
    if match:
        for k, v in _stat_handlers[item_type].items():
            if match.group(k):
                result[k] = v["func"](match.group(k))
    return result


def parse_sockets(item_text: str) -> Optional[Sockets]:
    """Parse the sockets of the item from the given item text using the corrected pattern."""
    sockets_match = _re_sockets.search(item_text)
    if sockets_match:
        sockets_str = sockets_match.group("sockets")
        linked = sockets_str.count(" ")
        white = sockets_str.count("W")
        return Sockets(linked=linked, white=white, color_str=sockets_str)
    return None


def parse_modifiers(item_text: str) -> Tuple[List[str], List[str]]:
    """Parse the implicit and explicit modifiers of the item from the given item text using the corrected logic."""
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
    """Parse the given item text and construct a ParsedItem instance with the extracted details."""
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
