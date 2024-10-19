CREATE TABLE persona(
cod_persona int primary key,
nombre varchar(70),
edad int,
cargo varchar(30)
);

CREATE TABLE pelicula(
cod_pelicula int primary key,
titulo varchar(100),
año int,
genero varchar(50),
recaudacion decimal(9,2)
);

CREATE TABLE interviene(
cod_persona int references persona (cod_persona),
cod_pelicula int references pelicula (cod_pelicula)
);