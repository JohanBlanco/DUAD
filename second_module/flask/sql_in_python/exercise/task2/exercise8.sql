-- Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.

select c.make, c.model, c.year, c.status
from lyfter_car_rental.cars c
join lyfter_car_rental.rents r on c.id = r.car_id
where r.status = 'Active' and c.status = 'rented';

select c.make, c.model, c.year, c.status, r.id, r.status
from lyfter_car_rental.cars c
left join lyfter_car_rental.rents r on c.id = r.car_id
where r.id is NULL and c.status = 'available' or r.status != 'Active';