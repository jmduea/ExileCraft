create table crafting_project
(
    id                        INTEGER default ROWID not null,
    item_class_id             TEXT,
    rarity                    TEXT    default 'Normal',
    name                      TEXT,
    base_item_id              TEXT,
    quality                   INTEGER default 0,
    item_level                integer default 0,
    sockets                   TEXT,
    enchant                   TEXT,
    physical_damage_min       integer,
    physical_damage_max       integer,
    cold_damage_min           integer,
    cold_damage_max           integer,
    fire_damage_min           integer,
    fire_damage_max           integer,
    lightning_damage_min      integer,
    lightning_damage_max      integer,
    chaos_damage_min          integer,
    chaos_damage_max          integer,
    critical_strike_chance    integer,
    attacks_per_second        integer,
    requirements_level        integer,
    requirements_str          integer,
    requirements_dex          integer,
    requirements_int          integer,
    prefix_modifier_1         TEXT    default NULL  null on conflict replace,
    prefix_modifier_2         TEXT    default NULL  null on conflict replace,
    prefix_modifier_3         TEXT    default NULL  null on conflict replace,
    suffix_modifier_1         TEXT    default NULL  null on conflict replace,
    suffix_modifier_2         TEXT    default NULL  null on conflict replace,
    suffix_modifier_3         TEXT    default NULL  null on conflict replace,
    shaper_item               boolean default FALSE null on conflict replace,
    elder_item                boolean default FALSE null on conflict replace,
    hunter_item               boolean default FALSE null on conflict replace,
    redeemer_item             boolean default FALSE null on conflict replace,
    crusader_item             boolean default FALSE null on conflict replace,
    warlord_item              boolean default FALSE null on conflict replace,
    synthesis_item            boolean default FALSE null on conflict replace,
    implicits                 TEXT                  null on conflict replace,
    item_tags                 TEXT,
    properties_armour         integer,
    properties_evasion        integer,
    properties_energy_shield  integer,
    properties_movement_speed integer,
    properties_block          integer,
    properties_range          integer,
    constraint crafting_project_pk
        primary key (id),
    constraint crafting_projects_base_items_id_fk
        foreign key (base_item_id) references base_items,
    constraint crafting_projects_base_items_item_class_id_fk
        foreign key (item_class_id) references base_items (item_class_id),
    constraint crafting_projects_base_items_requirements_dexterity_fk
        foreign key (requirements_dex) references base_items (requirements_dexterity),
    constraint crafting_projects_base_items_requirements_intelligence_fk
        foreign key (requirements_int) references base_items (requirements_intelligence),
    constraint crafting_projects_base_items_requirements_level_fk
        foreign key (requirements_level) references base_items (requirements_level),
    constraint crafting_projects_base_items_requirements_strength_fk
        foreign key (requirements_str) references base_items (requirements_strength)
);

