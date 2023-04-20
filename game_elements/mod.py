class Mod:
    def __init__(self, mod_id, adds_tags, domain, generation_type, generation_weights, grants_effects, groups, implicit_tags, is_essence_only, name, required_level, spawn_weights, stats, mod_type):
        self.mod_id = mod_id
        self.adds_tags = adds_tags
        self.domain = domain
        self.generation_type = generation_type
        self.generation_weights = generation_weights
        self.grants_effects = grants_effects
        self.groups = groups
        self.implicit_tags = implicit_tags
        self.is_essence_only = is_essence_only
        self.name = name
        self.required_level = required_level
        self.spawn_weights = spawn_weights
        self.stats = stats
        self.type = mod_type

    def __repr__(self):
        return f"Mod(mod_id='{self.mod_id}', name='{self.name}', type='{self.type}', domain='{self.domain}', required_level={self.required_level})"
