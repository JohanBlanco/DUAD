-- Un script que confirme la devolución del auto al completar el alquiler, 
-- colocando el auto como disponible y completando el estado del alquiler
UPDATE lyfter_car_rental.rents
set status  = 'Completed'
where car_id = 51 and user_id = 51 and rent_date = '2025-12-01';

UPDATE lyfter_car_rental.cars
set status  = 'available'
where id = 51;

