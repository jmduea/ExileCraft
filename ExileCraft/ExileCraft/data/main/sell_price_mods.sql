create table sell_price_mods
(
    id             INTEGER,
    fossil_id      INTEGER,
    sell_price_mod TEXT,
    primary key (id autoincrement),
    foreign key (fossil_id) references fossils
);

