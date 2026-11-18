-- Base de datos de ejemplo sanitizada para practicas docentes
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `alumnos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apellidos` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `nombre` varchar(25) COLLATE latin1_spanish_ci NOT NULL,
  `usuario` varchar(25) COLLATE latin1_spanish_ci NOT NULL,
  `contrasenya` varchar(20) COLLATE latin1_spanish_ci NOT NULL,
  `email` varchar(50) COLLATE latin1_spanish_ci DEFAULT NULL,
  `anyo` varchar(9) COLLATE latin1_spanish_ci NOT NULL,
  `curso` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `grupo` varchar(5) COLLATE latin1_spanish_ci NOT NULL,
  `numord` tinyint(4) DEFAULT NULL,
  `foto` varchar(25) COLLATE latin1_spanish_ci DEFAULT NULL,
  `aula` int(11) NOT NULL,
  `nia` varchar(9) COLLATE latin1_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

INSERT INTO `alumnos` (`id`, `apellidos`, `nombre`, `usuario`, `contrasenya`, `email`, `anyo`, `curso`, `grupo`, `numord`, `foto`, `aula`, `nia`) VALUES
(1, 'GARCIA PEREZ', 'JUAN', 'jgarcia', '123456', 'jgarcia@example.com', '2022-2023', '1DAW', 'A', 1, NULL, 101, '10000001'),
(2, 'LOPEZ GOMEZ', 'ANA', 'alopez', '123456', 'alopez@example.com', '2022-2023', '1DAW', 'A', 2, NULL, 101, '10000002'),
(3, 'MARTINEZ SANCHEZ', 'CARLOS', 'cmartinez', '123456', 'cmartinez@example.com', '2022-2023', '1DAW', 'A', 3, NULL, 101, '10000003'),
(4, 'RODRIGUEZ NAVARRO', 'ELENA', 'erodriguez', '123456', 'erodriguez@example.com', '2022-2023', '1DAW', 'A', 4, NULL, 101, '10000004'),
(5, 'FERNANDEZ VIDAL', 'MARC', 'mfernandez', '123456', 'mfernandez@example.com', '2022-2023', '1DAW', 'A', 5, NULL, 101, '10000005');
