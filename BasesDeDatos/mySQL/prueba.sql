# El hastag se usa para comentar una sola límea
/*
Se usa para comentar varias
líneas y no tener que estar poniendo mucos hastags.
*/
-- Tanbién sirve para comentar una sola línea
DROP DATABASE IF EXISTS personaPerro;
CREATE DATABASE personaPerro CHARACTER SET utf8mb4;
USE personaPerro;

CREATE TABLE persona(
dni varchar(9) PRIMARY KEY,
nombre varchar(50),
edad INT
);

CREATE TABLE perro(
cod INT PRIMARY KEY,
nombre varchar (20),
raza varchar (20),
dni varchar (9) REFERENCES persona (dni)
);

INSERT INTO persona VALUES ("31021118Y", "Samuel", 20)
;

INSERT INTO perro VALUES ("", "Irina", "desconocido", "31021118Y")
;

# UPDATE persona SET edad=21 WHERE nombre like "Samuel"

DELETE FROM persona WHERE edad=20

/*ALTER TABLE persona ADD apellido varchar(100);
ALTER TABLE persona MODIFY nombre varchar(75);
ALTER TABLE persona DROP edad;
*/

# SELECT * from resultado
# select descripcion from resultado
# select distinct * from resultado
# desc resultado
