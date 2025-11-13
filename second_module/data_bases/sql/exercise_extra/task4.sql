CREATE TABLE sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    invoice_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_price INTEGER NOT NULL,

    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(1, 1, 2, 200000);
INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(2, 1, 2, 400000);
INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(3, 1, 2, 60000);
INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(4, 1, 2, 80000);

INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(1, 2, 1, 100000);
INSERT INTO sales(product_id, invoice_id, quantity, total_price) VALUES(3, 2, 1, 30000);

-- Establezca quantity = 0 donde price <= 0


-- Aumente el price en 100 unidades para todos los productos cuando quantity sea menor a 10


-- Disminuya quantity en 1 para un product_id específico


-- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10

