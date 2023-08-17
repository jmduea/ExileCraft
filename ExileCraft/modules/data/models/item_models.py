# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# ##############################################################################
import enum
from dataclasses import dataclass
from random import randint
from typing import Dict, List, Optional, Union

from jinja2 import Template

from modules.shared.config.constants import (
    ITEM_PROPERTIES,
    ITEM_REQUIREMENTS,
)
from modules.shared.config.global_functions import (
    round_with_2_decimal_places,
)
from modules.shared.config.global_functions import round_with_no_decimal_places


class DOMAIN(enum.Enum):
    ITEM = (1, "Item", "item")
    FLASK = (2, "Flask", "flask")
    MONSTER = (3, "Monster", "monster")
    CHEST = (4, "Chest", "chest")
    AREA = (5, "Area", "area")
    RELIC = (7, "Relic", "relic")
    CRAFTED = (9, "Crafted", "crafted")
    JEWEL = (10, "Jewel", "jewel")
    ATLAS = (11, "Atlas", "atlas")
    LEAGUESTONE = (12, "Leaguestone", "leaguestone")
    ABYSS_JEWEL = (13, "Abyss Jewel", "abyss_jewel")
    MAP_DEVICE = (14, "Map Device", "map_device")
    DELVE_FOSSIL = (16, "Delve Fossil", "delve_fossil")
    DELVE_AREA = (17, "Delve Area", "delve_area")
    SYNTHESIS_AREA = (18, "Synthesis Area", "synthesis_area")
    SYNTHESIS_AREA_GLOBAL = (19, "Synthesis Area Global", "synthesis_area_global")
    SYNTHESIS = (20, "Synthesis", "synthesis")
    CLUSTER_JEWEL = (21, "Cluster Jewel", "cluster_jewel")
    HEIST_AREA = (22, "Heist Area", "heist_area")
    HEIST_GEAR = (23, "Heist Gear", "heist_gear")
    TRINKET = (24, "Trinket", "trinket")
    WATCHSTONE = (25, "Watchstone", "watchstone")
    VEILED_MODIFIER = (26, "Veiled Modifier", "veiled_modifier")
    EXPEDITION_REMNANTS = (27, "Expedition Remnants", "expedition_remnants")
    UNVEILED_MODIFIER = (28, "Unveiled Modifier", "unveiled_modifier")
    ELDRITCH_ALTAR = (29, "Eldritch Altar", "eldritch_altar")
    SENTINEL = (30, "Sentinel", "sentinel")
    MEMORY = (31, "Memory", "memory")
    SANCTIFIED_RELIC = (32, "Sanctified Relic", "sanctified_relic")
    CRUCIBLE_AREA = (33, "Crucible Area", "crucible_area")


