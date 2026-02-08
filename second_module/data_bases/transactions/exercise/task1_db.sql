-- search path
SET search_path TO transactions, public;

-- Plantee una base de datos simple con productos, usuarios y facturas.
-- Agregue todas las columnas necesarias para realizar las tareas planteadas.


CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    units_in_stock INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE Invoices (
    id SERIAL PRIMARY KEY,
    description VARCHAR(500),
    status VARCHAR(50) NOT NULL,
    user_id INTEGER NOT NULL REFERENCES Users(id)
);

CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,
    quantity INTEGER NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    product_id INTEGER NOT NULL REFERENCES Products(id),
    invoice_id INTEGER NOT NULL REFERENCES Invoices(id),
    user_id INTEGER NOT NULL REFERENCES Users(id)
);
