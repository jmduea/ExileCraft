from .shared.global_cache import GlobalCache
from .sim.crafting import CraftingManager

CACHE = GlobalCache()
CRAFTING_MANAGER = CraftingManager(item=None)