class ITEM_CATEGORY(enum.Enum):
    MAP = (1, "Map", "map")
    CAPTURED_BEAST = (2, "Captured Beast", "captured_beast")
    METAMORPH_SAMPLE = (3, "Metamorph Sample", "metamorph_sample")
    HELMET = (4, "Helmet", "helmet")
    BODY_ARMOUR = (5, "Body Armour", "body_armour")
    GLOVES = (6, "Gloves", "gloves")
    BOOTS = (7, "Boots", "boots")
    SHIELD = (8, "Shield", "shield")
    AMULET = (9, "Amulet", "amulet")
    BELT = (10, "Belt", "belt")
    RING = (11, "Ring", "ring")
    FLASK = (12, "Flask", "flask")
    ABYSS_JEWEL = (13, "Abyss Jewel", "abyss_jewel")
    JEWEL = (14, "Jewel", "jewel")
    QUIVER = (15, "Quiver", "quiver")
    CLAW = (16, "Claw", "claw")
    BOW = (17, "Bow", "bow")
    SCEPTRE = (18, "Sceptre", "sceptre")
    WAND = (19, "Wand", "wand")
    FISHING_ROD = (20, "Fishing Rod", "fishing_rod")
    STAFF = (21, "Staff", "staff")
    WARSTAFF = (22, "Warstaff", "warstaff")
    DAGGER = (23, "Dagger", "dagger")
    RUNE_DAGGER = (24, "Rune Dagger", "rune_dagger")
    ONE_HANDED_AXE = (25, "One Handed Axe", "one_handed_axe")
    TWO_HANDED_AXE = (26, "Two Handed Axe", "two_handed_axe")
    ONE_HANDED_MACE = (27, "One Handed Mace", "one_handed_mace")
    TWO_HANDED_MACE = (28, "Two Handed Mace", "two_handed_mace")
    ONE_HANDED_SWORD = (29, "One Handed Sword", "one_handed_sword")
    TWO_HANDED_SWORD = (30, "Two Handed Sword", "two_handed_sword")
    CLUSTER_JEWEL = (31, "Cluster Jewel", "cluster_jewel")
    HEIST_BLUEPRINT = (32, "Heist Blueprint", "heist_blueprint")
    HEIST_CONTRACT = (33, "Heist Contract", "heist_contract")
    HEIST_TOOL = (34, "Heist Tool", "heist_tool")
    HEIST_BROOCH = (35, "Heist Brooch", "heist_brooch")
    HEIST_GEAR = (36, "Heist Gear", "heist_gear")
    HEIST_CLOAK = (37, "Heist Cloak", "heist_cloak")
    TRINKET = (38, "Trinket", "trinket")
    INVITATION = (39, "Invitation", "invitation")
    GEM = (40, "Gem", "gem")
    CURRENCY = (41, "Currency", "currency")
    DIVINATION_CARD = (42, "Divination Card", "divination_card")
    VOIDSTONE = (43, "Voidstone", "voidstone")
    SENTINEL = (44, "Sentinel", "sentinel")
    MEMORY_LINE = (45, "Memory Line", "memory_line")


class ITEM_RARITY(enum.Enum):
    NORMAL = ("Normal", "normal")
    MAGIC = ("Magic", "magic")
    RARE = ("Rare", "rare")
    UNIQUE = ("Unique", "unique")


class INFLUENCE_TYPES(enum.Enum):
    SHAPER = ("Shaper", "shaper")
    ELDER = ("Elder", "elder")
    CRUSADER = ("Crusader", "crusader")
    WARLORD = ("Warlord", "warlord", "adjudicator")
    HUNTER = ("Hunter", "hunter", "basilisk")
    REDEEMER = ("Redeemer", "redeemer", "eyrie")
    NONE = ("None", "none")


class ITEM_CLASS_FLAGS(enum.Enum):
    WEAPON = "Weapon, weapon"
    ONE_HAND = "One Hand, one hand"
    MELEE = "Melee, melee"
    OFF_HAND = "Off Hand, Off-hand, off hand, off-hand"
    FLASK = "Flask, flask"
    ARMOUR = "Armour, armour"
    JEWELLERY = "Jewellery, jewellery"
    CURRENCY = "Currency, currency"


