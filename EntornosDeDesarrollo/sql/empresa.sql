-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-11-2023 a las 13:58:56
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
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `dept_no` int(11) NOT NULL,
  `dnombre` varchar(15) DEFAULT NULL,
  `loc` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`dept_no`, `dnombre`, `loc`) VALUES
(1, 'CONTABILIDAD', 'SEVILLA'),
(2, 'INVESTIGACIÓN', 'MADRID'),
(3, 'VENTAS', 'BARCELONA'),
(4, 'PRODUCCIÓN', 'BILBAO'),
(43, 'wrtwertwer', 'fhdfgh');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `emp_no` int(11) NOT NULL,
  `apellido` varchar(10) DEFAULT NULL,
  `oficio` varchar(10) DEFAULT NULL,
  `dir` int(11) DEFAULT NULL,
  `fecha_alt` date DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `comision` float DEFAULT NULL,
  `dept_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`emp_no`, `apellido`, `oficio`, `dir`, `fecha_alt`, `salario`, `comision`, `dept_no`) VALUES
(7369, 'SÁNCHEZ', 'EMPLEADO', 7902, '1990-12-17', 1040, NULL, 2),
(7499, 'ARROYO', 'VENDEDOR', 7698, '1990-02-20', 1500, 390, 3),
(7566, 'JIMÉNEZ', 'DIRECTOR', 7839, '1991-04-02', 2900, NULL, 2),
(7654, 'MARTÍN', 'VENDEDOR', 7698, '1991-09-29', 1600, 1020, 3),
(7698, 'NEGRO', 'DIRECTOR', 7839, '1991-05-01', 3005, NULL, 3),
(7782, 'CEREZO', 'DIRECTOR', 7839, '1991-06-09', 2885, NULL, 1),
(7788, 'GIL', 'ANALISTA', 7566, '1991-11-09', 3000, NULL, 2),
(7839, 'REY', 'PRESIDENTE', NULL, '1991-11-17', 4100, NULL, 1),
(7844, 'TOVAR', 'VENDEDOR', 7698, '1991-09-08', 1350, 0, 3),
(7876, 'ALONSO', 'EMPLEADO', 7788, '1991-09-23', 1430, NULL, 2),
(7900, 'JIMENO', 'EMPLEADO', 7698, '1991-12-03', 1335, NULL, 3),
(7934, 'MUÑOZ', 'EMPLEADO', 7782, '1992-01-23', 1690, NULL, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`dept_no`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`emp_no`),
  ADD KEY `empleados_ibfk_1` (`dept_no`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `dept_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`dept_no`) REFERENCES `departamentos` (`dept_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
