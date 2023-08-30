STATUS_WAITING = "waiting"
STATUS_RUNNING = "running"
STATUS_ERROR = "error"
STATUS_COMPLETE = "complete"

STATUS_COLORS = {
    STATUS_RUNNING: "#33a02c",
    STATUS_ERROR: "#e31a1c",
    STATUS_COMPLETE: "#b2df8a",
}

DEFAULT_STATE = {"progress": 0, "status": STATUS_WAITING}

import json
from concurrent.futures import ThreadPoolExecutor

import httpx
from bs4 import BeautifulSoup

item_classes = [
    "claws",
    "generic_daggers",
    "generic_one-handed_swords",
    "one-handed_axes",
    "one-handed_maces",
    "rune_daggers",
    "sceptres",
    "thrusting_one-handed_swords",
    "wands",
    "wands_(minion_type)",
    "bows",
    "generic_staves",
    "two-handed_axes",
    "two-handed_maces",
    "two-handed_swords",
    "warstaves",
    "amulets",
    "belts",
    "quivers",
    "rings_(minion_type)",
    "Unset_Ring",
    "body_armours_(dexterity)",
    "body_armours_(dexterity/intelligence)",
    "body_armours_(intelligence)",
    "body_armours_(strength)",
    "body_armours_(strength/dexterity)",
    "body_armours_(strength/dexterity/intelligence)",
    "body_armours_(strength/intelligence)",
    "boots_(dexterity)",
    "boots_(dexterity/intelligence)",
    "boots_(intelligence)",
    "boots_(strength)",
    "boots_(strength/dexterity)",
    "boots_(strength/intelligence)",
    "gloves_(dexterity)",
    "gloves_(dexterity/intelligence)",
    "gloves_(intelligence)",
    "gloves_(strength)",
    "gloves_(strength/dexterity)",
    "gloves_(strength/intelligence)",
    "helmets_(dexterity)",
    "helmets_(dexterity/intelligence)",
    "helmets_(intelligence)",
    "helmets_(strength)",
    "helmets_(strength/dexterity)",
    "helmets_(strength/intelligence)",
    "shields_(dexterity)",
    "shields_(dexterity/intelligence)",
    "shields_(intelligence)",
    "shields_(minion_type)",
    "shields_(strength)",
    "shields_(strength/dexterity)",
    "shields_(strength/intelligence)",
    "Crimson_Jewel",
    "Viridian_Jewel",
    "Cobalt_Jewel",
    "Murderous_Eye_Jewel",
    "Searching_Eye_Jewel",
    "Hypnotic_Eye_Jewel",
    "Ghastly_Eye_Jewel",
    "Large_Cluster_Jewel",
    "Medium_Cluster_Jewel",
    "Small_Cluster_Jewel",
    "life_flasks",
    "mana_flasks",
    "hybrid_flasks",
    "utility_flasks",
    "Iron_Flask",
]


