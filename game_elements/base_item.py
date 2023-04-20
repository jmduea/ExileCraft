class BaseItem:
    def __init__(self, data):
        self.id = data.get("id")
        self.domain = data.get("domain")
        self.drop_level = data.get("drop_level")
        self.implicits = data.get("implicits", [])
        self.inventory_height = data.get("inventory_height")
        self.inventory_width = data.get("inventory_width")
        self.item_class = data.get("item_class")
        self.name = data.get("name")
        self.properties = data.get("properties", {})
        self.release_state = data.get("release_state")
        self.requirements = data.get("requirements")
        self.tags = data.get("tags", [])
        self.visual_identity = data.get("visual_identity", {})

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.item_class!r})"
