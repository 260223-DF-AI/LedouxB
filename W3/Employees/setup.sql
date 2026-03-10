-- Create database
CREATE DATABASE sql_practice;
\c sql_practice

-- Create tables
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

-- Insert sample data
INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'Building A', 500000),
('Sales', 'Building B', 300000),
('Marketing', 'Building C', 200000),
('HR', 'Building D', 150000);

INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id) VALUES
('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('Website Redesign', '2024-01-01', '2024-06-30', 50000, 3),
('Mobile App', '2024-02-15', '2024-12-31', 150000, 1),
('Sales Portal', '2024-03-01', '2024-09-30', 75000, 2),
('HR System', '2024-04-01', '2024-08-31', 40000, 4);


-- 1.1 Add Column
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);

-- 1.2 Modify Column
ALTER TABLE departments ALTER COLUMN budget TYPE DECIMAL(15,2); 

-- 1.3 Creat Table
CREATE TABLE training_courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_hours INT,
    instructor VARCHAR(100)
);

-- 2.1 INSERT Ops
INSERT INTO employees
(first_name, last_name, email, salary, dept_id)
VALUES
('Grace', 'Lee', 'grace.lee@company.com', 58000, 4),
('Ivan', 'Chen', 'ivan@company.com', 61000, 4),
('Julia', 'Kim', 'julia@company.com', 55000, 4);

-- 2.2 UPDATE Ops
UPDATE employees
SET salary = salary*1.1
WHERE dept_id = 1;

-- 2.3 DELETE Ops
DELETE FROM projects
WHERE end_date < CURRENT_DATE;

/*
DELETE FROM employees
WHERE department IS NULL;
*/

-- 3.1
SELECT * FROM employees
ORDER BY salary DESC;

-- 3.2
SELECT * FROM employees
WHERE dept_id = 1;

-- 3.3
SELECT * FROM employees
WHERE hire_date >= '2021-01-01';

-- 3.4
SELECT * FROM employees
WHERE salary BETWEEN 60000 AND 80000;

-- 3.5
SELECT * FROM employees
WHERE email LIKE '%company%';

-- 3.6
SELECT * FROM departments
WHERE location IN ('Building A', 'Building B');

-- 3.7
SELECT SUM(salary)
FROM employees
GROUP BY dept_id;

-- 3.8
SELECT AVG(salary)
FROM employees;

SELECT MIN(salary)
FROM employees;

SELECT MAX(salary)
FROM employees;

-- 3.9
SELECT * FROM (
    SELECT COUNT(*) AS total FROM employees
    GROUP BY dept_id
) sub
WHERE total >= 2;

-- 3.10
SELECT
    e.first_name || ' ' || e.last_name AS full_name,
    d.dept_name AS department,
    '$' || e.salary AS salary_formatted
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 4.1
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 4.2
SELECT * FROM departments d
JOIN projects p ON d.dept_id = p.dept_id
WHERE (SELECT COUNT(*) FROM projects GROUP BY p.dept_id) > 0;

-- 4.3
SELECT * FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE salary = (SELECT MAX(salary) FROM employees e2 WHERE e2.dept_id = d.dept_id
);

-- 4.4
SELECT 
    *,
    FLOOR((CURRENT_DATE - hire_date) / 30) AS months,
    FLOOR((CURRENT_DATE - hire_date) / 365) AS years
FROM employees;