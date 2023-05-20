create table alias
(
    id          INTEGER,
    stat_id     INTEGER,
    alias_key   TEXT,
    alias_value TEXT,
    primary key (id autoincrement),
    foreign key (stat_id) references stats
);

