class StatTranslation:
    def __init__(self, ids, condition, format_, index_handlers, string):
        self.ids = ids
        self.condition = condition
        self.format = format_
        self.index_handlers = index_handlers
        self.string = string

    def __repr__(self):
        return f"StatTranslation(ids={self.ids}, condition={self.condition}, format={self.format}," \
               f" index_handlers={self.index_handlers}, string='{self.string}')"
