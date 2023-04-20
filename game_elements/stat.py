class Stat:
    def __init__(self, key, alias, is_aliased, is_local):
        self.key = key
        self.alias = alias
        self.is_aliased = is_aliased
        self.is_local = is_local

    def __repr__(self):
        return f"Stat(key={self.key}, alias={self.alias}, is_aliased={self.is_aliased}, is_local={self.is_local})"