def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_from_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def parse_soup_for_item_class(soup_dict, item_classes):
    """
    Parameters
    ----------
    soup_dict : dict
        A dictionary containing BeautifulSoup objects for each item class. The keys are the item class names and the values are the corresponding BeautifulSoup objects.
    item_classes : list
        A list of item class names for which the parsing needs to be performed.

    Returns
    -------
    dict
        A dictionary containing the parsed data for all item classes. The keys are the item class names and the values are the corresponding parsed data.

    """
    all_modifiers_data = {}
    for item_class in item_classes:
        soup = soup_dict.get(item_class)
        sections = soup.find_all("div", {"class": "mod-compat__section"})
        modifiers_data = {}

        for section in sections:
            mw_headline = section.find("span", {"class": "mw-headline"})
            mw_headline_text = mw_headline.text.strip() if mw_headline else ""
            gentype_data = {}

            gentypes = section.find_all("div", {"class": "mod-compat__gentype"})
            for gentype in gentypes:
                gentype_heading = gentype.find(
                    "span", {"class": "mod-compat__gentype-heading"}
                )
                heading_text = gentype_heading.text.strip() if gentype_heading else ""
                groups = {}
                group_divs = gentype.find_all("div", {"class": "mod-compat__group"})
                for group_div in group_divs:
                    group_label = group_div.find(
                        "div", {"class": "mod-compat__group-label"}
                    )
                    group_name = (
                        group_label.text.strip().replace("Group: ", "")
                        if group_label
                        else ""
                    )
                    display_name_tag = group_div.find("em", {"class": "tc -mod"})
                    display_name = (
                        display_name_tag.text.strip() if display_name_tag else ""
                    )
                    modifiers_table = group_div.find(
                        "table", {"class": "wikitable modifier-table"}
                    )
                    modifiers = []
                    if modifiers_table:
                        rows = modifiers_table.find_all("tr")[1:]  # Exclude header row
                        for row in rows:
                            cols = row.find_all("td")
                            modifier_name = cols[0].text.strip()
                            req_level = cols[1].text.strip()
                            stats = cols[2].text.strip()
                            tags = [tag.text.strip() for tag in cols[3].find_all("li")]
                            modifiers.append(
                                {
                                    "name": modifier_name,
                                    "req_level": req_level,
                                    "stats": stats,
                                    "tags": tags,
                                }
                            )
                    groups[group_name] = {
                        "modifiers": modifiers,
                        "display_name": display_name,
                    }
                gentype_data[heading_text] = groups
            modifiers_data[mw_headline_text] = gentype_data

        all_modifiers_data[item_class] = modifiers_data

    return all_modifiers_data


def fetch_soup(item_class):
    """
    Fetches and returns the BeautifulSoup object for the specified item class.

    Parameters
    ----------
    item_class : str
        The class of the item for which modifiers should be fetched. For example, "Amulet", "Ring", "Helmet".

    Returns
    -------
    tuple
        A tuple containing the item class and the BeautifulSoup object representing the fetched HTML content.
    """
    url = f"https://www.poewiki.net/wiki/List_of_modifiers_for_{item_class}"
    with httpx.Client() as client:
        response = client.get(url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
    return item_class, soup


def get_modifiers(item_classes):
    """Get modifiers for a list of item classes.

    Parameters
    ----------
    item_classes : list
        List of item classes for which modifiers are to be fetched.

    Returns
    -------
    dict
        Dictionary mapping item classes to soup objects containing modifiers.

    """
    with ThreadPoolExecutor() as executor:
        soup_items = executor.map(fetch_soup, item_classes)
        soup_dict = {item_class: soup for item_class, soup in soup_items}
    return soup_dict


class ModListCache:
    """

    The ModListCache class is responsible for caching and retrieving modifier lists for different item classes.

    Attributes:
        _cache (dict): A dictionary that holds the cached modifier data.

    Methods:
        __init__(): Initializes the ModListCache instance and loads the modifier data from a JSON file.

            Parameters:
                None

            Returns:
                None

        load_data(): Loads the modifier data from a JSON file and stores it in the cache dictionary.

            Parameters:
                None

            Returns:
                None

        get_mod_list(item_class): Retrieves the modifier list for a given item class from the cache.

            Parameters:
                item_class (str): The item class to get the modifier list for.

            Returns:
                dict: A dictionary representing the modifier list for the given item class. If the modifier
                      list is not found in the cache, an empty dictionary is returned.

    """

    def __init__(self):
        self._cache = {}
        self.load_data()

    def load_data(self):
        """
        Loads the modifiers data from a JSON file and stores it in the cache.

        The modifiers data is loaded from the file "modules\\shared\\caches\\modifiers_data.json".
        If the file doesn't exist or there is an error loading the data, an error message is printed.

        Returns
        -------
        None
        """
        modifiers_data_file = "modules\\shared\\caches\\modifiers_data.json"
        try:
            with open(modifiers_data_file, "r") as f:
                data = json.load(f)
            self._cache["modifiers"] = data
        except Exception as e:
            print(f"Error loading {modifiers_data_file}: {e}")

    def get_mod_list(self, item_class):
        """
        Returns
        -------
        Union[Dict, Dict[str, Dict[str, Dict[str, Dict[str, List[Dict[str, str]]]]]]]

        Parameters
        ----------
        item_class : str
            The class of the item for which the modifier list is requested.
        """
        return self._cache.get("modifiers").get(item_class, {})
