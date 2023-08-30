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
import glob
import json
import os

from modules.shared.config.constants import BLACKLISTED_ITEMS, item_class_whitelist

GENERATION_TYPE_BLACKLIST = ["<unknown>", "scourge_detriment", "scourge_benefit"]

MOD_DOMAIN_BLACKLIST = [
    "monster",
    "area",
    "map_device",
    "chest",
    "leaguestone",
    "mods_disallowed",
    "delve_area",
    "dummy",
    "heist_area",
    "atlas",
    "synthesis_a",
    "synthesis_globals",
    "memory_lines",
    "synthesis_bonus",
    "watchstone",
    "expedition_relic",
    "primordial_altar",
    "sentinel",
    "sanctum_relic",
    "templar_relic",
]

ENCHANTMENT_GENERATION_TYPES = [
    "enchantment",
    "blight_tower",
    "flask_enchantment_instilling",
    "flask_enchantment_enkindling",
]

ELDRITCH_IMPLICIT_GENERATION_TYPES = ["archnemesis", "searing_exarch_implicit"]

IMPLICIT_GENERATION_TYPES = ["unique", "corrupted"]

MOD_NAME_MAPPINGS = {
    "shaper": [
        "Elevated Shaper's",
        "The Shaper's",
        "of Elevated Shaping",
        "of Shaping",
    ],
    "elder": [
        "Elevated Elder's",
        "The Elder's",
        "of the Elevated Elder",
        "of the Elder",
    ],
    "crusader": [
        "Elevated Crusader's",
        "Crusader's",
        "of the Elevated Crusade",
        "of the Crusade",
    ],
    "redeemer": [
        "Elevated Redeemer's",
        "Redeemer's",
        "of Elevated Redemption",
        "of Redemption",
    ],
    "hunter": ["Elevated Hunter's", "Hunter's", "of the Elevated Hunt", "of the Hunt"],
    "warlord": [
        "Elevated Warlord's",
        "Warlord's",
        "of the Elevated Conquest",
        "of the Conquest",
    ],
    "delve": ["Subterranean", "of the Underground"],
}


