CREATE TABLE `usuarios` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` varchar(20) NOT NULL
);

CREATE TABLE `productos` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nombre` varchar(100) UNIQUE NOT NULL,
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

INSERT INTO `usuarios` (username, password, rol) VALUES
('UserAdmin', '2bb762d9735d915a05a65f973c43cae8d0d0a9670499e511ca25b312e45cc2c3', 'admin')
