class StatTranslation:
    def __init__(self, condition, format_, index_handlers, string):
        self.condition = condition
        self.format = format_
        self.index_handlers = index_handlers
        self.string = string

    def __repr__(self):
        return f"StatTranslation(condition={self.condition}, format={self.format}, index_handlers={self.index_handlers}, string='{self.string}')"
