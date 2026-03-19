-- Parking Lot*******
-- *                *
-- *                *
--- *****************

-- SETUP:
-- Connect to the server (Azure Data Studio / Database extension/psql)
-- Create a database (I recommend chinook_pg)
-- Execute the Chinook database (from the Chinook_pg.sql file) to create Chinook resources in your server (I recommend doing this from psql)

-- Comment can be done single line with --
-- Comment can be done multi line with /* */

/*
DQL - Data Query Language
Keywords:

SELECT - retrieve data, select the columns from the resulting set
FROM - the table(s) to retrieve data from
WHERE - a conditional filter of the data
GROUP BY - group the data based on one or more columns
HAVING - a conditional filter of the grouped data
ORDER BY - sort the data
*/

SELECT * FROM actor;
SELECT last_name FROM actor;
SELECT * FROM actor WHERE first_name = 'Morgan';
select * from actor where first_name = 'John';

-- BASIC CHALLENGES
-- List all customers (full name, customer id, and country) who are not in the USA
SELECT
    first_name || ' ' || last_name AS "full name",
    customer_id AS "customer id",
    country
FROM customer
WHERE country != 'USA'; 

-- List all customers from Brazil
SELECT
    first_name || ' ' || last_name AS "full name",
    customer_id AS "customer id",
    country
FROM customer
WHERE country = 'Brazil'; 

-- List all sales agents
SELECT
    first_name || ' ' || last_name AS "full name",
    title
FROM employee
WHERE title LIKE '%Sales%Agent%';

-- Retrieve a list of all countries in billing addresses on invoices
SELECT DISTINCT billing_country FROM invoice;

-- Retrieve how many invoices there were in 2009, and what was the sales total for that year?
SELECT COUNT(*), SUM(total) FROM invoice
WHERE EXTRACT(YEAR FROM invoice_date) = 2009

-- (challenge: find the invoice count sales total for every year using one query)
SELECT COUNT(*), SUM(total), EXTRACT(YEAR FROM invoice_date) FROM invoice
GROUP BY EXTRACT(YEAR FROM invoice_date);

-- how many line items were there for invoice #37
SELECT COUNT(*) FROM invoice_line
WHERE invoice_id = 37;

-- how many invoices per country? BillingCountry  # of invoices -
-- Retrieve the total sales per country, ordered by the highest total sales first.
SELECT COUNT(*), billing_country FROM invoice
GROUP BY billing_country;


-- JOINS CHALLENGES
-- Every Album by Artist
SELECT album.title, artist.name FROM album
JOIN artist on album.artist_id = artist.artist_id;

-- (inner keyword is optional for inner join)
-- All songs of the rock genre
SELECT track.name, genre.name FROM track
JOIN genre ON genre.genre_id = track.genre_id
WHERE genre.name = 'Rock';

-- Show all invoices of customers from brazil (mailing address not billing)
SELECT * FROM invoice i
JOIN customer c ON c.customer_id = i.customer_id
WHERE c.country = 'Brazil';

-- Show all invoices together with the name of the sales agent for each one
SELECT *, e.first_name || ' ' || e.last_name AS "Sales Rep" FROM invoice i
JOIN customer c ON i.customer_id = c.customer_id
JOIN employee e ON e.employee_id = c.support_rep_id;

-- Which sales agent made the most sales in 2009?
SELECT e.first_name || ' ' || e.last_name AS "Sales Rep", SUM(total) as sum_total FROM invoice i
JOIN customer c ON i.customer_id = c.customer_id
JOIN employee e ON e.employee_id = c.support_rep_id
WHERE EXTRACT(YEAR FROM i.invoice_date) = 2009
GROUP BY e.employee_id
ORDER BY sum_total DESC
LIMIT(1);

-- How many customers are assigned to each sales agent?
SELECT e.first_name || ' ' || e.last_name AS "Sales Rep", COUNT(*) FROM customer c
JOIN employee e ON c.support_rep_id = e.employee_id
GROUP BY e.employee_id;

-- Which track was purchased the most in 2010?
SELECT track.name, SUM(quantity) AS total FROM invoice_line
JOIN track ON invoice_line.track_id = track.track_id
JOIN invoice ON invoice.invoice_id = invoice_line.invoice_id
WHERE EXTRACT(YEAR FROM invoice.invoice_date) = 2010
GROUP BY track.name
ORDER BY total DESC, track.name ASC
LIMIT(1);

-- Show the top three best selling artists.
SELECT ar.name, SUM(i.quantity) FROM invoice_line i
JOIN track t ON i.track_id = t.track_id
JOIN album al ON t.album_id = al.album_id
JOIN artist ar ON al.artist_id = ar.artist_id
GROUP BY ar.name
ORDER BY SUM(i.quantity) DESC;

-- Which customers have the same initials as at least one other customer?
-- SELECT c1.customer_id, c2.customer_id, COUNT(*) FROM customer c1
-- JOIN customer c2 ON c1.customer_id = c2.customer_id
-- WHERE SUBSTRING(c1.first_name, 1, 1) = SUBSTRING(c2.first_name, 1, 1)
-- AND SUBSTRING(c1.last_name, 1, 1) = SUBSTRING(c2.last_name, 1, 1);

-- Which countries have the most invoices?


-- Which city has the customer with the highest sales total?


-- Who is the highest spending customer?


-- Return the email and full name of of all customers who listen to Rock.


-- Which artist has written the most Rock songs?


-- Which artist has generated the most revenue?




-- ADVANCED CHALLENGES
-- solve these with a mixture of joins, subqueries, CTE, and set operators.
-- solve at least one of them in two different ways, and see if the execution
-- plan for them is the same, or different.

-- 1. which artists did not make any albums at all?


-- 2. which artists did not record any tracks of the Latin genre?


-- 3. which video track has the longest length? (use media type table)


-- 4. boss employee (the one who reports to nobody)


-- 5. how many audio tracks were bought by German customers, and what was
--    the total price paid for them?


-- 6. list the names and countries of the customers supported by an employee
--    who was hired younger than 35.


-- DML exercises

-- 1. insert two new records into the employee table.


-- 2. insert two new records into the tracks table.


-- 3. update customer Aaron Mitchell's name to Robert Walter


-- 4. delete one of the employees you inserted.


-- 5. delete customer Robert Walter.
