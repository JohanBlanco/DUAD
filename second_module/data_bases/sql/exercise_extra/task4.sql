-- Establezca quantity = 0 donde price <= 0
select  prod.id product_id, prod.price price, 
        CASE WHEN prod.price <= 0 
                THEN 0
            ELSE
                item.quantity
        END AS quantity
from shopping_cart_items item
join products prod
where item.product_id = prod.id;

-- Aumente el price en 100 unidades para todos los productos cuando quantity sea menor a 10
select  prod.id product_id, prod.price price, item.quantity,
        CASE WHEN item.quantity <= 10
                THEN prod.price + 100
            ELSE
                prod.price
        END AS increassed_price
from shopping_cart_items item
join products prod
where item.product_id = prod.id;

-- Disminuya quantity en 1 para un product_id específico
select  prod.id product_id, item.quantity, (item.quantity - 1) decreassed_by_1_quantity
from shopping_cart_items item
join products prod
where item.product_id = prod.id and prod.id = 1;

-- Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10
SELECT * FROM products ORDER BY id ASC LIMIT 10;
