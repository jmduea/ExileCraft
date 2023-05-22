create table forced_mods
(
    id         INTEGER,
    fossil_id  INTEGER,
    forced_mod TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

