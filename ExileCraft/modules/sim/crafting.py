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
    def __init__(self, item: Optional[Item]):
        self.item: Optional[Item] = item

    @staticmethod
    def can_transmute(item: Item) -> bool:
        """Checks if the item can be transmuted."""
        return item.rarity == ITEM_RARITY.NORMAL

    def can_augment(self) -> bool:
        """Checks if the item can be augmented."""
        return (
            self.item.rarity == ITEM_RARITY.MAGIC
            and self.item.open_prefixes > 0
            or self.item.open_suffixes > 0
        )

    def transmute(self, item: Item):
        """Upgrade a normal item to a magic item."""
        if not self.can_transmute(item):
            raise ValueError("Item cannot be transmuted.")

        item.rarity = ITEM_RARITY.MAGIC

        # Randomly decide the number of prefixes and suffixes (0-1 each)
        num_prefixes = random.randint(0, 1)
        num_suffixes = random.randint(0, 1)

    @staticmethod
    def _get_combined_spawn_chance(mod_dict):
        total_weight = sum(
            mod_data.get("spawn_weight", 0) for mod_data in mod_dict.values()
        )
        # Convert total_weight to a probability
        # This needs adjustment based on your spawn weight definition
        # For now, I'm just normalizing it
        return total_weight / (total_weight + 1)

    def _apply_random_mod(self, mod_dict, mod_type):
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
