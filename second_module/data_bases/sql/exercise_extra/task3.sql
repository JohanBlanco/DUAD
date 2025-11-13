-- Agregue a invoices las columnas phone (TEXT, puede ser NULL) y cashier_code (TEXT, por defecto 'N/A')
CREATE TABLE invoices(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number VARCHAR(100) NOT NULL,
    purchease_date DATE NOT NULL,
    buyer_email VARCHAR(100) NOT NULL,
    total INTEGER NOT NULL,
    phone TEXT,
    cashier_code TEXT DEFAULT 'N/A'
);

-- Actualice varias facturas asignando valores a phone y cashier_code
INSERT INTO invoices(invoice_number,purchease_date, buyer_email, total, phone)
    VALUES('001', '2025-11-09', 'buyer1@gmail.com', 740000, NULL);

INSERT INTO invoices(invoice_number,purchease_date, buyer_email, total, phone)
    VALUES('002', '2025-11-09', 'buyer2@gmail.com', 130000, '88-88-88-88');

UPDATE invoices SET cashier_code = '0001' where id = 1;
UPDATE invoices SET phone = '' where id = 2;

-- Seleccione todas las facturas que tengan phone vacío o NULL
select * from invoices
where phone is NULL OR TRIM(phone) =  '';

-- Seleccione una sola factura por invoice_id
select * from invoices
where id = 1;