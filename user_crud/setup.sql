CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE vehicle_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);

INSERT INTO  user (
        first_name, 
        last_name, 
        hobbies
    ) VALUES (
        'John', 
        'Doe', 
        'Playing Tennis');


INSERT INTO  user (
        first_name,
        last_name,
        hobbies
    ) VALUES (
        'Jane',
        'Doe',
        'Playing Tennis');


INSERT INTO  user (
        first_name,
        last_name,
        hobbies
    ) VALUES (
        'Robert',
        'Martin',
        'Playing Tennis');

INSERT INTO vehicle_type (description) VALUES ('Car');
INSERT INTO vehicle_type (description) VALUES ('Truck');
INSERT INTO vehicle_type (description) VALUES ('SUV');
INSERT INTO vehicle_type (description) VALUES ('Motorcycle');
INSERT INTO vehicle_type (description) VALUES ('Bicycle');


INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "red",
    "hfg-456",
    1,
    1
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "blue",
    "pok-285",
    3,
    2
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "white",
    "nmt-490",
    3,
    3
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
) VALUES (
    "Yellow",
    "bym-271",
    2,
    3
);