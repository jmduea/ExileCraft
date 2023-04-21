class CostType:
    def __init__(self, cost_type_id, format_text, stat):
        self.id = cost_type_id
        self.format_text = format_text
        self.stat = stat

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id!r}, {self.format_text!r}, {self.stat!r})"
