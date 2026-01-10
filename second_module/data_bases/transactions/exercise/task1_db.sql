-- Plantee una base de datos simple con productos, usuarios y facturas.
-- Agregue todas las columnas necesarias para realizar las tareas planteadas.


CREATE TABLE transactions.Users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE transactions.Products (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    units_in_stock INT DEFAULT 0 NOT NULL
);

CREATE TABLE transactions.Invoices (
    id SERIAL PRIMARY KEY,
    description VARCHAR(500),
    status VARCHAR(50) NOT NULL,

    user_id BIGINT FOREIGN KEY REFERENCES transactions.Users(id)
);

CREATE TABLE transactions.Sales (
    id SERIAL PRIMARY KEY,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,

    product_id BIGINT FOREIGN KEY REFERENCES transactions.Products(id),
    invoice_id BIGINT FOREIGN KEY REFERENCES transactions.Invoice(id),
    user_id BIGINT FOREIGN KEY REFERENCES transactions.Users(id)
);