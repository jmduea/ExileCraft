create table translation
(
    id                  integer,
    stat_translation_id integer,
    condition_min       TEXT,
    condition_max       text,
    condition_negated   integer default 0,
    string              TEXT not null,
    format              TEXT not null,
    index_handlers      TEXT,
    constraint translation_pk
        primary key (id autoincrement),
    constraint translation_stat_translation_id_fk
        foreign key (stat_translation_id) references stat_translation
);

