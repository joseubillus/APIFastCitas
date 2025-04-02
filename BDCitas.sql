DROP DATABASE IF EXISTS BDCitas;
-- Crear base de datos
CREATE DATABASE BDCitas;
USE BDCitas;

-- Crear tabla Paciente
CREATE TABLE Paciente (
    id VARCHAR(50) PRIMARY KEY,
    nom VARCHAR(100),
    ape VARCHAR(100),
    tel INT,
    img VARCHAR(255)
);

-- Insertar 10 registros de ejemplo
INSERT INTO Paciente (id, nom, ape, tel, img) VALUES
('P001', 'Carlos', 'López', 5551234, 'img1.jpg'),
('P002', 'María', 'González', 5555678, 'img2.jpg'),
('P003', 'Luis', 'Martínez', 5558765, 'img3.jpg'),
('P004', 'Ana', 'Rodríguez', 5554321, 'img4.jpg'),
('P005', 'José', 'Pérez', 5559876, 'img5.jpg'),
('P006', 'Laura', 'Ramírez', 5556543, 'img6.jpg'),
('P007', 'Pedro', 'Torres', 5553210, 'img7.jpg'),
('P008', 'Lucía', 'Flores', 5551098, 'img8.jpg'),
('P009', 'Miguel', 'Sánchez', 5552134, 'img9.jpg'),
('P010', 'Sofía', 'Hernández', 5555467, 'img10.jpg');

SELECT * FROM Paciente;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(255) NOT NULL
);

INSERT INTO usuario (nombre_usuario, contrasena) VALUES
('jose', '123'),
('ana', '321'),
('luis789', '123');

SELECT * FROM usuario;