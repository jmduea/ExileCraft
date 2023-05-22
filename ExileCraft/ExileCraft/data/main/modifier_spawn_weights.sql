create table modifier_spawn_weights
(
    modifier_id TEXT,
    tag         TEXT,
    weight      INTEGER,
    constraint modifier_spawn_weights_modifiers_id_fk
        foreign key (modifier_id) references modifiers
);

