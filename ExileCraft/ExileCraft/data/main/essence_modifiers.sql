create table essence_modifiers
(
    id          INTEGER,
    essence_id  TEXT,
    item_class  TEXT,
    modifier_id TEXT,
    primary key (id autoincrement),
    foreign key (essence_id) references Essence,
    foreign key (modifier_id) references modifiers
);

