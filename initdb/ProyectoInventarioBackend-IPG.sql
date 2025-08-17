CREATE TABLE `usuarios` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` varchar(20) NOT NULL
);

CREATE TABLE `productos` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `precio` int NOT NULL
);

CREATE TABLE `inventario` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `producto_id` int NOT NULL,
  `cantidad` int NOT NULL DEFAULT 0,
  `actualizado_en` datetime DEFAULT (current_timestamp)
);

ALTER TABLE `inventario` ADD FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);
