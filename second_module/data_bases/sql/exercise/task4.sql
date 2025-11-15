-- Obtenga todos los productos almacenados
select * 
from products;

-- Obtenga todos los productos que tengan un precio mayor a 50000
select * 
from products
WHERE price > 50000;

-- Obtenga todas las compras de un mismo producto por id.
select *
from sales
where product_id = 1;
-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
select sum(total_by_product) as incomes
from (
    select product_id, sum(total_price) total_by_product
    from sales
    group by product_id
);

-- Obtenga todas las facturas realizadas por el mismo comprador
select *
from invoices
where buyer_email = 'buyer2@gmail.com';


-- Obtenga todas las facturas ordenadas por monto total de forma descendente
select *
from invoices
order by total desc;

-- Obtenga una sola factura por número de factura.
select *
from invoices
where invoice_number = '001';