class ModType:
    def __init__(self, mod_type_id, sell_price_types):
        self.mod_type_id = mod_type_id
        self.sell_price_types = sell_price_types

    def __repr__(self):
        return f"ModType(mod_type_id='{self.mod_type_id}', sell_price_types={self.sell_price_types})"
