from ExileCraft.databasehandler import tags_map

item_class_to_readable_name = {
  "AbyssJewel": {
    "name": "Abyss Jewels"
  },
  "Active Skill Gem": {
    "name": "Active Skill Gems"
  },
  "Amulet": {
    "name": "Amulets"
  },
  "ArchnemesisMod": {
    "name": "Archnemesis Mod"
  },
  "AtlasUpgradeItem": {
    "name": "Atlas Upgrade Items"
  },
  "Belt": {
    "name": "Belts"
  },
  "Body Armour": {
    "name": "Body Armours"
  },
  "Boots": {
    "name": "Boots"
  },
  "Bow": {
    "name": "Bows"
  },
  "Claw": {
    "name": "Claws"
  },
  "Currency": {
    "name": "Currency"
  },
  "DONOTUSE1": {
    "name": ""
  },
  "DONOTUSE2": {
    "name": ""
  },
  "DONOTUSE3": {
    "name": ""
  },
  "DONOTUSE4": {
    "name": ""
  },
  "DONOTUSE5": {
    "name": ""
  },
  "DONOTUSE6": {
    "name": ""
  },
  "DONOTUSE7": {
    "name": ""
  },
  "Dagger": {
    "name": "Daggers"
  },
  "DelveSocketableCurrency": {
    "name": "Delve Socketable Currency"
  },
  "DelveStackableSocketableCurrency": {
    "name": "Delve Stackable Socketable Currency"
  },
  "DivinationCard": {
    "name": "Divination Cards"
  },
  "ExpeditionLogbook": {
    "name": "Expedition Logbooks"
  },
  "FishingRod": {
    "name": "Fishing Rods"
  },
  "Gloves": {
    "name": "Gloves"
  },
  "HeistBlueprint": {
    "name": "Blueprints"
  },
  "HeistContract": {
    "name": "Contracts"
  },
  "HeistEquipmentReward": {
    "name": "Heist Brooches"
  },
  "HeistEquipmentTool": {
    "name": "Heist Tools"
  },
  "HeistEquipmentUtility": {
    "name": "Heist Cloaks"
  },
  "HeistEquipmentWeapon": {
    "name": "Heist Gear"
  },
  "HeistObjective": {
    "name": "Heist Targets"
  },
  "Helmet": {
    "name": "Helmets"
  },
  "HiddenItem": {
    "name": "Hidden Items"
  },
  "HideoutDoodad": {
    "name": "Hideout Doodads"
  },
  "HybridFlask": {
    "name": "Hybrid Flasks"
  },
  "Incubator": {
    "name": "Incubators"
  },
  "IncubatorStackable": {
    "name": "Incubators"
  },
  "IncursionItem": {
    "name": "Incursion Items"
  },
  "InstanceLocalItem": {
    "name": "Instance Local Item"
  },
  "Jewel": {
    "name": "Jewels"
  },
  "LabyrinthItem": {
    "name": "Labyrinth Items"
  },
  "LabyrinthMapItem": {
    "name": "Labyrinth Map Items"
  },
  "LabyrinthTrinket": {
    "name": "Labyrinth Trinkets"
  },
  "LargeRelic": {
    "name": "Large Relics"
  },
  "Leaguestone": {
    "name": "Leaguestones"
  },
  "LifeFlask": {
    "name": "Life Flasks"
  },
  "ManaFlask": {
    "name": "Mana Flasks"
  },
  "Map": {
    "name": "Maps"
  },
  "MapFragment": {
    "name": "Map Fragments"
  },
  "MediumRelic": {
    "name": "Medium Relics"
  },
  "MemoryLine": {
    "name": "Memory"
  },
  "MetamorphosisDNA": {
    "name": "Metamorph Samples"
  },
  "Microtransaction": {
    "name": "Microtransactions"
  },
  "MiscMapItem": {
    "name": "Misc Map Items"
  },
  "One Hand Axe": {
    "name": "One Hand Axes"
  },
  "One Hand Mace": {
    "name": "One Hand Maces"
  },
  "One Hand Sword": {
    "name": "One Hand Swords"
  },
  "PantheonSoul": {
    "name": "Pantheon Souls"
  },
  "QuestItem": {
    "name": "Quest Items"
  },
  "Quiver": {
    "name": "Quivers"
  },
  "Ring": {
    "name": "Rings"
  },
  "Rune Dagger": {
    "name": "Rune Daggers"
  },
  "Sceptre": {
    "name": "Sceptres"
  },
  "SentinelDrone": {
    "name": "Sentinel"
  },
  "Shield": {
    "name": "Shields"
  },
  "SmallRelic": {
    "name": "Small Relics"
  },
  "StackableCurrency": {
    "name": "Stackable Currency"
  },
  "Staff": {
    "name": "Staves"
  },
  "Support Skill Gem": {
    "name": "Support Skill Gems"
  },
  "Thrusting One Hand Sword": {
    "name": "Thrusting One Hand Swords"
  },
  "Trinket": {
    "name": "Trinkets"
  },
  "Two Hand Axe": {
    "name": "Two Hand Axes"
  },
  "Two Hand Mace": {
    "name": "Two Hand Maces"
  },
  "Two Hand Sword": {
    "name": "Two Hand Swords"
  },
  "Unarmed": {
    "name": ""
  },
  "UniqueFragment": {
    "name": "Pieces"
  },
  "UniqueShard": {
    "name": "Shards"
  },
  "UniqueShardBase": {
    "name": "Shard Hearts"
  },
  "UtilityFlask": {
    "name": "Utility Flasks"
  },
  "UtilityFlaskCritical": {
    "name": "Critical Utility Flasks"
  },
  "Wand": {
    "name": "Wands"
  },
  "Warstaff": {
    "name": "Warstaves"
  }
}


