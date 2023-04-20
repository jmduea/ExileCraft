class ClusterJewelNotable:
    def __init__(self, notable_data):
        self.id = notable_data.get("id")
        self.jewel_stat = notable_data.get("jewel_stat")
        self.name = notable_data.get("name")
