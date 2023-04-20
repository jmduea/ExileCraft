import json
from game_elements import (
    BaseItem, Tag, Stat, StatTranslation, Mod, ModType, ItemClass, HeistEquipment, Fossil, Essence, EssenceType,
    CraftingBenchOption, ClusterJewel, ClusterJewelNotable, AdvancedMod
)


def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


base_items_data = load_json_file('data/json/base_items.json')
base_items_objects = [BaseItem(item_data) for item_id, item_data in base_items_data.items()]

tags_data = load_json_file('data/json/tags.json')
tags = [Tag(name) for name in tags_data]

stats_data = load_json_file('data/json/stats.json')
stats = {key: Stat(key, data.get('alias', {}), data.get('is_aliased', False),
                   data.get('is_local', False)) for key, data in stats_data.items()}

stat_translations_data = load_json_file('data/json/stat_translations.json')
stat_translations = [StatTranslation(entry.get('condition', []), entry.get('format', []),
                                     entry.get('index_handlers', []),
                                     entry.get('string', '')) for entry in stat_translations_data]

mods_data = load_json_file('data/json/mods.json')
mods = {mod_id: Mod(mod_id, mod_info.get('adds_tags', []), mod_info.get('domain', ''),
                    mod_info.get('generation_type', ''), mod_info.get('generation_weights', []),
                    mod_info.get('grants_effects', []), mod_info.get('groups', []), mod_info.get('implicit_tags', []),
                    mod_info.get('is_essence_only', False), mod_info.get('name', ''), mod_info.get('required_level', 0),
                    mod_info.get('spawn_weights', []), mod_info.get('stats', []),
                    mod_info.get('type', '')) for mod_id, mod_info in mods_data.items()}

mod_types_data = load_json_file('data/json/mod_types.json')
mod_types = {mod_type_id: ModType(mod_type_id, mod_type_info.get('sell_price_types', [])) for mod_type_id, mod_type_info in mod_types_data.items()}

advanced_mod_data = load_json_file('data/json/advanced_mod.json')
advanced_mod_objects = [
    AdvancedMod(mod_data) for mod_data in advanced_mod_data
]

item_classes_data = load_json_file('data/json/item_classes.json')
item_classes = {item_class_id: ItemClass(item_class_id, item_class_info.get('name', '')) for item_class_id, item_class_info in item_classes_data.items()}

heist_equipment_data = load_json_file('data/json/heist_equipment.json')
heist_equipment_list = []
for equipment_data in heist_equipment_data:
    english_data = equipment_data.get('English', [])
    ids = equipment_data.get('ids', [])

    conditions = [entry.get('condition', []) for entry in english_data]
    formats = [entry.get('format', []) for entry in english_data]
    index_handlers = [entry.get('index_handlers', []) for entry in english_data]
    strings = [entry.get('string', '') for entry in english_data]

    heist_equipment = HeistEquipment(ids, conditions, formats, index_handlers, strings)
    heist_equipment_list.append(heist_equipment)

fossils_data = load_json_file('data/json/fossils.json')
fossils_objects = {fossil_id: Fossil(fossil_data) for fossil_id, fossil_data in fossils_data.items()}

flavour = load_json_file('data/json/flavour.json')

essences_data = load_json_file('data/json/essences.json')
essences_objects = {essence_id: Essence(essence_data) for essence_id, essence_data in essences_data.items()}

essence_types_data = load_json_file('data/json/essences.json')
essence_types = {essence_type_id: EssenceType(essence_type_data) for essence_type_id, essence_type_data in essence_types_data.items()}

crafting_bench_options_data = load_json_file('data/json/crafting_bench_options.json')
crafting_bench_options_objects = [CraftingBenchOption(option_data) for option_data in crafting_bench_options_data]

cluster_jewels_data = load_json_file('data/json/cluster_jewels.json')
cluster_jewels_objects = {
    jewel_id: ClusterJewel(jewel_data) for jewel_id, jewel_data in cluster_jewels_data.items()
}

cluster_jewel_notables_data = load_json_file('data/json/cluster_jewel_notables.json')
cluster_jewel_notables_objects = [
    ClusterJewelNotable(notable_data) for notable_data in cluster_jewel_notables_data
]



