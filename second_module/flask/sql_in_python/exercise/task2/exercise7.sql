-- Un script que deshabilite un automovil del alquiler
UPDATE lyfter_car_rental.rents
set status  = 'Cancelled'
where car_id = 51 and status = 'Active';

UPDATE lyfter_car_rental.cars
set status  = 'unavailable'
where id = 51;