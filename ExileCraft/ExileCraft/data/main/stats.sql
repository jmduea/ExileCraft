create table stats
(
    id         INTEGER,
    stat_key   TEXT,
    is_aliased BOOLEAN,
    is_local   BOOLEAN,
    primary key (id autoincrement),
    unique (stat_key)
);

