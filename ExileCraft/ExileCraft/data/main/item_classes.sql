create table item_classes
(
    id   TEXT,
    name TEXT,
    constraint item_classes_pk
        primary key (id),
    constraint item_classes_base_items_item_class_id_fk
        foreign key (id) references base_items (item_class_id)
);

