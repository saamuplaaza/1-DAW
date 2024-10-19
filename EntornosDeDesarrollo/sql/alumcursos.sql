-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-11-2023 a las 19:24:37
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `alumcursos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `NUM_ALUMNO` smallint(6) NOT NULL,
  `COD_CURSO` smallint(6) DEFAULT NULL,
  `NOMBRE` varchar(25) DEFAULT NULL,
  `DIRECCION` varchar(25) DEFAULT NULL,
  `TLF` varchar(10) DEFAULT NULL,
  `NOTA1` decimal(3,1) DEFAULT NULL,
  `NOTA2` decimal(3,1) DEFAULT NULL,
  `NOTA3` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`NUM_ALUMNO`, `COD_CURSO`, `NOMBRE`, `DIRECCION`, `TLF`, `NOTA1`, `NOTA2`, `NOTA3`) VALUES
(1010, 10, 'JUAN GOMEZ MAR', 'TALAVERA', '645666777', '7.0', '6.0', '8.0'),
(1011, 11, 'MARIA GOMEZ ABRIL', 'TALAVERA', '788999000', '6.0', '7.0', '8.0'),
(1012, 12, 'ALBERTO SÁNCHEZ MORENO', 'TOLEDO', '639009988', '5.0', '7.0', '7.0'),
(1020, 20, 'PILAR RAMOS BERT', 'TALAVERA', '64444456', '5.0', '5.0', '7.0'),
(1021, 21, 'HILDA GARCÍA ROMERO', 'TALAVERA', '645789098', '7.0', '7.0', '4.0'),
(1030, 30, 'CARLOS RAMOS MARTÍN', 'OROPESA', '644554433', '3.0', '2.0', '4.0'),
(1031, 31, 'PABLO SOLIS CARRETERO', 'CALERUELA', '678876543', '7.0', '5.0', '9.0'),
(1112, 12, 'JUANA GIL TRABADO', 'TALAVERA', '925555555', '9.0', '5.0', '4.0'),
(1120, 20, 'MARTA SERRANO SUELA', 'TALAVERA', '63344996', '6.0', '9.0', '6.0'),
(1121, 21, 'ANTONI DE LAS HERAS', 'NAVALCÁN', '678097654', '8.0', '7.0', '4.0'),
(1130, 30, 'FERNANDO CORREGIDOR', 'TALAVERA', '654332244', '4.0', '5.0', '9.0'),
(1131, 31, 'JOSE MARÍA MANZANO', 'GAMONAL', '645009988', '2.0', '5.0', '8.0'),
(1212, 12, 'RAMÓN GARCÍA PEREZ', 'TALAVERA', '639009988', '8.0', '7.0', '4.0'),
(1220, 20, 'MENODORA PANIAGUA', 'TALAVERA', '73344996', '4.0', '5.0', '8.0'),
(1221, 21, 'IVAN CARRASCO SOLA', 'TALAVERA', '777888999', '9.0', '5.0', '4.0'),
(1231, 31, 'FÁTIMA GARCÍA SÁNCHEZ', 'TALAVERA', '654009906', '6.0', '3.0', '4.0'),
(1321, 21, 'ALICIA MANZANO PEREZ', 'OROPESA', '234234567', '10.0', '5.0', '7.0'),
(1331, 31, 'JUAN PEDRO RIERA GRAU', 'OROPESA', '565443322', '9.0', '5.0', '4.0'),
(1521, 21, 'CRISTINA SABROSO FRAILE', 'TALAVERA', '639765432', '6.0', '9.0', '4.0'),
(1630, 30, 'ANTONIA GOMEZ SANCHEZ', 'TALAVERA', '645789099', '8.0', '8.0', '4.0'),
(2010, 10, 'ALBERTO RAMOS PEREZ', 'TOLEDO', '657777888', '5.0', '7.0', '6.0'),
(3010, 10, 'ANA MORENO GARCIA', 'TALAVERA', '925323456', '8.0', '9.0', '9.0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `COD_CURSO` smallint(6) NOT NULL,
  `DENOMINACION` varchar(10) DEFAULT NULL,
  `NOMBRECENTRO` varchar(25) DEFAULT NULL,
  `COSTE_MATRICULA` decimal(6,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`COD_CURSO`, `DENOMINACION`, `NOMBRECENTRO`, `COSTE_MATRICULA`) VALUES
(10, '1ESO', 'LA RONDA DEL CAÑILLO', '300'),
(11, '2ESO', 'LA RONDA DEL CAÑILLO', '350'),
(12, '3ESO', 'LA RONDA DEL CAÑILLO', '400'),
(20, '4ESO', 'LOS ALFAREROS', '300'),
(21, 'FPB', 'LOS ALFAREROS', '320'),
(30, '1BACH', 'LAS MENINAS', '500'),
(31, '2BACH', 'LAS MENINAS', '600');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`NUM_ALUMNO`),
  ADD KEY `SYSC0012206` (`COD_CURSO`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`COD_CURSO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `COD_CURSO` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `SYSC0012206` FOREIGN KEY (`COD_CURSO`) REFERENCES `cursos` (`COD_CURSO`) ON DELETE NO ACTION ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
