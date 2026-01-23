-- search path
SET search_path TO transactions, public;

-- Construya una transacción para realizar una compra,
-- que debe funcionar de la siguiente manera:

BEGIN TRANSACTION;

--     Validar que existe stock del producto
IF EXISTS (
    SELECT 1
    FROM Products
    WHERE id = 1 AND units_in_stock < 1
) THEN
    RAISE EXCEPTION 'Product out of stock';
END IF;

--     Validar que el usuario existe
IF NOT EXISTS (
    SELECT 1
    FROM Users
    WHERE id = 1
) THEN
    RAISE EXCEPTION 'User does not exist';
END IF;

--     Crear la factura con el usuario relacionado
INSERT INTO Invoices(description, status, user_id)
VALUES ('Compra de producto', 'pendiente', 1);

--     Reducir el stock del producto
UPDATE Products
SET units_in_stock = units_in_stock - 1
WHERE id = 1;

COMMIT;