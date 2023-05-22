create table stat_translation
(
    id     integer,
    ids    TEXT not null,
    hidden integer default 0,
    constraint stat_translation_pk
        primary key (id autoincrement)
);

