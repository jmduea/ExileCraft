create table fossils
(
    id                       INTEGER,
    fossil_key               TEXT,
    changes_quality          BOOLEAN,
    corrupted_essence_chance REAL,
    enchants                 BOOLEAN,
    mirrors                  BOOLEAN,
    name                     TEXT,
    rolls_lucky              BOOLEAN,
    rolls_white_sockets      BOOLEAN,
    primary key (id autoincrement),
    unique (fossil_key)
);

