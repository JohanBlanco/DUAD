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
WITH new_invoice AS (
    INSERT INTO Invoices (description, status, user_id)
    VALUES ('Compra', 'pendiente', 1)
    RETURNING id
)

INSERT INTO Sales (quantity, total_price, product_id, invoice_id, user_id)
SELECT 1, 1000, 1, id, 1
FROM new_invoice;

--     Reducir el stock del producto
UPDATE Products
SET units_in_stock = units_in_stock - 1
WHERE id = 1;

COMMIT;

-- CONTINUAR CON ESTA CORRECCION
-- Ventas: Nota que en tu transacción de compra creas la factura,
-- pero la tabla Sales (donde debería quedar registrado qué producto
-- se vendió y a qué precio) no recibe ningún dato. Para que la
-- transacción sea completa según el modelo que planteaste, 
-- ¿cómo podrías insertar el registro en Sales asegurándote de usar 
-- el mismo ID de la factura que se acaba de generar?