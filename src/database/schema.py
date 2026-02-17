SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER,
    height INTEGER,
    weight INTEGER
);

CREATE tABLE IF NOT EXISTS pokemon_stats (
    pokemon_id INTEGER PRIMARY KEY,
    hp INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    special_attack INTEGER NOT NULL,
    special_defense INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);

CREATE TABLE IF NOT EXISTS pokemon_types (
    pokemon_id INTEGER PRIMARY KEY,
    type_1 TEXT NOT NULL,
    type_2 TEXT,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);

CREATE TABLE IF NOT EXISTS type_chart (
    attacking_type TEXT NOT NULL,
    defending_type TEXT NOT NULL,
    multiplier DOUBLE NOT NULL,
    PRIMARY KEY (attacking_type, defending_type)
);
"""

DROP_SQL = """
DROP TABLE IF EXISTS type_chart;
DROP TABLE IF EXISTS pokemon_types;
DROP TABLE IF EXISTS pokemon_stats;
DROP TABLE IF EXISTS pokemon;
"""
