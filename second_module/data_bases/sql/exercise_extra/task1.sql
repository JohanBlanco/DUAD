DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS sales;
-- Cree la tabla categories con: id (PK autoincrement), name (UNIQUE, NOT NULL), description
CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT NOT NULL
);

-- Agregue a products la columna category_id (INTEGER, puede permitir NULL)
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    code VARCHAR(100) UNIQUE NOT NULL,
    price INTEGER NOT NULL,
    date_received DATE NOT NULL,
    brand VARCHAR(100) NOT NULL,
    category_id INTEGER,

    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Inserte al menos 3 filas en categories
INSERT INTO categories(name, description) VALUES('Fast Food', 'This category is for junk food');
INSERT INTO categories(name, description) VALUES('Healthy Food', 'This category is for healthy food');
INSERT INTO categories(name, description) VALUES('Beverage', 'This category is for any beverage');


-- Actualice algunos products asignándoles un category_id
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('H20', '001', 100000, '2025-11-09', 'Dos Pinos', NULL);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Coca Cola', '002', 200000, '2025-11-09', 'Coca Cola', NULL);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Pizza', '003', 30000, '2025-11-09', 'Dominos', NULL);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Hamburguer', '004', 40000, '2025-11-09', 'Burguer king', NULL);

UPDATE products SET category_id = 3 WHERE id = 1;
UPDATE products SET category_id = 3 WHERE id = 2;
UPDATE products SET category_id = 1 WHERE id = 3;
UPDATE products SET category_id = 1 WHERE id = 4;

-- Verifique con SELECT * FROM products (muestre id, product_name, price, quantity, category_id)
SELECT * FROM products;

