import json

from modules.shared.config.constants import BLACKLISTED_ITEMS, item_class_whitelist


class BaseItemsCache:
    """

    The `BaseItemsCache` class is used to load and cache base items data from a JSON file. It filters the loaded data based on certain conditions and provides access to the filtered data through a cache property.

    Methods:
    - `__init__()`: Initializes the class and calls the `load_data()` method.
    - `load_data()`: Loads the base items data from a JSON file, filters it based on certain conditions, and stores it in the cache.
    - `should_include(key, value)`: Checks whether a base item should be included in the filtered data based on its key and value. Returns a boolean value.
    - `cache()`: Property that returns the filtered base items data from the cache.

    """

    def __init__(self):
        self._cache = {}
        self.load_data()

    def load_data(self):
        """
        Loads and filters data from a JSON file.

        Returns
        -------
        None

        """
        base_items_file = "modules\\data\\json\\base_items.min.json"
        try:
            with open(base_items_file, "r") as f:
                data = json.load(f)
            filtered_data = {k: v for k, v in data.items() if self.should_include(k, v)}
            self._cache["base_items"] = filtered_data
        except Exception as e:
            print(f"Error loading {base_items_file}: {e}")

    def should_include(self, key, value):
        """
        Returns
        -------
        bool
            Returns a boolean value indicating whether the given key-value pair should be included.

        Parameters
        ----------
        key : str
            The key of the item.

        value : Dict[str, str]
            The value associated with the key, represented as a dictionary.

        """
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

    @property
    def cache(self):
        """
        Return the base items cache.

        Returns
        -------
        dict
            The base items cache.

        """
        return self._cache["base_items"]
