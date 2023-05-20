create table negative_mod_weights
(
    id        INTEGER,
    fossil_id INTEGER,
    tag       TEXT,
    weight    INTEGER,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

