create table modifier_grants_effects
(
    modifier_id       TEXT,
    granted_effect_id TEXT,
    level             INTEGER,
    foreign key (modifier_id) references modifiers
);

