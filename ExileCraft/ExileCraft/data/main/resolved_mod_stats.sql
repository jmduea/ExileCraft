create table resolved_mod_stats
(
    id                    INTEGER,
    mod_id                TEXT not null,
    stat_id               TEXT not null,
    min                   INTEGER,
    max                   INTEGER,
    stat_name             TEXT,
    translation_object_id INTEGER,
    translation_text      TEXT,
    primary key (id autoincrement),
    foreign key (mod_id) references modifiers,
    foreign key (stat_id) references stat_ids (stat_id),
    foreign key (translation_object_id) references translation_objects (id)
);

