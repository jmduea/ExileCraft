create table blocked_descriptions
(
    id                  INTEGER,
    fossil_id           INTEGER,
    blocked_description TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

