CREATE DATABASE StudentsDB;
USE StudentsDB;

CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    cgpa DECIMAL(4, 2) NOT NULL CHECK (cgpa >= 1 AND cgpa <= 4)
);

INSERT INTO student (id, name, age, cgpa)
VALUES
(22011942, 'Shahd Reda Farag', 20, 3.65),
(22010193, 'Karim Ahmed Khalil', 20, 3.43),
(22010082, 'Habeba Talaat Ahmed', 20, 3.47),
(22010271, 'Mona Adel Atteya', 21, 3.24),
(22010175, 'Amr Hussein Ismail', 20, 3.25);

SELECT * FROM student