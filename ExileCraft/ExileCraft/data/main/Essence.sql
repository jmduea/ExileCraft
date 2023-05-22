create table Essence
(
    id                     TEXT,
    name                   TEXT,
    spawn_level_min        INTEGER,
    spawn_level_max        INTEGER,
    level                  INTEGER,
    item_level_restriction INTEGER,
    is_corruption_only     BOOLEAN,
    tier                   INTEGER,
    primary key (id)
);

