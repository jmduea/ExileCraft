create table forbidden_tags
(
    id            INTEGER,
    fossil_id     INTEGER,
    forbidden_tag TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

