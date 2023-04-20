class ItemClass:
    def __init__(self, item_class_id, name):
        self.item_class_id = item_class_id
        self.name = name

    def __repr__(self):
        return f"ItemClass(item_class_id='{self.item_class_id}', name='{self.name}')"
