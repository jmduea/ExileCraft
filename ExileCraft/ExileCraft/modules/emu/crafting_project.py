class CraftingProject:
    """
    The CraftingProject class represents a crafting project in the ExileCraft application.

    Each instance of this class represents a single crafting project, with various attributes
    that describe the specifics of the project, such as the item's class ID, its rarity, name,
    base item ID, quality, item level, sockets, enchant, damage ranges, critical strike chance,
    attacks per second, requirements, modifiers, item attributes, and tags.

    Attributes:
        id (int): The ID of the crafting project.
        item_class_id (str): The class ID of the item.
        rarity (str): The rarity of the item.
        name (str): The name of the item.
        base_item_id (str): The ID of the base item.
        quality (int): The quality of the item.
        item_level (int): The level of the item.
        sockets (str): The sockets of the item.
        enchant (str): The enchant of the item.
        physical_damage_min (int): The minimum local physical damage of the item.
        physical_damage_max (int): The maximum local physical damage of the item.
        cold_damage_min (int): The minimum local cold damage of the item.
        cold_damage_max (int): The maximum local cold damage of the item.
        fire_damage_min (int): The minimum local fire damage of the item.
        fire_damage_max (int): The maximum local fire damage of the item.
        lightning_damage_min (int): The minimum local lightning damage of the item.
        lightning_damage_max (int): The maximum local lightning damage of the item.
        chaos_damage_min (int): The minimum local chaos damage of the item.
        chaos_damage_max (int): The maximum local chaos damage of the item.
        critical_strike_chance (int): The base critical strike chance of the item.
        attacks_per_second (int): The attack speed of the item.
        requirements_level (int): The level requirement of the item.
        requirements_str (int): The strength attribute requirements of the item.
        requirements_dex (int): The dexterity attribute requirements of the item.
        requirements_int (int): The intelligence attribute requirements of the item.
        prefix_modifier_1 (str): The first prefix modifier of the item.
        prefix_modifier_2 (str): The second prefix modifier of the item.
        prefix_modifier_3 (str): The third prefix modifier of the item.
        suffix_modifier_1 (str): The first suffix modifier of the item.
        suffix_modifier_2 (str): The second suffix modifier of the item.
        suffix_modifier_3 (str): The third suffix modifier of the item.
        shaper_item (bool): Indicates whether the item is a shaper item.
        elder_item (bool): Indicates whether the item is an elder item.
        hunter_item (bool): Indicates whether the item is a hunter item.
        redeemer_item (bool): Indicates whether the item is a redeemer item.
        crusader_item (bool): Indicates whether the item is a crusader item.
        warlord_item (bool): Indicates whether the item is a warlord item.
        synthesis_item (bool): Indicates whether the item is a synthesis item.
        implicits (str): The implicit(s) of the item.
        item_tags (str): All applicable tags of the item used to determine the modifiers available.
        properties_armour (int): The total armour stat of the item.
        properties_evasion (int): The total evasion stat of the item.
        properties_energy_shield (int) The total energy shield stat of the item.
        properties_movement_speed (int) The total movement speed % of the item.  # TODO: remove? falls under implicits
        properties_block (int) The total base % block chance of the item.
        properties_range (int) The total weapon range of the item.
    """
    def __init__(self, data):
        self.id = data['id']
        self.item_class = data['item_class']
        self.rarity = data['rarity']
        self.name = data['name']
        self.base_item_id = data['base_item_id']
        self.quality = data['quality']
        self.item_level = data['item_level']
        self.sockets = data['sockets']
        self.enchant = data['enchant']
        self.physical_damage_min = data['physical_damage_min']
        self.physical_damage_max = data['physical_damage_max']
        self.cold_damage_min = data['cold_damage_min']
        self.cold_damage_max = data['cold_damage_max']
        self.fire_damage_min = data['fire_damage_min']
        self.fire_damage_max = data['fire_damage_max']
        self.lightning_damage_min = data['lightning_damage_min']
        self.lightning_damage_max = data['lightning_damage_max']
        self.chaos_damage_min = data['chaos_damage_min']
        self.chaos_damage_max = data['chaos_damage_max']
        self.critical_strike_chance = data['critical_strike_chance']
        self.attacks_per_second = data['attacks_per_second']
        self.requirements_level = data['requirements_level']
        self.requirements_str = data['requirements_str']
        self.requirements_dex = data['requirements_dex']
        self.requirements_int = data['requirements_int']
        self.prefix_modifier_1 = data['prefix_modifier_1']
        self.prefix_modifier_2 = data['prefix_modifier_2']
        self.prefix_modifier_3 = data['prefix_modifier_3']
        self.suffix_modifier_1 = data['suffix_modifier_1']
        self.suffix_modifier_2 = data['suffix_modifier_2']
        self.suffix_modifier_3 = data['suffix_modifier_3']
        self.shaper_item = data['shaper_item']
        self.elder_item = data['elder_item']
        self.hunter_item = data['hunter_item']
        self.redeemer_item = data['redeemer_item']
        self.crusader_item = data['crusader_item']
        self.warlord_item = data['warlord_item']
        self.synthesis_item = data['synthesis_item']
        self.implicits = data['implicits']
        self.item_tags = data['item_tags']
        self.properties_armour = data['properties_armour']
        self.properties_evasion = data['properties_evasion']
        self.properties_energy_shield = data['properties_energy_shield']
        self.properties_ward = data['properties_ward']
        self.properties_movement_speed = data['properties_movement_speed']
        self.properties_block = data['properties_block']
        self.properties_range = data['properties_range']

    def __str__(self):
        return f"CraftingProject(id={self.id}, item_class={self.item_class}, rarity={self.rarity}," \
               f" name={self.name}, base_item_id={self.base_item_id}, quality={self.quality}," \
               f" item_level={self.item_level}, sockets={self.sockets}, enchant={self.enchant}," \
               f" physical_damage_min={self.physical_damage_min}, physical_damage_max={self.physical_damage_max}," \
               f" cold_damage_min={self.cold_damage_min}, cold_damage_max={self.cold_damage_max}," \
               f" fire_damage_min={self.fire_damage_min}, fire_damage_max={self.fire_damage_max}," \
               f" lightning_damage_min={self.lightning_damage_min}, lightning_damage_max={self.lightning_damage_max}," \
               f" chaos_damage_min={self.chaos_damage_min}, chaos_damage_max={self.chaos_damage_max}," \
               f" critical_strike_chance={self.critical_strike_chance}, attacks_per_second={self.attacks_per_second}," \
               f" requirements_level={self.requirements_level}, requirements_str={self.requirements_str}," \
               f" requirements_dex={self.requirements_dex}, requirements_int={self.requirements_int}," \
               f" prefix_modifier_1={self.prefix_modifier_1}, prefix_modifier_2={self.prefix_modifier_2}," \
               f" prefix_modifier_3={self.prefix_modifier_3}, suffix_modifier_1={self.suffix_modifier_1}," \
               f" suffix_modifier_2={self.suffix_modifier_2}, suffix_modifier_3={self.suffix_modifier_3}," \
               f" shaper_item={self.shaper_item}, elder_item={self.elder_item}, hunter_item={self.hunter_item}," \
               f" redeemer_item={self.redeemer_item}, crusader_item={self.crusader_item}," \
               f" warlord_item={self.warlord_item}," \
               f" synthesis_item={self.synthesis_item}, implicits={self.implicits}, item_tags={self.item_tags}," \
               f" properties_armour={self.properties_armour}, properties_evasion={self.properties_evasion}," \
               f" properties_energy_shield={self.properties_energy_shield}," \
               f" properties_ward={self.properties_ward}," \
               f" properties_movement_speed={self.properties_movement_speed}," \
               f" properties_block={self.properties_block}, properties_range={self.properties_range})"

