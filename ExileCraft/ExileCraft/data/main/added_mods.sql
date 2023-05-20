create table added_mods
(
    id        INTEGER,
    fossil_id INTEGER,
    added_mod TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

