-- Cree la tabla categories con: id (PK autoincrement), name (UNIQUE, NOT NULL), description
CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT NOT NULL
);

-- Agregue a products la columna category_id (INTEGER, puede permitir NULL)
ALTER TABLE products 
ADD COLUMN category_id INTEGER REFERENCES categories(id);

-- -- Inserte al menos 3 filas en categories
INSERT INTO categories(name, description) VALUES('Fast Food', 'This category is for junk food');
INSERT INTO categories(name, description) VALUES('Healthy Food', 'This category is for healthy food');
INSERT INTO categories(name, description) VALUES('Beverage', 'This category is for any beverage');

-- -- Actualice algunos products asignándoles un category_id
UPDATE products SET category_id = 3 WHERE id = 1;
UPDATE products SET category_id = 3 WHERE id = 2;
UPDATE products SET category_id = 1 WHERE id = 3;
UPDATE products SET category_id = 1 WHERE id = 4;

-- -- Verifique con SELECT * FROM products (muestre id, product_name, price, quantity, category_id)
SELECT * FROM products;

