import httpx
from bs4 import BeautifulSoup

POE_WIKI_API = "https://www.poewiki.net/w/api.php"
ITEM_CLASS_URL_MAP = {
    "Claw": "claws",
    "Dagger": "generic_daggers",
    "One Hand Sword": "generic_one-handed_swords",
    "One Hand Axe": "one-handed_axes",
    "One Hand Mace": "one-handed_maces",
    "Rune Dagger": "rune_daggers",
    "Sceptre": "sceptres",
    "Thrusting One Hand Sword": "thrusting_one-handed_swords",
    "Wand": "wands",
    "Bow": "bows",
    "Staff": "generic_staves",
    "Warstaff": "warstaves",
    "Two Hand Axe": "two-handed_axes",
    "Two Hand Mace": "two-handed_maces",
    "Two Hand Sword": "two-handed_swords",
    "Amulet": "amulets",
    "Belt": "belts",
}


def get_mod_stat_text_raw_by_id(mod_id):
    """
    Returns
    -------
    Union[None, str]
        The raw stat text for a given mod ID.

    Parameters
    ----------
    mod_id : str
        The ID of the mod to retrieve the raw stat text for.
    """
    params = {
        "action": "cargoquery",
        "format": "json",
        "limit": "500",
        "tables": "mods, mod_stats",
        "fields": "mods.stat_text_raw, mod_stats.min, mod_stats.max",
        "where": f'mods.id="{mod_id}"',
        "join_on": "mods._pageName=mod_stats._pageName",
        "formatversion": "latest",
    }
    headers = {"User-Agent": "ExileCraft/0.1.0"}
    req = httpx.get(POE_WIKI_API, headers=headers, params=params)
    res = req.json()
    return res.get("cargoquery", [{}])[0].get("title", {}).get("stat text raw", None)


def get_modifiers(item_classes):
    """
    Returns
    -------
    Union[List, List[Dict[str, str]], None]
        A list containing BeautifulSoup objects for each item class, representing the parsed HTML response from the respective URL.

    Parameters
    ----------
    item_classes : List[str]
        A list of item class strings for which the modifiers are to be retrieved.

    """
    soup_list = []
    for item_class in item_classes:
        url = f"https://www.poewiki.net/wiki/List_of_modifiers_for_{item_class}"
        response = httpx.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        soup_list.append(soup)
    return soup_list


# base_item_query_json = {
#     "action": "cargoquery",
#     "format": "json",
#     "limit": "500",
#     "tables": "items,",
#     "fields": "items.class_id=item_class, items.rarity_id=rarity, items.name=name, items.size_x=inventory_x_size, "
#     "items.size_y=inventory_y_size, items.is_in_game=is_in_game, items.drop_enabled=drop_enabled, "
#     "items.drop_level=drop_level, items.required_level=required_level, items.required_dexterity, "
#     "items.required_intelligence, items.required_strength, items.tags, items.metadata_id, items.influences, "
#     "items.is_fractured, items.is_synthesised, items.is_searing_exarch_item, items.is_eater_of_worlds_item, "
#     "items.is_veiled, items.is_replica, items.is_corrupted, items.is_unmodifiable, items.is_relic, "
#     "items.is_drop_restricted, items.inventory_icon, items.base_item_id",
#     "where": f"items.metadata_id={metadata_id}",
#     "utf8": 1,
#     "formatversion": "latest",
# }
