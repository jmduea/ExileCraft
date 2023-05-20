create table mod_implicit_tags
(
    id     INTEGER,
    mod_id TEXT,
    tag    TEXT,
    primary key (id),
    foreign key (mod_id) references modifiers
);

