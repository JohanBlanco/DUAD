-- 2. Agrupamiento y conteo cruzado
-- Usando las tablas de Books, Customers y Rents:

--     Obtenga el número total de veces que cada cliente ha rentado un libro
select c.id, c.Name, COUNT(r.CustomerID) 'Number of Rents'
from Customers c
left join Rents r
on c.id = r.CustomerID
group by c.id;

--     Ordene de mayor a menor y limite el resultado a los 3 clientes más activos
select c.id, c.Name, COUNT(r.CustomerID) number_of_rents
from Customers c
left join Rents r
on c.id = r.CustomerID
group by c.id
order by number_of_rents desc
limit 3;

-- Debe usar: GROUP BY, COUNT(), ORDER BY, LIMIT