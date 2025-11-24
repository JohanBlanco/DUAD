
# SQL Queries with Instructions and Images

## 1. Obtenga todos los libros y sus autores
```sql
select *
from Books b
inner join Authors a
on b.Author = a.id;
```
![image0](outputs/image0.png)

## 2. Obtenga todos los libros que no tienen autor
```sql
select b.id, b.name
from Books b
left join Authors a
on b.Author = a.id
where a.id is NULL;
```
![image1](outputs/image1.png)

## 3. Obtenga todos los autores que no tienen libros
```sql
select a.id, a.name
from Authors a 
left join Books b
on b.Author = a.id
where b.id is NULL;
```
![image2](outputs/image2.png)

## 4. Obtenga todos los libros que han sido rentados en algún momento
```sql
select b.id, b.name
from Books b
join Rents r
on b.id = r.BookID
group by name;
```
![image3](outputs/image3.png)

## 5. Obtenga todos los libros que nunca han sido rentados
```sql
select b.id, b.name
from Books b
left join Rents r
on b.id = r.BookID
where r.id  is NULL
group by b.id;
```
![image4](outputs/image4.png)

## 6. Obtenga todos los clientes que nunca han rentado un libro
```sql
select *
from Customers
where id not in (
    select distinct CustomerID
    from Rents
);
```
![image5](outputs/image5.png)

## 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
```sql
select b.id, b.name, r.State
from Books b
join Rents r
on b.id = r.BookID
where r.State = 'Overdue';
```
![image6](outputs/image6.png)
