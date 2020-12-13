DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS reservations;

CREATE TABLE flights (
  code TEXT UNIQUE PRIMARY KEY,
  departure TEXT NOT NULL,
  arrival TEXT NOT NULL,
  price TEXT NOT NULL
);

CREATE TABLE reservations (
  code TEXT,
  departure TEXT NOT NULL,
  arrival TEXT NOT NULL,
  price TEXT NOT NULL
);

INSERT INTO flights (code,departure,arrival,price) VALUES ('AF349','CDG','DXB','400');
INSERT INTO flights (code,departure,arrival,price) VALUES ('AF350','ORL','JFK','405');
INSERT INTO flights (code,departure,arrival,price) VALUES ('AF351','ORL','SIN','710');
INSERT INTO flights (code,departure,arrival,price) VALUES ('AF352','CDG','LHR','100');
INSERT INTO flights (code,departure,arrival,price) VALUES ('AF353','CDG','HKG','800');

