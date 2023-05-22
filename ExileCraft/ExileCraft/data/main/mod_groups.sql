create table mod_groups
(
    id         INTEGER,
    mod_id     TEXT,
    group_name TEXT,
    primary key (id),
    foreign key (mod_id) references modifiers,
    constraint mod_groups_modifiers_type_fk
        foreign key (group_name) references modifiers (type)
);