@dataclass
class Item:
    data: dict
    mods_cache: dict
    tags_cache: dict

    def __init__(
        self,
        data: dict,
        mods_cache: dict,
        tags_cache: dict,
        influence1: Optional[str] = None,
        influence2: Optional[str] = None,
    ):
        self.data: dict = data
        self._rarity: Optional[ITEM_RARITY] = ITEM_RARITY.NORMAL
        self.influences = self.set_influences(influence1, influence2)
        self._quality: int = 0
        self._item_level: int = self.data.get("drop_level")
        self.drop_level: int = self.data.get("drop_level")
        self.domain: str = self.data.get("domain")
        self.implicits: list = self.data.get("implicits")
        self.item_class: str = self.data.get("item_class")
        self.name: str = self.data.get("name")
        self.release_state: str = self.data.get("release_state")
        self.tags: set = self.data.get("tags")
        self.visual_identity = self.data.get("visual_identity").get("id")
        self.mods_cache = mods_cache
        self.tags_cache = tags_cache
        self.prefix1: Optional[Mod] = None
        self.prefix2: Optional[Mod] = None
        self.prefix3: Optional[Mod] = None
        self.suffix1: Optional[Mod] = None
        self.suffix2: Optional[Mod] = None
        self.suffix3: Optional[Mod] = None

    @property
    def rarity(self):
        """
        Gets the rarity of the item.

        Returns:
            ITEM_RARITY: The rarity of the item.
        """
        return self._rarity

    @rarity.setter
    def rarity(self, value: ITEM_RARITY):
        """
        Sets the rarity of the item.

        Args:
            value (ITEM_RARITY): The rarity of the item.
        Returns:
            None
        """
        if value in ITEM_RARITY:
            self._rarity = value
        else:
            raise ValueError(
                f"Invalid rarity: {value}. It must be one of {list(ITEM_RARITY)}"
            )

    @property
    def open_prefixes(self):
        if self.rarity == ITEM_RARITY.MAGIC:
            total_prefix_slots = 1
        elif self.rarity == ITEM_RARITY.RARE:
            total_prefix_slots = 3
        else:
            return 0

        used_prefix_slots = sum(
            p is not None for p in [self.prefix1, self.prefix2, self.prefix3]
        )
        return total_prefix_slots - used_prefix_slots

    @property
    def open_suffixes(self):
        if self.rarity == ITEM_RARITY.MAGIC:
            total_suffix_slots = 1
        elif self.rarity == ITEM_RARITY.RARE:
            total_suffix_slots = 3
        else:
            return 0

        used_suffix_slots = sum(
            s is not None for s in [self.suffix1, self.suffix2, self.suffix3]
        )
        return total_suffix_slots - used_suffix_slots

    def set_influences(self, influence1, influence2):
        influences = []
        if influence1:
            influences.append(self.get_influence_enum(influence1))
        if influence2:
            influences.append(self.get_influence_enum(influence2))
        return influences

    def get_influence_enum(self, influence_value):
        return next(
            (
                influence
                for influence in INFLUENCE_TYPES
                if influence_value in influence.value
            ),
            INFLUENCE_TYPES.NONE,
        )

    def add_influence(self, influence_value):
        influence_enum = self.get_influence_enum(influence_value)
        if influence_enum not in self.influences:
            self.influences.append(influence_enum)

    def remove_influence(self, influence_value):
        influence_enum = self.get_influence_enum(influence_value)
        if influence_enum in self.influences:
            self.influences.remove(influence_enum)

    @property
    def explicit_mods_dict(self):
        return {**self.applicable_prefix_mods, **self.applicable_suffix_mods}

    @property
    def applicable_mods(self):
        applicable_mods = {}
        for tag in self.tags:
            if tag in self.tags_cache:
                for mod_id, mod_data in self.tags_cache[tag].items():
                    if mod_data["domain"] != self.domain:
                        continue
                    if mod_data["required_level"] > self.item_level:
                        continue

                    # Check if the tag exists in spawn_weights and if its weight is 0
                    spawn_weight_for_tag = next(
                        (
                            weight_dict["weight"]
                            for weight_dict in mod_data["spawn_weights"]
                            if weight_dict["tag"] == tag
                        ),
                        None,
                    )
                    if spawn_weight_for_tag is None or spawn_weight_for_tag == 0:
                        continue

                    applicable_mods[mod_id] = mod_data

        return applicable_mods

    def implict_mods_list(self, applicable_mods):
        return {
            mod_id: mod_data
            for mod_id, mod_data in applicable_mods.items()
            if mod_data.get("generation_type") in ["unique", "corrupted"]
        }

    def get_spawn_chance_for_implicit(self, mod_or_id, remove=True):
        calculator = SpawnChanceCalculator(self.applicable_implicit_mods, self.tags)
        return calculator.spawn_chance(mod_or_id, remove)

    @property
    def applicable_implicit_mods(self):
        return self.implict_mods_list(self.applicable_mods)

    def suffix_mods_list(self, applicable_mods):
        return {
            mod_id: mod_data
            for mod_id, mod_data in applicable_mods.items()
            if mod_data["generation_type"] == "suffix"
        }

    @property
    def applicable_suffix_mods(self):
        return self.suffix_mods_list(self.applicable_mods)

    def prefix_mods_list(self, applicable_mods):
        return {
            mod_id: mod_data
            for mod_id, mod_data in applicable_mods.items()
            if mod_data.get("generation_type") == "prefix"
        }

    @property
    def applicable_prefix_mods(self):
        return self.prefix_mods_list(self.applicable_mods)

    @property
    def implicits_mods(self):
        implicit_mods = []
        implicits_dict = self.mods_cache.get("implicit", {})
        for implicit in self.implicits:
            mod_data = implicits_dict.get(implicit)
            if mod_data:
                implicit_mods.append(Mod.from_dict(mod_data))
        return implicit_mods

    @property
    def implicit_translation(self):
        translations = []
        for mod in self.implicits_mods:
            string = mod.translation_string
            if string:
                translations.append(string)
        translation_string = "\n".join(translations)
        return translation_string

    @property
    def requirements(self):
        return self.data.get("requirements", None)

    @property
    def properties(self):
        return self.data.get("properties", None)

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value

    @property
    def item_level(self):
        return self._item_level

    @item_level.setter
    def item_level(self, value):
        self._item_level = value

    @property
    def range(self):
        if self.properties:
            return self.properties.get("range", None)

    @property
    def physical_damage(self):
        if self.properties:
            return self.properties.get("physical_damage_min", None)

    @property
    def physical_damage_min(self):
        if self.physical_damage:
            return round(
                self.properties.get("physical_damage_min", 0)
                * (100 + self.quality)
                / 100
            )
        else:
            return None

    @property
    def physical_damage_max(self):
        if self.physical_damage:
            return round(
                self.properties.get("physical_damage_max", 0)
                * (100 + self.quality)
                / 100
            )
        else:
            return None

    @property
    def average_physical_damage(self):
        if self.physical_damage_min and self.physical_damage_max:
            return (self.physical_damage_min + self.physical_damage_max) / 2
        else:
            return None

    @property
    def physical_damage_range(self):
        if self.physical_damage_min and self.physical_damage_max:
            return self.physical_damage_max - self.physical_damage_min
        else:
            return None

    @property
    def critical_strike_chance(self):
        if self.properties:
            return round_with_2_decimal_places(
                self.properties.get("critical_strike_chance", 0) / 100
            )
        else:
            return None

    @property
    def attack_time(self):
        if self.properties:
            return (
                round_with_2_decimal_places(
                    1000 / self.properties.get("attack_time", 0)
                )
                if self.properties.get("attack_time")
                else None
            )
        else:
            return None

    @property
    def armour(self):
        if self.properties:
            return self.properties.get("armour", None)

    @property
    def armour_min(self):
        if self.armour:
            return self.armour.get("min", None)
        else:
            return None

    @property
    def armour_max(self):
        if self.armour:
            return self.armour.get("max", None)
        else:
            return None

    @property
    def average_armour(self):
        if self.armour_min and self.armour_max:
            return round_with_no_decimal_places(
                ((self.armour_min + self.armour_max) / 2) * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def armour_range(self):
        if self.armour_min and self.armour_max:
            return self.armour_max - self.armour_min
        else:
            return None

    @property
    def evasion(self):
        if self.properties:
            return self.properties.get("evasion", None)

    @property
    def evasion_min(self):
        if self.evasion:
            return self.evasion.get("min", 0)

    @property
    def evasion_max(self):
        if self.evasion:
            return self.evasion.get("max", 0)

    @property
    def average_evasion(self):
        if self.evasion_min and self.evasion_max:
            return round_with_no_decimal_places(
                ((self.evasion_min + self.evasion_max) / 2)
                * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def evasion_range(self):
        if self.evasion_min and self.evasion_max:
            return self.evasion_max - self.evasion_min
        else:
            return None

    @property
    def energy_shield(self):
        if self.properties:
            return self.properties.get("energy_shield", None)

    @property
    def energy_shield_min(self):
        if self.energy_shield:
            return self.energy_shield.get("min", None)

    @property
    def energy_shield_max(self):
        if self.energy_shield:
            return self.energy_shield.get("max", None)

    @property
    def average_energy_shield(self):
        if self.energy_shield_min and self.energy_shield_max:
            return round_with_no_decimal_places(
                ((self.energy_shield_min + self.energy_shield_max) / 2)
                * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def energy_shield_range(self):
        if self.energy_shield_min and self.energy_shield_max:
            return self.energy_shield_max - self.energy_shield_min
        else:
            return None

    @property
    def ward(self):
        if self.properties:
            return self.properties.get("ward", None)

    @property
    def ward_min(self):
        if self.ward:
            return self.ward.get("min", 0)

    @property
    def ward_max(self):
        if self.ward:
            return self.ward.get("max", 0)

    @property
    def average_ward(self):
        if self.ward_min and self.ward_max:
            return round_with_no_decimal_places(
                ((self.ward_min + self.ward_max) / 2) * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def ward_range(self):
        if self.ward_min and self.ward_max:
            return self.ward_max - self.ward_min
        else:
            return None

    @property
    def block(self):
        if self.properties:
            return round_with_2_decimal_places(self.properties.get("block", None))
        else:
            return None

    @property
    def movement_penalty(self):
        if self.properties:
            return self.properties.get("movement_penalty", None)
        else:
            return None

    @classmethod
    def get_property_value(cls, item_obj, attrs):
        values = []
        if item_obj:
            if isinstance(attrs, str):
                attrs = [attrs]
            for attr in attrs:
                value = getattr(item_obj, attr, None)
                if value is not None:
                    values.append(value)
            if all(value is not None for value in values):
                return values
        return None

    @classmethod
    def get_requirement_value(cls, item_requirements, attr):
        """
        Get the value of a property from the item properties.

        Args:
            item_requirements (ItemRequirements): The properties of the item.
            attr (str): The attribute(s) to retrieve the value from.

        Returns:
            Union[None, Any]: The value of the property, or None if not found.
        """
        if item_requirements is None:
            return None
        for requirement in item_requirements:
            if requirement == attr:
                return item_requirements.get(requirement)
        return None

    def get_requirements(self):
        """
        Get the requirements of the item.

        Returns:
            dict: A dictionary of requirements.
        """
        requirements = {}
        for name, attr, color in ITEM_REQUIREMENTS:
            value = self.get_requirement_value(self.requirements, attr)
            if value is not None:
                requirements[name] = (value, color)
        return requirements

    def formatted_requirements(self):
        """
        Gets the formatted requirements of the item.

        Returns:
            str: The formatted requirements of the item.
        """
        if requirements := self.get_requirements():
            return self.format_requirements_string(requirements)
        else:
            return None

    def formatted_properties(self):
        """
        Gets the formatted properties of the item.

        Returns:
            str: The formatted properties of the item.
        """
        if properties := self.get_properties():
            return self.format_properties_string(properties)
        else:
            return None

    def get_properties(self):
        properties = {}
        for name, attrs, color in ITEM_PROPERTIES:
            # Convert single attribute names to a list for consistency
            if isinstance(attrs, str):
                attrs = [attrs]
            values = [self.get_property_value(self, attr) for attr in attrs]

            # Flatten the values list if it contains sublists
            values = (
                [value for sublist in values for value in sublist]
                if isinstance(values[0], list)
                else values
            )

            # If there's only one value, directly assign it without a list
            if len(values) == 1:
                properties[name] = (values[0], color)
            else:
                properties[name] = (values, color)
        return properties

    @staticmethod
    def format_requirements_string(requirements):
        """
        Formats the requirements of an item for display in the GUI.

        Args:
            requirements (dict): A dictionary of requirements.

        Returns:
            str: A string containing the formatted requirements, ready to be
            displayed in the GUI.
        """
        template = Template(
            """
            <p align="center">
            {% for requirement_name, (value, color) in requirements.items() %}
                {% if value and value != "0" %}
                    {% if requirement_name == 'Requires Level' %}
                        <span style=" font-size:11pt; color:#827a6c;">{{
                        requirement_name }}: </span>
                        <span style=" font-size:11pt; font-weight:bold;
                        color:{{ color }};">{{ value }}</span>
                    {% else %}
                        <span style=" font-size:11pt; font-weight:bold;
                        color:{{ color }};">{{ value }} </span>
                        <span style=" font-size:11pt; color:#827a6c;">{{
                        requirement_name }}</span>
                    {% endif %}
                {% endif %}
            {% endfor %}
            </p>
        """
        )
        return template.render(requirements=requirements)

    @staticmethod
    def format_properties_string(properties):
        """
        Formats the properties of an item for display in the GUI.

        Args:
            properties (dict): A dictionary of properties, where each key is
            the name of a property and each value
                is a tuple containing the value of the property and the
                color to display the value in.

        Returns:
            str: A string containing the formatted properties, ready to be
            displayed in the GUI.
        """
        template = Template(
            """
            {% for property_name, (value, color) in properties.items() %}
                {% if value and value != "0" %}
                    {% if property_name == "Physical Damage" %}
                        {% set min_damage, max_damage = value %}
                        <p style="line-height:0.8; margin:0.5;"
                        align="center">
                            <span style=" font-size:11pt; font-weight:bold;
                            color:{{ color }};">{{ min_damage }} </span>
                            <span style=" font-size:11pt; color:#827a6c;">to
                            </span>
                            <span style=" font-size:11pt; font-weight:bold;
                            color:{{ color }};">{{ max_damage }} </span>
                            <span style=" font-size:11pt; color:#827a6c;">{{
                            property_name }}</span>
                        </p>
                    {% else %}
                        <p style="line-height:0.8; margin:0.5; padding-bottom:0.2em;"
                        align="center">
                            <span style=" font-size:11pt; color:#827a6c;">{{
                            property_name }}: </span>
                            <span style=" font-size:11pt; font-weight:bold;
                            color:{{ color }};">{{ value }}</span>
                        </p>
                    {% endif %}
                {% endif %}
            {% endfor %}
        """
        )
        return template.render(properties=properties)


@dataclass
class Stat:
    id: str
    max: int
    min: int
    stat_translation: List[Dict]


@dataclass
class Mod:
    adds_tags: List[str]
    domain: str
    generation_type: str
    generation_weights: List
    grants_effects: List
    groups: List[str]
    implicit_tags: List[str]
    is_essence_only: bool
    name: str
    required_level: int
    spawn_weights: List
    stats: List[Stat]
    type: str

    @staticmethod
    def from_dict(data: Dict) -> "Mod":
        stats = [Stat(**stat_data) for stat_data in data.get("stats", [])]
        return Mod(
            adds_tags=data.get("adds_tags", []),
            domain=data.get("domain", ""),
            generation_type=data.get("generation_type", ""),
            generation_weights=data.get("generation_weights", []),
            grants_effects=data.get("grants_effects", []),
            groups=data.get("groups", []),
            implicit_tags=data.get("implicit_tags", []),
            is_essence_only=data.get("is_essence_only", False),
            name=data.get("name", ""),
            required_level=data.get("required_level", 0),
            spawn_weights=data.get("spawn_weights", []),
            stats=stats,
            type=data.get("type", ""),
        )

    def count_stats(self):
        return len(self.stats)

    def get_formatted_translation(self, stat: Stat) -> str:
        for condition in stat.stat_translation["English"]:
            if "condition" in condition:
                cond = condition["condition"][0]
                if cond == {}:
                    if "{0}" in condition["string"]:
                        return condition["string"].format(stat.min)
                    else:
                        return condition["string"]
                if cond.get("min") and stat.min >= cond["min"]:
                    return condition["string"].format(stat.min)
                elif cond.get("max") and stat.max <= cond["max"]:
                    return condition["string"].format(stat.max)
        return ""

    @property
    def formatted_translation(self):
        return self.create_translation_string()

    def create_translation_string(self) -> str:
        translations = []
        handled_ids = set()  # Keep track of the ids that have already been processed

        for i, stat in enumerate(self.stats):
            if stat.id in handled_ids:
                continue

            if len(stat.stat_translation["ids"]) > 1:  # If it's a combined translation
                if other_stat := next(
                    (
                        s
                        for j, s in enumerate(self.stats)
                        if j != i
                        and s.id in stat.stat_translation["ids"]
                        and s.id != stat.id
                    ),
                    None,
                ):
                    range2 = (
                        f"{other_stat.min}-{other_stat.max}"
                        if other_stat.min != other_stat.max
                        else f"{other_stat.min}"
                    )

                    range1 = (
                        f"{stat.min}-{stat.max}"
                        if stat.min != stat.max
                        else f"{stat.min}"
                    )
                    # Generate a random value from the range
                    range1_random_value = (
                        randint(stat.min, stat.max)
                        if stat.min != stat.max
                        else stat.min
                    )
                    range2_random_value = (
                        randint(other_stat.min, other_stat.max)
                        if other_stat.min != other_stat.max
                        else other_stat.min
                    )

                    # Format the translation
                    formatted_translation = stat.stat_translation["English"][0][
                        "string"
                    ].format(
                        f"{range1_random_value}({range1})",
                        f"{range2_random_value}({range2})",
                    )
                    handled_ids.add(other_stat.id)
                    translations.append(formatted_translation)
            elif formatted_translation := self.get_formatted_translation(stat):
                translations.append(formatted_translation)

        return "\n".join(translations)

    @property
    def translation_string(self):
        return self.create_translation_string()


class SpawnChanceCalculator:
    def __init__(self, mod_dict, tags):
        self.mod_dict = mod_dict
        self.tags = tags
        self.total_spawn_weight = self.get_total_spawn_weight()

    def get_total_spawn_weight(self):
        total_spawn_weight = 0
        for mod in self.mod_dict.values():
            total_spawn_weight += self.get_spawn_weight(mod)
        return total_spawn_weight

    def get_mod(self, mod_id):
        return self.mod_dict.get(mod_id, None)

    def get_spawn_weight(self, mod):
        for tag, weight_dict in mod.get("spawn_weights", {}).items():
            if tag in self.tags:
                return weight_dict.get("weight", 0)
        return 0

    def spawn_chance(self, mod_or_id, remove=True):
        if isinstance(mod_or_id, str):
            mod = self.get_mod(mod_or_id)
            if mod is None:
                return 0
        elif isinstance(mod_or_id, dict):
            mod = mod_or_id
        else:
            raise TypeError("mod_or_id must be a Mod (dict) or a str")

        weight = self.get_spawn_weight(mod)
        chance = weight / self.total_spawn_weight if self.total_spawn_weight != 0 else 0

        if remove:
            if isinstance(mod_or_id, str):
                self.mod_dict.pop(mod_or_id, None)
            else:
                mod_id_to_remove = next(
                    (key for key, value in self.mod_dict.items() if value == mod), None
                )
                if mod_id_to_remove:
                    self.mod_dict.pop(mod_id_to_remove)

            for tag in mod.get("spawn_weights", {}).keys():
                self.tags[tag] -= mod["spawn_weights"][tag].get("weight", 0)

            self.total_spawn_weight = self.get_total_spawn_weight()

        return chance