class GlobalCache:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GlobalCache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = {}
        self.load_data()

    def load_data(self):
        cache_files = [
            "modules\\data\\json\\mods.min.json",
            "modules\\data\\json\\base_items.min.json",
            "modules\\data\\json\\item_classes.min.json",
            "modules\\data\\json\\mod_types.min.json",
            "modules\\data\\json\\stat_translations.min.json",
            "modules\\data\\json\\stats.min.json",
            "modules\\data\\json\\tags.min.json",
            "modules\\data\\json\\trade_market_category.json",
            "modules\\data\\json\\trade_market_category_groups.json",
        ]
        json_files = glob.glob(os.path.join("modules", "data", "json", "*.json"))
        json_files.sort()  # Ensure stat_translations are loaded first if they are named appropriately

        for json_file in json_files:
            if json_file not in cache_files:
                continue
            try:
                with open(json_file, "r") as f:
                    data = json.load(f)
                key = os.path.splitext(os.path.basename(json_file))[0]

                if key == "stat_translations.min":
                    key = "stat_translations"
                    self.cache[key] = {}
                    # Special handling for stat_translations: create a separate cache for each id
                    for stat_translation in data:
                        for stat_id in stat_translation["ids"]:
                            self.cache[key][stat_id] = stat_translation

                elif key == "mods.min":
                    key = "mods"
                    self.load_mods(data)

                elif os.path.basename(json_file) == "base_items.min.json":
                    filtered_data = {
                        k: v for k, v in data.items() if self.should_include(k, v)
                    }
                    self.cache[key] = filtered_data

                else:
                    self.cache[key] = data

            except Exception as e:
                print(f"Error loading {json_file}: {e}")
                continue

        return self.cache

    def build_cache_for_domain(self, mod_id, mod_data):
        domain = mod_data["domain"]
        generation_type = mod_data["generation_type"]

        if (
            domain in MOD_DOMAIN_BLACKLIST
            or generation_type in GENERATION_TYPE_BLACKLIST
        ):
            return

        current_domain = self.cache["mods"].setdefault(domain, {})

        if generation_type in ELDRITCH_IMPLICIT_GENERATION_TYPES:
            current_domain.setdefault("eldritch", {})[mod_id] = mod_data
        elif generation_type in IMPLICIT_GENERATION_TYPES:
            current_domain.setdefault("implicit", {})[mod_id] = mod_data
        elif generation_type in ENCHANTMENT_GENERATION_TYPES:
            current_domain.setdefault("enchantment", {})[mod_id] = mod_data
        else:
            current_generation = current_domain.setdefault(generation_type, {})

            if mod_data.get("is_essence_only"):
                current_generation.setdefault("essence", {})[mod_id] = mod_data
                return

            mod_group = next(
                (
                    group_name
                    for group_name, names in MOD_NAME_MAPPINGS.items()
                    if mod_data["name"] in names
                ),
                "base",
            )
            current_generation.setdefault(mod_group, {})[mod_id] = mod_data

    #
    #     def build_tags_cache(self, mod_id, mod_data):
    #         spawn_weights = mod_data.get("spawn_weights", [])
    #         for weight_dict in spawn_weights:
    #             weight = weight_dict["weight"]
    #             if weight > 0:
    #                 tag = weight_dict["tag"]
    #                 self.cache["tags_cache"].setdefault(tag, {})[mod_id] = mod_data
    #
    #     def load_mods(self, mods_data):
    #         self.cache["mods"] = {}
    #         self.cache["tags_cache"] = {}
    #
    #         for mod_id, mod_data in mods_data.items():
    #             if "Watchstone" in mod_id:
    #                 continue
    #             self.build_cache_for_domain(mod_id, mod_data)
    #             self.build_tags_cache(mod_id, mod_data)
    #
    #     def process_stats(self, domain, generation_type, group, group_data):
    #         if not isinstance(group_data, dict):
    #             print(
    #                 f"Unexpected data type in domain: {domain}, generation_type: {generation_type}, group: {group}"
    #             )
    #             return
    #         for stat in group_data.get("stats", []):
    #             if stat:
    #                 stat_id = stat.get("id")
    #                 if stat_id in self.cache["stat_translations"]:
    #                     stat_translation = self.cache["stat_translations"][stat_id]
    #                     stat["stat_translation"] = stat_translation
    #
    #     def match_stats_with_translations(self):
    #         try:
    #             for domain, domain_data in self.cache["mods"].items():
    #                 for generation_type, generation_type_data in domain_data.items():
    #                     for mod_id, mod_data in generation_type_data.items():
    #                         if generation_type in ["implicit", "enchantment", "eldritch"]:
    #                             self.process_stats(
    #                                 domain, generation_type, mod_id, mod_data
    #                             )
    #
    #                     for mod_group, mod_group_data in generation_type_data.items():
    #                         self.process_stats(
    #                             domain, generation_type, mod_group, mod_group_data
    #                         )
    #
    #         except Exception as e:
    #             print(f"Error matching stats with translations: {e}")
    #
    #     def associate_mods_with_items(self):
    #         for item_key, item_data in self.cache.get("base_items.min", {}).items():
    #             domain = item_data.get("domain")
    #             if domain in self.cache["mods"]:
    #                 domain_cache = self.cache["mods"][domain]
    #                 item_data["associated_mods"] = {}
    #                 for cache_key, cache_value in domain_cache.items():
    #                     if filtered_cache_value := {
    #                         mod_id: mod
    #                         for mod_id, mod in cache_value.items()
    #                         if any(
    #                             weight.get("tag") in item_data.get("tags", [])
    #                             for weight in mod.get("spawn_weights", [])
    #                             if weight.get("weight", 0) > 0
    #                         )
    #                     }:
    #                         item_data["associated_mods"][cache_key] = filtered_cache_value
    #
    #     def get_data(self, key):
    #         if key not in self.cache:
    #             raise KeyError(f"Key: {key} does not exist in the cache.")
    #         return self.cache[key]
    #
    #     @property
    #     def cache(self):
    #         return self._cache
    #
    def should_include(self, key, value):
        return (
            value.get("item_class") in item_class_whitelist
            and value.get("release_state") == "released"
            and value.get("domain") == "item"
            and all(
                tag not in value.get("tags", [])
                for tag in [
                    "talisman",
                    "quest_item",
                    "trade_market_legacy_item",
                    "labyrinth_trinket",
                    "demigods",
                ]
            )
            and "Talisman" not in key
            and "Royale" not in key
            and value.get("name") not in BLACKLISTED_ITEMS
        )


#
#     def get_associated_mods(self, item: Item):
#         item_data = item.data
#         if not item_data:
#             return {}
#
#         domain = item_data.get("domain")
#         associated_mods = {}
#
#         if domain in self.cache["mods"]:
#             domain_cache = self.cache["mods"][domain]
#             for cache_key, cache_value in domain_cache.items():
#                 if filtered_cache_value := {
#                     mod_id: mod
#                     for mod_id, mod in cache_value.items()
#                     if mod.get("required_level", 0) <= item.item_level
#                     if any(
#                         weight.get("tag") in item_data.get("tags", [])
#                         for weight in mod.get("spawn_weights", [])
#                         if weight.get("weight", 0) > 0
#                     )
#                 }:
#                     associated_mods[cache_key] = filtered_cache_value
#
#         return associated_mods