class Item:
    def __init__(self, item_data, db_handler):
        self.id = item_data[0]
        self.drop_level = item_data[1]
        self.implicits = item_data[2]
        self.inventory_height = item_data[3]
        self.inventory_width = item_data[4]
        self.item_class = item_data[5]
        self.name = item_data[6]
        self.tags = item_data[7]
        self.visual_identity_id = item_data[8]
        self.visual_identity_dds_file = item_data[9]
        self.requirements_strength = item_data[10]
        self.requirements_dexterity = item_data[11]
        self.requirements_intelligence = item_data[12]
        self.requirements_level = item_data[13]
        self.properties_armour = item_data[14]
        self.properties_evasion = item_data[15]
        self.properties_energy_shield = item_data[16]
        self.properties_movement_speed = item_data[17]
        self.properties_block = item_data[18]
        self.properties_life_per_use = item_data[19]
        self.properties_mana_per_use = item_data[20]
        self.properties_duration = item_data[21]
        self.properties_charges_max = item_data[22]
        self.properties_charges_per_use = item_data[23]
        self.properties_critical_strike_chance = item_data[24]
        self.properties_attack_time = item_data[25]
        self.properties_physical_damage_max = item_data[26]
        self.properties_physical_damage_min = item_data[27]
        self.properties_range = item_data[28]
        self.properties_stack_size = item_data[29]
        self.properties_stack_size_currency_tab = item_data[30]
        self.properties_directions = item_data[31]
        self.properties_description = item_data[32]
        self.properties_full_stack_turns_into = item_data[33]
        self.grants_buff_id = item_data[34]
        self.grants_buff_stats = item_data[35]
        self.domain = item_data[36]
        self.tag_ids = db_handler.get_tag_ids_for_item(self.id)
        self.tags_map = tags_map.get(self.item_class, {})

    def __repr__(self):
      return f"Item(id={self.id}, name={self.name}, item_class={self.item_class}, tag_ids={self.tag_ids}, tags_map={self.tags_map})"

    def __str__(self):
      return self.name

