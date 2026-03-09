CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    ISBN VARCHAR(13),
    price FLOAT(2),
    publication_date DATE,
    page_count INT,
    publisher_id INT REFERENCES publishers(id)
);

CREATE TABLE orders (
    id INT NOT NULL,
    customer_id INT,
    book_id INT NOT NULL,
    quantity INT,
    review VARCHAR(255),
    status VARCHAR(9),
    PRIMARY KEY(id, book_id)
);