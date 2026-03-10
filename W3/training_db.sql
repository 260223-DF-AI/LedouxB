-- DDL - CREATE, DROP, ALTER

CREATE DATABASE IF NOT EXISTS training_db;

CREATE TABLE IF NOT EXISTS asssociates (
    associate_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
);

TRUNCATE TABLE associates;

/*
    DROP TABLE associates;
*/


-- DML - INSERT, UPDATE, DELETE, TRUNCATE(?) 

INSERT INTO associates
(first_name,last_name, email, hire_date)
VALUES
('Benjamin', 'Ledoux','benjamin728@revature.net', '2025-02-23'),
('McKenzie', 'Ferrari', 'mckenzie327@revature.net', DEFAULT);

SELECT * FROM associates;

ALTER TABLE associates ADD COLUMN department VARCHAR(50) NOT NULL DEFAULT 'Training';
ALTER TABLE associates ALTER COLUMN hire_date SET NOT NULL;
ALTER TABLE associates ALTER COLUMN email TYPE VARCHAR(115);

-- DML - UPDATE

-- UPDATE associates SET department = 'Training' WHERE associate_id=1;
-- UPDATE associates SET department = 'HR' WHERE associate_id=2;



SELECT * FROM associates;