create table modifiers
(
    id                 TEXT null on conflict replace,
    name               TEXT,
    required_level     INTEGER,
    domain             TEXT,
    generation_type    TEXT,
    is_essence_only    BOOLEAN,
    type               TEXT,
    stats              JSON,
    grants_effects     TEXT,
    adds_tags          TEXT,
    implicit_tags      TEXT,
    generation_weights JSON,
    spawn_weights      JSON,
    groups             TEXT,
    primary key (id)
);

