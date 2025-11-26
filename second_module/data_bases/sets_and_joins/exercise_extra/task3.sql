-- 3. Consulta con múltiples JOINS anidados
-- Genere un SELECT que devuelva lo siguiente:

--     Nombre del cliente
--     Nombre del libro
--     Nombre del autor
--     Estado del alquiler (Rents.State)

-- Debe manejar el caso en que un libro no tenga autor 

select c.Name Customer, b.Name Book, a.Name Author, r.State "Book's State"
from Customers c
join Rents r on c.id = r.CustomerID
join Books b on b.id = r.BookID
join Authors a on a.id = b.Author;