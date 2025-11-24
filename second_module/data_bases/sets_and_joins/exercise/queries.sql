-- Obtenga todos los libros y sus autores
select *
from Books b
inner join Authors a
on b.Author = a.id;

-- Obtenga todos los libros que no tienen autor
select b.id, b.name
from Books b
left join Authors a
on b.Author = a.id
where a.id is NULL;

-- Obtenga todos los autores que no tienen libros
select a.id, a.name
from Authors a 
left join Books b
on b.Author = a.id
where b.id is NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
select b.id, b.name
from Books b
join Rents r
on b.id = r.BookID
group by name;

-- Obtenga todos los libros que nunca han sido rentados
select b.id, b.name
from Books b
left join Rents r
on b.id = r.BookID
where r.id  is NULL
group by b.id;

-- Obtenga todos los clientes que nunca han rentado un libro
select *
from Customers
where id not in (
    select distinct CustomerID
    from Rents
);

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
select b.id, b.name, r.State
from Books b
join Rents r
on b.id = r.BookID
where r.State = 'Overdue';