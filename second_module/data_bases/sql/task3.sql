ALTER TABLE invoices 
    ADD COLUMN buyer_phone CHAR(8) NOT NULL DEFAULT '';

ALTER TABLE invoices 
    ADD COLUMN cashier_code VARCHAR(50) NOT NULL DEFAULT '';
