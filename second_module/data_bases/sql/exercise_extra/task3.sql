-- Agregue a invoices las columnas phone (TEXT, puede ser NULL) y cashier_code (TEXT, por defecto 'N/A')
ALTER TABLE invoices 
ADD COLUMN phone TEXT;

ALTER TABLE invoices 
ADD COLUMN cashier_code TEXT DEFAULT 'N/A';

-- Actualice varias facturas asignando valores a phone y cashier_code
UPDATE invoices SET cashier_code = '0001' where id = 1;
UPDATE invoices SET phone = '' where id = 2;

-- Seleccione todas las facturas que tengan phone vacío o NULL
select * from invoices
where phone is NULL OR TRIM(phone) =  '';

-- Seleccione una sola factura por invoice_id
select * from invoices
where id = 1;