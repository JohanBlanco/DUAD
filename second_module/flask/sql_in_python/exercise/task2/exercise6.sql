-- Un script que confirme la devolución del auto al completar el alquiler, 
-- colocando el auto como disponible y completando el estado del alquiler
UPDATE lyfter_car_rental.rents
set status  = 'Completed'
where id = 51;

UPDATE lyfter_car_rental.cars
set status  = 'available'
where id = 51;

