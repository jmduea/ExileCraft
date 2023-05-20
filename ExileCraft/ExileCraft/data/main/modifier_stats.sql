create table modifier_stats
(
    id          TEXT,
    min         integer,
    max         integer,
    modifier_id TEXT,
    constraint modifier_stats_modifiers_id_fk
        foreign key (modifier_id) references modifiers
);

