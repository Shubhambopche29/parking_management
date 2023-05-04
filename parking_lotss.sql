create database parkinglots_db;
use parkinglots_db;
CREATE TABLE IF NOT EXISTS parking_records
             (vehicle_number TEXT, vehicle_type TEXT, contact_number TEXT, ticket_number TEXT, entry_time TEXT, exit_time TEXT, total_cost REAL);
INSERT INTO parking_records (vehicle_number, vehicle_type, contact_number, ticket_number, entry_time, exit_time, total_cost) VALUES
('ABC123', 'Car', '9876543210', 'A1B2C3D4', '2022-01-01 09:00:00', '2022-01-01 10:30:00', 15),
('DEF456', 'Bike', '1234567890', 'E5F6G7H8', '2022-01-01 10:00:00', '2022-01-01 11:30:00', 10),
('GHI789', 'Truck', '9999999999', 'I9J8K7L6', '2022-01-01 11:00:00', '2022-01-01 13:30:00', 30),
('JKL012', 'Physically disabled', '1111111111', 'M0N1O2P3', '2022-01-01 12:00:00', '2022-01-01 14:30:00', 20),
('MNO345', 'Car', '2222222222', 'Q4R5S6T7', '2022-01-01 13:00:00', '2022-01-01 15:30:00', 20),
('PQR678', 'Bike', '3333333333', 'U8V9W0X1', '2022-01-01 14:00:00', '2022-01-01 16:30:00', 15),
('STU901', 'Truck', '4444444444', 'Y2Z3A4B5', '2022-01-01 15:00:00', '2022-01-01 18:30:00', 45),
('VWX234', 'Physically disabled', '5555555555', 'C6D7E8F9', '2022-01-01 16:00:00', '2022-01-01 19:30:00', 30),
('YZA567', 'Car', '6666666666', 'G0H1I2J3', '2022-01-01 17:00:00', '2022-01-01 20:30:00', 30),
('BCD890', 'Bike', '7777777777', 'K4L5M6N7', '2022-01-01 18:00:00', '2022-01-01 21:30:00', 25),
('EFG123', 'Truck', '8888888888', 'O8P9Q0R1', '2022-01-01 19:00:00', '2022-01-01 23:30:00', 60),
('HIJ456', 'Physically disabled', '9999999999', 'S2T3U4V5', '2022-01-01 20:00:00', '2022-01-02 01:30:00', 45);     


    
ALTER TABLE parking_records ADD total_vehicles INT;
select * from parking_records;
use parkinglots_db;
select * from parking_records;