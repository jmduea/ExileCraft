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
from random import random
from typing import Optional

from modules.data.models.item_models import Item, ITEM_RARITY


class CraftingManager:
    """
    A class for managing crafting operations on items.

    Args:
        item (Optional[Item]): An instance of the Item class representing the item to be crafted.

    Attributes:
        item (Optional[Item]): An instance of the Item class representing the item to be crafted.

    Methods:
        can_transmute(item: Item) -> bool:
            Checks if the item can be transmuted.

        can_augment() -> bool:
            Checks if the item can be augmented.

        transmute(item: Item):
            Upgrade a normal item to a magic item.

        _get_combined_spawn_chance(mod_dict):
            Calculates the combined spawn chance of mods in a given dictionary.

        _apply_random_mod(mod_dict, mod_type):
            Applies a random mod of a given type to the item.

    """

    def __init__(self, item: Optional[Item]):
        self.item: Optional[Item] = item

    @staticmethod
    def can_transmute(item: Item) -> bool:
        """
        Parameters
        ----------
        item : Item
            The item to check if it can be transmuted.

        Returns
        -------
        bool
            Returns True if the item can be transmuted, and False otherwise.
        """
        return item.rarity == ITEM_RARITY.NORMAL

    def can_augment(self) -> bool:
        """
        Check if an item can be augmented.

        Parameters:
        - self: The `CraftingManager` object.

        Returns:
        - bool: True if the item can be augmented, False otherwise.

        Example usage:
        ```
        crafting_manager = CraftingManager()
        result = crafting_manager.can_augment()
        ```

        Note:
        An item can be augmented if it has a rarity of "MAGIC" and has at least one open prefix or suffix.
        """
        return (
            self.item.rarity == ITEM_RARITY.MAGIC
            and self.item.open_prefixes > 0
            or self.item.open_suffixes > 0
        )

    def transmute(self, item: Item):
        """
        Parameters
        ----------
        item : Item
            The item to be transmuted.

        Raises
        ------
        ValueError
            If the item cannot be transmuted.

        Returns
        -------
        None

        Notes
        -----
        This method transmutes the given item by changing its rarity to MAGIC. It also randomly decides the number of prefixes and suffixes for the transmuted item, with a range of 0 to 1 for each.

        Example
        -------
        >>> item = Item()
        >>> CraftingManager().transmute(item)
        """
        if not self.can_transmute(item):
            raise ValueError("Item cannot be transmuted.")

        item.rarity = ITEM_RARITY.MAGIC

        # Randomly decide the number of prefixes and suffixes (0-1 each)
        num_prefixes = random.randint(0, 1)
        num_suffixes = random.randint(0, 1)

    @staticmethod
    def _get_combined_spawn_chance(mod_dict):
        """
        Parameters
        ----------
        mod_dict : dict
            A dictionary that contains information about the spawn weight of each mod.

        Returns
        -------
        float
            The combined spawn chance as a probability.

        Notes
        -----
        This method calculates the combined spawn chance of all mods in the `mod_dict` by summing up their spawn weights. The spawn weight of each mod determines its likelihood of being spawned. The higher the spawn weight, the higher the chance of spawning the corresponding mod.

        The spawn weight of each mod is defined in the `mod_dict` dictionary. The dictionary should have the mod names as keys and the spawn weights as values. The spawn weight can be any numeric value.

        The combined spawn chance is calculated by summing up the spawn weights of all mods and normalizing it to a probability value between 0 and 1. This is done using the formula:
            combined_spawn_chance = total_weight / (total_weight + 1)

        Please ensure that the `mod_dict` dictionary is structured in the expected format before calling this method.

        Example usage:
            >>> mod_dict = {"mod1": {"spawn_weight": 2}, "mod2": {"spawn_weight": 3}}
            >>> combined_spawn_chance = _get_combined_spawn_chance(mod_dict)
            >>> print(combined_spawn_chance)
            0.625
        """
        total_weight = sum(
            mod_data.get("spawn_weight", 0) for mod_data in mod_dict.values()
        )
        # Convert total_weight to a probability
        # This needs adjustment based on your spawn weight definition
        # For now, I'm just normalizing it
        return total_weight / (total_weight + 1)

    def _apply_random_mod(self, mod_dict, mod_type):
        """
        Parameters
        ----------
        mod_dict : dict
            A dictionary containing the different mods and their corresponding spawn weights.
        mod_type : str
            The type of mod to apply. Should be either "prefix" or "suffix".

        """
        # Pick a random mod based on its spawn weight
        mods = list(mod_dict.keys())
        weights = [mod_data.get("spawn_weight", 0) for mod_data in mod_dict.values()]
        selected_mod = random.choices(mods, weights=weights, k=1)[0]

        # Apply the mod to the item
        if mod_type == "prefix":
            if not self.item.prefix1:
                self.item.prefix1 = selected_mod
            elif not self.item.prefix2:
                self.item.prefix2 = selected_mod
            else:
                self.item.prefix3 = selected_mod
        elif mod_type == "suffix":
            if not self.item.suffix1:
                self.item.suffix1 = selected_mod
            elif not self.item.suffix2:
                self.item.suffix2 = selected_mod
            else:
                self.item.suffix3 = selected_mod
