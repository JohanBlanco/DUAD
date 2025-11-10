select * from products;

select * from products
WHERE price > 50000;

select * from shopping_cart_items
where product_id = 1;

-- started creating the embeded query, to make it easier to understand, I know I dont need all the columns
select sum(total) total from (
    select product.id, sum(item.quantity) quantity, product.name, product.price, sum(item.total) total
    from shopping_cart_items as item
    inner join products as product
    where product.id = item.product_id
    group by product_id
);

select cart.user_email, invoice.id
from invoices as invoice
inner join shopping_carts as cart
where cart.id = invoice.shopping_cart_id;

select id, total
from invoices
order by total desc;

select *
from invoices
where id = 1;