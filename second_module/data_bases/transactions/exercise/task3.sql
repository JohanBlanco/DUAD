-- search path
SET search_path TO transactions, public;

-- Construya una transacción para realizar el retorno de un producto, que funcione de la siguiente manera:

BEGIN TRANSACTION;

--     Validar que la factura existe en la DB
IF NOT EXISTS (
    SELECT 1
    FROM Invoices
    WHERE id = 1
) THEN
    RAISE EXCEPTION 'invoice does not exist';
END IF;

--     Aumentar el stock del producto en la cantidad que se compró
UPDATE Products
SET units_in_stock = units_in_stock + 1
WHERE id = 1;

--     Actualizar la factura y marcarla como retornada.
UPDATE Invoices
SET status = 'returned'
WHERE id = 1;