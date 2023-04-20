class HeistEquipment:
    def __init__(self, ids, conditions, formats, index_handlers, strings):
        self.ids = ids
        self.conditions = conditions
        self.formats = formats
        self.index_handlers = index_handlers
        self.strings = strings

    def __repr__(self):
        return f"HeistEquipment(ids={self.ids}, conditions={self.conditions}, formats={self.formats}," \
               f" index_handlers={self.index_handlers}, strings={self.strings})"
