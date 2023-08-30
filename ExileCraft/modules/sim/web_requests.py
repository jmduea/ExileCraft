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
import requests

MOD_STAT_INFO = """{{#cargo_query: tables=mods, mod_stats, mod_spawn_weights |fields=mod_stats.id, mods.domain, 
mods.generation_type, mods.mod_groups, mods.stat_text_raw, mods.tier_text, mods.id, mod_stats.min, mod_stats.max, 
mod_spawn_weights.tag, mod_spawn_weights.value, mod_spawn_weights.ordinal, mod_stats.min, mod_stats.max, 
mods.tier_text |where=(mods.domain=1 OR mods.domain=2 OR mods.domain=9 or mods.domain =10 or mods.domain=13 OR 
mods.domain=16 OR mods.domain=20 OR mods.domain=21 OR mods.domain=26 OR mods.domain=28) AND (mods.generation_type=1 
OR mods.generation_type=2 OR mods.generation_type=5 OR mods.generation_type=10 OR mods.generation_type=11 OR 
mods.generation_type=21 OR mods.generation_type=22 OR mods.generation_type=28 OR mods.generation_type=29) |join 
on=mods.id=mod_stats.id, mods.id=mod_spawn_weights._ID |limit=15000 |offset=0 |format=json }}"""

BASE_URL = "https://www.poewiki.net/w/api.php?action=cargoquery&format=json"
MOD_TABLE = "mods"
MOD_STAT_TEXT_RAW_FIELDS = "mods.id,mods.stat_text_raw"
MOD_GROUPS_STAT_TEXT_RAW_FIELDS = "mods.mod_groups,mods.stat_text_raw"
GROUP_BY_MOD_GROUPS = "mods.mod_groups"


def get_mod_stat_text_raw(mod_id: str) -> str:
    """
    Parameters
    ----------
    mod_id : str
        The ID of the mod for which to retrieve the raw stat text.

    Returns
    -------
    str
        The raw stat text of the specified mod. If an error occurs or the mod is not found, None is returned.

    """
    where = f"mods.id='{mod_id}'"
    query_url = (
        f"{BASE_URL}&tables={MOD_TABLE}&fields={MOD_STAT_TEXT_RAW_FIELDS}&where={where}"
    )
    response = requests.get(query_url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        if "cargoquery" in data:
            return data["cargoquery"][0]["title"]["stat text raw"]
        print("Error in response:", data)
    else:
        print(f"Error fetching data: {response.status_code}")
    return None


def get_mod_stat_text_raw_by_groups(mod_groups_key: str) -> dict:
    """
    Parameters
    ----------
    mod_groups_key : str
        The key to search for in the mod groups. It is used to narrow down the search results.

    Returns
    -------
    dict
        A dictionary containing the grouped statistics of the matching mod groups. The key of each entry in the dictionary represents the mod group, and the value is a list of stat text raw for that mod group.

    Raises
    ------
    None

    """
    where = f"mods.mod_groups LIKE '%{mod_groups_key}%'"
    query_url = (
        f"{BASE_URL}&tables={MOD_TABLE}&fields={MOD_GROUPS_STAT_TEXT_RAW_FIELDS}&where={where}&group_by"
        f"={GROUP_BY_MOD_GROUPS}"
    )
    response = requests.get(query_url)
    print(response)

    grouped_stats = {}

    if response.status_code == 200:
        data = response.json()
        if "cargoquery" in data:
            for item in data["cargoquery"]:
                group = item["title"]["mod_groups"]
                stat_text_raw = item["title"]["stat text raw"]
                if group not in grouped_stats:
                    grouped_stats[group] = []
                grouped_stats[group].append(stat_text_raw)
        else:
            print("Error in response:", data)
            return None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

    return grouped_stats


if __name__ == "__main__":
    mod_id = "ChanceToSuppressSpellsEldritchImplicit2"
    mod_groups_key = "ChanceToSuppressSpells"
    mod_id_stat_text_raw = get_mod_stat_text_raw(mod_id)
    mod_group_stat_text_raw = get_mod_stat_text_raw_by_groups(mod_groups_key)
    print(mod_id_stat_text_raw)
    print(mod_group_stat_text_raw)
