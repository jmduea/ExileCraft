class CraftingBenchOption:
    def __init__(self, data):
        self.actions = data.get("actions", {})
        self.bench_tier = data.get("bench_tier", 0)
        self.cost = data.get("cost", {})
        self.item_classes = data.get("item_classes", [])
        self.master = data.get("master", "")
