-- Inserte al menos 10 filas en products con product_name, price, quantity
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Big Cola', '005', 100000, '2025-11-09', 'Dos Pinos', 3);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Fanta Colita', '006', 200000, '2025-11-09', 'Coca Cola', 3);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Fabta Naranja', '007', 30000, '2025-11-09', 'Dominos', 3);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Fanta Uva', '008', 40000, '2025-11-09', 'Burguer king', 3);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Tropical Te de Apple', '009', 100000, '2025-11-09', 'Dos Pinos', 3);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Fiesta Fries', '010', 200000, '2025-11-09', 'Coca Cola', 1);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Burrito', '011', 30000, '2025-11-09', 'Dominos', 1);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Sandwich', '012', 40000, '2025-11-09', 'Burguer king', 1);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Chalupa', '013', 30000, '2025-11-09', 'Dominos', 1);
INSERT INTO products(name, code, price,date_received, brand, category_id) VALUES('Yuca Frita', '014', 40000, '2025-11-09', 'Burguer king', 1);

-- Seleccione todos los productos
select * from products;

-- Seleccione productos con price > 50000
select * from products
where price > 50000;

-- Seleccione productos cuyo product_name contenga la palabra “apple” usando LIKE
select * from products
where name like '%apple%';

-- Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5
SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;
