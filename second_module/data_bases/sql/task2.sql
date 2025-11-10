DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS shopping_carts;
DROP TABLE IF EXISTS shopping_cart_items;
DROP TABLE IF EXISTS invoices;

CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    code VARCHAR(100) UNIQUE NOT NULL,
    price INTEGER NOT NULL,
    date_received DATE NOT NULL,
    brand VARCHAR(100) NOT NULL
);

CREATE TABLE shopping_carts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email VARCHAR(100) NOT NULL
);

CREATE TABLE shopping_cart_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    shopping_cart_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total INTEGER NOT NULL,

    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (shopping_cart_id) REFERENCES shopping_cart(id)
);

CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_id INTEGER UNIQUE NOT NULL,
    invoice_number VARCHAR(100) NOT NULL,
    purchease_date DATE NOT NULL,
    buyer_email VARCHAR(100) NOT NULL,
    total INTEGER NOT NULL,

    FOREIGN KEY (shopping_cart_id) REFERENCES shopping_cart(id)
);

INSERT INTO products(name, code, price,date_received, brand) VALUES('H20', '001', 100, '2025-11-09', 'Dos Pinos');
INSERT INTO products(name, code, price,date_received, brand) VALUES('Coca Cola', '002', 200, '2025-11-09', 'Coca Cola');
INSERT INTO products(name, code, price,date_received, brand) VALUES('Pizza', '003', 1000, '2025-11-09', 'Dominos');
INSERT INTO products(name, code, price,date_received, brand) VALUES('Hamburguer', '004', 100, '2025-11-09', 'Burguer king');

INSERT INTO shopping_carts(user_email) VALUES('buyer1@gmail.com');
INSERT INTO shopping_carts(user_email) VALUES('buyer2@gmail.com');

INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(1, 1, 2, 200);
INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(2, 1, 2, 400);
INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(3, 1, 2, 2000);
INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(4, 1, 2, 200);

INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(1, 2, 1, 100);
INSERT INTO shopping_cart_items(product_id, shopping_cart_id, quantity, total) VALUES(3, 2, 1, 1000);

INSERT INTO invoices(shopping_cart_id, invoice_number,purchease_date, buyer_email, total)
    VALUES(1, '001', '2025-11-09', 'buyer1@gmail.com', 2800);
INSERT INTO invoices(shopping_cart_id, invoice_number,purchease_date, buyer_email, total)
    VALUES(2, '002', '2025-11-09', 'buyer2@gmail.com', 1100);