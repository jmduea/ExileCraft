class Essence:
    def __init__(self, data):
        self.item_level_restriction = data.get("item_level_restriction", 0)
        self.level = data.get("level", 0)
        self.mods = data.get("mods", {})
        self.name = data.get("name", "")
        self.spawn_level_max = data.get("spawn_level_max", 0)
        self.spawn_level_min = data.get("spawn_level_min", 0)
        self.type = EssenceType(data.get("type", {}))


class EssenceType:
    def __init__(self, data):
        self.is_corruption_only = data.get("is_corruption_only", False)
        self.tier = data.get("tier", 0)
