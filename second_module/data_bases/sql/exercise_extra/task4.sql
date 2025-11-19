-- Establezca quantity = 0 donde price <= 0
UPDATE shopping_cart_items
SET quantity = 0
WHERE product_id IN (
    SELECT id
    FROM products
    WHERE price <= 0
);

-- Aumente el price en 100 unidades para todos los productos cuando quantity sea menor a 10
UPDATE products
SET price = price + 100
WHERE id IN (
    SELECT product_id
    FROM shopping_cart_items
    WHERE quantity <= 10
);

-- Disminuya quantity en 1 para un product_id específico
UPDATE shopping_cart_items
SET quantity = quantity - 1
WHERE product_id = 1;

-- -- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
SELECT * FROM products ORDER BY id ASC LIMIT 10;
