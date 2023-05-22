create table allowed_tags
(
    id          INTEGER,
    fossil_id   INTEGER,
    allowed_tag TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

