create table modifier_generation_weights
(
    mod_id TEXT,
    tag_id TEXT,
    weight INTEGER,
    constraint modifier_generation_weights_modifiers_id_fk
        foreign key (mod_id) references modifiers
);

