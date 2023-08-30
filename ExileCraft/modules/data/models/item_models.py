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

from modules.shared.config.constants import ITEM_PROPERTIES, ITEM_REQUIREMENTS
from modules.shared.config.global_functions import round_with_2_decimal_places
from modules.shared.config.global_functions import round_with_no_decimal_places


class DOMAIN(enum.Enum):
    """
    Enumeration representing different domains.
    Each domain has a unique ID, name, and code.
    """

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
    """
    The `ITEM_CATEGORY` class is an enumeration that represents different categories of items in a game. Each item category has a unique identifier, a name, and a code.

    Attributes:
        - identifier (int): The unique identifier for the item category.
        - name (str): The name of the item category.
        - code (str): The code representing the item category.

    Enum Values:
        - MAP: Represents a map item category.
        - CAPTURED_BEAST: Represents a captured beast item category.
        - METAMORPH_SAMPLE: Represents a metamorph sample item category.
        - HELMET: Represents a helmet item category.
        - BODY_ARMOUR: Represents a body armour item category.
        - GLOVES: Represents a gloves item category.
        - BOOTS: Represents a boots item category.
        - SHIELD: Represents a shield item category.
        - AMULET: Represents an amulet item category.
        - BELT: Represents a belt item category.
        - RING: Represents a ring item category.
        - FLASK: Represents a flask item category.
        - ABYSS_JEWEL: Represents an abyss jewel item category.
        - JEWEL: Represents a jewel item category.
        - QUIVER: Represents a quiver item category.
        - CLAW: Represents a claw item category.
        - BOW: Represents a bow item category.
        - SCEPTRE: Represents a sceptre item category.
        - WAND: Represents a wand item category.
        - FISHING_ROD: Represents a fishing rod item category.
        - STAFF: Represents a staff item category.
        - WARSTAFF: Represents a warstaff item category.
        - DAGGER: Represents a dagger item category.
        - RUNE_DAGGER: Represents a rune dagger item category.
        - ONE_HANDED_AXE: Represents a one-handed axe item category.
        - TWO_HANDED_AXE: Represents a two-handed axe item category.
        - ONE_HANDED_MACE: Represents a one-handed mace item category.
        - TWO_HANDED_MACE: Represents a two-handed mace item category.
        - ONE_HANDED_SWORD: Represents a one-handed sword item category.
        - TWO_HANDED_SWORD: Represents a two-handed sword item category.
        - CLUSTER_JEWEL: Represents a cluster jewel item category.
        - HEIST_BLUEPRINT: Represents a heist blueprint item category.
        - HEIST_CONTRACT: Represents a heist contract item category.
        - HEIST_TOOL: Represents a heist tool item category.
        - HEIST_BROOCH: Represents a heist brooch item category.
        - HEIST_GEAR: Represents a heist gear item category.
        - HEIST_CLOAK: Represents a heist cloak item category.
        - TRINKET: Represents a trinket item category.
        - INVITATION: Represents an invitation item category.
        - GEM: Represents a gem item category.
        - CURRENCY: Represents a currency item category.
        - DIVINATION_CARD: Represents a divination card item category.
        - VOIDSTONE: Represents a voidstone item category.
        - SENTINEL: Represents a sentinel item category.
        - MEMORY_LINE: Represents a memory line item category.
    """

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
    """
    This class represents the different rarities of an item. It is an enumeration with four possible values: NORMAL, MAGIC, RARE, and UNIQUE.

    Each item rarity has a display name and a code name associated with it. The display name is a human-readable string that describes the rarity, while the code name is a machine-readable string that can be used for identification or serialization.

    Attributes:
        NORMAL: Represents the normal rarity.
        MAGIC: Represents the magic rarity.
        RARE: Represents the rare rarity.
        UNIQUE: Represents the unique rarity.

    Example usage:
        >>> rarity = ITEM_RARITY.MAGIC
        >>> print(rarity)
        ITEM_RARITY.MAGIC

        >>> print(rarity.value)
        ('Magic', 'magic')
    """

    NORMAL = ("Normal", "normal")
    MAGIC = ("Magic", "magic")
    RARE = ("Rare", "rare")
    UNIQUE = ("Unique", "unique")


