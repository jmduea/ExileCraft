create table base_items
(
    metadata                          TEXT,
    drop_level                        INTEGER,
    implicits                         TEXT,
    item_class_id                     TEXT,
    name                              TEXT,
    tags                              TEXT,
    visual_identity_id                TEXT,
    visual_identity_dds_file          TEXT,
    requirements_strength             INTEGER,
    requirements_dexterity            INTEGER,
    requirements_intelligence         INTEGER,
    requirements_level                INTEGER,
    properties_armour                 INTEGER,
    properties_evasion                INTEGER,
    properties_energy_shield          INTEGER,
    properties_movement_speed         INTEGER,
    properties_block                  INTEGER,
    properties_life_per_use           INTEGER,
    properties_mana_per_use           INTEGER,
    properties_duration               INTEGER,
    properties_charges_max            INTEGER,
    properties_charges_per_use        INTEGER,
    properties_critical_strike_chance INTEGER,
    properties_attack_time            INTEGER,
    properties_physical_damage_max    INTEGER,
    properties_physical_damage_min    INTEGER,
    properties_range                  INTEGER,
    grants_buff_id                    TEXT,
    grants_buff_stats                 TEXT,
    domain                            TEXT,
    id                                integer,
    primary key (id autoincrement),
    foreign key (item_class_id) references item_classes,
    constraint base_items_modifiers_domain_fk
        foreign key (domain) references modifiers (domain)
);

create index base_items_item_class_id_tags_name_index
    on base_items (item_class_id, tags, name);

