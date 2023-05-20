create table descriptions
(
    id          INTEGER,
    fossil_id   INTEGER,
    description TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