class INFLUENCE_TYPES(enum.Enum):
    """
    Enum defining different types of influence.

    Attributes:
        SHAPER: Influence type Shaper, with aliases "shaper".
        ELDER: Influence type Elder, with aliases "elder".
        CRUSADER: Influence type Crusader, with aliases "crusader".
        WARLORD: Influence type Warlord, with aliases "warlord" and "adjudicator".
        HUNTER: Influence type Hunter, with aliases "hunter" and "basilisk".
        REDEEMER: Influence type Redeemer, with aliases "redeemer" and "eyrie".
        NONE: No influence type, with aliases "none".
    """

    SHAPER = ("Shaper", "shaper")
    ELDER = ("Elder", "elder")
    CRUSADER = ("Crusader", "crusader")
    WARLORD = ("Warlord", "warlord", "adjudicator")
    HUNTER = ("Hunter", "hunter", "basilisk")
    REDEEMER = ("Redeemer", "redeemer", "eyrie")
    NONE = ("None", "none")


class ITEM_CLASS_FLAGS(enum.Enum):
    """
    The ITEM_CLASS_FLAGS class is an enumeration that represents the different flags that can be associated with an item in a game. Each flag describes a specific category or classification of the item.

    Attributes:
        WEAPON: Represents an item that is classified as a weapon.
        ONE_HAND: Represents an item that can be wielded with one hand.
        MELEE: Represents a weapon that is designed for close combat.
        OFF_HAND: Represents an item that is meant to be used in the off hand, typically paired with a main weapon.
        FLASK: Represents an item that is a consumable flask.
        ARMOUR: Represents an item that provides protection or defense.
        JEWELLERY: Represents an item that is classified as jewellery.
        CURRENCY: Represents an item that serves as a form of currency.

    Example Usage:
        item_flag = ITEM_CLASS_FLAGS.WEAPON
        print(item_flag.value)  # Output: "Weapon, weapon"
        print(item_flag.name)   # Output: "WEAPON"

    Notes:
        - The ITEM_CLASS_FLAGS enumeration can be used to categorize items and determine their properties or requirements.
        - Each flag is represented as a string value.
        - It is recommended to use the value attribute to get the string representation of a flag.
        - The name attribute can be used to get the name of a flag (e.g., "WEAPON").

    """

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
    """
    Class representing an item in the game.

    Attributes:
        data (dict): The data dictionary of the item.
        rarity (ITEM_RARITY): The rarity of the item.
        influences (List[INFLUENCE_TYPES]): The influences on the item.
        quality (int): The quality of the item.
        item_level (int): The item level of the item.
        drop_level (int): The drop level of the item.
        domain (str): The domain of the item.
        implicits (List): The implicits of the item.
        item_class (str): The item class of the item.
        name (str): The name of the item.
        release_state (str): The release state of the item.
        tags (set): The tags of the item.
        visual_identity (str): The visual identity of the item.
        prefix1 (Optional[Mod]): The first prefix mod of the item.
        prefix2 (Optional[Mod]): The second prefix mod of the item.
        prefix3 (Optional[Mod]): The third prefix mod of the item.
        suffix1 (Optional[Mod]): The first suffix mod of the item.
        suffix2 (Optional[Mod]): The second suffix mod of the item.
        suffix3 (Optional[Mod]): The third suffix mod of the item.

    Methods:
        set_influences(self, influence1, influence2) -> List[INFLUENCE_TYPES]: Sets the influences of the item.
        get_influence_enum(self, influence_value) -> INFLUENCE_TYPES: Returns the influence enum for a given value.
        add_influence(self, influence_value): Adds an influence to the item.
        remove_influence(self, influence_value): Removes an influence from the item.
        get_requirements(self) -> dict: Returns the requirements of the item.
        formatted_requirements(self) -> str: Returns the formatted requirements of the item.
        get_properties(self) -> dict: Returns the properties of the item.
        formatted_properties(self) -> str: Returns the formatted properties of the item.
        get_property_value(cls, item_obj, attrs) -> Optional[Union[Any, List[Any]]]: Returns the value of a property from the item properties.
        get_requirement_value(cls, item_requirements, attr) -> Optional[Any]: Returns the value of a requirement from the item requirements.
    """

    data: dict

    def __init__(
        self,
        data: dict,
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
        self.prefix1: Optional[Mod] = None
        self.prefix2: Optional[Mod] = None
        self.prefix3: Optional[Mod] = None
        self.suffix1: Optional[Mod] = None
        self.suffix2: Optional[Mod] = None
        self.suffix3: Optional[Mod] = None

    @property
    def rarity(self):
        """

        This method calculates the rarity of an item.

        Parameters:
            - item (Item): An instance of the Item class.

        Returns:
            - float: The calculated rarity of the item.

        Example usage:
            item = Item()
            item_rarity = item.rarity()

        """
        return self._rarity

    @rarity.setter
    def rarity(self, value: ITEM_RARITY):
        """
        Parameters
        ----------
        value : ITEM_RARITY
            The rarity value to be set for the item.

        Raises
        ------
        ValueError
            If the provided rarity value is not valid.

        """
        if value in ITEM_RARITY:
            self._rarity = value
        else:
            raise ValueError(
                f"Invalid rarity: {value}. It must be one of {list(ITEM_RARITY)}"
            )

    @property
    def open_prefixes(self):
        """

        Calculates the number of open prefix slots for an item.

        Parameters:
        ----------
        self : Item
            The item for which to calculate the number of open prefix slots.

        Returns:
        -------
        int
            The number of open prefix slots for the item.

        """
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
        """

        open_suffixes method

        Calculates the number of open suffix slots on an item based on its rarity.

        Parameters:
            None

        Returns:
            int: The number of open suffix slots on the item.

        Example:
            item = Item(rarity=ITEM_RARITY.RARE, suffix1="suffix1", suffix2="suffix2")
            open_suffixes = item.open_suffixes()

        """
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
        """
        Set influences for an Item.

        Parameters
        ----------
        influence1 : Union[None, None, None, None, Dict[str, Dict[str, Dict[str, List]]], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            The first influence to be set. Can be None if no influence is applicable.
        influence2 : Union[None, None, None, None, Dict[str, Dict[str, Dict[str, List[str]]]], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            The second influence to be set. Can be None if no influence is applicable.

        Returns
        -------
        List[Union[List]], List[Union[List[modules.data.models.item_models.INFLUENCE_TYPES]]]
            A list of influences that have been set for the Item. Each influence is represented as an enum from the
            'modules.data.models.item_models.INFLUENCE_TYPES' enumeration.

        """
        influences = []
        if influence1:
            influences.append(self.get_influence_enum(influence1))
        if influence2:
            influences.append(self.get_influence_enum(influence2))
        return influences

    def get_influence_enum(self, influence_value):
        """
        Returns
        -------
        modules.data.models.item_models.INFLUENCE_TYPES: The enum value representing the influence type.

        Parameters
        ----------
        influence_value : Union[list_iterator, Dict[str, Dict[str, Dict[str, List]]], Dict[str, Dict[str, Dict[str, List[str]]]], str]: The value to match against the influence types.

        """
        return next(
            (
                influence
                for influence in INFLUENCE_TYPES
                if influence_value in influence.value
            ),
            INFLUENCE_TYPES.NONE,
        )

    def add_influence(self, influence_value):
        """
        Returns
        -------
        None

        Parameters
        ----------
        influence_value : Union[list_iterator, str]
            The value representing the influence to be added.
            It can be a list iterator or a string.

        """
        influence_enum = self.get_influence_enum(influence_value)
        if influence_enum not in self.influences:
            self.influences.append(influence_enum)

    def remove_influence(self, influence_value):
        """
        Removes the specified influence from the item.

        Parameters
        ----------
        influence_value : str
            The value of the influence to be removed.

        Returns
        -------
        None
        """
        influence_enum = self.get_influence_enum(influence_value)
        if influence_enum in self.influences:
            self.influences.remove(influence_enum)

    @property
    def requirements(self):
        """

        This method returns the requirements of an item.

        Parameters:
        - data: Dict[str, Union[str, int, List[Dict[str, Union[str, int]]]]]
            A dictionary containing the data of the item.

        Returns:
        - Optional[List[Dict[str, Union[str, float, int, None]]]]:
            The requirements of the item. If there are no requirements, None is returned.

        """
        return self.data.get("requirements", None)

    @property
    def properties(self):
        """
        Gets the properties of the item.

        Returns:
            Union[Dict[str, Union[str, int, float]], None]: A dictionary containing the properties of the item. If the item does not have any properties, None is returned.
        """
        return self.data.get("properties", None)

    @property
    def quality(self):
        """
        Calculate the quality of an item based on its properties.

        Parameters:
            item (Item): The item for which to calculate the quality.
            properties (Dict[str, Union[int, float]]): The properties of the item.

        Returns:
            Optional"""
        return self._quality

    @quality.setter
    def quality(self, value):
        """
        Parameters
        ----------
        value : Union[int, float]
            The value to set as the quality of the item. It can be either an integer or a float.

        """
        self._quality = value

    @property
    def item_level(self):
        """
        Calculate and return the item level of an Item.

        Parameters:
        - None

        Returns:
        - The item level as an integer.

        Example usage:
        ```
        item = Item()
        level = item.item_level()
        print(level)
        ```
        """
        return self._item_level

    @item_level.setter
    def item_level(self, value):
        """
        Parameters
        ----------
        value : Union[int, float]
            The level of the item. It can be either an integer or a float.

        """
        self._item_level = value

    @property
    def range(self):
        """
        Method Name: range
        Parameters:
            - self: Item
        Returns:
            - range: Optional[Union[int, float]]

        Description:
            This method returns the range of an item by checking the "range" property in the item's properties dictionary. If the property exists, the range value is returned; otherwise, None is returned.

            The range value can be either an integer or a float. If the item has no range property, the return value will be None.

            Example usage:
                # Create an item
                item = Item()

                # Access the range property
                item_range = item.range
        """
        if self.properties:
            return self.properties.get("range", None)

    @property
    def physical_damage(self):
        """
        Calculate the physical damage of an item.

        Args:
            self (Item): The item.

        Returns:
            Union[int, None]: The physical damage of the item if it has the "physical_damage_min" property,
            or None if the property is not found.

        Example:
            item = Item()
            damage = item.physical_damage
        """
        if self.properties:
            return self.properties.get("physical_damage_min", None)

    @property
    def physical_damage_min(self):
        """
        Get the minimum physical damage of an item.

        Parameters:
        - None

        Returns:
        - Union[float, None]: The minimum physical damage of the item if it has physical damage, else None.

        Example Usage:
        item = Item()
        min_damage = item.physical_damage_min()
        print(min_damage)
        """
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
        """

        Calculate the maximum physical damage of an item.

        Parameters:
        - self (Item): The item object.

        Returns:
        - Union[float, None]: The maximum physical damage of the item, rounded to 2 decimal places. Returns None if the item doesn't have physical damage.

        Example:
        ```
        item = Item()
        item.physical_damage = True
        item.quality = 10
        item.properties = {"physical_damage_max": 50}

        result = item.physical_damage_max()
        print(result)  # Output: 55.0
        ```

        """
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
        """

        Calculate the average physical damage of an item.

        Parameters:
        - self (Item): The item object.

        Returns:
        - Union[float, None]: The average physical damage of the item. If the item does not have both minimum and maximum physical damage values, returns None.


        Example Usage:
        ```
        item = Item()
        item.physical_damage_min = 10
        item.physical_damage_max = 20
        avg_physical_damage = item.average_physical_damage()
        print(avg_physical_damage)  # Output: 15.0
        ```
        """
        if self.physical_damage_min and self.physical_damage_max:
            return (self.physical_damage_min + self.physical_damage_max) / 2
        else:
            return None

    @property
    def physical_damage_range(self):
        """

        Calculates the range of physical damage for an item.

        Parameters:
        - None

        Returns:
        - A float value representing the range of physical damage for the item. Returns None if the item's minimum and maximum physical damage values are not set.

        Example usage:
            item = Item()
            damage_range = item.physical_damage_range

        Notes:
        - This method assumes that the item's `physical_damage_min` and `physical_damage_max` properties have been set.

        """
        if self.physical_damage_min and self.physical_damage_max:
            return self.physical_damage_max - self.physical_damage_min
        else:
            return None

    @property
    def critical_strike_chance(self):
        """

        Calculate the critical strike chance of an item.

        Parameters:
            self (Item): The item object.

        Returns:
            Optional[float]: The critical strike chance of the item as a decimal (e.g. 0.05 for 5% chance). Returns None if the item has no critical strike chance properties.

        """
        if self.properties:
            return round_with_2_decimal_places(
                self.properties.get("critical_strike_chance", 0) / 100
            )
        else:
            return None

    @property
    def attack_time(self):
        """
        Calculates the attack time of an Item.

        Parameters:
        - self (Item): The item for which to calculate the attack time.

        Returns:
        - Optional[float]: The attack time of the item in milliseconds. Returns None if the attack time is not defined in the item properties.

        Example usage:
            item = Item(...)
            attack_time = item.attack_time

        Note:
        - The attack time is calculated as the inverse of the attack time property defined in the item properties, rounded to 2 decimal places.
        - If the attack time property is not defined in the item properties, None is returned.

        """
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
        """Get the armour value of the item.

        Returns:
            Union[int, None]: The armour value of the item. Returns None if the item has no armour property.
        """
        if self.properties:
            return self.properties.get("armour", None)

    @property
    def armour_min(self):
        """
        Get the minimum armour value of an item.

        Parameters:
            self (Item): The item object.

        Returns:
            Optional[Union[float, int]]: The minimum armour value of the item. Returns None if the item has no armour value.

        Example:
            item = Item()
            min_armour = item.armour_min()
        """
        if self.armour:
            return self.armour.get("min", None)
        else:
            return None

    @property
    def armour_max(self):
        """

        Calculate the maximum armor value for an item.

        Parameters:
        - self (Item): The item for which to calculate the maximum armor value.

        Returns:
        - Union[float, None]: The maximum armor value if it exists, otherwise None.

        """
        if self.armour:
            return self.armour.get("max", None)
        else:
            return None

    @property
    def average_armour(self):
        """

        Calculate the average armour of an item.

        Parameters:
        - self: The item object.

        Returns:
        - The average armour of the item, rounded to 0 decimal places. If either the minimum or maximum armour is missing, returns None.

        """
        if self.armour_min and self.armour_max:
            return round_with_no_decimal_places(
                ((self.armour_min + self.armour_max) / 2) * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def armour_range(self):
        """
        Calculate the range of armor for an item.

        Parameters:
            None

        Returns:
            Union[float, None]: The range of armor for the item if both the minimum and maximum armor values are provided. None otherwise.
        """
        if self.armour_min and self.armour_max:
            return self.armour_max - self.armour_min
        else:
            return None

    @property
    def evasion(self):
        """
        Calculate the evasion value of an item.

        Parameters:
            self (Item): The item object.

        Returns:
            float or None: The calculated evasion value of the item if it has the "evasion" property,
            otherwise None.

        Example:
            item = Item()
            evasion_value = item.evasion()
        """
        if self.properties:
            return self.properties.get("evasion", None)

    @property
    def evasion_min(self):
        """
        This method returns the minimum evasion value for an item.

        Parameters:
            self (Item): The item object.

        Returns:
            int: The minimum evasion value for the item.
        """
        if self.evasion:
            return self.evasion.get("min", 0)

    @property
    def evasion_max(self):
        """
        Returns the maximum evasion value for the item.

        If the item has an evasion attribute, it returns the maximum value specified in the attribute.
        Otherwise, it returns 0.

        Returns:
            Optional[int]: The maximum evasion value for the item, or None if the item does not have an evasion attribute.
        """
        if self.evasion:
            return self.evasion.get("max", 0)

    @property
    def average_evasion(self):
        """
        Calculate the average evasion for an item.

        Parameters:
        - self (Item): The item.

        Returns:
        - Union[float, None]: The average evasion of the item. It returns `None` if the item doesn't have a minimum and maximum evasion value.

        Example:
            item = Item()
            item.evasion_min = 10
            item.evasion_max = 20
            item.quality = 50
            avg_evasion = item.average_evasion
            print(avg_evasion)  # Output: 15.0

        """
        if self.evasion_min and self.evasion_max:
            return round_with_no_decimal_places(
                ((self.evasion_min + self.evasion_max) / 2)
                * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def evasion_range(self):
        """
        Calculate the evasion range of an item.

        Parameters:
            self (Item): The item object.

        Returns:
            float: The range of evasion for the item. If evasion_min and evasion_max are both provided, it returns the difference between them. Otherwise, it returns None.

        Example:
            >>> item = Item(evasion_min=10, evasion_max=20)
            >>> item.evasion_range()
            10
            >>> item = Item(evasion_min=None, evasion_max=20)
            >>> item.evasion_range()
            None
        """
        if self.evasion_min and self.evasion_max:
            return self.evasion_max - self.evasion_min
        else:
            return None

    @property
    def energy_shield(self):
        """
        Calculates the energy shield value of an item.

        Parameters:
        - self (Item): The item object for which to calculate the energy shield value.

        Returns:
        - int or None: The calculated energy shield value of the item, or None if the item has no energy shield property.

        Example Usage:
            item = Item()
            shield_value = item.energy_shield()
            print(shield_value)
        """
        if self.properties:
            return self.properties.get("energy_shield", None)

    @property
    def energy_shield_min(self):
        """
        Calculate the minimum value of an item's energy shield.

        Parameters:
            self (Item): The item instance.

        Returns:
            Optional[Union[float, int]]: The minimum value of the item's energy shield if it exists, otherwise None.

        """
        if self.energy_shield:
            return self.energy_shield.get("min", None)

    @property
    def energy_shield_max(self):
        """Calculate the maximum energy shield for an item.

        This method calculates the maximum value of the energy shield property for an item. If the item has an energy shield property, the maximum value is returned. Otherwise, `None` is returned.

        Args:
            self (Item): The item for which to calculate the maximum energy shield.

        Returns:
            Union[float, None]: The maximum energy shield value, or `None` if the item has no energy shield property.

        """
        if self.energy_shield:
            return self.energy_shield.get("max", None)

    @property
    def average_energy_shield(self):
        """
        Calculate the average energy shield of an item.

        Parameters:
            None

        Returns:
            Union[int, None]: The average energy shield value of the item, rounded to the nearest whole number. If the energy shield values are not specified (energy_shield_min and energy_shield_max), returns None.

        Example:
            >>> item = Item()
            >>> item.energy_shield_min = 10
            >>> item.energy_shield_max = 20
            >>> item.quality = 10
            >>> item.average_energy_shield
            31

            >>> item.energy_shield_min = None
            >>> item.energy_shield_max = None
            >>> item.average_energy_shield
            None
        """
        if self.energy_shield_min and self.energy_shield_max:
            return round_with_no_decimal_places(
                ((self.energy_shield_min + self.energy_shield_max) / 2)
                * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def energy_shield_range(self):
        """
        Calculates the range of an item's energy shield based on its minimum and maximum energy shield values.

        Parameters:
            None

        Returns:
            Union[float, None]: The range of the item's energy shield if both minimum and maximum values are provided. None if either the minimum or maximum value is missing.
        """
        if self.energy_shield_min and self.energy_shield_max:
            return self.energy_shield_max - self.energy_shield_min
        else:
            return None

    @property
    def ward(self):
        """
        This method is a property accessor for the 'ward' attribute of the Item class.

        Parameters:
            None

        Returns:
            Optional[str]: The value of the 'ward' attribute if it exists, otherwise None.

        Example usage:
            item = Item(...)
            ward = item.ward
        """
        if self.properties:
            return self.properties.get("ward", None)

    @property
    def ward_min(self):
        """
        Calculate the minimum ward value for an item.

        Parameters:
        - None

        Returns:
        - The minimum ward value (float)
        """
        if self.ward:
            return self.ward.get("min", 0)

    @property
    def ward_max(self):
        """

        Calculate the maximum value for wards in an Item.

        Parameters:
        - None

        Returns:
        - int: The maximum value for wards in the Item.

        Example usage:
        >>> item = Item()
        >>> item.ward_max
        0

        """
        if self.ward:
            return self.ward.get("max", 0)

    @property
    def average_ward(self):
        """
        Calculate the average ward of an Item.

        This method calculates the average ward of an Item based on the ward_min, ward_max, and quality attributes of the Item object.

        Parameters:
            None

        Returns:
            Optional[float]: The average ward of the Item as a floating-point number. If either ward_min or ward_max is missing, or both, or if the quality attribute is missing, None is returned.

        Example usage:
            item = Item()
            item.ward_min = 10
            item.ward_max = 20
            item.quality = 50
            result = item.average_ward

        """
        if self.ward_min and self.ward_max:
            return round_with_no_decimal_places(
                ((self.ward_min + self.ward_max) / 2) * ((100 + self.quality) / 100)
            )
        else:
            return None

    @property
    def ward_range(self):
        """ """
        if self.ward_min and self.ward_max:
            return self.ward_max - self.ward_min
        else:
            return None

    @property
    def block(self):
        """ """
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
