from modules.shared.caches.base_items_cache import BaseItemsCache
from modules.shared.caches.global_cache import GlobalCache
from .shared.caches.mod_list_cache import ModListCache
from .sim.crafting import CraftingManager


CRAFTING_MANAGER = CraftingManager(item=None)
BASE_ITEMS_CACHE = BaseItemsCache()
MOD_LIST_CACHE = ModListCache()
