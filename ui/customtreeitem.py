

class TreeItem:
    def __init__(self, data, parent=None):
        self.parent_item = parent
        self.item_data = data
        self.child_items = []

    def append_child(self, child):
        self.child_items.append(child)

    def child(self, row):
        return self.child_items[row]

    def child_count(self):
        return len(self.child_items)

    def column_count(self):
        return len(self.item_data)

    def data(self, column):
        try:
            return self.item_data[column]
        except IndexError:
            return None

    def parent(self):
        return self.parent_item

    def row(self):
        if self.parent_item:
            return self.parent_item.child_items.index(self)
        return 0
